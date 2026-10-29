/**
 * Main Application Module cho ứng dụng Ôn tập Từ vựng Đa môn học (jpd)
 * Quản lý trạng thái học, chọn môn học, phân loại Từ vựng / Hán tự, giao diện quiz, giao diện danh sách, lưu trữ cục bộ và phím tắt.
 */

// ==========================================
// TRỢ LÝ PHÁT ÂM TIẾNG NHẬT (WEB SPEECH API)
// ==========================================
const STORAGE_KEY_SPEECH_RATE = 'quizlet_speech_rate_v1';
let currentSpeechRate = parseFloat(localStorage.getItem(STORAGE_KEY_SPEECH_RATE) || '0.75');

function setSpeechRate(newRate) {
    currentSpeechRate = parseFloat(newRate) || 0.75;
    localStorage.setItem(STORAGE_KEY_SPEECH_RATE, String(currentSpeechRate));
    document.querySelectorAll('.speech-rate-select').forEach(sel => {
        sel.value = String(currentSpeechRate);
    });
}

function speakJapanese(text) {
    if (!('speechSynthesis' in window)) return;
    try {
        window.speechSynthesis.cancel();
        // Xóa furigana/chú thích trong ngoặc đơn
        const clean = (text || '').replace(/[\(（][^\)）]+[\)）]/g, '').trim();
        const utter = new SpeechSynthesisUtterance(clean);
        utter.lang = 'ja-JP';
        utter.rate = currentSpeechRate; // Tốc độ nghe chậm rãi (mặc định 0.75x)
        window.speechSynthesis.speak(utter);
    } catch (e) {
        console.warn('SpeechSynthesis error:', e);
    }
}
window.speakJapanese = speakJapanese;
window.setSpeechRate = setSpeechRate;

// ==========================================
// BỘ CHUYỂN ĐỔI ROMAJI ➔ HIRAGANA (TỰ LUẬN)
// ==========================================
const ROMAJI_TABLE = {
    // 4 chars
    'tchi': 'っち', 'cchi': 'っち',
    // 3 chars
    'nna': 'んな', 'nni': 'んに', 'nnu': 'んぬ', 'nne': 'んね', 'nno': 'んの',
    'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
    'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ', 'shi': 'し',
    'sya': 'しゃ', 'syu': 'しゅ', 'syo': 'しょ',
    'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ', 'chi': 'ち',
    'tya': 'ちゃ', 'tyu': 'ちゅ', 'tyo': 'ちょ',
    'tsu': 'つ', 'tu': 'つ',
    'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',
    'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
    'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',
    'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',
    'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',
    'zya': 'じゃ', 'zyu': 'じゅ', 'zyo': 'じょ',
    'jya': 'じゃ', 'jyu': 'じゅ', 'jyo': 'じょ',
    'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
    'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',
    'dya': 'ぢゃ', 'dyu': 'ぢゅ', 'dyo': 'ぢょ',
    'xtu': 'っ', 'ltu': 'っ',
    // 2 chars
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'sa': 'さ', 'si': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'ta': 'た', 'ti': 'ち', 'te': 'て', 'to': 'と',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'hu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'wa': 'わ', 'wo': 'を',
    'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
    'za': 'ざ', 'zi': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
    'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど',
    'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
    'ja': 'じゃ', 'ji': 'じ', 'ju': 'じゅ', 'je': 'じぇ', 'jo': 'じょ',
    'nn': 'ん', "n'": 'ん',
    // 1 char
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    '-': 'ー'
};

function katakanaToHiragana(text) {
    if (!text) return '';
    return text.replace(/[\u30a1-\u30f6]/g, ch => String.fromCharCode(ch.charCodeAt(0) - 0x60));
}

function convertRomajiToHiragana(text, isFinal = false) {
    if (!text) return '';
    let result = '';
    let str = text;
    let i = 0;

    while (i < str.length) {
        // Xử lý phụ âm đôi (sokuon: っ)
        if (i + 1 < str.length && 
            str[i].toLowerCase() === str[i + 1].toLowerCase() && 
            /[bcdfghjklmpqrstvwxyz]/i.test(str[i]) && 
            str[i].toLowerCase() !== 'n') {
            result += 'っ';
            i++;
            continue;
        }

        // Cụm 4 ký tự
        if (i + 4 <= str.length) {
            const chunk4 = str.slice(i, i + 4).toLowerCase();
            if (ROMAJI_TABLE[chunk4]) {
                result += ROMAJI_TABLE[chunk4];
                i += 4;
                continue;
            }
        }

        // Cụm 3 ký tự
        if (i + 3 <= str.length) {
            const chunk3 = str.slice(i, i + 3).toLowerCase();
            if (ROMAJI_TABLE[chunk3]) {
                result += ROMAJI_TABLE[chunk3];
                i += 3;
                continue;
            }
        }

        // Cụm 2 ký tự
        if (i + 2 <= str.length) {
            const chunk2 = str.slice(i, i + 2).toLowerCase();
            if (ROMAJI_TABLE[chunk2]) {
                result += ROMAJI_TABLE[chunk2];
                i += 2;
                continue;
            }
        }

        // Ký tự 'n' đứng cuối hoặc trước phụ âm (trừ a, e, i, o, u, y)
        if (str[i].toLowerCase() === 'n') {
            if (i + 1 === str.length) {
                if (isFinal) {
                    result += 'ん';
                    i++;
                    continue;
                }
            } else if (!/[aeiouy]/i.test(str[i + 1])) {
                result += 'ん';
                i++;
                continue;
            }
        }

        // 1 ký tự nguyên âm
        const chunk1 = str[i].toLowerCase();
        if (ROMAJI_TABLE[chunk1]) {
            result += ROMAJI_TABLE[chunk1];
            i += 1;
            continue;
        }

        // Giữ nguyên ký tự tiếng Nhật hoặc ký tự khác
        result += str[i];
        i++;
    }

    return result;
}

function normalizeKana(str) {
    if (!str) return '';
    let s = str.trim().toLowerCase();
    s = convertRomajiToHiragana(s, true);
    s = katakanaToHiragana(s);
    s = s.replace(/[\s\u3000]/g, '');
    return s;
}

