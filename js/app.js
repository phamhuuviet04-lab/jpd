/**
 * Main Application Module cho ứng dụng Ôn tập Từ vựng Đa môn học (jpd)
 * Quản lý trạng thái học, chọn môn học, phân loại Từ vựng / Hán tự, giao diện quiz, giao diện danh sách, lưu trữ cục bộ và phím tắt.
 */

// ==========================================
// TRẠNG THÁI ỨNG DỤNG (STATE)
// ==========================================
const STORAGE_KEY_SELECTED_SUBJECT = 'selectedSubject_quizlet';
const STORAGE_KEY_CUSTOM_SUBJECTS = 'custom_subjects_v1';

let currentSubjectId = 'japanese';
let currentSubject = null;

let allQuestions = [];
let selectedLesson = 'all'; // 'all' hoặc ID bài học (vd: '1', '2', '東 (ĐÔNG)', ...)
let selectedPart = 'all';   // 'all' hoặc ID phần (vd: '1', '2', ...)

let markedQuestions = [];
let lastMarkedQuestionId = null;
let currentQuizMode = 'jp-vi';

let reviewQueue = [];
let currentQuestion = null;
let focusedListIndex = 0;

// Tham chiếu phần tử UI (sẽ khởi tạo khi DOM sẵn sàng)
let ui = {};

// ==========================================
// QUẢN LÝ MÔN HỌC (SUBJECTS MANAGEMENT)
// ==========================================
function getAllSubjects() {
    const builtIn = window.APP_SUBJECTS || {};
    
    // Tải các môn học tùy chỉnh người dùng thêm trên trình duyệt
    let custom = {};
    try {
        custom = JSON.parse(localStorage.getItem(STORAGE_KEY_CUSTOM_SUBJECTS) || '{}');
    } catch (e) {
        console.error('Lỗi khi đọc custom_subjects:', e);
    }

    return { ...builtIn, ...custom };
}

function getStorageKey(type) {
    // Tương thích ngược dữ liệu bài học Tiếng Nhật đã có từ trước
    if (currentSubjectId === 'japanese') {
        if (type === 'marked') return 'markedQuestions_jp_v2';
        if (type === 'last') return 'lastMarkedQuestionId_jp_v2';
        if (type === 'mode') return 'quizMode_jp_v2';
    }
    return `${type}_${currentSubjectId}_v1`;
}

function loadSubjectState() {
    const markedKey = getStorageKey('marked');
    const lastKey = getStorageKey('last');
    const modeKey = getStorageKey('mode');

    try {
        markedQuestions = JSON.parse(localStorage.getItem(markedKey) || '[]');
    } catch (e) {
        markedQuestions = [];
    }

    const savedLast = localStorage.getItem(lastKey);
    lastMarkedQuestionId = savedLast !== null ? Number(savedLast) : null;

    const defaultMode = currentSubject.quizType === 'standard' ? 'standard' : 'jp-vi';
    currentQuizMode = localStorage.getItem(modeKey) || defaultMode;
}

function saveMarkedState() {
    localStorage.setItem(getStorageKey('marked'), JSON.stringify(markedQuestions));
}

function saveLastMarkedState() {
    if (lastMarkedQuestionId !== null) {
        localStorage.setItem(getStorageKey('last'), String(lastMarkedQuestionId));
    } else {
        localStorage.removeItem(getStorageKey('last'));
    }
}

function saveQuizModeState() {
    localStorage.setItem(getStorageKey('mode'), currentQuizMode);
}

function switchSubject(newSubjectId) {
    const subjects = getAllSubjects();
    if (!subjects[newSubjectId]) {
        newSubjectId = Object.keys(subjects)[0];
    }

    currentSubjectId = newSubjectId;
    currentSubject = subjects[currentSubjectId];
    localStorage.setItem(STORAGE_KEY_SELECTED_SUBJECT, currentSubjectId);

    // Nạp câu hỏi của môn học này
    allQuestions = parseRawText(currentSubject.rawText, currentSubject.lessonParts);

    // Nạp trạng thái môn học (tiến độ đã học, mode hỏi đáp)
    loadSubjectState();

    // Reset bộ lọc bài học
    selectedLesson = 'all';
    selectedPart = 'all';

    // Cập nhật giao diện thanh môn học & thông tin
    updateSubjectHeaderUI();
    renderSubjectMenu();
    renderLessonTabs();
    renderPartTabs();
    updateQuizModeUI();

    // Điều hướng lại màn hình đang mở
    if (!ui.listScreen.classList.contains('hidden')) {
        renderListScreen();
    } else {
        startQuiz();
    }
}

function updateSubjectHeaderUI() {
    if (!currentSubject) return;

    const iconEl = document.getElementById('active-subject-icon');
    const nameEl = document.getElementById('active-subject-name');
    const badgeEl = document.getElementById('active-subject-badge');
    const subtitleEl = document.getElementById('quiz-subtitle');
    const listTitleEl = document.getElementById('list-screen-title');
    const furiganaWrapper = document.getElementById('furigana-toggle-wrapper');
    const japaneseSubTabs = document.getElementById('japanese-sub-tabs');
    const subTabVocab = document.getElementById('sub-tab-vocab');
    const subTabKanji = document.getElementById('sub-tab-kanji');
    const japaneseSubDesc = document.getElementById('japanese-sub-desc');

    if (iconEl) iconEl.innerText = currentSubject.icon || '📚';
    if (nameEl) {
        if (currentSubjectId === 'japanese_kanji') {
            nameEl.innerText = "Tiếng Nhật (Hán tự)";
        } else {
            nameEl.innerText = currentSubject.name || 'Môn học';
        }
    }
    if (badgeEl) {
        badgeEl.innerText = currentSubject.badge || `${allQuestions.length} câu`;
        badgeEl.style.display = currentSubject.badge ? 'inline-block' : 'none';
    }
    if (subtitleEl) {
        subtitleEl.innerText = `jpd • ${currentSubject.fullName || currentSubject.name}`;
    }
    if (listTitleEl) {
        listTitleEl.innerText = `Danh sách câu hỏi - ${currentSubject.fullName || currentSubject.name}`;
    }

    // Hiển thị hoặc ẩn tùy chọn Furigana
    if (furiganaWrapper) {
        if (currentSubject.hasFurigana) {
            furiganaWrapper.classList.remove('hidden');
            furiganaWrapper.classList.add('flex');
        } else {
            furiganaWrapper.classList.add('hidden');
            furiganaWrapper.classList.remove('flex');
        }
    }

    // Quản lý thanh chủ đề con cho Tiếng Nhật (Từ vựng / Hán tự)
    if (japaneseSubTabs) {
        const isJapanese = currentSubject.category === 'japanese' || currentSubjectId.startsWith('japanese');
        if (isJapanese) {
            japaneseSubTabs.classList.remove('hidden');
            japaneseSubTabs.classList.add('flex');

            if (currentSubjectId === 'japanese_kanji') {
                if (subTabKanji) subTabKanji.className = "px-3 py-1 text-xs md:text-sm font-bold rounded-md transition shadow-sm bg-blue-600 text-white";
                if (subTabVocab) subTabVocab.className = "px-3 py-1 text-xs md:text-sm font-bold rounded-md transition text-gray-600 hover:text-blue-600 hover:bg-white";
                if (japaneseSubDesc) japaneseSubDesc.innerText = `Ôn tập 9 chữ Hán & từ ghép (${allQuestions.length} câu)`;
            } else {
                if (subTabVocab) subTabVocab.className = "px-3 py-1 text-xs md:text-sm font-bold rounded-md transition shadow-sm bg-blue-600 text-white";
                if (subTabKanji) subTabKanji.className = "px-3 py-1 text-xs md:text-sm font-bold rounded-md transition text-gray-600 hover:text-blue-600 hover:bg-white";
                if (japaneseSubDesc) japaneseSubDesc.innerText = `Giáo trình Dekiru Nihongo Bài 4 - 7 (${allQuestions.length} câu)`;
            }
        } else {
            japaneseSubTabs.classList.add('hidden');
            japaneseSubTabs.classList.remove('flex');
        }
    }
}

