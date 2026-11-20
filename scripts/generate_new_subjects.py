import os
import re
import json
import pptx

SOURCE_DIR = r"C:\Users\TUF FX506\Desktop\GoogleSlides_Clones"
OUTPUT_DIR = r"c:\Users\TUF FX506\Downloads\quizlet\js"

def clean_text(t):
    if not t:
        return ''
    return re.sub(r'[\u200b\u200c\u200d\uFEFF\xa0\ufffd]', '', t).strip()

def escape_template_literal(s):
    if not s:
        return ''
    # Escape backticks and ${} for JS template strings
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

SUBJECT_CONFIGS = {
    'csd': {
        'filename': 'SEMESTER_4_CSD201.pptx',
        'var_name': 'CSD',
        'sub_id': 'csd',
        'name': 'CSD201 (CTDL & GT)',
        'fullName': 'CSD201 - Data Structures & Algorithms (304 câu Slide)',
        'icon': '🌳',
        'badge': 'CSD201 • 304 câu',
        'category': 'software_engineering',
        'image_folder': 'images/csd',
        'js_file': 'csd_data.js',
        'lang_from': 'Slide câu hỏi CSD201',
        'lang_to': 'Đáp án & Giải thích',
        'mode_label': '📝 Trắc nghiệm Slide CSD201',
        'dividers': {
            17: ('1. Đúng / Sai', 'Đúng / Sai (True / False)'),
            28: ('2. Thuật toán', 'Thuật toán & Cấu trúc dữ liệu (Algorithm)'),
            269: ('3. Độ phức tạp', 'Độ phức tạp thuật toán (Complexity)'),
            286: ('4. Câu hỏi ngắn', 'Câu hỏi ngắn lý thuyết (Short Question)'),
            313: ('5. Ôn tập tổng hợp', 'Ôn tập tổng hợp nâng cao')
        }
    },
    'prj': {
        'filename': 'SEMESTER_4_PRJ301&amp;302.pptx',
        'var_name': 'PRJ',
        'sub_id': 'prj',
        'name': 'PRJ301 (Java Web)',
        'fullName': 'PRJ301 & PRJ302 - Java Web Application (396 câu Slide)',
        'icon': '☕',
        'badge': 'PRJ301 • 396 câu',
        'category': 'software_engineering',
        'image_folder': 'images/prj',
        'js_file': 'prj_data.js',
        'lang_from': 'Slide câu hỏi PRJ301',
        'lang_to': 'Đáp án & Giải thích',
        'mode_label': '📝 Trắc nghiệm Slide PRJ301',
        'dividers': {
            10: ('1. 2 - 3 đáp án', 'Dạng 2 - 3 đáp án đúng (Multi-select)'),
            20: ('2. Cú pháp & Code', 'Cú pháp & Code (Syntax)'),
            164: ('3. Câu ngắn', 'Câu hỏi ngắn lý thuyết (Short Question)'),
            248: ('4. Câu trung bình', 'Câu hỏi trung bình (Medium Question)'),
            336: ('5. Câu dài', 'Câu hỏi dài & Tình huống (Long Question)'),
            408: ('6. NOT Question', 'Câu hỏi phủ định NOT')
        }
    },
    'iot': {
        'filename': 'SEMESTER_4_IOT102.pptx',
        'var_name': 'IOT',
        'sub_id': 'iot',
        'name': 'IOT102 (Internet of Things)',
        'fullName': 'IOT102 - Internet of Things (346 câu Slide)',
        'icon': '🌐',
        'badge': 'IOT102 • 346 câu',
        'category': 'software_engineering',
        'image_folder': 'images/iot',
        'js_file': 'iot_data.js',
        'lang_from': 'Slide câu hỏi IOT102',
        'lang_to': 'Đáp án & Giải thích',
        'mode_label': '📝 Trắc nghiệm Slide IOT102',
        'dividers': {
            8: ('1. Dạng bài tập', 'Dạng bài tập tính toán & Mạch điện'),
            83: ('2. Câu ngắn', 'Câu hỏi ngắn lý thuyết (Short Question)'),
            217: ('3. Câu dài', 'Câu hỏi dài & Tình huống (Long Question)'),
            345: ('4. NOT Question', 'Câu hỏi phủ định NOT'),
            361: ('5. Đúng / Sai', 'Đúng / Sai (True / False)')
        }
    },
    'jpd_fe': {
        'filename': 'SEMESTER_4_JPD123.pptx',
        'var_name': 'JPD_FE',
        'sub_id': 'japanese_fe',
        'name': 'Ôn thi FE (JPD123)',
        'fullName': 'Tiếng Nhật JPD123 (203 câu Ôn thi FE)',
        'icon': '🎯',
        'badge': 'FE JPD123 • 203 câu',
        'category': 'japanese',
        'image_folder': 'images/jpd',
        'js_file': 'jpd_fe_data.js',
        'lang_from': 'Slide câu hỏi FE JPD123',
        'lang_to': 'Đáp án & Giải thích',
        'mode_label': '📝 Trắc nghiệm Slide FE JPD123',
        'dividers': {
            5: ('1. Hán tự', 'Hán tự Kanji (50 câu)'),
            57: ('2. Từ để hỏi', 'Từ để hỏi (15 câu)'),
            73: ('3. Giao tiếp', 'Hội thoại & Giao tiếp (8 câu)'),
            82: ('4. Địa điểm & Vị trí', 'Địa điểm & Vị trí (10 câu)'),
            93: ('5. Sự vật & Sự việc', 'Sự vật & Sự việc (10 câu)'),
            104: ('6. Tính từ', 'Tính từ (30 câu)'),
            137: ('7. Động từ', 'Động từ (35 câu)'),
            175: ('8. Trợ từ', 'Trợ từ (32 câu)'),
            208: ('9. Từ khác loại', 'Từ khác loại (7 câu)'),
            216: ('10. Xếp câu', 'Xếp câu ngữ pháp (2 câu)'),
            219: ('11. Nghĩa của từ', 'Nghĩa của từ vựng (4 câu)')
        }
    }
}