window.convertRomajiToHiragana = convertRomajiToHiragana;
window.normalizeKana = normalizeKana;


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

    const isSpeaking = currentSubject.quizType === 'speaking' || currentSubjectId === 'japanese_speaking';
    const isGrammar = currentSubject.quizType === 'grammar' || currentSubjectId === 'japanese_grammar';
    let defaultMode = 'jp-vi';
    if (isSpeaking || currentSubject.quizType === 'standard') {
        defaultMode = 'standard';
    } else if (isGrammar) {
        defaultMode = 'all';
    }

    const savedMode = localStorage.getItem(modeKey);
    if (isSpeaking) {
        currentQuizMode = 'standard';
    } else if (isGrammar) {
        currentQuizMode = (savedMode && ['all', 'concept', 'translation'].includes(savedMode)) ? savedMode : 'all';
    } else {
        currentQuizMode = savedMode || defaultMode;
    }
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
    const subTabGrammar = document.getElementById('sub-tab-grammar');
    const subTabSpeaking = document.getElementById('sub-tab-speaking');
    const japaneseSubDesc = document.getElementById('japanese-sub-desc');

    if (iconEl) iconEl.innerText = currentSubject.icon || '📚';
    if (nameEl) {
        if (currentSubjectId === 'japanese_kanji') {
            nameEl.innerText = "Tiếng Nhật (Hán tự)";
        } else if (currentSubjectId === 'japanese_grammar') {
            nameEl.innerText = "Tiếng Nhật (Ngữ pháp)";
        } else if (currentSubjectId === 'japanese_speaking') {
            nameEl.innerText = "Tiếng Nhật (Luyện nói)";
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

    // Quản lý thanh chủ đề con cho Tiếng Nhật (Từ vựng / Hán tự / Ngữ pháp / Luyện nói)
    if (japaneseSubTabs) {
        const isJapanese = currentSubject.category === 'japanese' || currentSubjectId.startsWith('japanese');
        if (isJapanese) {
            japaneseSubTabs.classList.remove('hidden');
            japaneseSubTabs.classList.add('flex');

            const activeClass = "px-3 py-1 text-xs md:text-sm font-bold rounded-md transition shadow-sm bg-blue-600 text-white";
            const inactiveClass = "px-3 py-1 text-xs md:text-sm font-bold rounded-md transition text-gray-600 hover:text-blue-600 hover:bg-white";

            if (currentSubjectId === 'japanese_kanji') {
                if (subTabKanji) subTabKanji.className = activeClass;
                if (subTabVocab) subTabVocab.className = inactiveClass;
                if (subTabGrammar) subTabGrammar.className = inactiveClass;
                if (subTabSpeaking) subTabSpeaking.className = inactiveClass;
                if (japaneseSubDesc) japaneseSubDesc.innerText = `${currentSubject.badge || 'Hán tự Bài 4 - 6'} (${allQuestions.length} câu)`;
            } else if (currentSubjectId === 'japanese_grammar') {
                if (subTabGrammar) subTabGrammar.className = activeClass;
                if (subTabVocab) subTabVocab.className = inactiveClass;
                if (subTabKanji) subTabKanji.className = inactiveClass;
                if (subTabSpeaking) subTabSpeaking.className = inactiveClass;
                const cCount = allQuestions.filter(q => q.grammarType === 'concept').length;
                const tCount = allQuestions.filter(q => q.grammarType === 'translation').length;
                if (japaneseSubDesc) japaneseSubDesc.innerText = `Ngữ pháp Bài 4 - 6 (${allQuestions.length} câu: ${cCount} Hỏi ngữ pháp • ${tCount} Dịch câu)`;
            } else if (currentSubjectId === 'japanese_speaking') {
                if (subTabSpeaking) subTabSpeaking.className = activeClass;
                if (subTabVocab) subTabVocab.className = inactiveClass;
                if (subTabKanji) subTabKanji.className = inactiveClass;
                if (subTabGrammar) subTabGrammar.className = inactiveClass;
                if (japaneseSubDesc) japaneseSubDesc.innerText = `Luyện nói Hội thoại Bài 4 - 7 (${allQuestions.length} câu hỏi giao tiếp thực tế)`;
            } else {
                if (subTabVocab) subTabVocab.className = activeClass;
                if (subTabKanji) subTabKanji.className = inactiveClass;
                if (subTabGrammar) subTabGrammar.className = inactiveClass;
                if (subTabSpeaking) subTabSpeaking.className = inactiveClass;
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
    // Tiếng Nhật (gồm cả vocab, kanji, ngữ pháp, luyện nói), và các môn tự tạo
    const mainEntries = [
        {
            id: 'japanese',
            label: 'Tiếng Nhật',
            icon: '🇯🇵',
            isActive: currentSubjectId === 'japanese' || currentSubjectId === 'japanese_kanji' || currentSubjectId === 'japanese_grammar' || currentSubjectId === 'japanese_speaking',
            onSelect: () => {
                // Giữ lại môn con đang học hoặc chuyển sang japanese
                if (currentSubjectId !== 'japanese' && currentSubjectId !== 'japanese_kanji' && currentSubjectId !== 'japanese_grammar' && currentSubjectId !== 'japanese_speaking') {
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
function countMatchesGrammar(q) {
    if (currentSubject.quizType !== 'grammar' && currentSubjectId !== 'japanese_grammar') return true;
    if (currentQuizMode === 'concept') return q.grammarType === 'concept';
    if (currentQuizMode === 'translation') return q.grammarType === 'translation';
    return true;
}

function getFilteredQuestions() {
    return allQuestions.filter(q => {
        const matchLesson = (selectedLesson === 'all' || q.lesson === selectedLesson);
        const matchPart = (selectedPart === 'all' || q.part === selectedPart);
        const matchGrammar = countMatchesGrammar(q);
        return matchLesson && matchPart && matchGrammar;
    });
}

function switchQuizMode(mode) {
    if (mode && mode !== currentQuizMode) {
        currentQuizMode = mode;
        saveQuizModeState();
        updateQuizModeUI();
        renderLessonTabs();
        renderPartTabs();
        if (!ui.listScreen.classList.contains('hidden')) {
            renderListScreen();
        } else {
            startQuiz();
        }
    }
}

function updateQuizModeUI() {
    const quizContainer = document.getElementById('quiz-mode-container');
    const listContainer = document.getElementById('list-mode-container');
    const listToolbar = document.getElementById('list-mode-toolbar');
    const listDesc = document.getElementById('list-mode-desc');

    const isSpeaking = currentSubject.quizType === 'speaking' || currentSubjectId === 'japanese_speaking';
    const isGrammar = !isSpeaking && (currentSubject.quizType === 'grammar' || currentSubjectId === 'japanese_grammar');
    const isVocab = !isSpeaking && !isGrammar && currentSubject.quizType !== 'standard';

    let buttonsHTML = '';

    if (isSpeaking) {
        buttonsHTML = `
            <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition bg-blue-600 text-white shadow-sm" data-mode="standard">
                🗣️ Phản xạ nói (Hỏi ➔ Đáp & Hiện nghĩa)
            </button>
        `;
        currentQuizMode = 'standard';
        if (listToolbar) listToolbar.style.display = 'flex';
        if (listDesc) listDesc.innerText = '🗣️ Danh sách câu hỏi luyện nói tiếng Nhật (Bấm chọn câu để xem chi tiết & phát âm)';
    } else if (isGrammar) {
        const labels = currentSubject.modeLabels || {
            'all': '🌟 Tất cả (Cả 2 dạng)',
            'concept': '📖 Hỏi ngữ pháp là gì',
            'translation': '✍️ Dịch từ câu tiếng Việt qua'
        };

        buttonsHTML = `
            <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition" data-mode="all">
                ${labels['all']}
            </button>
            <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition" data-mode="concept">
                ${labels['concept']}
            </button>
            <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition" data-mode="translation">
                ${labels['translation']}
            </button>
        `;

        if (listToolbar) listToolbar.style.display = 'flex';
        if (listDesc) {
            if (currentQuizMode === 'concept') {
                listDesc.innerText = '📖 Chế độ: Chỉ hỏi ngữ pháp là gì (Cấu trúc & Quy tắc)';
            } else if (currentQuizMode === 'translation') {
                listDesc.innerText = '✍️ Chế độ: Chỉ dịch từ câu tiếng Việt sang tiếng Nhật';
            } else {
                listDesc.innerText = '🌟 Chế độ: Tất cả 2 dạng câu hỏi (Song hành)';
            }
        }
    } else if (isVocab) {
        const labels = currentSubject.modeLabels || {
            'jp-vi': `${currentSubject.icon || '📖'} ➔ 🇻🇳 ${currentSubject.name} - Việt`,
            'vi-jp': `🇻🇳 ➔ ${currentSubject.icon || '📖'} Việt - ${currentSubject.name}`,
            'mix': '🔀 Trộn cả hai'
        };

        buttonsHTML = '';
        Object.keys(labels).forEach(modeKey => {
            buttonsHTML += `
                <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition" data-mode="${modeKey}">
                    ${labels[modeKey]}
                </button>
            `;
        });

        if (listToolbar) listToolbar.style.display = 'flex';
        if (listDesc) {
            if (currentSubjectId === 'japanese_kanji') {
                if (currentQuizMode === 'write') {
                    listDesc.innerText = '✍️ Chế độ tự luận: Gõ cách đọc Hiragana cho từng chữ Hán';
                } else if (currentQuizMode === 'jp-vi') {
                    listDesc.innerText = '🈸 ➔ 🇻🇳 Chế độ trắc nghiệm: Chọn cách đọc & nghĩa từ chữ Hán';
                } else if (currentQuizMode === 'vi-jp') {
                    listDesc.innerText = '🇻🇳 ➔ 🈸 Chế độ trắc nghiệm: Chọn chữ Hán từ nghĩa tiếng Việt';
                } else {
                    listDesc.innerText = '🔀 Chế độ trắc nghiệm xáo trộn';
                }
            } else {
                listDesc.innerText = '';
            }
        }
    } else {
        buttonsHTML = `
            <button class="quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition bg-blue-600 text-white shadow-sm" data-mode="standard">
                📝 Trắc nghiệm tiêu chuẩn
            </button>
        `;
        currentQuizMode = 'standard';
        if (listToolbar) listToolbar.style.display = 'none';
    }

    [quizContainer, listContainer].forEach(cnt => {
        if (!cnt) return;
        cnt.innerHTML = buttonsHTML;
        cnt.querySelectorAll('.quiz-mode-btn').forEach(btn => {
            const mode = btn.getAttribute('data-mode');
            if (mode === currentQuizMode) {
                btn.className = "quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition bg-blue-600 text-white shadow-sm";
            } else {
                btn.className = "quiz-mode-btn px-3 py-1.5 text-xs md:text-sm font-bold rounded-md transition text-gray-600 hover:text-blue-600 hover:bg-blue-50";
            }

            btn.addEventListener('click', () => {
                switchQuizMode(mode);
            });
        });
    });
}

function updateQuestionDisplay() {
    if (!currentQuestion) return;
    const hideFurigana = currentSubject.hasFurigana && document.getElementById('toggle-furigana')?.checked;
    const isSpeaking = currentSubject.quizType === 'speaking' || currentSubjectId === 'japanese_speaking';

    if (currentQuestion.direction === 'write') {
        const meaningText = currentQuestion.meaning || '';
        ui.question.innerHTML = `
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
                <div class="flex items-baseline gap-2.5">
                    <span class="text-4xl sm:text-5xl font-black text-gray-900 tracking-wider font-serif select-none">${currentQuestion.prompt}</span>
                    <span class="text-xs text-gray-400 font-bold uppercase tracking-wider">(Hán tự)</span>
                </div>
                ${meaningText ? `
                    <div class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-blue-50 border border-blue-200 rounded-xl text-blue-900 text-xs sm:text-sm font-semibold shadow-2xs self-center sm:self-auto">
                        <span class="text-blue-600 font-bold">💡 Nghĩa:</span>
                        <span class="font-bold text-blue-800">${meaningText}</span>
                    </div>
                ` : ''}
            </div>
        `;
        return;
    }

    if (isSpeaking) {
        const promptText = hideFurigana 
            ? currentQuestion.prompt.replace(/\s*\([^)]+\)/g, '') 
            : currentQuestion.prompt;
        const safePrompt = promptText.replace(/'/g, "\\'");
        ui.question.innerHTML = `
            <div class="flex items-start justify-between gap-3">
                <span class="flex-1 text-lg sm:text-xl font-bold text-gray-800">${promptText}</span>
                <button type="button" onclick="speakJapanese('${safePrompt}')" class="shrink-0 inline-flex items-center gap-1.5 px-2.5 py-1 bg-blue-50 text-blue-600 hover:bg-blue-100 border border-blue-200 rounded-lg text-xs font-bold shadow-2xs active:scale-95 transition" title="Nghe câu hỏi">
                    <span>🔊</span> <span>Nghe</span>
                </button>
            </div>
        `;
        return;
    }

    if (currentQuestion.direction === 'jp-vi' || currentQuestion.direction === 'standard') {
        const displayText = hideFurigana 
            ? currentQuestion.prompt.replace(/\s*\([^)]+\)/g, '') 
            : currentQuestion.prompt;
        const safePrompt = displayText.replace(/'/g, "\\'");
        const isJapanese = currentSubjectId.startsWith('japanese');
        ui.question.innerHTML = `
            <div class="flex items-center justify-between gap-3">
                <span class="text-lg sm:text-xl font-bold text-gray-800">${displayText}</span>
                ${isJapanese ? `
                    <button type="button" onclick="speakJapanese('${safePrompt}')" class="shrink-0 inline-flex items-center gap-1 px-2.5 py-1 bg-blue-50 text-blue-600 hover:bg-blue-100 border border-blue-200 rounded-lg text-xs font-bold shadow-2xs active:scale-95 transition" title="Nghe phát âm">
                        <span>🔊</span> <span>Nghe</span>
                    </button>
                ` : ''}
            </div>
        `;
    } else {
        ui.question.innerHTML = `<span class="text-lg sm:text-xl font-bold text-gray-800">${currentQuestion.prompt}</span>`;
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

function formatSpeakingExplanation(expl, safeQuestion, safeCorrect, userSelected = null, isWrong = false) {
    const raw = expl || '';
    const qMatch = raw.match(/🗣️\s*Dịch câu hỏi:\s*["“]?(.*?)["”]?(\n|$)/i);
    const aMatch = raw.match(/💬\s*Dịch câu trả lời:\s*["“]?(.*?)["”]?(\n|$)/i);
    const qMeaning = qMatch ? qMatch[1].trim() : "";
    const aMeaning = aMatch ? aMatch[1].trim() : "";

    let otherAnswers = [];
    const otherMatch = raw.match(/🌟\s*Cách trả lời khác để luyện nói:([\s\S]*?)(?:💡|$)/i);
    if (otherMatch && otherMatch[1]) {
        otherAnswers = otherMatch[1].trim().split('\n').map(l => l.trim()).filter(l => l);
    }

    const tipMatch = raw.match(/💡\s*Mẹo(?:\s+giao\s+tiếp|\s+ngữ\s+pháp)?:\s*([\s\S]*)$/i);
    const tipText = tipMatch ? tipMatch[1].trim() : "";

    return `
        <div class="mt-3 space-y-3">
            ${isWrong && userSelected ? `
                <div class="p-3.5 bg-red-100/90 border-2 border-red-300 rounded-xl text-red-950 shadow-xs">
                    <div class="text-xs uppercase font-extrabold text-red-700 mb-1 flex items-center gap-1">
                        <span>⚠️</span> <span>Bạn đã chọn:</span>
                    </div>
                    <div class="text-base font-bold text-red-900 leading-snug">${userSelected}</div>
                </div>
            ` : ''}

            <!-- Câu hỏi hội thoại & Dịch nghĩa -->
            <div class="p-3.5 bg-blue-50/90 border border-blue-200 rounded-xl shadow-xs">
                <div class="flex items-center justify-between gap-2 mb-1.5">
                    <span class="text-xs uppercase font-extrabold text-blue-700 flex items-center gap-1">
                        <span>🗣️</span> <span>Câu hỏi hội thoại:</span>
                    </span>
                    <button type="button" onclick="event.stopPropagation(); speakJapanese('${safeQuestion}')" class="px-2.5 py-1 text-xs bg-white text-blue-600 border border-blue-200 rounded-lg hover:bg-blue-100 flex items-center gap-1 font-bold shadow-xs active:scale-95 transition">
                        <span>🔊</span> <span>Nghe câu hỏi</span>
                    </button>
                </div>
                <div class="text-base md:text-lg font-bold text-blue-950 mb-1 leading-snug">${safeQuestion}</div>
                ${qMeaning ? `<div class="text-xs md:text-sm text-blue-900 font-semibold bg-blue-100/70 p-2 rounded-lg">💬 Dịch nghĩa: "${qMeaning}"</div>` : ''}
            </div>

            <!-- Câu trả lời chuẩn & Dịch nghĩa -->
            <div class="p-3.5 bg-emerald-50/90 border-2 border-emerald-300 rounded-xl shadow-xs">
                <div class="flex items-center justify-between gap-2 mb-1.5">
                    <span class="text-xs uppercase font-extrabold text-emerald-700 flex items-center gap-1">
                        <span>💬</span> <span>Câu trả lời chuẩn (đơn giản, đúng trọng tâm):</span>
                    </span>
                    <button type="button" onclick="event.stopPropagation(); speakJapanese('${safeCorrect}')" class="px-2.5 py-1 text-xs bg-white text-emerald-700 border border-emerald-200 rounded-lg hover:bg-emerald-100 flex items-center gap-1 font-bold shadow-xs active:scale-95 transition">
                        <span>🔊</span> <span>Nghe câu đáp</span>
                    </button>
                </div>
                <div class="text-base md:text-lg font-bold text-emerald-950 mb-1 leading-snug">${safeCorrect}</div>
                ${aMeaning ? `<div class="text-xs md:text-sm text-emerald-900 font-semibold bg-emerald-100/80 p-2 rounded-lg">➔ Nghĩa: "${aMeaning}"</div>` : ''}
            </div>

            ${otherAnswers.length > 0 ? `
                <div class="p-3.5 bg-amber-50 border border-amber-200 rounded-xl text-xs md:text-sm text-amber-950 shadow-xs">
                    <div class="font-bold text-amber-900 flex items-center gap-1.5 mb-1.5">
                        <span>🌟</span> <span>Các cách trả lời thực tế khác:</span>
                    </div>
                    <ul class="space-y-1.5 pl-1 text-gray-800">
                        ${otherAnswers.map(ans => `<li class="flex items-start gap-1.5"><span class="text-amber-500 font-bold">•</span><span class="flex-1">${ans.replace(/^•\s*/, '')}</span></li>`).join('')}
                    </ul>
                </div>
            ` : ''}

            ${tipText ? `
                <div class="p-3.5 bg-indigo-50 border border-indigo-200 rounded-xl text-xs md:text-sm text-indigo-950 shadow-xs">
                    <div class="font-bold text-indigo-900 flex items-center gap-1.5 mb-1">
                        <span>💡</span> <span>Mẹo ngữ pháp & Cấu trúc:</span>
                    </div>
                    <div class="text-gray-800 leading-relaxed">${tipText}</div>
                </div>
            ` : ''}
        </div>
    `;
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
        qDiv.className = "p-3.5 sm:p-4 border border-slate-200 rounded-xl bg-white shadow-2xs hover:border-blue-300 transition-all";
        qDiv.setAttribute('data-qid', q.id);
        
        const isMarked = markedQuestions.includes(q.id);
        
        const header = document.createElement('div');
        header.className = "flex justify-between items-start gap-3 mb-2.5";

        let lessonInfo = '';
        if (q.lesson && q.lesson !== 'all') {
            const prefix = /^\d+$/.test(q.lesson) ? 'Bài ' : '';
            const partInfo = q.partTitle ? ` • Phần ${q.part}: ${q.partTitle}` : (q.part && q.part !== 'all' ? ` • Phần ${q.part}` : '');
            lessonInfo = `<span class="inline-block text-xs font-bold px-2 py-0.5 rounded bg-indigo-100 text-indigo-700 mb-1">${prefix}${q.lesson}${partInfo}</span>`;
        }

        const isSpeaking = currentSubject.quizType === 'speaking' || currentSubjectId === 'japanese_speaking' || q.speakingType;
        let badgeType = '';
        if (isSpeaking) {
            badgeType = `<span class="inline-block text-xs font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-800 border border-amber-200 mb-1">🗣️ Luyện nói</span>`;
        } else if (currentSubject.quizType === 'grammar' || currentSubjectId === 'japanese_grammar' || q.grammarType) {
            if (q.grammarType === 'concept') {
                badgeType = `<span class="inline-block text-xs font-bold px-2 py-0.5 rounded bg-purple-100 text-purple-700 border border-purple-200 mb-1">📖 Hỏi ngữ pháp là gì</span>`;
            } else if (q.grammarType === 'translation') {
                badgeType = `<span class="inline-block text-xs font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-700 border border-emerald-200 mb-1">✍️ Dịch từ câu tiếng Việt qua</span>`;
            }
        }

        const safeQuestionText = (q.question || '').replace(/'/g, "\\'");
        const safeCorrectText = (q.correct[0] || '').replace(/'/g, "\\'");
        const isKanji = currentSubjectId === 'japanese_kanji';
        let kanjiReading = '';
        if (isKanji && q.correct && q.correct[0]) {
            kanjiReading = q.correct[0].split(':')[0].trim();
        }
        const safeKanjiReading = kanjiReading.replace(/'/g, "\\'");
        const speakBtnHtml = isSpeaking
            ? `<button type="button" onclick="event.stopPropagation(); speakJapanese('${safeQuestionText}')" class="ml-2 inline-flex items-center gap-1 px-2.5 py-0.5 text-xs bg-blue-50 text-blue-600 border border-blue-200 rounded-md font-bold hover:bg-blue-100 active:scale-95 transition" title="Nghe câu hỏi"><span>🔊</span> <span>Nghe</span></button>`
            : (isKanji && kanjiReading ? `<button type="button" onclick="event.stopPropagation(); speakJapanese('${safeKanjiReading}')" class="ml-2 inline-flex items-center gap-1 px-2.5 py-0.5 text-xs bg-blue-50 text-blue-600 border border-blue-200 rounded-md font-bold hover:bg-blue-100 active:scale-95 transition" title="Nghe phát âm (${kanjiReading})"><span>🔊</span> <span>Nghe</span></button>` : '');

        header.innerHTML = `
            <div class="flex items-start gap-2.5 flex-1">
                <span class="inline-flex items-center justify-center min-w-7 h-7 sm:min-w-8 sm:h-8 rounded-full bg-blue-100 text-blue-700 font-bold text-xs sm:text-sm shadow-2xs">
                    ${index + 1}
                </span>
                <div class="flex-1">
                    <div class="flex items-center gap-1.5 flex-wrap">
                        ${lessonInfo}
                        ${badgeType}
                    </div>
                    <div class="flex items-baseline gap-1 flex-wrap">
                        <h3 class="font-bold text-gray-800 text-sm sm:text-base whitespace-pre-wrap">${q.question}</h3>
                        ${speakBtnHtml}
                    </div>
                </div>
            </div>
            <label class="flex items-center gap-1.5 cursor-pointer bg-white px-2.5 py-1 border border-slate-200 rounded-lg shadow-2xs hover:bg-blue-50 transition shrink-0">
                <input type="checkbox" class="mark-checkbox w-4 h-4 accent-blue-600 rounded" data-id="${q.id}" ${isMarked ? 'checked' : ''}>
                <span class="text-xs font-bold text-gray-700">Đã học</span>
            </label>
        `;
        
        const optionsDiv = document.createElement('div');
        optionsDiv.className = "space-y-1.5";
        q.options.forEach(opt => {
            const isCorrect = q.correct.includes(opt);
            const optDiv = document.createElement('div');
            optDiv.className = `p-2 sm:p-2.5 rounded-lg text-xs sm:text-sm ${isCorrect ? 'bg-green-100/90 font-bold border border-green-400 text-green-900' : 'bg-slate-50 border border-slate-200 text-gray-700'}`;
            optDiv.innerHTML = `${isCorrect ? '✅ ' : '⬜ '}${opt}`;
            optionsDiv.appendChild(optDiv);
        });
        
        qDiv.appendChild(header);
        qDiv.appendChild(optionsDiv);
        if (q.explanation && !q.explanation.startsWith('→ Đáp án:')) {
            const isGrammar = currentSubject.quizType === 'grammar' || currentSubjectId === 'japanese_grammar';
            const isSpeakingQ = isSpeaking;
            const explDiv = document.createElement('div');

            if (isSpeakingQ) {
                explDiv.className = "mt-3";
                explDiv.innerHTML = formatSpeakingExplanation(q.explanation, safeQuestionText, safeCorrectText);
            } else {
                explDiv.className = isGrammar
                    ? "mt-3 p-3.5 bg-indigo-50 border border-indigo-200 rounded-lg text-xs md:text-sm text-indigo-950 leading-relaxed shadow-sm"
                    : "mt-3 p-3 bg-blue-50 border border-blue-200 rounded-lg text-xs md:text-sm text-blue-900 leading-relaxed";
                
                const formatted = q.explanation
                    .replace(/➔/g, '<br>➔')
                    .replace(/📌/g, '<br>📌');
                
                explDiv.innerHTML = isGrammar 
                    ? `<div class="font-bold text-indigo-900 mb-1 flex items-center gap-1"><span>📐</span> <span>Cấu trúc ngữ pháp & Giải thích:</span></div><div class="text-gray-800 leading-relaxed">${formatted}</div>`
                    : `💡 <b>Giải thích:</b> ${q.explanation}`;
            }
            qDiv.appendChild(explDiv);
        }
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
    const isSpeaking = currentSubject.quizType === 'speaking' || currentSubjectId === 'japanese_speaking';
    const isGrammar = !isSpeaking && (currentSubject.quizType === 'grammar' || currentSubjectId === 'japanese_grammar');
    const isReverse = (!isSpeaking && !isGrammar && direction === 'vi-jp' && currentSubject.quizType !== 'standard');
    const isWrite = (!isSpeaking && !isGrammar && direction === 'write');

    if (isWrite) {
        let targetReading = '';
        let targetMeaning = '';
        if (baseQ.correct && baseQ.correct[0]) {
            const parts = baseQ.correct[0].split(':');
            targetReading = parts[0].trim();
            targetMeaning = (parts[1] || '').trim();
        }
        return {
            id: baseQ.id,
            direction: 'write',
            prompt: baseQ.question,
            kanji: baseQ.question,
            reading: targetReading,
            meaning: targetMeaning,
            options: [],
            correct: [targetReading],
            lesson: baseQ.lesson,
            part: baseQ.part,
            partTitle: baseQ.partTitle,
            type: 'text',
            correctPrimary: baseQ.question,
            correctSecondary: baseQ.correct[0],
            // Giữ alias cho Tiếng Nhật
            correctJapanese: targetReading,
            correctVietnamese: targetMeaning,
            baseQ: baseQ
        };
    } else if (isReverse) {
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
            direction: isSpeaking || isGrammar || direction === 'standard' ? 'standard' : 'jp-vi',
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
        if (currentSubject.quizType === 'speaking' || currentSubject.quizType === 'grammar' || currentSubject.quizType === 'standard') {
            dir = 'standard';
        } else if (dir === 'mix') {
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
            const prefix = /^\d+$/.test(currentQuestion.lesson) ? 'Bài ' : '';
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

        if (currentSubjectId === 'japanese_speaking' || currentSubject.quizType === 'speaking') {
            ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-amber-100 text-amber-800 rounded-full inline-flex items-center gap-1 border border-amber-300";
            ui.directionBadge.innerHTML = "<span>🗣️</span><span>Luyện phản xạ nói: Chọn câu đáp phù hợp (bấm chọn hiện dịch nghĩa)</span>";
        } else if (currentSubjectId === 'japanese_kanji') {
            if (currentQuestion.direction === 'vi-jp') {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full inline-flex items-center gap-1 border border-emerald-300";
                ui.directionBadge.innerHTML = "<span>🇻🇳 ➔ 🈸</span><span>Chọn chữ Hán tương ứng</span>";
            } else if (currentQuestion.direction === 'write') {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-amber-100 text-amber-800 rounded-full inline-flex items-center gap-1 border border-amber-300";
                ui.directionBadge.innerHTML = "<span>✍️ 🈸 ➔ あ</span><span>Tự luận: Gõ cách đọc Hiragana của chữ Hán</span>";
            } else {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-blue-100 text-blue-800 rounded-full inline-flex items-center gap-1 border border-blue-200";
                ui.directionBadge.innerHTML = "<span>🈸 ➔ 🇻🇳</span><span>Chọn cách đọc & nghĩa của từ này</span>";
            }
        } else if (currentSubjectId === 'japanese_grammar' || currentSubject.quizType === 'grammar') {
            const gType = currentQuestion.baseQ?.grammarType;
            if (gType === 'concept') {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-purple-100 text-purple-800 rounded-full inline-flex items-center gap-1 border border-purple-300";
                ui.directionBadge.innerHTML = "<span>📖</span><span>Hỏi ngữ pháp là gì: Chọn quy tắc & cách dùng đúng</span>";
            } else if (gType === 'translation') {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full inline-flex items-center gap-1 border border-emerald-300";
                ui.directionBadge.innerHTML = "<span>🇻🇳 ➔ 🇯🇵</span><span>Dịch câu: Chọn câu tiếng Nhật đúng cho câu tiếng Việt</span>";
            } else {
                ui.directionBadge.className = "text-xs font-bold px-3 py-1 bg-indigo-100 text-indigo-800 rounded-full inline-flex items-center gap-1 border border-indigo-200";
                ui.directionBadge.innerHTML = "<span>📐</span><span>Chọn đáp án đúng ngữ pháp</span>";
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
        ui.qTypeBadge.className = "text-xs font-bold px-2 py-1 bg-yellow-100 text-yellow-800 rounded inline-block";
        ui.qTypeBadge.innerText = `CHỌN ${currentQuestion.correct.length} ĐÁP ÁN`;
    } else if (currentQuestion.type === 'text') {
        ui.qTypeBadge.classList.remove('hidden');
        ui.qTypeBadge.className = "text-xs font-bold px-2.5 py-1 bg-amber-100 text-amber-800 rounded inline-block";
        ui.qTypeBadge.innerText = "TỰ LUẬN (GÕ HIRAGANA)";
    } else {
        ui.qTypeBadge.classList.add('hidden');
    }
    
    ui.options.innerHTML = "";

    // Chế độ tự luận: Hiển thị ô nhập văn bản Hiragana
    if (currentQuestion.type === 'text') {
        ui.options.innerHTML = `
            <div class="space-y-2.5">
                <div class="bg-slate-50 p-3 sm:p-4 rounded-xl border border-slate-300 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-100 transition shadow-2xs">
                    <div class="flex items-center justify-between mb-1.5">
                        <label for="kanji-input-answer" class="text-xs sm:text-sm font-bold text-gray-700 flex items-center gap-1.5">
                            <span>⌨️</span> <span>Cách đọc Hiragana:</span>
                        </label>
                        <span class="text-[11px] text-gray-400 font-medium hidden sm:inline">Nhấn Enter để kiểm tra</span>
                    </div>
                    <div class="relative">
                        <input 
                            type="text" 
                            id="kanji-input-answer" 
                            class="w-full text-xl sm:text-2xl font-bold py-2.5 px-3.5 bg-white border-2 border-gray-300 rounded-xl focus:outline-none focus:border-blue-600 focus:ring-2 focus:ring-blue-100 text-gray-800 transition shadow-inner font-sans tracking-wide"
                            placeholder="vd: ひがし" 
                            autocomplete="off" 
                            autocapitalize="none" 
                            spellcheck="false"
                        />
                        <button type="button" id="kanji-clear-input-btn" class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 w-7 h-7 flex items-center justify-center rounded-full hover:bg-gray-100 transition hidden text-sm font-bold" title="Xóa">
                            ✕
                        </button>
                    </div>
                    
                    <div class="mt-2.5 flex items-center justify-between text-xs text-gray-500 flex-wrap gap-2 pt-2 border-t border-slate-200">
                        <label class="flex items-center gap-1.5 cursor-pointer select-none text-gray-600 hover:text-blue-600 font-medium text-xs">
                            <input type="checkbox" id="toggle-romaji-convert" checked class="w-3.5 h-3.5 accent-blue-600 rounded">
                            <span>Tự chuyển Romaji ➔ Hiragana khi gõ (vd: gõ "higashi" ra "ひがし")</span>
                        </label>
                    </div>
                </div>

                <div class="flex gap-2.5">
                    <button type="button" id="kanji-check-btn" class="flex-1 bg-blue-600 hover:bg-blue-700 active:scale-98 text-white font-bold py-2.5 sm:py-3 px-4 rounded-xl shadow-md transition flex items-center justify-center gap-2 text-sm sm:text-base cursor-pointer">
                        <span>Kiểm tra đáp án</span>
                        <kbd class="hidden sm:inline-block px-2 py-0.5 text-xs bg-blue-700 text-blue-100 rounded font-mono shadow-xs">↵ Enter</kbd>
                    </button>
                    <button type="button" id="kanji-giveup-btn" class="px-3.5 py-2.5 sm:py-3 bg-gray-100 hover:bg-gray-200 active:scale-98 text-gray-700 font-bold rounded-xl border border-gray-300 shadow-2xs transition text-xs sm:text-sm whitespace-nowrap cursor-pointer" title="Bỏ cuộc và xem đáp án câu này">
                        <span>👀 Xem đáp án</span>
                    </button>
                </div>
            </div>
        `;

        const inputEl = document.getElementById('kanji-input-answer');
        const clearBtn = document.getElementById('kanji-clear-input-btn');
        const checkBtn = document.getElementById('kanji-check-btn');
        const giveupBtn = document.getElementById('kanji-giveup-btn');
        const romajiToggle = document.getElementById('toggle-romaji-convert');

        const savedRomajiPref = localStorage.getItem('romaji_convert_pref');
        if (savedRomajiPref !== null && romajiToggle) {
            romajiToggle.checked = savedRomajiPref === 'true';
        }
        if (romajiToggle) {
            romajiToggle.addEventListener('change', () => {
                localStorage.setItem('romaji_convert_pref', String(romajiToggle.checked));
                if (inputEl) inputEl.focus();
            });
        }

        if (inputEl) {
            setTimeout(() => inputEl.focus(), 60);

            let isComposing = false;
            inputEl.addEventListener('compositionstart', () => { isComposing = true; });
            inputEl.addEventListener('compositionend', () => { isComposing = false; });

            inputEl.addEventListener('input', () => {
                if (clearBtn) {
                    clearBtn.classList.toggle('hidden', !inputEl.value);
                }
                if (isComposing) return;
                if (!romajiToggle || !romajiToggle.checked) return;

                const cursor = inputEl.selectionStart;
                const originalVal = inputEl.value;
                const convertedVal = convertRomajiToHiragana(originalVal, false);

                if (convertedVal !== originalVal) {
                    inputEl.value = convertedVal;
                    const diff = convertedVal.length - originalVal.length;
                    const newPos = Math.max(0, cursor + diff);
                    inputEl.setSelectionRange(newPos, newPos);
                }
            });

            inputEl.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    checkAnswerWrite();
                }
            });
        }

        if (clearBtn && inputEl) {
            clearBtn.addEventListener('click', () => {
                inputEl.value = '';
                clearBtn.classList.add('hidden');
                inputEl.focus();
            });
        }

        if (checkBtn) {
            checkBtn.addEventListener('click', () => checkAnswerWrite());
        }

        if (giveupBtn) {
            giveupBtn.addEventListener('click', () => checkAnswerWrite(true));
        }

        updateQuestionDisplay();
        ui.feedback.classList.add('hidden');
        ui.nextBtn.classList.add('hidden');
        ui.skipBtn.classList.remove('hidden');
        return;
    }
    const hideFurigana = currentSubject.hasFurigana && document.getElementById('toggle-furigana')?.checked;

    currentQuestion.options.forEach((opt, index) => {
        const label = document.createElement('label');
        label.className = "flex items-center p-3 sm:p-3.5 border-2 border-gray-200/80 rounded-xl cursor-pointer hover:border-blue-400 hover:bg-blue-50/60 transition bg-white shadow-2xs";
        const inputType = currentQuestion.type;
        const inputClass = inputType === 'radio' ? 'rounded-full' : 'rounded';

        const displayOptText = (currentQuestion.direction === 'vi-jp' && hideFurigana)
            ? opt.replace(/\s*\([^)]+\)/g, '')
            : opt;

        label.innerHTML = `
            <input type="${inputType}" name="answer" value="${opt.replace(/"/g, '&quot;')}" class="mr-3 w-4 h-4 sm:w-5 sm:h-5 cursor-pointer accent-blue-600 ${inputClass} shrink-0">
            <span class="text-gray-800 font-semibold text-sm sm:text-base flex items-center gap-2 flex-1">
                <span class="inline-flex items-center justify-center w-5 h-5 sm:w-6 sm:h-6 text-xs font-bold text-gray-500 bg-gray-100 rounded-md shadow-2xs shrink-0">${index + 1}</span>
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

    document.querySelectorAll('input[name="answer"]').forEach(inp => {
        inp.disabled = true;
        const parentLabel = inp.closest('label');
        if (!parentLabel) return;
        const val = inp.value;
        const isRightOpt = currentQuestion.correct.includes(val);
        const isUserChecked = inp.checked;

        if (isRightOpt) {
            parentLabel.className = "flex items-center p-3 sm:p-3.5 border-2 border-green-500 bg-green-50/90 rounded-xl transition shadow-2xs text-green-950 font-bold";
        } else if (isUserChecked) {
            parentLabel.className = "flex items-center p-3 sm:p-3.5 border-2 border-red-400 bg-red-50/90 rounded-xl transition shadow-2xs text-red-950 font-semibold opacity-90";
        } else {
            parentLabel.className = "flex items-center p-3 sm:p-3.5 border-2 border-gray-100 bg-gray-50/60 rounded-xl opacity-60";
        }
    });

    const isSpeaking = currentSubject.quizType === 'speaking' || currentSubjectId === 'japanese_speaking';
    const isGrammar = !isSpeaking && (currentSubject.quizType === 'grammar' || currentSubjectId === 'japanese_grammar');
    const isVocab = !isSpeaking && !isGrammar && currentSubject.quizType !== 'standard';

    if (isCorrect) {
        if (isSpeaking) {
            ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-green-50 text-green-900 border-2 border-green-300 shadow-sm";
            ui.feedbackTitle.innerText = "✅ Phản xạ chính xác! Đã trả lời đúng ngữ cảnh.";
            const expl = currentQuestion.baseQ?.explanation || '';
            const safePrompt = (currentQuestion.prompt || '').replace(/'/g, "\\'");
            const safeCorrect = (currentQuestion.correct[0] || '').replace(/'/g, "\\'");
            const safeSelected = (selected[0] || '').replace(/'/g, "\\'");
            ui.feedbackText.innerHTML = `
                ${formatSpeakingExplanation(expl, safePrompt, safeCorrect, safeSelected, false)}
                <p class="text-xs text-green-600 mt-2.5 font-normal">Tuyệt vời, câu này sẽ không lặp lại nữa.</p>
            `;
            reviewQueue.shift();
        } else if (isGrammar) {
            ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-green-50 text-green-800 border-2 border-green-200 shadow-sm";
            ui.feedbackTitle.innerText = "✅ Chính xác!";
            const expl = currentQuestion.baseQ?.explanation;
            const hasExpl = expl && !expl.startsWith('→ Đáp án:');
            let explHtml = '';
            if (hasExpl) {
                const formatted = expl
                    .replace(/➔/g, '<br>➔')
                    .replace(/📌/g, '<br>📌')
                    .replace(/💡/g, '');
                explHtml = `
                    <div class="mt-2.5 p-3 bg-white border border-green-300 rounded-xl text-sm text-green-950 leading-relaxed shadow-xs">
                        <div class="font-bold text-green-900 flex items-center gap-1.5 mb-1">
                            <span class="text-base">📐</span> <span>Cấu trúc ngữ pháp & Quy tắc:</span>
                        </div>
                        <div class="text-gray-800 text-sm leading-relaxed">
                            ${formatted}
                        </div>
                    </div>
                `;
            }

            ui.feedbackText.innerHTML = `
                <div class="mt-0.5">
                    <span class="text-xs uppercase font-bold text-green-700">Đáp án đúng:</span>
                    <div class="text-base font-bold text-green-900 mt-0.5">${currentQuestion.correct.join(', ')}</div>
                </div>
                ${explHtml}
                <p class="text-xs text-green-600 mt-2 font-normal">Tuyệt vời, câu này sẽ không lặp lại nữa.</p>
            `;
            reviewQueue.shift();
        } else if (isVocab) {
            ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-green-50 text-green-800 border-2 border-green-200 shadow-sm";
            ui.feedbackTitle.innerText = "✅ Chính xác!";
            ui.feedbackText.innerHTML = `
                <div class="mt-1 flex items-baseline gap-2 flex-wrap">
                    <span class="text-xl font-bold text-green-900">${currentQuestion.correctPrimary}</span>
                    <span class="text-gray-400">•</span>
                    <span class="text-base font-semibold text-green-800">${currentQuestion.correctSecondary}</span>
                </div>
                <p class="text-xs text-green-600 mt-2 font-normal">Tuyệt vời, câu này sẽ không lặp lại nữa.</p>
            `;
            reviewQueue.shift();
        } else {
            ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-green-50 text-green-800 border-2 border-green-200 shadow-sm";
            ui.feedbackTitle.innerText = "✅ Chính xác!";
            const expl = currentQuestion.baseQ?.explanation;
            const hasExpl = expl && !expl.startsWith('→ Đáp án:');
            ui.feedbackText.innerHTML = `
                <div class="mt-1 font-semibold text-green-900">
                    Đáp án đúng: ${currentQuestion.correct.join(', ')}
                </div>
                ${hasExpl ? `<div class="mt-2 text-xs md:text-sm bg-white p-2.5 rounded-xl border border-green-300 text-green-900 leading-relaxed shadow-xs">💡 <b>Giải thích chi tiết:</b> ${expl}</div>` : ''}
                <p class="text-xs text-green-600 mt-2 font-normal">Tuyệt vời, câu này sẽ không lặp lại nữa.</p>
            `;
            reviewQueue.shift();
        }
    } else {
        if (isSpeaking) {
            ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-red-50 text-red-900 border-2 border-red-300 shadow-sm";
            ui.feedbackTitle.innerText = "❌ Chưa chính xác! Câu trả lời phù hợp & nghĩa:";
            const expl = currentQuestion.baseQ?.explanation || '';
            const safePrompt = (currentQuestion.prompt || '').replace(/'/g, "\\'");
            const safeCorrect = (currentQuestion.correct[0] || '').replace(/'/g, "\\'");
            const safeSelected = (selected[0] || '').replace(/'/g, "\\'");
            ui.feedbackText.innerHTML = `
                ${formatSpeakingExplanation(expl, safePrompt, safeCorrect, safeSelected, true)}
                <p class="text-xs text-red-600 mt-2.5 font-normal">Câu này sẽ lặp lại ở cuối danh sách để bạn luyện tập.</p>
            `;
        } else if (isGrammar) {
            ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-red-50 text-red-800 border-2 border-red-200 shadow-sm";
            ui.feedbackTitle.innerText = "❌ Sai rồi! Đáp án đúng:";
            const expl = currentQuestion.baseQ?.explanation;
            const hasExpl = expl && !expl.startsWith('→ Đáp án:');
            let explHtml = '';
            if (hasExpl) {
                const formatted = expl
                    .replace(/➔/g, '<br>➔')
                    .replace(/📌/g, '<br>📌')
                    .replace(/💡/g, '');
                explHtml = `
                    <div class="mt-2.5 p-3 bg-red-50/80 border border-red-200 rounded-xl text-sm text-red-950 leading-relaxed shadow-xs">
                        <div class="font-bold text-red-900 flex items-center gap-1.5 mb-1">
                            <span class="text-base">📐</span> <span>Cấu trúc ngữ pháp & Quy tắc:</span>
                        </div>
                        <div class="text-gray-800 text-sm leading-relaxed">
                            ${formatted}
                        </div>
                    </div>
                `;
            }

            ui.feedbackText.innerHTML = `
                <div class="mt-1 p-3 bg-white rounded-xl border border-red-200 shadow-xs">
                    <span class="text-xs uppercase font-bold text-red-700">Đáp án đúng:</span>
                    <div class="text-base font-bold text-red-900 mt-0.5 mb-1">${currentQuestion.correct.join(', ')}</div>
                    ${explHtml}
                </div>
                <p class="text-xs text-red-600 mt-2 font-normal">Câu này sẽ lặp lại ở cuối danh sách để bạn luyện tập.</p>
            `;
        } else if (isVocab) {
            ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-red-50 text-red-800 border-2 border-red-200 shadow-sm";
            ui.feedbackTitle.innerText = "❌ Sai rồi! Đáp án đúng:";
            ui.feedbackText.innerHTML = `
                <div class="mt-1.5 p-3 bg-white rounded-xl border border-red-200 shadow-xs">
                    <div class="text-lg sm:text-xl font-bold text-red-900 mb-0.5">${currentQuestion.correctPrimary}</div>
                    <div class="text-sm font-semibold text-gray-700">Nghĩa: <span class="text-red-700 font-bold">${currentQuestion.correctSecondary}</span></div>
                </div>
                <p class="text-xs text-red-600 mt-2 font-normal">Câu này sẽ lặp lại ở cuối danh sách để bạn luyện tập.</p>
            `;
        } else {
            ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-red-50 text-red-800 border-2 border-red-200 shadow-sm";
            ui.feedbackTitle.innerText = "❌ Sai rồi! Đáp án đúng:";
            const expl = currentQuestion.baseQ?.explanation;
            const hasExpl = expl && !expl.startsWith('→ Đáp án:');
            ui.feedbackText.innerHTML = `
                <div class="mt-1.5 p-3 bg-white rounded-xl border border-red-200 shadow-xs">
                    <div class="text-base font-bold text-red-900 mb-0.5">Đáp án đúng: ${currentQuestion.correct.join(', ')}</div>
                    ${hasExpl ? `<div class="mt-2 text-xs md:text-sm bg-red-50 p-2.5 rounded-xl border border-red-200 text-red-900 leading-relaxed">💡 <b>Giải thích chi tiết:</b> ${expl}</div>` : ''}
                </div>
                <p class="text-xs text-red-600 mt-2 font-normal">Câu này sẽ lặp lại ở cuối danh sách để bạn luyện tập.</p>
            `;
        }
        
        const failedItem = reviewQueue.shift();
        reviewQueue.push(failedItem);
    }

    setTimeout(() => {
        if (ui.nextBtn) ui.nextBtn.focus();
    }, 60);
}

function checkAnswerWrite(isGiveUp = false) {
    if (!currentQuestion || currentQuestion.type !== 'text') return;

    const inputEl = document.getElementById('kanji-input-answer');
    const checkBtn = document.getElementById('kanji-check-btn');
    const giveupBtn = document.getElementById('kanji-giveup-btn');
    if (!inputEl) return;

    let userRaw = inputEl.value.trim();
    if (!userRaw && !isGiveUp) {
        inputEl.focus();
        inputEl.classList.add('ring-4', 'ring-amber-300');
        setTimeout(() => inputEl.classList.remove('ring-4', 'ring-amber-300'), 800);
        return;
    }

    // Chuyển đổi ký tự Romaji còn sót lại (ví dụ chữ 'n' cuối từ)
    userRaw = convertRomajiToHiragana(userRaw, true);
    inputEl.value = userRaw;

    const targetReading = currentQuestion.reading || (currentQuestion.correct && currentQuestion.correct[0] ? currentQuestion.correct[0].split(':')[0].trim() : '');
    const targetMeaning = currentQuestion.meaning || (currentQuestion.correctSecondary ? (currentQuestion.correctSecondary.split(':')[1] || '').trim() : '');
    const normUser = normalizeKana(userRaw);
    const normTarget = normalizeKana(targetReading);

    const isCorrect = !isGiveUp && (normUser === normTarget);

    inputEl.disabled = true;
    if (checkBtn) checkBtn.disabled = true;
    if (giveupBtn) giveupBtn.disabled = true;

    ui.skipBtn.classList.add('hidden');
    ui.feedback.classList.remove('hidden');
    ui.nextBtn.classList.remove('hidden');

    const safeReading = targetReading.replace(/'/g, "\\'");

    if (isCorrect) {
        inputEl.className = "w-full text-xl sm:text-2xl font-bold py-2.5 px-3.5 bg-green-50 border-2 border-green-500 rounded-xl text-green-900 font-sans tracking-wide shadow-inner";
        ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-green-50 text-green-900 border-2 border-green-300 shadow-sm";
        ui.feedbackTitle.innerText = "✅ Chính xác!";

        ui.feedbackText.innerHTML = `
            <div class="mt-1.5 p-3 sm:p-3.5 bg-white rounded-xl border border-green-200 shadow-xs space-y-1.5">
                <div class="flex items-center gap-3 flex-wrap">
                    <span class="text-3xl font-black text-green-900 font-serif">${currentQuestion.kanji || currentQuestion.prompt}</span>
                    <span class="text-2xl font-bold text-green-700">${targetReading}</span>
                    <button type="button" onclick="speakJapanese('${safeReading}')" class="px-2.5 py-1 text-xs bg-green-100 hover:bg-green-200 text-green-800 rounded-lg font-bold transition flex items-center gap-1 shadow-2xs active:scale-95" title="Nghe phát âm">
                        <span>🔊</span> <span>Nghe phát âm</span>
                    </button>
                </div>
                ${targetMeaning ? `<div class="text-sm font-semibold text-gray-700">Nghĩa tiếng Việt: <span class="text-green-800 font-bold">${targetMeaning}</span></div>` : ''}
            </div>
            <p class="text-xs text-green-600 mt-2 font-normal">Tuyệt vời, câu này sẽ không lặp lại nữa.</p>
        `;

        speakJapanese(targetReading);
        reviewQueue.shift();
    } else {
        inputEl.className = "w-full text-xl sm:text-2xl font-bold py-2.5 px-3.5 bg-red-50 border-2 border-red-400 rounded-xl text-red-900 font-sans tracking-wide shadow-inner";
        ui.feedback.className = "p-4 sm:p-5 rounded-2xl bg-red-50 text-red-900 border-2 border-red-300 shadow-sm";
        ui.feedbackTitle.innerText = isGiveUp ? "👀 Đáp án câu này:" : "❌ Chưa chính xác! Đáp án đúng:";

        ui.feedbackText.innerHTML = `
            <div class="mt-1.5 p-3 sm:p-3.5 bg-white rounded-xl border border-red-200 shadow-xs space-y-2">
                ${!isGiveUp ? `
                    <div class="text-xs text-red-600 font-bold flex items-center gap-1.5">
                        <span>Bạn đã nhập:</span> 
                        <span class="text-sm font-extrabold text-red-800 bg-red-50 px-2.5 py-0.5 rounded border border-red-200">${userRaw || '(để trống)'}</span>
                    </div>
                ` : ''}
                <div class="flex items-center gap-3 pt-1 border-t border-gray-100 flex-wrap">
                    <span class="text-3xl font-black text-gray-900 font-serif">${currentQuestion.kanji || currentQuestion.prompt}</span>
                    <span class="text-2xl font-bold text-red-700">${targetReading}</span>
                    <button type="button" onclick="speakJapanese('${safeReading}')" class="px-2.5 py-1 text-xs bg-red-100 hover:bg-red-200 text-red-800 rounded-lg font-bold transition flex items-center gap-1 shadow-2xs active:scale-95" title="Nghe phát âm">
                        <span>🔊</span> <span>Nghe phát âm</span>
                    </button>
                </div>
                ${targetMeaning ? `<div class="text-sm font-semibold text-gray-700">Nghĩa tiếng Việt: <span class="text-red-800 font-bold">${targetMeaning}</span></div>` : ''}
            </div>
            <p class="text-xs text-red-600 mt-2 font-normal">Câu này sẽ lặp lại ở cuối bài để bạn luyện tập lại.</p>
        `;

        speakJapanese(targetReading);
        const failedItem = reviewQueue.shift();
        reviewQueue.push(failedItem);
    }

    setTimeout(() => {
        if (ui.nextBtn) ui.nextBtn.focus();
    }, 60);
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
            count = allQuestions.filter(countMatchesGrammar).length;
        } else {
            const prefix = /^\d+$/.test(les) ? 'Bài ' : '';
            label = `${prefix}${les}`;
            count = allQuestions.filter(q => q.lesson === les && countMatchesGrammar(q)).length;
        }

        const isActive = selectedLesson === les;
        const btn = document.createElement('button');
        btn.setAttribute('data-lesson', les);
        btn.className = `lesson-tab px-3 py-1 rounded-full font-bold text-xs sm:text-sm shadow-2xs transition border-2 ${
            isActive
                ? 'border-indigo-600 bg-indigo-600 text-white shadow-xs'
                : 'border-indigo-200 bg-white text-indigo-700 hover:bg-indigo-50'
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
            count = allQuestions.filter(q => (selectedLesson === 'all' || q.lesson === selectedLesson) && countMatchesGrammar(q)).length;
        } else {
            const title = (selectedLesson !== 'all' && lessonPartsDict[selectedLesson]?.[p])
                ? `: ${lessonPartsDict[selectedLesson][p]}`
                : '';
            label = `Phần ${p}${title}`;
            count = allQuestions.filter(q => (selectedLesson === 'all' || q.lesson === selectedLesson) && q.part === p && countMatchesGrammar(q)).length;
        }

        const btn = document.createElement('button');
        btn.setAttribute('data-part', p);
        const isActive = selectedPart === p;
        btn.className = `part-tab px-2.5 py-1 rounded-full font-semibold text-xs shadow-2xs transition border-2 ${
            isActive 
                ? 'border-emerald-600 bg-emerald-600 text-white shadow-xs' 
                : 'border-emerald-200 bg-white text-emerald-700 hover:bg-emerald-50'
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

    // 4. Sự kiện Furigana & Tốc độ phát âm
    document.getElementById('toggle-furigana')?.addEventListener('change', () => {
        updateQuestionDisplay();
    });

    document.querySelectorAll('.speech-rate-select').forEach(sel => {
        sel.value = String(currentSpeechRate);
        sel.addEventListener('change', (e) => {
            setSpeechRate(e.target.value);
        });
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

    document.getElementById('sub-tab-grammar')?.addEventListener('click', () => {
        if (currentSubjectId !== 'japanese_grammar') {
            switchSubject('japanese_grammar');
        }
    });

    document.getElementById('sub-tab-speaking')?.addEventListener('click', () => {
        if (currentSubjectId !== 'japanese_speaking') {
            switchSubject('japanese_speaking');
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
            const isTyping = e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA');

            // Khi đang hiện kết quả feedback (đã trả lời xong), bấm Enter để chuyển ngay câu tiếp theo
            if (e.key === 'Enter') {
                if (!ui.feedback.classList.contains('hidden')) {
                    e.preventDefault();
                    handleNextAction();
                    return;
                }
            }

            // Nếu đang gõ trong ô nhập tự luận, không can thiệp phím số và phím mũi tên
            if (isTyping) {
                return;
            }

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
