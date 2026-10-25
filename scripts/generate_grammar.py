# -*- coding: utf-8 -*-
"""
Main Generator Script cho js/grammar_data.js
Chia các câu hỏi ngữ pháp thành 2 dạng chuẩn mực:
- [HỎI NGỮ PHÁP]: Hỏi khái niệm, công thức, quy tắc, ý nghĩa ngữ pháp
- [DỊCH CÂU]: Dịch câu từ tiếng Việt sang tiếng Nhật tương ứng
Mỗi điểm ngữ pháp có 1 cặp câu hỏi song hành (1 câu hỏi ngữ pháp là gì, 1 câu dịch câu tiếng Việt qua)
"""
import sys
import os

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Đảm bảo đường dẫn import thư mục scripts
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from grammar_lesson4 import register_lesson_4
from grammar_lesson5 import register_lesson_5
from grammar_lesson6 import register_lesson_6

questions = []

def add_pair(lesson, part, part_title, 
             concept_prompt, concept_opts, concept_ans, concept_expl,
             trans_prompt, trans_opts, trans_ans, trans_expl):
    """
    Thêm 1 cặp câu hỏi cho 1 điểm ngữ pháp:
    1. Câu hỏi ngữ pháp là gì [HỎI NGỮ PHÁP]
    2. Câu dịch câu từ tiếng Việt sang tiếng Nhật [DỊCH CÂU]
    """
    letters = ['A', 'B', 'C', 'D']

    # 1. Câu hỏi ngữ pháp là gì
    q_num1 = len(questions) + 1
    opt_lines1 = []
    for idx, opt in enumerate(concept_opts):
        letter = letters[idx]
        check = "  ✓" if letter == concept_ans else ""
        opt_lines1.append(f"  {letter}. {opt}{check}")
    
    q_str1 = f"""Câu {q_num1} [BÀI {lesson} - PHẦN {part}: {part_title}] [HỎI NGỮ PHÁP]
{concept_prompt.strip()}
""" + "\n".join(opt_lines1) + f"""
→ Đáp án: {concept_ans}
Giải thích: {concept_expl.strip()}
────────────────────────────────────────────────────────────"""
    questions.append((q_str1, 'concept', lesson, part))

    # 2. Câu dịch từ câu tiếng Việt qua
    q_num2 = len(questions) + 1
    opt_lines2 = []
    for idx, opt in enumerate(trans_opts):
        letter = letters[idx]
        check = "  ✓" if letter == trans_ans else ""
        opt_lines2.append(f"  {letter}. {opt}{check}")
    
    q_str2 = f"""Câu {q_num2} [BÀI {lesson} - PHẦN {part}: {part_title}] [DỊCH CÂU]
{trans_prompt.strip()}
""" + "\n".join(opt_lines2) + f"""
→ Đáp án: {trans_ans}
Giải thích: {trans_expl.strip()}
────────────────────────────────────────────────────────────"""
    questions.append((q_str2, 'translation', lesson, part))

# Đăng ký các câu hỏi từng bài
register_lesson_4(add_pair)
register_lesson_5(add_pair)
register_lesson_6(add_pair)

# Tổng hợp
all_q_strings = [q[0] for q in questions]
concept_count = sum(1 for q in questions if q[1] == 'concept')
trans_count = sum(1 for q in questions if q[1] == 'translation')

print(f"Tổng số câu hỏi được tạo: {len(questions)}")
print(f"  - Dạng [HỎI NGỮ PHÁP]: {concept_count} câu")
print(f"  - Dạng [DỊCH CÂU]:     {trans_count} câu")

out_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "js", "grammar_data.js")

full_content = """/**
 * KHO DỮ LIỆU CÂU HỎI NGỮ PHÁP TIẾNG NHẬT (BÀI 4 - 6)
 * Được biên soạn chi tiết theo chuẩn 2 dạng câu hỏi song hành cho từng điểm ngữ pháp:
 * 1. [HỎI NGỮ PHÁP]: Hỏi khái niệm, công thức, cấu trúc, quy tắc ngữ pháp
 * 2. [DỊCH CÂU]: Dịch từ câu tiếng Việt sang câu tiếng Nhật tương ứng
 * 
 * Nội dung bao quát toàn bộ giáo trình Dekiru Nihongo:
 * - Bài 4: Phương hướng, Vị trí, Phương tiện, Thời gian di chuyển, Tính từ い/な, Tồn tại にあります, Nối câu そして/が, Phó từ, Trợ từ ね, Thời tiết
 * - Bài 5: Quá khứ Động từ, どこか/どこも, Làm cùng ai と/ひとりで, それから, Quá khứ Tính từ, どうでしたか, Lý do 〜から, ほしい, 〜たい, Mục đích di chuyển に行きます
 * - Bài 6: Rủ rê 〜ませんか/〜ましょう, Từ chối 〜から, Sự kiện diễn ra であります, Lượng từ 〜まい, So sánh hơn より, So sánh lựa chọn どちら, So sánh nhất 一番, Đã làm chưa もう〜ましたか, Gợi ý Nはどうですか, Phân biệt ね/よ, Đồng ý そうしましょう
 */

window.RAW_DATABASE_GRAMMAR = `
""" + "\n".join(all_q_strings) + """
`;

window.GRAMMAR_LESSON_PARTS = {
    "4": {
        "1": "どこ？ (Vị trí, Phương tiện, Thời gian)",
        "2": "どんなところ？ (Tính từ, Tồn tại, Nối câu, Phủ định)",
        "3": "季節・料理 (Phó từ, Trợ từ ね, Thời tiết)"
    },
    "5": {
        "1": "週末 (Quá khứ Động từ, Đi đâu, と, それから)",
        "2": "休みの後で (Quá khứ Tính từ, どうでしたか, Lý do 〜から)",
        "3": "今度の休みに (ほしい, 〜たい, Mục đích di chuyển)"
    },
    "6": {
        "1": "一緒に行きませんか (Rủ rê 〜ませんか, 〜ましょう, であります, 〜まい)",
        "2": "どちらがいいですか。 (So sánh hơn より, どちら, 一番)",
        "3": "約束 (Đã làm chưa もう, Gợi ý Nはどうですか, ね/よ, そうしましょう)"
    }
};
"""

with open(out_file, "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Đã xuất thành công file: {out_file} ({len(questions)} câu)")