function renderSubjectMenu() {
    const container = document.getElementById('subject-tabs-container');
    if (!container) return;
    container.innerHTML = '';

    const subjects = getAllSubjects();
    const customSubjects = JSON.parse(localStorage.getItem(STORAGE_KEY_CUSTOM_SUBJECTS) || '{}');

    // Gom nhóm các môn chính để thanh menu trên cùng luôn gọn đẹp
    // Tiếng Nhật (gồm cả vocab và kanji), và các môn tự tạo
    const mainEntries = [
        {
            id: 'japanese',
            label: 'Tiếng Nhật',
            icon: '🇯🇵',
            isActive: currentSubjectId === 'japanese' || currentSubjectId === 'japanese_kanji',
            onSelect: () => {
                // Giữ lại môn con đang học hoặc chuyển sang japanese
                if (currentSubjectId !== 'japanese' && currentSubjectId !== 'japanese_kanji') {
                    switchSubject('japanese');
                }
            }
        }
    ];

    // Thêm các môn custom do người dùng tự tạo
    Object.keys(customSubjects).forEach(subId => {
        const sub = customSubjects[subId];
        mainEntries.push({
            id: subId,
            label: sub.name,
            icon: sub.icon || '📖',
            isCustom: true,
            isActive: currentSubjectId === subId,
            onSelect: () => switchSubject(subId)
        });
    });

    mainEntries.forEach(entry => {
        const btn = document.createElement('div');
        btn.className = `group relative inline-flex items-center rounded-lg text-xs md:text-sm font-bold transition select-none ${
            entry.isActive
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-gray-600 hover:text-blue-600 hover:bg-white'
        }`;

        const mainBtn = document.createElement('button');
        mainBtn.className = "px-3 py-1.5 flex items-center gap-1.5 focus:outline-none";
        mainBtn.innerHTML = `
            <span>${entry.icon}</span>
            <span>${entry.label}</span>
        `;
        mainBtn.addEventListener('click', entry.onSelect);
        btn.appendChild(mainBtn);

        // Nút xóa nếu là custom môn
        if (entry.isCustom) {
            const delBtn = document.createElement('button');
            delBtn.className = `pr-2 pl-0.5 opacity-60 hover:opacity-100 transition text-xs font-normal ${entry.isActive ? 'text-blue-100 hover:text-white' : 'text-gray-400 hover:text-red-500'}`;
            delBtn.title = "Xóa môn học này";
            delBtn.innerHTML = "×";
            delBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                if (confirm(`Bạn có chắc muốn xóa môn "${entry.label}" khỏi trình duyệt không?`)) {
                    deleteCustomSubject(entry.id);
                }
            });
            btn.appendChild(delBtn);
        }

        container.appendChild(btn);
    });
}

function deleteCustomSubject(subId) {
    try {
        const custom = JSON.parse(localStorage.getItem(STORAGE_KEY_CUSTOM_SUBJECTS) || '{}');
        delete custom[subId];
        localStorage.setItem(STORAGE_KEY_CUSTOM_SUBJECTS, JSON.stringify(custom));
        if (currentSubjectId === subId) {
            switchSubject('japanese');
        } else {
            renderSubjectMenu();
        }
    } catch (e) {
        console.error('Lỗi khi xóa môn:', e);
    }
}

// ==========================================
// HÀM TIỆN ÍCH & LỌC CÂU HỎI
// ==========================================
function getFilteredQuestions() {
    return allQuestions.filter(q => {
        const matchLesson = (selectedLesson === 'all' || q.lesson === selectedLesson);
        const matchPart = (selectedPart === 'all' || q.part === selectedPart);
        return matchLesson && matchPart;
    });
}

function updateQuizModeUI() {
    const container = document.getElementById('quiz-mode-container');
    if (!container) return;

    const isVocab = currentSubject.quizType !== 'standard';

    if (!isVocab) {
        // Môn trắc nghiệm thông thường (không cần đảo ngược)
        container.innerHTML = `
            <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition bg-blue-600 text-white shadow-sm" data-mode="standard">
                📝 Trắc nghiệm tiêu chuẩn
            </button>
        `;
        currentQuizMode = 'standard';
        return;
    }

    const labels = currentSubject.modeLabels || {
        'jp-vi': `${currentSubject.icon || '📖'} ➔ 🇻🇳 ${currentSubject.name} - Việt`,
        'vi-jp': `🇻🇳 ➔ ${currentSubject.icon || '📖'} Việt - ${currentSubject.name}`,
        'mix': '🔀 Trộn cả hai'
    };

    container.innerHTML = `
        <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition" data-mode="jp-vi">
            ${labels['jp-vi']}
        </button>
        <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition" data-mode="vi-jp">
            ${labels['vi-jp']}
        </button>
        <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition" data-mode="mix">
            ${labels['mix']}
        </button>
    `;

    container.querySelectorAll('.quiz-mode-btn').forEach(btn => {
        const mode = btn.getAttribute('data-mode');
        if (mode === currentQuizMode) {
            btn.className = "quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition bg-blue-600 text-white shadow-sm";
        } else {
            btn.className = "quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition text-gray-600 hover:text-blue-600 hover:bg-blue-50";
        }

        btn.addEventListener('click', () => {
            if (mode && mode !== currentQuizMode) {
                currentQuizMode = mode;
                saveQuizModeState();
                updateQuizModeUI();
                startQuiz();
            }
        });
    });
}

