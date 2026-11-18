import json
import re
import os

def clean_text(t):
    if not t:
        return ''
    return re.sub(r'[\u200b\u200c\u200d\uFEFF\xa0\ufffd]', '', t).strip()

def get_category_info(slide_num):
    """
    Phân loại chính xác theo nội dung ghi chú ở các slide đen ngăn cách:
    - Slide 20: Đúng / Sai (True / False)
    - Slide 21: '2 3 đáp án' (Nhiều đáp án)
    - Slide 69: 'Dấu ______' (Điền vào chỗ trống)
    - Slide 85: 'Not/ is true' (Đúng / Sai & NOT)
    - Slide 107: 'Câu ngắn'
    - Slide 173: 'Câu trung bình'
    - Slide 230: 'Câu dài'
    - Slide 302-303: '2 Answers' (Ôn thêm chọn 2 đáp án)
    - Slide 315: '3 Answers' (Ôn thêm chọn 3 đáp án)
    - Slide 333: 'NOT question' (Ôn thêm câu hỏi NOT)
    - Slide 366: 'Ngắn dễ học nè' (Ôn thêm câu ngắn)
    - Slide 424: 'Dài' (Ôn thêm câu dài)
    """
    if slide_num == 20:
        return '1. Đúng / Sai', 'Đúng / Sai (True / False)'
    elif slide_num <= 68:
        return '2. 2 3 đáp án', '2 3 đáp án (Nhiều đáp án)'
    elif slide_num <= 84:
        return '3. Dấu ______', 'Dấu ______ (Điền vào chỗ trống)'
    elif slide_num <= 106:
        return '4. Not/ is true', 'Not/ is true (Đúng / Sai & Phủ định)'
    elif slide_num <= 172:
        return '5. Câu ngắn', 'Câu ngắn'
    elif slide_num <= 229:
        return '6. Câu trung bình', 'Câu trung bình'
    elif slide_num <= 301:
        return '7. Câu dài', 'Câu dài'
    elif slide_num <= 314:
        return '8. Ôn thêm - 2 Answers', 'Ôn thêm - 2 Answers (Chọn 2 đáp án)'
    elif slide_num <= 332:
        return '9. Ôn thêm - 3 Answers', 'Ôn thêm - 3 Answers (Chọn 3 đáp án)'
    elif slide_num <= 365:
        return '10. Ôn thêm - NOT question', 'Ôn thêm - NOT question (Câu hỏi NOT)'
    elif slide_num <= 423:
        return '11. Ôn thêm - Ngắn dễ học nè', 'Ôn thêm - Ngắn dễ học nè'
    else:
        return '12. Ôn thêm - Dài', 'Ôn thêm - Dài (Câu dài nâng cao)'