def parse_and_generate(key):
    cfg = SUBJECT_CONFIGS[key]
    path = os.path.join(SOURCE_DIR, cfg['filename'])
    prs = pptx.Presentation(path)
    
    dividers = cfg['dividers']
    current_cat_id = '1. Chung'
    current_cat_name = 'Chung'
    
    questions = []
    
    for i, slide in enumerate(prs.slides):
        slide_num = i + 1
        
        if slide_num in dividers:
            current_cat_id, current_cat_name = dividers[slide_num]
            continue
            
        note = ''
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame:
            note = slide.notes_slide.notes_text_frame.text.strip()
        note = clean_text(note)
        lines = [l.strip() for l in note.split('\n') if l.strip()]
        if not lines:
            continue
            
        first = lines[0]
        
        # Bỏ qua slide thông tin / docs / rules / intros
        if any(first.startswith(x) for x in [
            'Thông tin', 'Tài liệu', 'Source', 'Update', 'Các bạn', 'DOCS', 
            'Chữa đề', 'Chữa source', 'PRJ301 FE', 'https://', 'SK_initHtmlViewer', 
            'aa', 'Theory CSD', 'NGUỒN THAM KHẢO', 'ĐIỀN VÀO CHỖ TRỐNG', 'slide dưới'
        ]):
            continue
            
        ans = None
        rem_lines = []
        
        # Case 1: Standard answer letter e.g. A, B, C, AB, ABC, A.
        m = re.match(r'^([A-Fa-f]{1,4})(?:[\s\.\:\,\(\-\—\?\!\/]|$)(.*)', first)
        if m and m.group(1).upper() not in ['ALL', 'TOTAL', 'THEORY', 'DOCS', 'NOTE']:
            ans = m.group(1).upper()
            extra = m.group(2).strip()
            rem_lines = lines[1:]
            if extra:
                rem_lines.insert(0, extra)
        elif re.match(r'^([A-Fa-f])([0-9a-zA-Z\u00C0-\u024F\u1EA0-\u1EF9\u3040-\u30ff\u4e00-\u9faf\[].*)', first):
            # Attached directly e.g. Dtime, D8 sao, Bchắc, Astack
            m_att = re.match(r'^([A-Fa-f])([0-9a-zA-Z\u00C0-\u024F\u1EA0-\u1EF9\u3040-\u30ff\u4e00-\u9faf\[].*)', first)
            ans = m_att.group(1).upper()
            rem_lines = lines[1:]
            rem_lines.insert(0, m_att.group(2).strip())
        else:
            # Check arrow in text
            m_arrow = re.search(r'(?:=>|->|Đáp án[:\s]*|chọn[:\s]*)\s*([A-F]{1,3})', note, re.I)
            if m_arrow:
                ans = m_arrow.group(1).upper()
                rem_lines = lines
            elif len(lines) > 1:
                # Check line 2
                m_l2 = re.match(r'^([A-Fa-f]{1,4})(?:[\s\.\:\,\(\-\—\?\!]|$)', lines[1])
                if m_l2 and m_l2.group(1).upper() not in ['ALL', 'TOTAL']:
                    ans = m_l2.group(1).upper()
                    rem_lines = [lines[0]] + lines[2:]
                    
        if not ans:
            continue
            
        # Normalize double letters
        if ans == 'AA': ans = 'A'
        elif ans == 'DD': ans = 'D'
        elif ans == 'BB': ans = 'B'
        elif ans == 'CC': ans = 'C'
        
        ans_list = list(ans)
        max_letter = max(ans_list)
        if max_letter == 'F':
            all_opts = ['A', 'B', 'C', 'D', 'E', 'F']
        elif max_letter == 'E':
            all_opts = ['A', 'B', 'C', 'D', 'E']
        else:
            all_opts = ['A', 'B', 'C', 'D']
            
        rem_text = '\n'.join(rem_lines).strip()
        q_vn = ''
        m_q = re.search(r'(?:Dịch câu hỏi|Dịch|Câu hỏi)[:\s]+(.*?)(?:\n|$)', rem_text, re.I)
        if m_q:
            q_vn = m_q.group(1).strip()
            
        questions.append({
            'slide': slide_num,
            'cat_id': current_cat_id,
            'cat_name': current_cat_name,
            'ans': ans_list,
            'all_opts': all_opts,
            'q_vn': q_vn,
            'expl': rem_text
        })
        
    print(f"[{key.upper()}] Parsed {len(questions)} questions from {cfg['filename']}")
    
    # Generate lesson parts dictionary
    lesson_parts = {}
    for d_id, (cat_id, cat_name) in dividers.items():
        lesson_parts[cat_id] = { "all": cat_name }
        
    blocks = []
    for idx, q in enumerate(questions, 1):
        slide_num = q['slide']
        cat_id = q['cat_id']
        ans_list = q['ans']
        all_opts = q['all_opts']
        q_vn = q['q_vn']
        expl = q['expl']
        
        clean_expl_lines = [l.strip() for l in expl.split('\n') if l.strip()]
        expl_text = '\n'.join(clean_expl_lines)
        if not expl_text:
            expl_text = f"Đáp án đúng trên slide: {', '.join(ans_list)}"
            
        vn_html = ""
        if q_vn:
            safe_q_vn = q_vn.replace('"', '&quot;')
            vn_html = f'\n<div class="swr-vn-trans text-xs sm:text-sm text-blue-900 font-semibold bg-blue-50/90 border border-blue-200 px-3 py-2 rounded-xl mt-2 flex items-start gap-2 shadow-2xs"><span>🇻🇳</span> <span><b>Dịch câu hỏi:</b> {safe_q_vn}</span></div>'
            
        block = f"""Câu {idx} [CHƯƠNG: {cat_id}]
<div class="swr-slide-wrapper text-center my-2">
  <img src="{cfg['image_folder']}/slide_{slide_num:03d}.png" class="max-h-[520px] w-auto mx-auto rounded-xl shadow-md border border-slate-200 object-contain hover:shadow-lg transition cursor-pointer" alt="Slide {slide_num}" loading="lazy" onclick="openImageModal(this.src)" title="Nhấp để phóng to ảnh">
</div>{vn_html}"""

        for opt in all_opts:
            check = "  ✓" if opt in ans_list else ""
            block += f"\n  {opt}. {opt}{check}"
            
        block += f"\n→ Đáp án: {', '.join(ans_list)}"
        block += f"\nGhi chú: {expl_text}"
        block += "\n────────────────────────────────────────────────────────────"
        blocks.append(block)
        
    raw_db_text = "\n".join(blocks)
    raw_db_text_escaped = escape_template_literal(raw_db_text)
    lesson_parts_json = json.dumps(lesson_parts, ensure_ascii=False, indent=4)
    
    var_prefix = cfg['var_name']
    
    js_content = f"""/**
 * {cfg['fullName'].upper()}
 * Tự động tạo từ slide ôn thi {cfg['name']}.
 */

window.{var_prefix}_LESSON_PARTS = {lesson_parts_json};

window.RAW_DATABASE_{var_prefix} = `
{raw_db_text_escaped}
`;

if (!window.APP_SUBJECTS) {{
    window.APP_SUBJECTS = {{}};
}}

window.APP_SUBJECTS["{cfg['sub_id']}"] = {{
    id: "{cfg['sub_id']}",
    name: "{cfg['name']}",
    fullName: "{cfg['fullName']}",
    icon: "{cfg['icon']}",
    badge: "{cfg['badge']}",
    category: "{cfg['category']}",
    hasFurigana: false,
    quizType: "standard",
    shuffleOptions: false,
    langFrom: "{cfg['lang_from']}",
    langTo: "{cfg['lang_to']}",
    modeLabels: {{
        "standard": "{cfg['mode_label']}"
    }},
    lessonParts: window.{var_prefix}_LESSON_PARTS,
    rawText: window.RAW_DATABASE_{var_prefix}
}};
"""

    out_file = os.path.join(OUTPUT_DIR, cfg['js_file'])
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"Wrote {len(js_content)} chars to {out_file}")

def main():
    for k in ['csd', 'prj', 'iot', 'jpd_fe']:
        parse_and_generate(k)

if __name__ == '__main__':
    main()