function updateQuestionDisplay() {
    if (!currentQuestion) return;
    const hideFurigana = currentSubject.hasFurigana && document.getElementById('toggle-furigana')?.checked;

    if (currentQuestion.direction === 'jp-vi' || currentQuestion.direction === 'standard') {
        ui.question.innerText = hideFurigana 
            ? currentQuestion.prompt.replace(/\s*\([^)]+\)/g, '') 
            : currentQuestion.prompt;
    } else {
        ui.question.innerText = currentQuestion.prompt;
    }

    if (currentQuestion.direction === 'vi-jp') {
        document.querySelectorAll('#options-container label').forEach((lbl, idx) => {
            const span = lbl.querySelector('.option-text');
            const rawOpt = currentQuestion.options[idx];
            if (span && rawOpt) {
                span.innerText = hideFurigana 
                    ? rawOpt.replace(/\s*\([^)]+\)/g, '') 
                    : rawOpt;
            }
        });
    }
}

// ==========================================
// QUẢN LÝ TIẾN ĐỘ ĐÃ HỌC (MARKED QUESTIONS)
// ==========================================
function updateLastMarkedQuestion(id) {
    if (id === null || id === undefined || Number.isNaN(Number(id))) return;
    lastMarkedQuestionId = Number(id);
    saveLastMarkedState();
}

function clearLastMarkedQuestion() {
    lastMarkedQuestionId = null;
    saveLastMarkedState();
}

function getMostRecentMarkedQuestionId() {
    let latestIndex = -1;
    let latestId = null;
    allQuestions.forEach((q, idx) => {
        if (markedQuestions.includes(q.id) && idx > latestIndex) {
            latestIndex = idx;
            latestId = q.id;
        }
    });
    return latestId;
}

function syncLastMarkedQuestionFromSelection() {
    const latestId = getMostRecentMarkedQuestionId();
    if (latestId !== null) {
        updateLastMarkedQuestion(latestId);
        return;
    }

    if (lastMarkedQuestionId === null) {
        clearLastMarkedQuestion();
    }
}

function getTargetLastQuestionId() {
    const latestCurrentId = getMostRecentMarkedQuestionId();
    if (latestCurrentId !== null) return latestCurrentId;

    if (lastMarkedQuestionId !== null && allQuestions.some(q => q.id === lastMarkedQuestionId)) {
        return lastMarkedQuestionId;
    }

    return null;
}

function updateFocus() {
    const listItems = document.querySelectorAll('#questions-list-container > div');
    listItems.forEach((item, idx) => {
        if (idx === focusedListIndex) {
            item.classList.add('ring-4', 'ring-blue-400', 'border-blue-400', 'bg-blue-50');
            item.classList.remove('border', 'bg-gray-50');
        } else {
            item.classList.remove('ring-4', 'ring-blue-400', 'border-blue-400', 'bg-blue-50');
            item.classList.add('border', 'bg-gray-50');
        }
    });
}