def main():
    notes_path = 'scratch/swr_notes.json'
    with open(notes_path, 'r', encoding='utf-8') as f:
        slides = json.load(f)

    questions = []
    
    for s in slides:
        num = s['slide']
        if num < 20: # Bỏ qua các slide thông tin đầu slide
            continue
        
        notes = clean_text(s['notes'])
        lines = [l.strip() for l in notes.split('\n') if l.strip()]
        if not lines:
            continue
            
        first_line = lines[0]
        
        # Bỏ qua các slide tiêu đề phân loại / divider đen sì ngăn cách
        if re.match(r'^(2 3 đáp án|Dấu ______?|Not/\s*is true|Câu ngắn|Câu trung bình|Câu dài|Ôn thêm|2 Answers|3 Answers|NOT question|Ngắn dễ học nè|Dài)$', first_line, re.I):
            continue

        ans = None
        remaining_lines = []
        
        m = re.match(r'^([A-F]+)(?:[\s\.\:\,\(\u200b\-\—]|$)', first_line)
        if m and not first_line.startswith(('Tài liệu', 'Thông tin', 'Source', 'Update', 'Các bạn')):
            ans = m.group(1)
            remaining_lines = lines[1:] if len(lines) > 1 else []
            extra_first = first_line[len(m.group(0)):].strip()
            if extra_first:
                remaining_lines.insert(0, extra_first)
        else:
            m_full = re.search(r'Đáp án(?:\s*đúng)?[:\s]+([A-F,\s]+)', notes)
            if m_full:
                ans = ''.join(re.findall(r'[A-F]', m_full.group(1)))
                remaining_lines = lines
                
        if not ans:
            continue
            
        ans_list = list(ans)
        max_letter = max(ans_list)
        
        # Xác định số lượng options phù hợp
        if max_letter == 'F' or any('F' in l for l in remaining_lines[:2] if 'F' in l and ('Đáp án' in l or 'F.' in l or 'F)' in l)):
            all_opts = ['A', 'B', 'C', 'D', 'E', 'F']
        elif max_letter == 'E' or any('E' in l for l in remaining_lines[:2] if 'E' in l and ('Đáp án' in l or 'E.' in l or 'E)' in l)):
            all_opts = ['A', 'B', 'C', 'D', 'E']
        else:
            all_opts = ['A', 'B', 'C', 'D']
            
        cat_id, cat_title = get_category_info(num)
        
        # Trích xuất dịch câu hỏi tiếng Việt nếu có trong ghi chú
        rem_text = '\n'.join(remaining_lines).strip()
        q_vn = ''
        m_q = re.search(r'(?:Dịch câu hỏi|Dịch|Câu hỏi)[:\s]+(.*?)(?:\n|$)', rem_text, re.I)
        if m_q:
            q_vn = m_q.group(1).strip()
        elif remaining_lines and not re.match(r'^(?:Đáp án|Dịch đáp án|Giải thích|Note|Option|[A-F][\.\:\)])', remaining_lines[0], re.I):
            if len(remaining_lines[0]) > 15:
                q_vn = remaining_lines[0]
                
        questions.append({
            'slide': num,
            'cat_id': cat_id,
            'cat_title': cat_title,
            'ans': ans_list,
            'all_opts': all_opts,
            'q_vn': q_vn,
            'expl': rem_text
        })
        
    print(f'Total questions parsed: {len(questions)}')
    
    # Generate RAW_DATABASE_SWR
    blocks = []
    for idx, q in enumerate(questions, 1):
        slide_num = q['slide']
        cat_id = q['cat_id']
        cat_title = q['cat_title']
        ans_list = q['ans']
        all_opts = q['all_opts']
        q_vn = q['q_vn']
        expl = q['expl']
        
        clean_expl_lines = []
        for line in expl.split('\n'):
            line_s = line.strip()
            if not line_s:
                continue
            clean_expl_lines.append(line_s)
        
        expl_text = '\n'.join(clean_expl_lines)
        if not expl_text:
            expl_text = f"Đáp án đúng trên slide: {', '.join(ans_list)}"
            
        vn_html = ""
        if q_vn:
            safe_q_vn = q_vn.replace('"', '&quot;')
            vn_html = f'\n<div class="swr-vn-trans text-xs sm:text-sm text-blue-900 font-semibold bg-blue-50/90 border border-blue-200 px-3 py-2 rounded-xl mt-2 flex items-start gap-2 shadow-2xs"><span>🇻🇳</span> <span><b>Dịch câu hỏi:</b> {safe_q_vn}</span></div>'

        block = f"""Câu {idx} [CHƯƠNG: {cat_id}]
<div class="swr-slide-wrapper text-center my-2">
  <img src="images/swr/slide_{slide_num:03d}.png" class="max-h-[380px] w-auto mx-auto rounded-xl shadow-md border border-slate-200 object-contain hover:shadow-lg transition cursor-pointer" alt="Slide {slide_num}" loading="lazy" onclick="openImageModal(this.src)" title="Nhấp để phóng to ảnh">
</div>{vn_html}"""
        
        for opt in all_opts:
            check = "  ✓" if opt in ans_list else ""
            block += f"\n  {opt}. {opt}{check}"
            
        block += f"\n→ Đáp án: {', '.join(ans_list)}"
        block += f"\nGhi chú: {expl_text}"
        block += "\n────────────────────────────────────────────────────────────"
        blocks.append(block)

    raw_database_text = "\n".join(blocks)
    
    js_content = f"""/**
 * SWR302 - SOFTWARE REQUIREMENTS (469 CÂU HỎI TRẮC NGHIỆM TỪ SLIDE)
 * Tự động tạo từ slide ôn thi SWR302.
 * Phân loại chính xác 100% theo các slide đen ngăn cách:
 *  1. Đúng / Sai (True / False)
 *  2. 2 3 đáp án (Nhiều đáp án)
 *  3. Dấu ______ (Điền vào chỗ trống)
 *  4. Not/ is true (Đúng / Sai & Phủ định NOT)
 *  5. Câu ngắn
 *  6. Câu trung bình
 *  7. Câu dài
 *  8. Ôn thêm - 2 Answers (Chọn 2 đáp án)
 *  9. Ôn thêm - 3 Answers (Chọn 3 đáp án)
 * 10. Ôn thêm - NOT question (Câu hỏi NOT)
 * 11. Ôn thêm - Ngắn dễ học nè
 * 12. Ôn thêm - Dài
 */

window.SWR_LESSON_PARTS = {{
    "1. Đúng / Sai": {{ "all": "Slide 20: Đúng / Sai (True / False)" }},
    "2. 2 3 đáp án": {{ "all": "Slide 22 - 68: Dạng 2 3 đáp án (Nhiều đáp án)" }},
    "3. Dấu ______": {{ "all": "Slide 70 - 84: Dấu ______ (Điền vào chỗ trống)" }},
    "4. Not/ is true": {{ "all": "Slide 86 - 106: Not/ is true (Phủ định & Đúng/Sai)" }},
    "5. Câu ngắn": {{ "all": "Slide 108 - 172: Câu ngắn" }},
    "6. Câu trung bình": {{ "all": "Slide 174 - 229: Câu trung bình" }},
    "7. Câu dài": {{ "all": "Slide 231 - 301: Câu dài" }},
    "8. Ôn thêm - 2 Answers": {{ "all": "Slide 304 - 314: Ôn thêm - 2 Answers (2 đáp án)" }},
    "9. Ôn thêm - 3 Answers": {{ "all": "Slide 316 - 332: Ôn thêm - 3 Answers (3 đáp án)" }},
    "10. Ôn thêm - NOT question": {{ "all": "Slide 334 - 365: Ôn thêm - NOT question (Câu hỏi NOT)" }},
    "11. Ôn thêm - Ngắn dễ học nè": {{ "all": "Slide 367 - 423: Ôn thêm - Ngắn dễ học nè" }},
    "12. Ôn thêm - Dài": {{ "all": "Slide 425 - 509: Ôn thêm - Dài (Câu dài nâng cao)" }}
}};

window.RAW_DATABASE_SWR = `
{raw_database_text}
`;

// Tự động tích hợp môn học vào APP_SUBJECTS
if (!window.APP_SUBJECTS) {{
    window.APP_SUBJECTS = {{}};
}}

window.APP_SUBJECTS["swr"] = {{
    id: "swr",
    name: "SWR302 (Kỹ thuật Yêu cầu)",
    fullName: "SWR302 - Software Requirements (469 câu Slide)",
    icon: "📋",
    badge: "SWR302 • 469 câu",
    category: "software_engineering",
    hasFurigana: false,
    quizType: "standard",
    shuffleOptions: false, // Giữ cố định A, B, C, D để bấm phím 1=A, 2=B, 3=C, 4=D
    langFrom: "Slide câu hỏi SWR302",
    langTo: "Đáp án & Giải thích",
    modeLabels: {{
        "standard": "📝 Trắc nghiệm Slide SWR302"
    }},
    lessonParts: window.SWR_LESSON_PARTS,
    rawText: window.RAW_DATABASE_SWR
}};
"""

    output_path = 'js/swr_data.js'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print(f'Wrote {len(js_content)} characters to {output_path}')

if __name__ == '__main__':
    main()