function activateListItem(index, moveToNext = true) {
    const listItems = document.querySelectorAll('#questions-list-container > div');
    if (!listItems[index]) return;

    focusedListIndex = index;
    updateFocus();

    const cb = listItems[index].querySelector('.mark-checkbox');
    if (cb) {
        cb.checked = !cb.checked;
        cb.dispatchEvent(new Event('change'));
    }

    if (moveToNext && index < listItems.length - 1) {
        focusedListIndex = index + 1;
        updateFocus();
        listItems[focusedListIndex].scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function scrollToLastLearned() {
    const targetId = getTargetLastQuestionId();
    if (targetId === null) {
        alert('Bạn chưa đánh dấu câu nào là đã học trong mục này!');
        return;
    }

    const target = document.querySelector(`[data-qid="${targetId}"]`);
    if (!target) return;
    target.scrollIntoView({ behavior: 'smooth', block: 'center' });
    target.classList.add('ring-4', 'ring-amber-400', 'border-amber-400');
    setTimeout(() => {
        target.classList.remove('ring-4', 'ring-amber-400', 'border-amber-400');
    }, 2000);
}

function updateSelectAllButtonState() {
    const btn = document.getElementById('select-all-btn');
    if (!btn) return;
    const filtered = getFilteredQuestions();
    const allSelected = filtered.length > 0 && filtered.every(q => markedQuestions.includes(q.id));
    btn.disabled = allSelected;
    btn.classList.toggle('opacity-50', allSelected);
    btn.classList.toggle('cursor-not-allowed', allSelected);
}

// ==========================================
// MÀN HÌNH DANH SÁCH (LIST VIEW)
// ==========================================
function renderListScreen() {
    const filtered = getFilteredQuestions();
    ui.totalQuestions.innerText = filtered.length;
    const markedInFilter = markedQuestions.filter(id => filtered.some(q => q.id === id));
    ui.selectedCount.innerText = markedInFilter.length;
    const container = document.getElementById('questions-list-container');
    container.innerHTML = '';
    
    filtered.forEach((q, index) => {
        const qDiv = document.createElement('div');
        qDiv.className = "p-4 border rounded-lg bg-gray-50 shadow-sm transition-all";
        qDiv.setAttribute('data-qid', q.id);
        
        const isMarked = markedQuestions.includes(q.id);
        
        const header = document.createElement('div');
        header.className = "flex justify-between items-start gap-4 mb-3";

        let lessonInfo = '';
        if (q.lesson && q.lesson !== 'all') {
            const prefix = currentSubjectId === 'japanese_kanji' ? 'Hán tự: ' : (/^\d+$/.test(q.lesson) ? 'Bài ' : '');
            const partInfo = q.partTitle ? ` • Phần ${q.part}: ${q.partTitle}` : (q.part && q.part !== 'all' ? ` • Phần ${q.part}` : '');
            lessonInfo = `<span class="inline-block text-xs font-bold px-2 py-0.5 rounded bg-indigo-100 text-indigo-700 mb-1">${prefix}${q.lesson}${partInfo}</span>`;
        }

        header.innerHTML = `
            <div class="flex items-start gap-3 flex-1">
                <span class="inline-flex items-center justify-center min-w-9 h-9 rounded-full bg-blue-100 text-blue-700 font-bold text-sm shadow-sm">
                    ${index + 1}
                </span>
                <div class="flex-1">
                    ${lessonInfo}
                    <h3 class="font-bold text-gray-800 whitespace-pre-wrap">${q.question}</h3>
                </div>
            </div>
            <label class="flex items-center gap-2 cursor-pointer bg-white px-3 py-1.5 border rounded shadow-sm hover:bg-blue-50 transition">
                <input type="checkbox" class="mark-checkbox w-4 h-4 accent-blue-600" data-id="${q.id}" ${isMarked ? 'checked' : ''}>
                <span class="text-sm font-bold text-gray-700">Đã học</span>
            </label>
        `;
        
        const optionsDiv = document.createElement('div');
        optionsDiv.className = "space-y-2";
        q.options.forEach(opt => {
            const isCorrect = q.correct.includes(opt);
            const optDiv = document.createElement('div');
            optDiv.className = `p-3 rounded-lg ${isCorrect ? 'bg-green-100 font-bold border border-green-400 text-green-800' : 'bg-white border border-gray-200 text-gray-600'}`;
            optDiv.innerHTML = `${isCorrect ? '✅ ' : '⬜ '}${opt}`;
            optionsDiv.appendChild(optDiv);
        });
        
        qDiv.appendChild(header);
        qDiv.appendChild(optionsDiv);
        qDiv.addEventListener('click', (event) => {
            if (event.target.closest('.mark-checkbox')) return;
            const itemIndex = Array.from(container.children).indexOf(qDiv);
            focusedListIndex = itemIndex;
            updateFocus();
            const cb = qDiv.querySelector('.mark-checkbox');
            if (cb) {
                cb.checked = !cb.checked;
                cb.dispatchEvent(new Event('change'));
            }
        });
        container.appendChild(qDiv);
    });
    
    document.querySelectorAll('.mark-checkbox').forEach(cb => {
        cb.addEventListener('change', (e) => {
            const id = parseInt(e.target.getAttribute('data-id'));
            if (e.target.checked) {
                if (!markedQuestions.includes(id)) markedQuestions.push(id);
                updateLastMarkedQuestion(id);
            } else {
                markedQuestions = markedQuestions.filter(mId => mId !== id);
                syncLastMarkedQuestionFromSelection();
            }
            saveMarkedState();
            ui.selectedCount.innerText = markedQuestions.length;
            updateSelectAllButtonState();
        });
    });

    updateSelectAllButtonState();
    focusedListIndex = 0;
    updateFocus();
}

// ==========================================
// CHỨC NĂNG HỌC & TẠO CÂU HỎI (QUIZ)
// ==========================================
function getDistractors(baseQ, candidatePool, count = 3) {
    const isDifferent = item => 
        item.question !== baseQ.question && 
        item.correct[0] !== baseQ.correct[0];

    let pool = candidatePool.filter(isDifferent);

    if (pool.length < count) {
        const sameLesson = allQuestions.filter(item => item.lesson === baseQ.lesson && isDifferent(item));
        pool = [...pool, ...sameLesson];
    }

    if (pool.length < count) {
        const any = allQuestions.filter(isDifferent);
        pool = [...pool, ...any];
    }

    const seen = new Set();
    const uniquePool = [];
    for (const item of pool) {
        if (!seen.has(item.question)) {
            seen.add(item.question);
            uniquePool.push(item);
        }
    }

    uniquePool.sort(() => Math.random() - 0.5);
    return uniquePool.slice(0, count).map(item => item.question);
}

function createQuizItem(baseQ, direction, candidatePool) {
    const isReverse = (direction === 'vi-jp' && currentSubject.quizType !== 'standard');

    if (isReverse) {
        const distractors = getDistractors(baseQ, candidatePool, 3);
        const options = [baseQ.question, ...distractors].sort(() => Math.random() - 0.5);
        return {
            id: baseQ.id,
            direction: 'vi-jp',
            prompt: baseQ.correct[0],
            options: options,
            correct: [baseQ.question],
            lesson: baseQ.lesson,
            part: baseQ.part,
            partTitle: baseQ.partTitle,
            type: 'radio',
            correctPrimary: baseQ.question,
            correctSecondary: baseQ.correct[0],
            // Giữ alias cho Tiếng Nhật
            correctJapanese: baseQ.question,
            correctVietnamese: baseQ.correct[0],
            baseQ: baseQ
        };
    } else {
        return {
            id: baseQ.id,
            direction: direction === 'standard' ? 'standard' : 'jp-vi',
            prompt: baseQ.question,
            options: [...baseQ.options].sort(() => Math.random() - 0.5),
            correct: [...baseQ.correct],
            lesson: baseQ.lesson,
            part: baseQ.part,
            partTitle: baseQ.partTitle,
            type: baseQ.type,
            correctPrimary: baseQ.question,
            correctSecondary: baseQ.correct[0],
            // Giữ alias cho Tiếng Nhật
            correctJapanese: baseQ.question,
            correctVietnamese: baseQ.correct[0],
            baseQ: baseQ
        };
    }
}

function startQuiz() {
    const filtered = getFilteredQuestions();
    let questionsToLearn = filtered;
    if (markedQuestions.length > 0) {
        const markedInFilter = filtered.filter(q => markedQuestions.includes(q.id));
        if (markedInFilter.length > 0) {
            questionsToLearn = markedInFilter;
        }
    }

    if (questionsToLearn.length === 0) {
        ui.listScreen.classList.add('hidden');
        ui.quizScreen.classList.remove('hidden');
        ui.question.innerHTML = "Không có câu hỏi nào trong mục này.";
        ui.options.innerHTML = "";
        ui.skipBtn.style.display = "none";
        ui.progress.style.display = "none";
        if (ui.directionBadge) ui.directionBadge.style.display = "none";
        if (ui.qTypeBadge) ui.qTypeBadge.style.display = "none";
        ui.feedback.classList.add('hidden');
        ui.nextBtn.classList.add('hidden');
        return;
    }

    const candidatePool = filtered.length >= 4 ? filtered : allQuestions;

    const items = questionsToLearn.map(baseQ => {
        let dir = currentQuizMode;
        if (dir === 'mix') {
            dir = Math.random() < 0.5 ? 'jp-vi' : 'vi-jp';
        }
        return createQuizItem(baseQ, dir, candidatePool);
    });

    reviewQueue = items.sort(() => Math.random() - 0.5);
    
    ui.listScreen.classList.add('hidden');
    ui.quizScreen.classList.remove('hidden');
    
    ui.options.innerHTML = "";
    ui.feedback.classList.add('hidden');
    ui.nextBtn.classList.add('hidden');
    ui.skipBtn.style.display = "";
    ui.skipBtn.classList.remove('hidden');
    ui.progress.style.display = "";
    if (ui.directionBadge) ui.directionBadge.style.display = "";
    if (ui.qTypeBadge) ui.qTypeBadge.style.display = "";
    
    loadNextQuestion();
}

function loadNextQuestion() {
    if (reviewQueue.length === 0) {
        ui.question.innerHTML = "🎉 Tuyệt vời! Bạn đã hoàn thành toàn bộ bài ôn tập mục này.";
        ui.options.innerHTML = "";
        ui.skipBtn.style.display = "none";
        ui.progress.style.display = "none";
        if (ui.directionBadge) ui.directionBadge.style.display = "none";
        if (ui.qTypeBadge) ui.qTypeBadge.style.display = "none";
        return;
    }

    currentQuestion = reviewQueue[0];
    ui.progress.innerText = `Còn ${reviewQueue.length} câu`;
    
    const lessonBadge = document.getElementById('lesson-badge');
    if (lessonBadge) {
        if (currentQuestion.lesson && currentQuestion.lesson !== 'all') {
            const prefix = currentSubjectId === 'japanese_kanji' ? 'Hán tự: ' : (/^\d+$/.test(currentQuestion.lesson) ? 'Bài ' : '');
            const partInfo = currentQuestion.partTitle 
                ? ` • Phần ${currentQuestion.part}: ${currentQuestion.partTitle}` 
                : (currentQuestion.part && currentQuestion.part !== 'all' ? ` • Phần ${currentQuestion.part}` : '');
            lessonBadge.style.display = "inline-block";
            lessonBadge.innerText = `${prefix}${currentQuestion.lesson}${partInfo}`;
        } else {
            lessonBadge.style.display = "none";
        }
    }

    if (ui.directionBadge) {
        ui.directionBadge.style.display = "";

        if (currentSubjectId === 'japanese_kanji') {
            if (currentQuestion.direction === 'vi-jp') {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full inline-flex items-center gap-1 border border-emerald-300";
                ui.directionBadge.innerHTML = "<span>🇻🇳 ➔ 🈸</span><span>Chọn chữ Hán tương ứng</span>";
            } else {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-blue-100 text-blue-800 rounded-full inline-flex items-center gap-1 border border-blue-200";
                ui.directionBadge.innerHTML = "<span>🈸 ➔ 🇻🇳</span><span>Chọn cách đọc & nghĩa của từ này</span>";
            }
        } else {
            const icon = currentSubject.icon || '📖';
            const subName = currentSubject.name || 'Môn';

            if (currentQuestion.direction === 'vi-jp') {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full inline-flex items-center gap-1 border border-emerald-300";
                ui.directionBadge.innerHTML = `<span>🇻🇳 ➔ ${icon}</span><span>Chọn từ ${subName} tương ứng</span>`;
            } else if (currentQuestion.direction === 'jp-vi') {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-blue-100 text-blue-800 rounded-full inline-flex items-center gap-1 border border-blue-200";
                ui.directionBadge.innerHTML = `<span>${icon} ➔ 🇻🇳</span><span>Chọn nghĩa tiếng Việt của từ này</span>`;
            } else {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-purple-100 text-purple-800 rounded-full inline-flex items-center gap-1 border border-purple-200";
                ui.directionBadge.innerHTML = `<span>${icon}</span><span>Chọn đáp án đúng nhất</span>`;
            }
        }
    }

    if (currentQuestion.type === 'checkbox') {
        ui.qTypeBadge.classList.remove('hidden');
        ui.qTypeBadge.innerText = `CHỌN ${currentQuestion.correct.length} ĐÁP ÁN`;
    } else {
        ui.qTypeBadge.classList.add('hidden');
    }
    
    ui.options.innerHTML = "";
    const hideFurigana = currentSubject.hasFurigana && document.getElementById('toggle-furigana')?.checked;

    currentQuestion.options.forEach((opt, index) => {
        const label = document.createElement('label');
        label.className = "flex items-start p-4 border-2 border-gray-100 rounded-lg cursor-pointer hover:border-blue-300 hover:bg-blue-50 transition";
        const inputType = currentQuestion.type;
        const inputClass = inputType === 'radio' ? 'rounded-full' : 'rounded';

        const displayOptText = (currentQuestion.direction === 'vi-jp' && hideFurigana)
            ? opt.replace(/\s*\([^)]+\)/g, '')
            : opt;

        label.innerHTML = `
            <input type="${inputType}" name="answer" value="${opt.replace(/"/g, '&quot;')}" class="mt-1 mr-4 w-5 h-5 cursor-pointer accent-blue-600 ${inputClass}">
            <span class="text-gray-700 font-medium">
                <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-xs font-bold text-gray-500 bg-gray-200 rounded shadow-sm">${index + 1}</span>
                <span class="option-text">${displayOptText}</span>
            </span>
        `;
        ui.options.appendChild(label);
    });

    updateQuestionDisplay();

    // Tự động kiểm tra đáp án khi người dùng chọn
    document.querySelectorAll('input[name="answer"]').forEach(input => {
        input.addEventListener('change', () => {
            const selectedCount = document.querySelectorAll('input[name="answer"]:checked').length;
            if (currentQuestion.type === 'radio') {
                checkAnswer();
            } else if (currentQuestion.type === 'checkbox') {
                if (selectedCount === currentQuestion.correct.length) {
                    checkAnswer();
                }
            }
        });
    });

    ui.feedback.classList.add('hidden');
    ui.nextBtn.classList.add('hidden');
    ui.skipBtn.classList.remove('hidden');
}

function checkAnswer() {
    const selectedNodes = document.querySelectorAll('input[name="answer"]:checked');
    const selected = Array.from(selectedNodes).map(el => el.value);
    
    const isCorrect = selected.length === currentQuestion.correct.length && 
                      selected.every(val => currentQuestion.correct.includes(val));

    ui.skipBtn.classList.add('hidden');
    ui.feedback.classList.remove('hidden');
    ui.nextBtn.classList.remove('hidden');

    document.querySelectorAll('input[name="answer"]').forEach(inp => inp.disabled = true);
    selectedNodes.forEach(node => {
        node.parentElement.classList.add('bg-gray-100');
    });

    const isVocab = currentSubject.quizType !== 'standard';

    if (isCorrect) {
        ui.feedback.className = "mt-6 p-5 rounded-lg bg-green-50 text-green-800 border-2 border-green-200";
        ui.feedbackTitle.innerText = "✅ Chính xác!";

        if (isVocab) {
            ui.feedbackText.innerHTML = `
                <div class="mt-1 flex items-baseline gap-2 flex-wrap">
                    <span class="text-xl font-bold text-green-900">${currentQuestion.correctPrimary}</span>
                    <span class="text-gray-400">•</span>
                    <span class="text-base font-semibold text-green-800">${currentQuestion.correctSecondary}</span>
                </div>
                <p class="text-xs text-green-600 mt-2 font-normal">Tuyệt vời, câu này sẽ không lặp lại nữa.</p>
            `;
        } else {
            ui.feedbackText.innerHTML = `
                <div class="mt-1 font-semibold text-green-900">
                    Đáp án đúng: ${currentQuestion.correct.join(', ')}
                </div>
                <p class="text-xs text-green-600 mt-2 font-normal">Tuyệt vời, câu này sẽ không lặp lại nữa.</p>
            `;
        }
        reviewQueue.shift(); 
    } else {
        ui.feedback.className = "mt-6 p-5 rounded-lg bg-red-50 text-red-800 border-2 border-red-200";
        ui.feedbackTitle.innerText = "❌ Sai rồi! Đáp án đúng:";

        if (isVocab) {
            ui.feedbackText.innerHTML = `
                <div class="mt-2 p-3 bg-white rounded-lg border border-red-200 shadow-sm">
                    <div class="text-xl font-bold text-red-900 mb-1">${currentQuestion.correctPrimary}</div>
                    <div class="text-sm font-semibold text-gray-700">Nghĩa: <span class="text-red-700 font-bold">${currentQuestion.correctSecondary}</span></div>
                </div>
                <p class="text-xs text-red-600 mt-2 font-normal">Câu này sẽ lặp lại ở cuối danh sách để bạn luyện tập.</p>
            `;
        } else {
            ui.feedbackText.innerHTML = `
                <div class="mt-2 p-3 bg-white rounded-lg border border-red-200 shadow-sm">
                    <div class="text-base font-bold text-red-900 mb-1">Đáp án: ${currentQuestion.correct.join(', ')}</div>
                </div>
                <p class="text-xs text-red-600 mt-2 font-normal">Câu này sẽ lặp lại ở cuối danh sách để bạn luyện tập.</p>
            `;
        }
        
        const failedItem = reviewQueue.shift();
        reviewQueue.push(failedItem);
    }
}

function handleNextAction() {
    if (!ui.feedback.classList.contains('hidden')) {
        ui.nextBtn.click();
    } else if (!ui.skipBtn.classList.contains('hidden')) {
        ui.skipBtn.click();
    }
}

// ==========================================
// TABS & BỘ LỌC BÀI HỌC / PHẦN (DYNAMIC)
// ==========================================
function renderLessonTabs() {
    const container = document.getElementById('lesson-tabs');
    if (!container) return;
    container.innerHTML = '';

    // Tìm tất cả các bài học riêng biệt trong câu hỏi
    const lessonSet = new Set();
    allQuestions.forEach(q => {
        if (q.lesson && q.lesson !== 'all') {
            lessonSet.add(q.lesson);
        }
    });

    const uniqueLessons = Array.from(lessonSet).sort((a, b) => {
        const numA = parseInt(a);
        const numB = parseInt(b);
        if (!isNaN(numA) && !isNaN(numB)) return numA - numB;
        return a.localeCompare(b);
    });

    const lessonsToRender = ['all', ...uniqueLessons];

    lessonsToRender.forEach(les => {
        let label = '';
        let count = 0;
        if (les === 'all') {
            label = 'Tất cả';
            count = allQuestions.length;
        } else {
            const prefix = currentSubjectId === 'japanese_kanji' ? '' : (/^\d+$/.test(les) ? 'Bài ' : '');
            label = `${prefix}${les}`;
            count = allQuestions.filter(q => q.lesson === les).length;
        }

        const isActive = selectedLesson === les;
        const btn = document.createElement('button');
        btn.setAttribute('data-lesson', les);
        btn.className = `lesson-tab px-4 py-1.5 rounded-full font-bold text-sm shadow-sm transition border-2 ${
            isActive
                ? 'border-indigo-500 bg-indigo-500 text-white'
                : 'border-indigo-300 bg-white text-indigo-600 hover:bg-indigo-50'
        }`;
        btn.textContent = `${label} (${count})`;

        btn.addEventListener('click', () => {
            selectedLesson = les;
            selectedPart = 'all';
            renderLessonTabs();
            renderPartTabs();
            if (!ui.listScreen.classList.contains('hidden')) {
                renderListScreen();
            } else {
                startQuiz();
            }
        });

        container.appendChild(btn);
    });
}

function renderPartTabs() {
    const container = document.getElementById('part-tabs');
    if (!container) return;
    container.innerHTML = '';

    // Tìm tất cả các phần thuộc bài đã chọn
    const partSet = new Set();
    allQuestions.forEach(q => {
        if ((selectedLesson === 'all' || q.lesson === selectedLesson) && q.part && q.part !== 'all') {
            partSet.add(q.part);
        }
    });

    // Nếu không có phần nào, ẩn thanh tab phần đi cho gọn gàng
    if (partSet.size === 0) {
        container.style.display = 'none';
        return;
    }
    container.style.display = 'flex';

    const uniqueParts = Array.from(partSet).sort((a, b) => {
        const numA = parseInt(a);
        const numB = parseInt(b);
        if (!isNaN(numA) && !isNaN(numB)) return numA - numB;
        return a.localeCompare(b);
    });

    const parts = ['all', ...uniqueParts];
    const lessonPartsDict = currentSubject.lessonParts || {};

    parts.forEach(p => {
        let label = '';
        let count = 0;
        if (p === 'all') {
            label = 'Tất cả phần';
            count = allQuestions.filter(q => selectedLesson === 'all' || q.lesson === selectedLesson).length;
        } else {
            const title = (selectedLesson !== 'all' && lessonPartsDict[selectedLesson]?.[p])
                ? `: ${lessonPartsDict[selectedLesson][p]}`
                : '';
            label = `Phần ${p}${title}`;
            count = allQuestions.filter(q => (selectedLesson === 'all' || q.lesson === selectedLesson) && q.part === p).length;
        }

        const btn = document.createElement('button');
        btn.setAttribute('data-part', p);
        const isActive = selectedPart === p;
        btn.className = `part-tab px-3.5 py-1.5 rounded-full font-semibold text-xs md:text-sm shadow-sm transition border-2 ${
            isActive 
                ? 'border-emerald-600 bg-emerald-600 text-white shadow' 
                : 'border-emerald-300 bg-white text-emerald-700 hover:bg-emerald-50'
        }`;
        btn.textContent = `${label} (${count})`;

        btn.addEventListener('click', () => {
            selectedPart = p;
            renderPartTabs();
            if (!ui.listScreen.classList.contains('hidden')) {
                renderListScreen();
            } else {
                startQuiz();
            }
        });

        container.appendChild(btn);
    });
}

// ==========================================
// MODAL THÊM MÔN HỌC MỚI
// ==========================================
function setupModal() {
    const modal = document.getElementById('add-subject-modal');
    const openBtn = document.getElementById('add-subject-btn');
    const closeBtn = document.getElementById('close-modal-btn');
    const tabQuick = document.getElementById('tab-btn-quick');
    const tabCode = document.getElementById('tab-btn-code');
    const formQuick = document.getElementById('quick-add-form');
    const guideCode = document.getElementById('code-add-guide');
    const saveBtn = document.getElementById('save-new-subject-btn');

    if (!modal) return;

    if (openBtn) {
        openBtn.addEventListener('click', () => {
            modal.classList.remove('hidden');
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            modal.classList.add('hidden');
        });
    }

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.add('hidden');
        }
    });

    if (tabQuick && tabCode) {
        tabQuick.addEventListener('click', () => {
            tabQuick.className = "font-bold pb-2 px-3 border-b-2 border-blue-600 text-blue-600";
            tabCode.className = "font-semibold pb-2 px-3 text-gray-500 hover:text-gray-800 border-b-2 border-transparent";
            formQuick.classList.remove('hidden');
            guideCode.classList.add('hidden');
        });

        tabCode.addEventListener('click', () => {
            tabCode.className = "font-bold pb-2 px-3 border-b-2 border-blue-600 text-blue-600";
            tabQuick.className = "font-semibold pb-2 px-3 text-gray-500 hover:text-gray-800 border-b-2 border-transparent";
            guideCode.classList.remove('hidden');
            formQuick.classList.add('hidden');
        });
    }

    if (saveBtn) {
        saveBtn.addEventListener('click', () => {
            const subId = (document.getElementById('new-sub-id')?.value || '').trim().toLowerCase().replace(/[^a-z0-9_-]/g, '_');
            const subName = (document.getElementById('new-sub-name')?.value || '').trim();
            const subIcon = (document.getElementById('new-sub-icon')?.value || '').trim() || '📖';
            const subBadge = (document.getElementById('new-sub-badge')?.value || '').trim() || 'Tự tạo';
            const subRaw = (document.getElementById('new-sub-raw')?.value || '').trim();

            if (!subId) {
                alert('Vui lòng nhập Mã định danh ID (ví dụ: korean, tienganh, toan)');
                return;
            }
            if (!subName) {
                alert('Vui lòng nhập Tên môn học (ví dụ: Tiếng Hàn, Tiếng Anh)');
                return;
            }
            if (!subRaw) {
                alert('Vui lòng dán nội dung câu hỏi');
                return;
            }

            // Kiểm tra phân tích câu hỏi thử
            const testParsed = parseRawText(subRaw);
            if (testParsed.length === 0) {
                alert('Không thể nhận diện câu hỏi nào từ nội dung vừa dán! Vui lòng kiểm tra lại định dạng câu hỏi theo mẫu: Câu 1 [BÀI X] ...');
                return;
            }

            const newSubjectConfig = {
                id: subId,
                name: subName,
                fullName: `${subName} (${testParsed.length} câu)`,
                icon: subIcon,
                badge: subBadge,
                hasFurigana: false,
                quizType: 'vocab',
                langFrom: subName,
                langTo: 'Tiếng Việt',
                modeLabels: {
                    'jp-vi': `${subIcon} ➔ 🇻🇳 ${subName} - Việt`,
                    'vi-jp': `🇻🇳 ➔ ${subIcon} Việt - ${subName}`,
                    'mix': '🔀 Trộn cả hai'
                },
                lessonParts: {},
                rawText: subRaw
            };

            // Lưu vào localStorage
            try {
                const custom = JSON.parse(localStorage.getItem(STORAGE_KEY_CUSTOM_SUBJECTS) || '{}');
                custom[subId] = newSubjectConfig;
                localStorage.setItem(STORAGE_KEY_CUSTOM_SUBJECTS, JSON.stringify(custom));
            } catch (err) {
                alert('Lỗi lưu trữ: ' + err.message);
                return;
            }

            modal.classList.add('hidden');
            switchSubject(subId);
            alert(`Đã thêm thành công môn "${subName}" với ${testParsed.length} câu hỏi!`);
        });
    }
}

// ==========================================
// KHỞI TẠO ỨNG DỤNG & SỰ KIỆN
// ==========================================
function initApp() {
    // 1. Ánh xạ các phần tử giao diện
    ui = {
        loadingScreen: document.getElementById('loading-screen'),
        quizScreen: document.getElementById('quiz-screen'),
        listScreen: document.getElementById('list-screen'),
        totalQuestions: document.getElementById('total-questions'),
        selectedCount: document.getElementById('selected-count'),
        navList: document.getElementById('nav-list'),
        navQuiz: document.getElementById('nav-quiz'),
        progress: document.getElementById('progress'),
        qTypeBadge: document.getElementById('question-type-badge'),
        directionBadge: document.getElementById('direction-badge'),
        question: document.getElementById('question-text'),
        options: document.getElementById('options-container'),
        skipBtn: document.getElementById('skip-btn'),
        feedback: document.getElementById('feedback'),
        feedbackTitle: document.getElementById('feedback-title'),
        feedbackText: document.getElementById('feedback-text'),
        nextBtn: document.getElementById('next-btn'),
    };

    // 2. Xác định môn học ban đầu
    const allSubs = getAllSubjects();
    const savedSubjectId = localStorage.getItem(STORAGE_KEY_SELECTED_SUBJECT);
    if (savedSubjectId && allSubs[savedSubjectId]) {
        currentSubjectId = savedSubjectId;
    } else {
        currentSubjectId = Object.keys(allSubs)[0] || 'japanese';
    }
    currentSubject = allSubs[currentSubjectId];

    // Nạp câu hỏi môn học ban đầu
    allQuestions = parseRawText(currentSubject.rawText, currentSubject.lessonParts);
    loadSubjectState();

    if (allQuestions.length === 0) {
        ui.loadingScreen.innerText = "❌ Lỗi: Không tìm thấy dữ liệu câu hỏi. Hãy kiểm tra lại file code!";
        return;
    }

    // 3. Sự kiện chuyển đổi màn hình Quiz / Danh sách
    ui.navQuiz.addEventListener('click', () => {
        ui.navQuiz.className = "px-6 py-2 bg-blue-600 text-white rounded-lg font-bold shadow-md transition";
        ui.navList.className = "px-6 py-2 bg-white text-blue-600 rounded-lg font-bold shadow-md hover:bg-blue-50 transition";
        startQuiz();
    });

    ui.navList.addEventListener('click', () => {
        ui.navList.className = "px-6 py-2 bg-blue-600 text-white rounded-lg font-bold shadow-md transition";
        ui.navQuiz.className = "px-6 py-2 bg-white text-blue-600 rounded-lg font-bold shadow-md hover:bg-blue-50 transition";
        ui.quizScreen.classList.add('hidden');
        ui.listScreen.classList.remove('hidden');
        renderListScreen();
    });

    // 4. Sự kiện Furigana
    document.getElementById('toggle-furigana')?.addEventListener('change', () => {
        updateQuestionDisplay();
    });

    // 5. Sự kiện chuyển đổi Từ vựng / Hán tự của Tiếng Nhật
    document.getElementById('sub-tab-vocab')?.addEventListener('click', () => {
        if (currentSubjectId !== 'japanese') {
            switchSubject('japanese');
        }
    });

    document.getElementById('sub-tab-kanji')?.addEventListener('click', () => {
        if (currentSubjectId !== 'japanese_kanji') {
            switchSubject('japanese_kanji');
        }
    });

    // 6. Sự kiện các nút chức năng trong Quiz
    ui.nextBtn.onclick = () => loadNextQuestion();
    ui.skipBtn.onclick = () => {
        const skippedItem = reviewQueue.shift();
        reviewQueue.push(skippedItem);
        loadNextQuestion();
    };

    // 7. Sự kiện các nút hành động trong Màn hình danh sách
    document.getElementById('scroll-last-btn')?.addEventListener('click', () => {
        scrollToLastLearned();
    });

    document.getElementById('select-all-btn')?.addEventListener('click', () => {
        const filtered = getFilteredQuestions();
        if (filtered.length === 0) return;
        filtered.forEach(q => {
            if (!markedQuestions.includes(q.id)) markedQuestions.push(q.id);
        });
        updateLastMarkedQuestion(filtered[filtered.length - 1]?.id ?? null);
        saveMarkedState();
        renderListScreen();
    });

    document.getElementById('clear-all-btn')?.addEventListener('click', () => {
        const filtered = getFilteredQuestions();
        const filteredIds = filtered.map(q => q.id);
        const previousLastQuestionId = getTargetLastQuestionId();
        markedQuestions = markedQuestions.filter(id => !filteredIds.includes(id));
        if (previousLastQuestionId !== null) {
            updateLastMarkedQuestion(previousLastQuestionId);
        } else {
            clearLastMarkedQuestion();
        }
        saveMarkedState();
        renderListScreen();
    });

    // 8. Nút cuộn về đầu trang
    const backToTopBtn = document.getElementById('back-to-top-btn');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (!ui.listScreen.classList.contains('hidden')) {
                if (window.scrollY > 300) {
                    backToTopBtn.classList.remove('hidden');
                } else {
                    backToTopBtn.classList.add('hidden');
                }
            } else {
                backToTopBtn.classList.add('hidden');
            }
        });
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // 9. Xử lý chuột phụ (Back / Forward side buttons)
    document.addEventListener('mousedown', (e) => {
        if (e.button === 3) {
            e.preventDefault();
            ui.skipBtn.click();
            return;
        }
        if (e.button === 4 || e.button === 5) {
            e.preventDefault();
            handleNextAction();
        }
    });

    // 10. Xử lý phím tắt
    document.addEventListener('keydown', (e) => {
        // Trong màn hình danh sách
        if (!ui.listScreen.classList.contains('hidden')) {
            const listItems = document.querySelectorAll('#questions-list-container > div');
            if (listItems.length === 0) return;

            if (e.key === 'Enter') {
                e.preventDefault();
                activateListItem(focusedListIndex, true);
            } else if (e.key === 'ArrowDown') {
                e.preventDefault();
                if (focusedListIndex < listItems.length - 1) {
                    focusedListIndex++;
                    updateFocus();
                    listItems[focusedListIndex].scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                if (focusedListIndex > 0) {
                    focusedListIndex--;
                    updateFocus();
                    listItems[focusedListIndex].scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
            return;
        }

        // Trong màn hình Quiz
        if (!ui.quizScreen.classList.contains('hidden')) {
            if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
                handleNextAction();
            }

            if (e.key >= '1' && e.key <= '9') {
                if (ui.feedback.classList.contains('hidden')) {
                    const index = parseInt(e.key) - 1;
                    const inputs = document.querySelectorAll('input[name="answer"]');
                    if (index >= 0 && index < inputs.length) {
                        const input = inputs[index];
                        if (input.type === 'radio') {
                            input.checked = true;
                            input.dispatchEvent(new Event('change'));
                        } else if (input.type === 'checkbox') {
                            input.checked = !input.checked;
                            input.dispatchEvent(new Event('change'));
                        }
                    }
                }
            }
        }
    });

    // 11. Khởi tạo modal thêm môn học
    setupModal();

    // 12. Cập nhật giao diện ban đầu và bắt đầu học
    updateSubjectHeaderUI();
    renderSubjectMenu();
    updateQuizModeUI();
    renderLessonTabs();
    renderPartTabs();
    ui.loadingScreen.classList.add('hidden');
    startQuiz();
}

// Chạy ứng dụng khi DOM tải xong
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    initApp();
}
