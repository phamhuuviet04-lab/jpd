# -*- coding: utf-8 -*-
"""
Script to generate js/grammar_data.js with complete grammar questions for Bài 4, 5, 6
"""
import sys
import re

questions = []

def add_q(lesson, part, part_title, prompt, options, correct_letter, explanation):
    q_num = len(questions) + 1
    opt_lines = []
    letters = ['A', 'B', 'C', 'D']
    for idx, opt in enumerate(options):
        letter = letters[idx]
        is_corr = (letter == correct_letter)
        check = "  ✓" if is_corr else ""
        opt_lines.append(f"  {letter}. {opt}{check}")
    
    q_str = f"""Câu {q_num} [BÀI {lesson} - PHẦN {part}: {part_title}]
{prompt.strip()}
""" + "\n".join(opt_lines) + f"""
→ Đáp án: {correct_letter}
Giải thích: {explanation.strip()}
────────────────────────────────────────────────────────────"""
    questions.append(q_str)

# ==============================================================================
# BÀI 4 - PHẦN 1: どこ？ (Phương hướng, Vị trí, Phương tiện, Thời gian di chuyển)
# ==============================================================================
P4_1 = "どこ？"

add_q("4", "1", P4_1,
    "Mẫu câu「Thành phố は đất nước の [hướng] です。」dùng để làm gì?",
    [
        "Nói về dân số của một thành phố",
        "Xác định vị trí phương hướng của thành phố thuộc một quốc gia",
        "Hỏi giá vé đi đến thành phố",
        "Miêu tả thời tiết của đất nước"
    ],
    "B",
    "Cấu trúc này dùng để diễn đạt thành phố nằm ở hướng nào (đông, tây, nam, bắc, trung tâm) của một quốc gia. Ví dụ: Lang Sonは ベトナムの きたです。"
)

add_q("4", "1", P4_1,
    "Để hỏi \"Nhà của bạn ở đâu?\" một cách lịch sự, câu tiếng Nhật nào sau đây là đúng?",
    [
        "お家は なんですか。",
        "お家は だれですか。",
        "お家は どこですか。",
        "お家は どうですか。"
    ],
    "C",
    "「どこ」là từ để hỏi nơi chốn, vị trí. 「お家は どこですか。」nghĩa là \"Nhà bạn ở đâu?\"."
)

add_q("4", "1", P4_1,
    "Dịch câu sau sang tiếng Nhật: \"Lạng Sơn ở phía bắc Việt Nam.\"",
    [
        "Lang Sonは ベトナムの きたです。",
        "Lang Sonは ベトナムの みなみです。",
        "Lang Sonは ベトナムの ひがしです。",
        "Lang Sonは ベトナムの にしです。"
    ],
    "A",
    "Phía bắc tiếng Nhật là きた (北). Do đó câu đúng là: Lang Sonは ベトナムの きたです。"
)

add_q("4", "1", P4_1,
    "Dịch câu sau sang tiếng Nhật: \"Cà Mau ở phía nam Việt Nam.\"",
    [
        "Cà Mauは ベトナムの きたです。",
        "Cà Mauは ベトナムの にしです。",
        "Cà Mauは ベトナムの みなみです。",
        "Cà Mauは ベトナムの まんなかです。"
    ],
    "C",
    "Phía nam tiếng Nhật là みなみ (南). Do đó câu đúng là: Cà Mauは ベトナムの みなみです。"
)

add_q("4", "1", P4_1,
    "Dịch câu sau sang tiếng Nhật: \"Nghệ An ở miền Trung (chính giữa) Việt Nam.\"",
    [
        "Nghệ Anは ベトナムの ひがしです。",
        "Nghệ Anは ベトナムの まんなかです。",
        "Nghệ Anは ベトナムの きたです。",
        "Nghệ Anは ベトナムの にしです。"
    ],
    "B",
    "Chính giữa, trung tâm là まんなか (真ん中). Câu đúng là: Nghệ Anは ベトナムの まんなかです。"
)

add_q("4", "1", P4_1,
    "Hoàn thành hội thoại hỏi vị trí cụ thể:\nA:「お家は どこですか。」\nB:「ハノイです。」\nA:「ハノイの どこですか。」\nB:「ホアン・マイです。ホアン・マイは ハノイの ______ です。」(phía nam)",
    [
        "きた",
        "ひがし",
        "にし",
        "南 (みなみ)"
    ],
    "D",
    "Quận Hoàng Mai nằm ở phía Nam thành phố Hà Nội:「ハノイの 南(みなみ)です。」"
)

add_q("4", "1", P4_1,
    "Dịch câu sau sang tiếng Nhật: \"Sydney ở phía đông nước Úc (オーストラリア).\"",
    [
        "シドニーは オーストラリアの ひがしです。",
        "シドニーは オーストラリアの にしです。",
        "シドニーは オーストラリアの きたです。",
        "シドニーは オーストラリアの みなみです。"
    ],
    "A",
    "Phía đông là ひがし (東). Câu đúng: シドニーは オーストラリアの ひがしです。"
)

add_q("4", "1", P4_1,
    "Dịch câu sau sang tiếng Nhật: \"Matxcơva ở phía tây nước Nga (ロシア).\"",
    [
        "モスクワは ロシアの きたです。",
        "モスクワは ロシアの ひがしです。",
        "モスクワは ロシアの にしです。",
        "モスクワは ロシアの まんなかです。"
    ],
    "C",
    "Phía tây là にし (西). Câu đúng: モスクワは ロシアの にしです。"
)

add_q("4", "1", P4_1,
    "Trong tiếng Nhật, để chỉ phương tiện giao thông dùng để di chuyển, ta dùng trợ từ nào?",
    [
        "Trợ từ に",
        "Trợ từ で",
        "Trợ từ を",
        "Trợ từ へ"
    ],
    "B",
    "Trợ từ で đi sau danh từ chỉ phương tiện để biểu thị phương tiện, công cụ di chuyển (Phương tiện + で + 行きます)."
)

add_q("4", "1", P4_1,
    "Chọn câu hỏi đúng cho tình huống: \"Bạn đi đến Pháp (フランス) bằng phương tiện gì?\"",
    [
        "どこで フランスへ 行きますか。",
        "なんで フランスへ 行きますか。",
        "だれで フランスへ 行きますか。",
        "いつで フランスへ 行きますか。"
    ],
    "B",
    "Hỏi đi bằng phương tiện gì dùng「なんで / なにで + địa điểm へ 行きますか。」."
)

add_q("4", "1", P4_1,
    "Hoàn thành câu trả lời về phương tiện:\nA:「なんで びょういんへ 行きますか。」\nB:「________ で 行きます。」(Taxi)",
    [
        "タクシー",
        "あるいて",
        "じてんしゃへ",
        "ひこうきを"
    ],
    "A",
    "Taxi tiếng Nhật là タクシー. Đi bằng taxi là「タクシーで 行きます。」."
)

add_q("4", "1", P4_1,
    "LƯU Ý NGỮ PHÁP ĐẶC BIỆT: Khi nói \"Đi bộ đến trường / ga\", câu nào sau đây là ĐÚNG?",
    [
        "あるきで えきへ 行きます。",
        "あるいて えきへ 行きます。",
        "あるいてで えきへ 行きます。",
        "あるくで えきへ 行きます。"
    ],
    "B",
    "Khi đi bộ, ta dùng dạng「あるいて 行きます」và TUYỆT ĐỐI KHÔNG dùng trợ từ で."
)

add_q("4", "1", P4_1,
    "Mẫu câu「[Địa điểm 1] から [Địa điểm 2] まで どのくらい かかりますか。」có ý nghĩa là gì?",
    [
        "Từ địa điểm 1 đến địa điểm 2 có cái gì?",
        "Từ địa điểm 1 đến địa điểm 2 mất khoảng bao lâu?",
        "Địa điểm 1 và địa điểm 2 cái nào đẹp hơn?",
        "Tại sao bạn đi từ địa điểm 1 đến địa điểm 2?"
    ],
    "B",
    "「どのくらい かかりますか / どのくらいですか」dùng để hỏi về khoảng thời gian (hoặc chi phí) di chuyển từ điểm xuất phát (から) đến đích đến (まで)."
)

add_q("4", "1", P4_1,
    "Hoàn thành câu trả lời về thời gian di chuyển:\nA:「うちから 会社まで どのくらいですか。」\nB:「でんしゃで 20ぷん ________ です。」(khoảng 20 phút)",
    [
        "まで",
        "から",
        "くらい",
        "より"
    ],
    "C",
    "Hậu tố「〜くらい / 〜ぐらい」được thêm sau từ chỉ lượng/thời gian để biểu thị mức độ \"khoảng, chừng\"."
)

add_q("4", "1", P4_1,
    "Hoàn thành đoạn hội thoại:\nA:「日本から アメリカまで どのくらいですか。」\nB:「________ で 12じかんぐらい です。」(máy bay)",
    [
        "でんしゃ",
        "ひこうき",
        "しんかんせん",
        "じてんしゃ"
    ],
    "B",
    "Đi từ Nhật sang Mỹ mất 12 tiếng thì phương tiện hợp lý là máy bay: ひこうき (飛行機)."
)

add_q("4", "1", P4_1,
    "Cách nói \"1 tiếng rưỡi\" trong tiếng Nhật là gì?",
    [
        "1じかん",
        "1じかんはん",
        "1じはんかん",
        "1ふんはん"
    ],
    "B",
    "1 tiếng là 1じかん (1時間). Thêm はん (bán - rưỡi) ở cuối ➔ 1じかんはん (1時間半)."
)

# ==============================================================================
# BÀI 4 - PHẦN 2: どんなところ？ (Miêu tả N, Tính từ đuôi い/な, Tồn tại, Nối câu, Phủ định)
# ==============================================================================
P4_2 = "どんなところ？"

add_q("4", "2", P4_2,
    "Trong Bài 4.2, câu hỏi「N は どうですか。」dùng để làm gì?",
    [
        "Hỏi N ở vị trí nào",
        "Hỏi N giá bao nhiêu tiền",
        "Hỏi về tính chất, đặc điểm của N (N trông như thế nào?)",
        "Hỏi N có bao nhiêu người"
    ],
    "C",
    "Mẫu câu「N は どうですか。」ở Bài 4 dùng để hỏi miêu tả tính chất, trạng thái của N (\"N như thế nào?\") và được trả lời bằng tính từ."
)

add_q("4", "2", P4_2,
    "Khi được hỏi:「すずきさんの家は どうですか。」(Nhà bạn Suzuki như thế nào?), câu trả lời nào sau đây đúng ngữ pháp?",
    [
        "おおきいです。",
        "ハノイです。",
        "うちへ行きます。",
        "3じかんです。"
    ],
    "A",
    "Trả lời cho câu hỏi tính chất「〜はどうですか」bằng tính từ, ví dụ: おおきいです (To/rộng lớn)."
)

add_q("4", "2", P4_2,
    "Dịch câu sau sang tiếng Nhật: \"Công viên ABC rất nhộn nhịp (náo nhiệt).\"",
    [
        "ABCこうえんは しずかです。",
        "ABCこうえんは にぎやかです。",
        "ABCこうえんは ひろくないです。",
        "ABCこうえんは ふるいです。"
    ],
    "B",
    "Tính từ đuôi な: にぎやか (nhộn nhịp, náo nhiệt). Câu đúng: ABCこうえんは にぎやかです。"
)

add_q("4", "2", P4_2,
    "Dịch câu sau sang tiếng Nhật: \"Công viên Wakaba yên tĩnh.\"",
    [
        "わかば公園は にぎやかです。",
        "わかば公園は しずかです。",
        "わかば公園は あついです。",
        "わかば公園は からいです。"
    ],
    "B",
    "Tính từ đuôi な: しずか (yên tĩnh). Câu đúng: わかば公園は しずかです。"
)

add_q("4", "2", P4_2,
    "Quy tắc ngữ pháp khi dùng TÍNH TỪ ĐUÔI い đứng trước để bổ nghĩa cho danh từ là gì?",
    [
        "Bỏ đuôi い thêm な rồi ghép với danh từ",
        "Giữ nguyên đuôi い rồi ghép trực tiếp với danh từ (イA + N)",
        "Bỏ đuôi い rồi ghép trực tiếp với danh từ",
        "Phải thêm trợ từ の giữa tính từ và danh từ"
    ],
    "B",
    "Tính từ đuôi い khi bổ nghĩa cho danh từ giữ nguyên い: Ví dụ: たかいビル (tòa nhà cao), ひくい山 (ngọn núi thấp), ふるい教会 (nhà thờ cổ)."
)

add_q("4", "2", P4_2,
    "Quy tắc ngữ pháp khi dùng TÍNH TỪ ĐUÔI な đứng trước để bổ nghĩa cho danh từ là gì?",
    [
        "Bỏ đuôi な rồi ghép trực tiếp với danh từ",
        "Phải giữ lại đuôi「な」rồi mới ghép với danh từ (ナA + な + N)",
        "Phải thêm trợ từ の thay thế cho な",
        "Phải đổi đuôi な thành い"
    ],
    "B",
    "Tính từ đuôi な khi đứng trước bổ nghĩa cho danh từ BẮT BUỘC phải có「な」. Ví dụ: きれいな山 (ngọn núi đẹp), しずかな公園 (công viên yên tĩnh), ゆうめいな人 (người nổi tiếng)."
)

add_q("4", "2", P4_2,
    "Chọn câu đúng ngữ pháp để nói: \"Núi Phú Sĩ là ngọn núi đẹp.\"",
    [
        "ふじさんは きれい 山です。",
        "ふじさんは きれいの 山です。",
        "ふじさんは きれいな 山です。",
        "ふじさんは きれいくない 山です。"
    ],
    "C",
    "きれい là tính từ đuôi な (đặc biệt kết thúc bằng âm i), khi đứng trước danh từ phải có「な」: きれいな 山."
)

add_q("4", "2", P4_2,
    "Chọn câu đúng ngữ pháp để nói: \"Núi Phú Sĩ là ngọn núi cao.\"",
    [
        "ふじさんは たかいな 山です。",
        "ふじさんは たかい 山です。",
        "ふじさんは たか的山です。",
        "ふじさんは たか 山です。"
    ],
    "B",
    "たかい là tính từ đuôi い, khi bổ nghĩa cho danh từ 山 thì giữ nguyên い: たかい 山."
)

add_q("4", "2", P4_2,
    "Dịch câu sau: \"Sông Nile là một con sông đẹp.\"",
    [
        "ナイル川は きれい かわです。",
        "ナイル川は きれいな かわです。",
        "ナイル川は たかい かわです。",
        "ナイル川は ひくい かわです。"
    ],
    "B",
    "Tính từ きれい (đẹp) đi kèm danh từ かわ (dòng sông) thành「きれいな かわ」."
)

add_q("4", "2", P4_2,
    "Cấu trúc「N1 は どんな N2 ですか。」có ý nghĩa là gì?",
    [
        "N1 có bao nhiêu N2?",
        "N1 là N2 như thế nào?",
        "N1 ở đâu trong N2?",
        "Khi nào N1 trở thành N2?"
    ],
    "B",
    "「どんな + Danh từ」nghĩa là \"... như thế nào\". Ví dụ:「みどり公園は どんなところですか。」➔ \"Công viên Midori là nơi như thế nào?\"."
)

add_q("4", "2", P4_2,
    "Hoàn thành câu trả lời:\nA:「みどり公園は どんなところですか。」\nB:「____________ ところです。」(nơi đẹp)",
    [
        "きれいく",
        "きれいな",
        "きれい",
        "きれいの"
    ],
    "B",
    "Bổ nghĩa cho danh từ ところ (nơi chốn):「きれいな ところです。」"
)

add_q("4", "2", P4_2,
    "Mẫu câu「N1 に N2 が あります。」dùng để diễn đạt điều gì?",
    [
        "Ai đó làm việc gì ở N1",
        "Ở địa điểm N1 có sự tồn tại của sự vật/địa danh N2",
        "Đi từ N1 đến N2",
        "N1 to hơn N2"
    ],
    "B",
    "Mẫu câu「N1(nơi chốn) に N2(đồ vật/địa điểm tĩnh) が あります」nghĩa là \"Ở N1 có N2\"."
)

add_q("4", "2", P4_2,
    "Dịch câu sau sang tiếng Nhật: \"Ở Hakone có suối nước nóng (onsen).\"",
    [
        "はこねで おんせんが あります。",
        "はこねに おんせんが あります。",
        "はこねへ おんせんが あります。",
        "はこねから おんせんが あります。"
    ],
    "B",
    "Chỉ địa điểm tồn tại dùng trợ từ に:「はこねに おんせんが あります。」"
)

add_q("4", "2", P4_2,
    "Dịch câu sau sang tiếng Nhật: \"Ở thành phố tôi có một tòa lâu đài to.\"",
    [
        "私のまちに おおきい おしろが あります。",
        "私のまちで おおきい おしろが あります。",
        "私のまちは おおきいな おしろです。",
        "私のまちにおおきいおしろを行きます。"
    ],
    "A",
    "Tồn tại ở thành phố tôi (私のまちに) + vật tồn tại (おおきい おしろが) + あります."
)

add_q("4", "2", P4_2,
    "Để hỏi \"Ở thành phố của bạn có cái gì?\", câu hỏi chuẩn ngữ pháp là:",
    [
        "あなたのまちに なにが ありますか。",
        "あなたのまちで なにが しますか。",
        "あなたのまちは どうですか。",
        "あなたのまちへ どこに行きますか。"
    ],
    "A",
    "Hỏi vật tồn tại ở một địa điểm:「[Địa điểm] に なにが ありますか。」"
)

add_q("4", "2", P4_2,
    "Liên từ「そして、」(và, rồi thì) dùng để nối 2 mệnh đề có tính chất như thế nào?",
    [
        "Nối 2 mệnh đề tương phản, trái ngược nhau (khen - chê)",
        "Nối 2 mệnh đề có ý nghĩa cùng chiều (tốt - tốt, hoặc xấu - xấu)",
        "Dùng để giải thích nguyên nhân vì sao",
        "Dùng để hỏi lựa chọn cái nào hơn"
    ],
    "B",
    "「そして、」dùng để bổ sung thông tin cùng chiều (thuận chiều), khen thì cùng khen, chê thì cùng chê. Ví dụ: きれいです。そして、ゆうめいです。"
)

add_q("4", "2", P4_2,
    "Dịch câu sau sang tiếng Nhật: \"Lâu đài Himeji đẹp. Và nổi tiếng.\"",
    [
        "ひめじじょうは きれいです。が、ゆうめいです。",
        "ひめじじょうは きれいです。そして、ゆうめいです。",
        "ひめじじょうは きれいです。から、ゆうめいです。",
        "ひめじじょうは きれいです。でも、ゆうめいです。"
    ],
    "B",
    "Hai đặc điểm cùng chiều tốt (đẹp & nổi tiếng) nối với nhau bằng「そして、」."
)

add_q("4", "2", P4_2,
    "Trợ từ liên kết「〜が、」(nhưng...) dùng để nối 2 mệnh đề có tính chất như thế nào?",
    [
        "Nối 2 mệnh đề có ý nghĩa tương phản, trái ngược nhau",
        "Nối 2 mệnh đề có ý nghĩa tương đồng",
        "Chỉ nguyên nhân kết quả",
        "Chỉ mục đích hành động"
    ],
    "A",
    "「[Mệnh đề 1] が、[Mệnh đề 2]」dùng để nối 2 vế câu trái ngược, tương phản nhau (Ví dụ: tuy thấp nhưng đẹp, tuy nhỏ nhưng sạch)."
)

add_q("4", "2", P4_2,
    "Chọn câu đúng ngữ pháp: \"Núi Takao thấp nhưng đẹp.\"",
    [
        "たかお山は ひくいそして、きれいです。",
        "たかお山は ひくいですから、きれいです。",
        "たかお山は ひくいですが、きれいです。",
        "たかお山は ひくいですが、きれいくないです。"
    ],
    "C",
    "Nối tính từ đuôi い với vế sau mang nghĩa trái ngược:「ひくいですが、きれいです。」"
)

add_q("4", "2", P4_2,
    "Chọn câu đúng ngữ pháp: \"Căn phòng của tôi nhỏ nhưng sạch đẹp.\"",
    [
        "わたしの部屋は 小さいですが、きれいです。",
        "わたしの部屋は 小さいですから、きれいです。",
        "わたしの部屋は 小さいそして、きれいです。",
        "わたしの部屋は 小さいですが、きたないです。"
    ],
    "A",
    "Cặp tính từ tương phản (nhỏ - sạch đẹp):「小さいですが、きれいです。」"
)

add_q("4", "2", P4_2,
    "Quy tắc chuyển TÍNH TỪ ĐUÔI い sang THỂ PHỦ ĐỊNH (không...) là gì?",
    [
        "Bỏ đuôi い thêm「くないです」",
        "Bỏ đuôi い thêm「じゃありません」",
        "Giữ nguyên い thêm「ないです」",
        "Bỏ đuôi い thêm「ませんでした」"
    ],
    "A",
    "Tính từ đuôi い phủ định: bỏ い + くないです. Ví dụ: たかい ➔ たかくないです (không cao/đắt)."
)

add_q("4", "2", P4_2,
    "NGOẠI LỆ QUAN TRỌNG: Thể phủ định của tính từ「いい」(tốt) là gì?",
    [
        "いくないです",
        "いいくないです",
        "よくないです",
        "いいじゃありません"
    ],
    "C",
    "Tính từ「いい」là ngoại lệ bất quy tắc, khi chia phủ định phải biến đổi gốc thành「よくないです」."
)

add_q("4", "2", P4_2,
    "Quy tắc chuyển TÍNH TỪ ĐUÔI な sang THỂ PHỦ ĐỊNH (không...) là gì?",
    [
        "Thêm くないです vào sau tính từ",
        "Bỏ đuôi な và thêm「じゃありません」(hoặc ではありません)",
        "Đổi な thành い rồi thêm くないです",
        "Giữ nguyên な rồi thêm ありません"
    ],
    "B",
    "Tính từ đuôi な phủ định: A(bỏ な) + じゃありません. Ví dụ: しずか ➔ しずかじゃありません (không yên tĩnh)."
)

# ==============================================================================
# BÀI 4 - PHẦN 3: 季節・料理 (Trợ từ ね, Phó từ mức độ, Thời tiết theo mùa)
# ==============================================================================
P4_3 = "季節・料理"

add_q("4", "3", P4_3,
    "Trợ từ「ね」ở cuối câu trong Bài 4.3 có chức năng chính là gì?",
    [
        "Hỏi thông tin chưa biết",
        "Thể hiện cảm thán hoặc tìm kiếm sự đồng tình từ người nghe (~nhỉ!)",
        "Ra lệnh bắt buộc người khác làm theo",
        "Chỉ phương hướng di chuyển"
    ],
    "B",
    "「〜ね」ở cuối câu dùng để (1) Cảm thán, (2) Kêu gọi sự đồng tình từ người nghe. Tương đương với \"...nhỉ!\" trong tiếng Việt."
)

add_q("4", "3", P4_3,
    "Khi thấy trời nóng và muốn chia sẻ cảm thán với người bên cạnh, bạn nói:",
    [
        "あついですか。",
        "あついですね。",
        "あつくないですね。",
        "あついでしたね。"
    ],
    "B",
    "Câu cảm thán thời tiết nóng:「あついですね。」(Nóng nhỉ!)."
)

add_q("4", "3", P4_3,
    "Phó từ「とても」(rất) kết hợp với tính từ ở dạng nào?",
    [
        "Chỉ đi với tính từ dạng phủ định",
        "Đi với tính từ dạng khẳng định (thể hiện mức độ cao)",
        "Chỉ đi với câu nghi vấn",
        "Không đi được với tính từ"
    ],
    "B",
    "「とても」nghĩa là \"rất\", luôn đi với tính từ khẳng định. Ví dụ: とても おおきいです (rất to), とても にぎやかです (rất nhộn nhịp)."
)

add_q("4", "3", P4_3,
    "Phó từ「すこし」(một chút, hơi...) kết hợp với tính từ ở dạng nào?",
    [
        "Đi với tính từ dạng khẳng định (thể hiện mức độ nhẹ)",
        "Chỉ đi với tính từ dạng phủ định",
        "Chỉ đi với động từ thể quá khứ",
        "Bắt buộc đi với từ nghi vấn"
    ],
    "A",
    "「すこし」nghĩa là \"một chút, hơi...\", đi với tính từ khẳng định. Ví dụ: すこし すっぱいです (hơi chua), すこし ふるいビルです (tòa nhà hơi cũ)."
)

add_q("4", "3", P4_3,
    "QUY TẮC BẮT BUỘC: Phó từ「あまり」(không... lắm) kết hợp với tính từ ở dạng nào?",
    [
        "Chỉ đi với tính từ dạng khẳng định",
        "Bắt buộc đi với tính từ DẠNG PHỦ ĐỊNH (くない / じゃありません)",
        "Đi với cả khẳng định lẫn phủ định mà không đổi nghĩa",
        "Chỉ đi với câu hỏi lựa chọn"
    ],
    "B",
    "「あまり」mang nghĩa \"không... lắm\" và BẮT BUỘC phải đi với tính từ ở thể phủ định: あまり あつくないです, あまり しずかじゃありません."
)

add_q("4", "3", P4_3,
    "Phó từ「ぜんぜん」(hoàn toàn không...) kết hợp với tính từ ở dạng nào?",
    [
        "Chỉ đi với tính từ thể khẳng định",
        "Bắt buộc đi với tính từ THỂ PHỦ ĐỊNH (hoàn toàn không...)",
        "Chỉ đi với danh từ số nhiều",
        "Đi với động từ thể mệnh lệnh"
    ],
    "B",
    "「ぜんぜん」trong ngữ pháp chuẩn sơ cấp kết hợp với thể phủ định để mang nghĩa \"hoàn toàn không...\" (ぜんぜん さむくないです)."
)

add_q("4", "3", P4_3,
    "Điền phó từ thích hợp vào chỗ trống (bức tranh mướp đắng rất đắng):\n「これは ________ にがいです。」(Cái này rất đắng.)",
    [
        "あまり",
        "とても",
        "ぜんぜん",
        "すこしもない"
    ],
    "B",
    "Câu ở thể khẳng định mang nghĩa \"rất đắng\" ➔ Dùng とても:「これは とても にがいです。」"
)

add_q("4", "3", P4_3,
    "Điền phó từ thích hợp vào chỗ trống (nước tôi mùa đông KHÔNG lạnh lắm):\n「私のくには ふゆ、________ 寒くないです。」",
    [
        "とても",
        "すこし",
        "あまり",
        "いちばん"
    ],
    "C",
    "Vế sau ở thể phủ định (寒くないです), để diễn đạt ý \"không... lắm\" ta dùng「あまり」."
)

add_q("4", "3", P4_3,
    "Mẫu câu「N(quốc gia/thành phố) は [thời gian]、Adj です。」có ý nghĩa là gì?",
    [
        "Nói về sự phát triển kinh tế của quốc gia theo thời gian",
        "Miêu tả đặc điểm thời tiết/tính chất của đất nước/thành phố vào một mốc thời gian cụ thể",
        "Hỏi giờ máy bay bay đến quốc gia đó",
        "So sánh thời gian giữa hai thành phố"
    ],
    "B",
    "Mẫu câu này dùng để nói về đặc điểm thời tiết hoặc đặc trưng của một vùng vào một tháng, một mùa hoặc trong năm. Ví dụ: 私の国は 8月、とてもあついです。"
)

add_q("4", "3", P4_3,
    "Hoàn thành câu trả lời trong hội thoại:\nA:「Bさんのお国は 8月、どうですか。」\nB:「私の国は 8月、________________。」",
    [
        "とても あついです",
        "あまり あついです",
        "とても あつくないです",
        "すこし あつかったです"
    ],
    "A",
    "Trả lời cho câu hỏi về tháng 8: とても đi với khẳng định「とても あついです」(rất nóng)."
)

add_q("4", "3", P4_3,
    "Hoàn thành câu trả lời trong hội thoại:\nA:「Bさんのお国は 6月、どうですか。」\nB:「私の国は 6月、________________。」(mưa nhiều)",
    [
        "雨が すくないです",
        "雨が おおいです",
        "雨が いいです",
        "雨が わるいです"
    ],
    "B",
    "Mưa nhiều trong tiếng Nhật là「雨が おおいです (雨が多いです)」."
)

add_q("4", "3", P4_3,
    "Hoàn thành câu trả lời phủ định có mức độ:\nA:「タイは 12月、さむいですか。」\nB:「いいえ、________________。」(không lạnh lắm)",
    [
        "とても さむいです",
        "あまり さむくないです",
        "すこし さむいです",
        "あまり さむいです"
    ],
    "B",
    "Trả lời phủ định nhẹ:「いいえ、あまり さむくないです。」(Không, không lạnh lắm)."
)

add_q("4", "3", P4_3,
    "Dịch câu sau: \"Mùa thu ở thành phố tôi thời tiết rất đẹp.\"",
    [
        "私のまちは あき、てんきが わるいです。",
        "私のまちは あき、てんきが いいです。",
        "私のまちは あき、てんきが よくありません。",
        "私のまちは あき、あめです。"
    ],
    "B",
    "Thời tiết đẹp: てんきが いいです (天気がいいです). Câu đúng: 私のまちは あき、てんきがいいです。"
)

add_q("4", "3", P4_3,
    "Chọn câu hoàn chỉnh đúng ngữ pháp theo bài tập slide 15:\n\"Hokkaido vào tháng 2 tuyết rất nhiều.\"",
    [
        "北海道は 2月、雪があまり多いです。",
        "北海道は 2月、雪がとても多いです。",
        "北海道は 2月、雪がとても多くないです。",
        "北海道は 2月、雪がすこし多いではありません。"
    ],
    "B",
    "Theo bài tập slide 15:「北海道は 2月、雪がとても多いです。」(Hokkaido tháng 2 tuyết rất nhiều)."
)

add_q("4", "3", P4_3,
    "Hoàn thành câu theo mẫu:\n\"Tòa nhà Yamada là một tòa nhà hơi cũ.\"",
    [
        "ヤマダビルは すこし ふるいビルです。",
        "ヤマダビルは あまり ふるいビルです。",
        "ヤマダビルは とても ふるくないビルです。",
        "ヤマダビルは すこしな ふるいビルです。"
    ],
    "A",
    "Hơi cũ: すこし + tính từ đuôi い + danh từ ➔「すこし ふるいビルです。」"
)

# ==============================================================================
# BÀI 5 - PHẦN 1: 週末 (Quá khứ Động từ, Đi đâu, Làm cùng ai, それから)
# ==============================================================================
P5_1 = "週末"

add_q("5", "1", P5_1,
    "Động từ thể khẳng định ở thì QUÁ KHỨ trong tiếng Nhật có đuôi là gì?",
    [
        "〜ます",
        "〜ません",
        "〜ました",
        "〜ませんでした"
    ],
    "C",
    "Thì quá khứ khẳng định của động từ kết thúc bằng「〜ました」. Ví dụ: いきました (đã đi), たべました (đã ăn)."
)

add_q("5", "1", P5_1,
    "Động từ thể phủ định ở thì QUÁ KHỨ trong tiếng Nhật có đuôi là gì?",
    [
        "〜ます",
        "〜ません",
        "〜ました",
        "〜ませんでした"
    ],
    "D",
    "Thì quá khứ phủ định của động từ kết thúc bằng「〜ませんでした」. Ví dụ: いきませんでした (đã không đi), たべませんでした (đã không ăn)."
)

add_q("5", "1", P5_1,
    "Chia động từ「かいものします」(mua sắm) sang thì quá khứ khẳng định:",
    [
        "かいものしました",
        "かいものしません",
        "かいものしませんでした",
        "かいものしたいです"
    ],
    "A",
    "かいものします ➔ かいものしました (đã mua sắm)."
)

add_q("5", "1", P5_1,
    "Chia động từ「そうじします」(dọn dẹp) sang thì quá khứ phủ định:",
    [
        "そうじしました",
        "そうじしませんでした",
        "そうじしません",
        "そうじしたくないです"
    ],
    "B",
    "Quá khứ phủ định: そうじします ➔ そうじしませんでした (đã không dọn dẹp)."
)

add_q("5", "1", P5_1,
    "Dịch câu sau: \"Hôm qua tôi đã đi đến siêu thị.\"",
    [
        "きのう スーパーへ 行きます。",
        "きのう スーパーへ 行きません。",
        "きのう スーパーへ 行きました。",
        "きのう スーパーへ 行きませんでした。"
    ],
    "C",
    "Có từ chỉ thời gian quá khứ「きのう」(hôm qua), động từ phải chia quá khứ khẳng định: 行きました。"
)

add_q("5", "1", P5_1,
    "Dịch câu sau: \"Hôm qua tôi đã không ăn bánh mì. Tôi đã ăn cơm.\"",
    [
        "きのう パンを 食べませんでした。ごはんを 食べました。",
        "きのう パンを 食べません。ごはんを 食べます。",
        "きのう パンを 食べました。ごはんを 食べませんでした。",
        "きのう パンを 食べなかったです。ごはんを 食べでした。"
    ],
    "A",
    "Đã không ăn bánh mì: パンを 食べませんでした. Đã ăn cơm: ごはんを 食べました."
)

add_q("5", "1", P5_1,
    "Để hỏi \"Chủ nhật bạn đã làm gì?\", câu hỏi tiếng Nhật nào sau đây là chuẩn?",
    [
        "日曜日、何を しますか。",
        "日曜日、何を しましたか。",
        "日曜日、どこへ 行きましたか。",
        "日曜日、だれと 会いましたか。"
    ],
    "B",
    "Hỏi hành động đã làm trong quá khứ dùng:「[Thời gian quá khứ]、何(なに)を しましたか。」."
)

add_q("5", "1", P5_1,
    "Mẫu câu「きのう、どこか(へ) 行きましたか。」có ý nghĩa là gì?",
    [
        "Hôm qua bạn đi đến đâu?",
        "Hôm qua bạn có đi đâu (chỗ nào đó) không?",
        "Hôm qua bạn đi với ai?",
        "Khi nào bạn đi chơi?"
    ],
    "B",
    "「どこか」là từ bất định mang nghĩa \"nơi nào đó / đâu đó\". Câu này hỏi người nghe hôm qua có đi đâu ra ngoài không."
)

add_q("5", "1", P5_1,
    "Khi được hỏi:「きのう、どこか行きましたか。」và bạn hoàn toàn ở nhà không đi đâu cả, câu trả lời đúng chuẩn là:",
    [
        "いいえ、どこへも 行きました。",
        "いいえ、どこへも 行きませんでした。",
        "はい、どこへも 行きませんでした。",
        "いいえ、どこかへ 行きませんでした。"
    ],
    "B",
    "Phủ định hoàn toàn: Từ để hỏi + も + Động từ phủ định ➔「いいえ、どこへも 行きませんでした。」(hoặc どこも行きませんでした)."
)

add_q("5", "1", P5_1,
    "Hoàn thành hội thoại khẳng định đi đâu đó:\nA:「きのう、どこか行きましたか。」\nB:「はい、新宿(しんじゅく)へ 行きました。デパートで ____________。」",
    [
        "かいものします",
        "かいものしました",
        "かいものしませんでした",
        "かいものしたいです"
    ],
    "B",
    "Kể lại hành động đã diễn ra hôm qua tại Shinjuku ➔ Chia quá khứ: かいものしました."
)

add_q("5", "1", P5_1,
    "Trong mẫu câu「[Người] と Vます/ました。」, trợ từ「と」mang ý nghĩa là gì?",
    [
        "Đi đến địa điểm",
        "Làm hành động V cùng VỚI người đó",
        "Cho, tặng người đó cái gì",
        "Hỏi thông tin từ người đó"
    ],
    "B",
    "Trợ từ と đứng sau danh từ chỉ người mang nghĩa \"với, cùng với\". Ví dụ: かぞくと しょくじしました (dùng bữa cùng gia đình)."
)

add_q("5", "1", P5_1,
    "Dịch câu sau: \"Tôi xem phim cùng với người yêu (こいびと).\"",
    [
        "こいびとで えいがを 見ます。",
        "こいびとと えいがを 見ます。",
        "こいびとへ えいがを 見ます。",
        "こいびとに えいがを 見ます。"
    ],
    "B",
    "Cùng với người yêu ➔ こいびとと (恋人と) + えいがを 見ます."
)

add_q("5", "1", P5_1,
    "LƯU Ý NGỮ PHÁP QUAN TRỌNG: Khi làm một hành động một mình (không có ai cùng), ta dùng từ nào?",
    [
        "ひとりと",
        "ひとりで",
        "ひとりへ",
        "ひとりから"
    ],
    "B",
    "Làm một mình dùng cụm phó từ「ひとりで」và TUYỆT ĐỐI KHÔNG dùng trợ từ と. Ví dụ: ひとりで テレビを 見ました (xem TV một mình)."
)

add_q("5", "1", P5_1,
    "Hoàn thành câu hỏi và trả lời:\nA:「日曜日、______ と バーベキューを しましたか。」\nB:「ともだちと しました。」",
    [
        "どこ",
        "なに",
        "だれ",
        "いつ"
    ],
    "C",
    "Hỏi làm cùng ai dùng từ để hỏi だれ (ai):「だれと 〜しましたか。」"
)

add_q("5", "1", P5_1,
    "Liên từ「それから、」(Sau đó...) dùng để làm gì?",
    [
        "Giải thích nguyên nhân của hành động",
        "Liệt kê 2 hành động theo trình tự thời gian (hành động 1 xảy ra trước, rồi đến hành động 2)",
        "Nối 2 tính từ trái ngược nhau",
        "Đưa ra điều kiện giả định"
    ],
    "B",
    "「V1ました。それから、V2ました。」dùng để liên kết 2 hành động liên tiếp nhau theo trình tự trước - sau (\"Làm V1, sau đó làm V2\")."
)

add_q("5", "1", P5_1,
    "Dịch câu sau: \"Hôm qua tôi đã dọn nhà. Sau đó, tôi đã giặt quần áo.\"",
    [
        "きのう 家をそうじしました。そして、せんたくします。",
        "きのう 家をそうじしました。それから、せんたくしました。",
        "きのう 家をそうじしましたから、せんたくしませんでした。",
        "きのう 家をそうじしましたが、せんたくしました。"
    ],
    "B",
    "Liệt kê chuỗi hành động trong quá khứ theo thứ tự: そうじしました。それから、せんたくしました。"
)

add_q("5", "1", P5_1,
    "Dịch câu sau: \"Hôm kia tôi đã gặp bạn. Sau đó, chúng tôi đã đi mua sắm.\"",
    [
        "おととい 友達に会いました。それから、買い物しました。",
        "おととい 友達に会います。そして、買い物します。",
        "おととい 友達に会いましたから、買い物しませんでした。",
        "おととい 友達に会いましたが、買い物しました。"
    ],
    "A",
    "Chuỗi 2 hành động quá khứ: 友達に会いました。それから、買い物しました。"
)

add_q("5", "1", P5_1,
    "Chọn câu đúng để nói: \"Tuần trước tôi đã không gặp cô Thủy.\"",
    [
        "せんしゅう Thuyせんせいに 会いました。",
        "せんしゅう Thuyせんせいに 会いませんでした。",
        "せんしゅう Thuyせんせいに 会いません。",
        "せんしゅう Thuyせんせいに 会いたいです。"
    ],
    "B",
    "Tuần trước (せんしゅう) là thời gian quá khứ, đã không gặp: 会いませんでした (あいませんでした)."
)

# ==============================================================================
# BÀI 5 - PHẦN 2: 休みの後で (Quá khứ Tính từ, どうでしたか, Lý do 〜から)
# ==============================================================================
P5_2 = "休みの後で"

add_q("5", "2", P5_2,
    "Quy tắc chuyển TÍNH TỪ ĐUÔI い sang thì QUÁ KHỨ KHẲNG ĐỊNH là gì?",
    [
        "Bỏ đuôi い thêm「かったです」",
        "Bỏ đuôi い thêm「でした」",
        "Giữ nguyên い thêm「でした」",
        "Bỏ đuôi い thêm「くなかったです」"
    ],
    "A",
    "Tính từ đuôi い ở quá khứ khẳng định: bỏ い + かったです. Ví dụ: あつい ➔ あつかったです (đã nóng)."
)

add_q("5", "2", P5_2,
    "Quy tắc chuyển TÍNH TỪ ĐUÔI い sang thì QUÁ KHỨ PHỦ ĐỊNH là gì?",
    [
        "Bỏ đuôi い thêm「じゃありませんでした」",
        "Bỏ đuôi い thêm「くなかったです」",
        "Giữ nguyên い thêm「くないでした」",
        "Bỏ đuôi い thêm「ませんでした」"
    ],
    "B",
    "Tính từ đuôi い ở quá khứ phủ định: bỏ い + くなかったです. Ví dụ: あつい ➔ あつくなかったです (đã không nóng)."
)

add_q("5", "2", P5_2,
    "NGOẠI LỆ ĐẶC BIỆT: Tính từ「いい」(tốt, đẹp) ở thì quá khứ khẳng định và phủ định lần lượt là:",
    [
        "いかった / いくなかった",
        "よかった / よくなかった",
        "いいでした / いいじゃありませんでした",
        "よいでした / よくないでした"
    ],
    "B",
    "「いい」biến đổi bất quy tắc ở quá khứ thành: よかった (khẳng định) và よくなかった (phủ định)."
)

add_q("5", "2", P5_2,
    "Quy tắc chuyển TÍNH TỪ ĐUÔI な và DANH TỪ sang thì QUÁ KHỨ KHẲNG ĐỊNH là gì?",
    [
        "Thêm かったです",
        "Thêm「でした」(ナA / N + でした)",
        "Thêm なかったです",
        "Thêm ますでした"
    ],
    "B",
    "Tính từ đuôi な và danh từ ở quá khứ khẳng định đi với「でした」. Ví dụ: ひまでした (đã rảnh), 雨でした (trời đã mưa)."
)

add_q("5", "2", P5_2,
    "Quy tắc chuyển TÍNH TỪ ĐUÔI な và DANH TỪ sang thì QUÁ KHỨ PHỦ ĐỊNH là gì?",
    [
        "Thêm くなかったです",
        "Thêm「じゃありませんでした」(hoặc ではありませんでした)",
        "Thêm ませんでした",
        "Thêm ないでした"
    ],
    "B",
    "Tính từ đuôi な và danh từ ở quá khứ phủ định: ナA / N + じゃありませんでした. Ví dụ: ひまじゃありませんでした, 雨じゃありませんでした."
)

add_q("5", "2", P5_2,
    "Dịch câu sau: \"Sáng nay trời đã rất lạnh.\"",
    [
        "けさは さむいです。",
        "けさは さむかったです。",
        "けさは さむいでした。",
        "けさは さむくないです。"
    ],
    "B",
    "けさ (sáng nay) biểu thị thời gian quá khứ, tính từ さむい chia thành: さむかったです。"
)

add_q("5", "2", P5_2,
    "Dịch câu sau: \"Hôm qua anh Tanaka đã rất bận.\"",
    [
        "きのう たなかさんは いそがしいです。",
        "きのう たなかさんは いそがしいでした。",
        "きのう たなかさんは いそがしかったです。",
        "きのう たなかさんは いそがしくないです。"
    ],
    "C",
    "Hôm qua (きのう) bận rộn ➔ いそがしい chia thành いそがしかったです (tuyệt đối không nói いそがしいでした)."
)

add_q("5", "2", P5_2,
    "Dịch câu sau: \"Bài kiểm tra hôm qua đã không khó.\"",
    [
        "きのうのテストは むずかしくないです。",
        "きのうのテストは むずかしくなかったです。",
        "きのうのテストは むずかしいじゃありませんでした。",
        "きのうのテストは むずかしいでした。"
    ],
    "B",
    "Tính từ đuôi い (むずかしい) chia quá khứ phủ định: むずかしくなかったです."
)

add_q("5", "2", P5_2,
    "Dịch câu sau: \"Hôm qua công viên đã rất yên tĩnh.\"",
    [
        "きのう 公園は しずかかったです。",
        "きのう 公園は しずかでした。",
        "きのう 公園は しずかです。",
        "きのう 公園は しずかじゃありませんでした。"
    ],
    "B",
    "しずか là tính từ đuôi な, quá khứ khẳng định dùng: しずかでした."
)

add_q("5", "2", P5_2,
    "Dịch câu sau: \"Bữa tiệc hôm qua đã không vui vẻ.\"",
    [
        "パーティーは たのしくなかったです。",
        "パーティーは たのしいじゃありませんでした。",
        "パーティーは たのしくないです。",
        "パーティーは たのしいでした。"
    ],
    "A",
    "たのしい là tính từ đuôi い, quá khứ phủ định là: たのしくなかったです."
)

add_q("5", "2", P5_2,
    "Dịch câu sau: \"Bữa tiệc hôm qua đã không náo nhiệt (nhộn nhịp).\"",
    [
        "パーティーは にぎやかじゃありませんでした。",
        "パーティーは にぎやかしくなかったです。",
        "パーティーは にぎやかじゃありません。",
        "パーティーは にぎやかでした。"
    ],
    "A",
    "にぎやか là tính từ đuôi な, quá khứ phủ định là: にぎやかじゃありませんでした."
)

add_q("5", "2", P5_2,
    "Câu hỏi「どうでしたか。」dùng để làm gì?",
    [
        "Hỏi về phương hướng đi lại",
        "Hỏi về cảm nhận, tình hình của sự việc/trải nghiệm trong quá khứ (\"Đã như thế nào?\")",
        "Hỏi nguyên nhân vì sao chưa làm",
        "Hỏi giá tiền của món hàng"
    ],
    "B",
    "「どうでしたか。」là dạng quá khứ của「どうですか。」, dùng để hỏi cảm nhận về một sự việc, chuyến đi hay trải nghiệm đã xảy ra trong quá khứ."
)

add_q("5", "2", P5_2,
    "Hoàn thành hội thoại hỏi cảm nhận quá khứ:\nA:「先週のテストは どうでしたか。」\nB:「________________________。」(đã rất khó)",
    [
        "むずかしいです",
        "むずかしくないです",
        "むずかしかったです",
        "むずかしいでした"
    ],
    "C",
    "Hỏi ở quá khứ (どうでしたか) thì câu trả lời tính từ cũng phải chia ở thì quá khứ: むずかしかったです。"
)

add_q("5", "2", P5_2,
    "Hoàn thành hội thoại:\nA:「初めて横浜に行きました。」\nA:「そうですか。どうでしたか。」\nB:「人が多かったです________、楽しかったです。」",
    [
        "から",
        "そして",
        "が",
        "より"
    ],
    "C",
    "Nối 2 vế tương phản trong quá khứ (đông người NHƯNG vui):「人が多かったです が、楽しかったです。」"
)

add_q("5", "2", P5_2,
    "Mẫu câu dùng để hỏi lý do \"Tại sao...?\" trong tiếng Nhật là gì?",
    [
        "どこで〜",
        "どうして〜",
        "だれが〜",
        "いくら〜"
    ],
    "B",
    "Từ để hỏi lý do, nguyên nhân là「どうして」(Tại sao). Ví dụ: どうして やすみましたか (Tại sao bạn nghỉ?)."
)

add_q("5", "2", P5_2,
    "Trong mẫu câu trả lời lý do「[Mệnh đề 1] から、[Mệnh đề 2]。」, từ「から」mang ý nghĩa là gì?",
    [
        "Từ địa điểm nào đó",
        "Vì, do (chỉ nguyên nhân, lý do)",
        "Đến tận khi nào",
        "Hơn là"
    ],
    "B",
    "Trợ từ liên kết「〜から」đứng sau mệnh đề giải thích nguyên nhân mang nghĩa \"Vì... nên...\". Ví dụ: かぜでしたから、やすみました (Vì bị cảm nên tôi đã nghỉ)."
)

add_q("5", "2", P5_2,
    "Hoàn thành câu trả lời lý do:\nA:「どうして けさ やすみましたか。」\nB:「____________________、やすみました。」(Vì bị cảm)",
    [
        "かぜでしたから",
        "かぜですから",
        "かぜでしたそして",
        "かぜでしたが"
    ],
    "A",
    "Bị cảm trong quá khứ: かぜでした + から ➔「かぜでしたから、やすみました。」"
)

add_q("5", "2", P5_2,
    "Dịch câu sau: \"Vì bận nên tuần trước tôi đã không dọn nhà.\"",
    [
        "いそがしかったですから、先週そうじしませんでした。",
        "いそがしいですから、先週そうじしました。",
        "いそがしいでしたが、先週そうじしませんでした。",
        "いそがしくなかったですから、先週そうじしませんでした。"
    ],
    "A",
    "Tuần trước bận (quá khứ): いそがしかったです + から ➔ いそがしかったですから、先週そうじしませんでした。"
)

# ==============================================================================
# BÀI 5 - PHẦN 3: 今度の休みに (ほしい, すき/きらい, 〜たい, Mục đích di chuyển)
# ==============================================================================
P5_3 = "今度の休みに"

add_q("5", "3", P5_3,
    "Cấu trúc「(私は) N が ほしいです。」dùng để diễn đạt điều gì?",
    [
        "Tôi muốn làm hành động N",
        "Tôi muốn có đồ vật, sự vật N",
        "Tôi thích làm việc N",
        "Tôi đã mua N rồi"
    ],
    "B",
    "「N が ほしいです」dùng để diễn đạt mong muốn sở hữu một vật hoặc một thứ gì đó (\"Tôi muốn có N\"). Lưu ý N là danh từ."
)

add_q("5", "3", P5_3,
    "Dịch câu sau: \"Tôi muốn có một chiếc xe đạp mới.\"",
    [
        "新しいじてんしゃを ほしいです。",
        "新しいじてんしゃが ほしいです。",
        "新しいじてんしゃへ ほしいです。",
        "新しいじてんしゃで ほしいです。"
    ],
    "B",
    "Trợ từ đi trước tính từ「ほしい」luôn là「が」: 新しいじてんしゃが ほしいです。"
)

add_q("5", "3", P5_3,
    "Trợ từ nào đi trước các tính từ chỉ sở thích「すき」(thích) và「きらい」(ghét)?",
    [
        "Trợ từ を",
        "Trợ từ が",
        "Trợ từ に",
        "Trợ từ で"
    ],
    "B",
    "Đối tượng của sở thích/ghét đi với trợ từ が: N が すきです / N が きらいです."
)

add_q("5", "3", P5_3,
    "Dịch câu sau: \"Tôi thích thể thao, ghét rượu vang (ワイン).\"",
    [
        "スポーツを すきです。ワインを きらいです。",
        "スポーツが すきです。ワインが きらいです。",
        "スポーツに すきです。ワインに きらいです。",
        "スポーツで すきです。ワインで きらいです。"
    ],
    "B",
    "Cả すき và きらい đều đi với trợ từ が: スポーツが すきです。ワインが きらいです。"
)

add_q("5", "3", P5_3,
    "Quy tắc chuyển động từ sang thể mong muốn thực hiện hành động (Muốn làm V) là gì?",
    [
        "V(bỏ ます) + たいです",
        "V(bỏ ます) + ほしいです",
        "V(nguyên mẫu) + たいです",
        "V(bỏ ます) + ますたい"
    ],
    "A",
    "Muốn làm hành động gì: Động từ thể ます bỏ ます + たいです. Ví dụ: たべます ➔ たべたいです (muốn ăn)."
)

add_q("5", "3", P5_3,
    "Chia động từ「のみます」(uống) sang thể muốn làm:",
    [
        "のみほしいです",
        "のみたいです",
        "のむたいです",
        "のまないたいです"
    ],
    "B",
    "のみます ➔ bỏ ます thêm たいです ➔ のみたいです (muốn uống)."
)

add_q("5", "3", P5_3,
    "Dịch câu sau: \"Tôi muốn leo núi (やまに のぼります).\"",
    [
        "やまに のぼりほしいです。",
        "やまに のぼりたいです。",
        "やまに のぼるたいです。",
        "やまに のぼりましたいです。"
    ],
    "B",
    "のぼります ➔ のぼりたいです. Câu đúng: やまに のぼりたいです。"
)

add_q("5", "3", P5_3,
    "Thể PHỦ ĐỊNH của mong muốn làm gì (Không muốn làm V) được chia như thế nào?",
    [
        "V(bỏ ます) + たくないです",
        "V(bỏ ます) + たいじゃありません",
        "V(bỏ ます) + ないたいです",
        "Vません + たいです"
    ],
    "A",
    "「〜たい」chia giống như một tính từ đuôi い: bỏ い + くないです ➔「V(bỏ ます) + たくないです」. Ví dụ: 飲みたくないです (không muốn uống)."
)

add_q("5", "3", P5_3,
    "Dịch câu sau: \"Ngày mai tôi không muốn đi đâu cả.\"",
    [
        "あしたは どこへも 行きたいです。",
        "あしたは どこへも 行きたくないです。",
        "あしたは どこかへ 行きたくないです。",
        "あしたは どこへも 行きませんたいです。"
    ],
    "B",
    "Hoàn toàn không muốn đi đâu: どこへも + 行きたくないです (tuyệt đối không đi đâu)."
)

add_q("5", "3", P5_3,
    "Khi nói \"Đi đến một sự kiện (buổi hòa nhạc, bữa tiệc...)\", ta dùng cấu trúc nào?",
    [
        "[Sự kiện] で 行きます",
        "[Sự kiện] に 行きます",
        "[Sự kiện] を 行きます",
        "[Sự kiện] から 行きます"
    ],
    "B",
    "Đi tham dự một sự kiện ta dùng trợ từ に: コンサートに 行きます, パーティーに 行きます, 旅行に 行きます."
)

add_q("5", "3", P5_3,
    "Cấu trúc chỉ MỤC ĐÍCH DI CHUYỂN:「[Địa điểm] へ [V(bỏ ます)] に 行きます。」mang nghĩa là gì?",
    [
        "Đi đến địa điểm bằng phương tiện V",
        "Đi đến địa điểm ĐỂ làm hành động V",
        "Đến địa điểm và sau đó không làm V",
        "Vì làm V nên phải đến địa điểm"
    ],
    "B",
    "Mẫu câu「Địa điểm へ V(bỏ ます) に 行きます/来ます/帰ります」biểu thị mục đích của việc đi/đến/về: \"Đi/đến/về đâu ĐỂ làm gì\"."
)

add_q("5", "3", P5_3,
    "Dịch câu sau: \"Tôi đến quán giải khát (きっさてん) để uống cà phê.\"",
    [
        "きっさてんへ コーヒーを のむに 行きます。",
        "きっさてんへ コーヒーを のみに 行きます。",
        "きっさてんへ コーヒーを のみで 行きます。",
        "きっさてんで コーヒーを のみに 行きます。"
    ],
    "B",
    "Uống cà phê: コーヒーを のみます ➔ bỏ ます + に 行きます ➔ コーヒーを のみに 行きます."
)

add_q("5", "3", P5_3,
    "Dịch câu sau: \"Tôi đến hiệu sách (本や) để mua từ điển (じしょ).\"",
    [
        "本やへ じしょを かうに 行きます。",
        "本やへ じしょを かいに 行きます。",
        "本やへ じしょを かいで 行きます。",
        "本やで じしょを かいに 行きます。"
    ],
    "B",
    "かいます ➔ かいに 行きます. Câu đúng: 本やへ じしょを かいに 行きます。"
)

add_q("5", "3", P5_3,
    "Dịch câu sau: \"Tôi đến công viên để chụp ảnh (しゃしんを とります).\"",
    [
        "こうえんへ しゃしんを とりに 行きます。",
        "こうえんへ しゃしんを とるに 行きます。",
        "こうえんで しゃしんを とりに 行きます。",
        "こうえんへ しゃしんを とりへ 行きます。"
    ],
    "A",
    "とります ➔ とりに 行きます. Câu đúng: こうえんへ しゃしんを とりに 行きます。"
)

add_q("5", "3", P5_3,
    "Khi mục đích di chuyển là một DANH TỪ HÀNH ĐỘNG (như 勉強, 買い物...), cấu trúc câu sẽ là:",
    [
        "[Địa điểm] へ [Danh từ] で 行きます",
        "[Địa điểm] へ [Danh từ] に 行きます",
        "[Địa điểm] で [Danh từ] を 行きます",
        "[Địa điểm] に [Danh từ] へ 行きます"
    ],
    "B",
    "Với danh từ hành động, ta ghép trực tiếp: Danh từ + に 行きます. Ví dụ: 日本へ 日本語の勉強に 行きます (Đến Nhật để học tiếng Nhật)."
)

add_q("5", "3", P5_3,
    "Từ bất định「なにか」(cái gì đó) được dùng như thế nào trong câu mời mọc/hỏi thăm?",
    [
        "なにか 食べたいですか。(Bạn có muốn ăn cái gì đó không?)",
        "なにかを 食べたいですか。",
        "なにが 食べたいですか。(Chỉ dùng khi hỏi cụ thể)",
        "なんでも 食べたいですか。"
    ],
    "A",
    "「なにか」là từ bất định mang nghĩa \"cái gì đó\", có thể đứng độc lập trước động từ mà không cần trợ từ を: なにか 食べたいですか。"
)

add_q("5", "3", P5_3,
    "Hoàn thành hội thoại:\nA:「なにか 食べたいですか。」\nB:「はい、ケーキを ____________。」",
    [
        "たべました",
        "おねがいします",
        "いきましょう",
        "ほしいでした"
    ],
    "B",
    "Khi người khác hỏi có muốn ăn gì không, ta gọi món kèm từ lịch sự:「ケーキを おねがいします。」(Làm ơn cho tôi bánh ngọt)."
)

add_q("5", "3", P5_3,
    "Hoàn thành câu hỏi:\n「ふゆやすみは ________ 行きましたか。」(Kỳ nghỉ đông bạn có đi đâu chơi không?)\n→「はい、ほっかいどうへ 行きました。」",
    [
        "どこへも",
        "どこかへ",
        "だれと",
        "なにを"
    ],
    "B",
    "Hỏi có đi đâu đó không:「どこかへ 行きましたか。」."
)

# ==============================================================================
# BÀI 6 - PHẦN 1: 一緒に行きませんか (Rủ rê 〜ませんか, 〜ましょう, であります, 〜まい)
# ==============================================================================
P6_1 = "一緒に行きませんか"

add_q("6", "1", P6_1,
    "Mẫu câu「Vませんか。」dùng để làm gì trong giao tiếp tiếng Nhật?",
    [
        "Hỏi xem người nghe có bao giờ làm V chưa",
        "Rủ rê, mời mọc người nghe cùng thực hiện hành động V một cách lịch sự",
        "Cấm đoán người nghe không được làm V",
        "Xác nhận người nghe đã hoàn thành V hay chưa"
    ],
    "B",
    "「Vませんか」là cấu trúc mời mọc, rủ rê rất lịch sự (\"Cùng làm V với tôi nhé?\"), tôn trọng ý kiến của đối phương."
)

add_q("6", "1", P6_1,
    "Dịch câu sau: \"Tối nay cùng đi ăn cơm không?\"",
    [
        "今晩、いっしょに ご飯を 食べますか。",
        "今晩、いっしょに ご飯を 食べませんか。",
        "今晩、いっしょに ご飯を 食べましたか。",
        "今晩、いっしょに ご飯を 食べましょうか。"
    ],
    "B",
    "Rủ rê lịch sự:「今晩、いっしょに ご飯を 食べませんか。」."
)

add_q("6", "1", P6_1,
    "Khi ĐỒNG Ý với một lời rủ rê「Vませんか。」, câu trả lời chuẩn xác và nhiệt tình nhất là:",
    [
        "いいですね。Vましょう。",
        "いいですね。Vません。",
        "そうですか。Vました。",
        "はい、Vますか。"
    ],
    "A",
    "Đồng ý lời rủ rê:「いいですね。Vましょう。」(Hay quá! Cùng làm thôi!)."
)

add_q("6", "1", P6_1,
    "Hoàn thành hội thoại đồng ý:\nA:「いっしょに ビールを 飲みませんか。」\nB:「いいですね。____________。」",
    [
        "のみません",
        "のみましょう",
        "のみました",
        "のみたいでした"
    ],
    "B",
    "Đáp lại lời mời uống bia:「いいですね。飲みましょう。」"
)

add_q("6", "1", P6_1,
    "Khi muốn TỪ CHỐI KHÉO một lời mời mà không làm mất lòng đối phương, người Nhật thường mở đầu bằng câu:",
    [
        "だめです。",
        "いやです。",
        "すみません、[thời gian] は ちょっと…",
        "いきません。"
    ],
    "C",
    "Cách từ chối lịch sự và khéo léo trong văn hóa giao tiếp Nhật Bản:「すみません、今晩は ちょっと…」(Xin lỗi, tối nay tôi có chút việc kẹt...)."
)

add_q("6", "1", P6_1,
    "Để giải thích lý do từ chối sau câu「すみません、ちょっと…」, ta dùng cấu trúc nào?",
    [
        "[Lý do] がありますから / [Lý do]ですから",
        "[Lý do] をしますから",
        "[Lý do] がありますそして",
        "[Lý do] ですが"
    ],
    "A",
    "Nêu lý do từ chối: [Lý do] + がありますから (Vì có việc/có hẹn/có bài thi...) hoặc Tính từ + ですから (Vì bận...)."
)

add_q("6", "1", P6_1,
    "Hoàn thành câu từ chối vì có việc bận (用事 - ようじ):\nA:「あした いっしょに 映画を見ませんか。」\nB:「すみません、あしたは ちょっと…。ようじが ____________。」",
    [
        "ありますから",
        "ありませんから",
        "ありましたから",
        "ありましょうから"
    ],
    "A",
    "Vì có việc bận:「ようじが ありますから。」"
)

add_q("6", "1", P6_1,
    "Hoàn thành câu từ chối vì có hẹn trước (約束 - やくそく):\n「すみません、今晩は ちょっと…。やくそくが ____________。」",
    [
        "ありますから",
        "ありませんから",
        "ありませんでしたから",
        "あるでしょうから"
    ],
    "A",
    "Vì có hẹn:「やくそくが ありますから。」"
)

add_q("6", "1", P6_1,
    "Mẫu câu「N1 (địa điểm) で N2 (sự kiện) が あります。」dùng để diễn đạt điều gì?",
    [
        "N1 có đồ vật N2 đang nằm yên",
        "Ở địa điểm N1 diễn ra một sự kiện, hoạt động, lễ hội, bữa tiệc N2",
        "N2 di chuyển từ N1 đến nơi khác",
        "N1 và N2 có mối quan hệ sở hữu"
    ],
    "B",
    "Khác với「にあります」(tồn tại tĩnh của vật), cấu trúc「N1 で N2 があります」dùng khi N2 là sự kiện, trận đấu, buổi hòa nhạc, lễ hội ĐƯỢC TỔ CHỨC TẠI N1."
)

add_q("6", "1", P6_1,
    "PHÂN BIỆT TRỢ TỪ: Điền trợ từ thích hợp vào câu sau:\n「土曜日、浅草(あさくさ) ______ お祭りが あります。」(Thứ 7 ở Asakusa diễn ra lễ hội)",
    [
        "に",
        "で",
        "へ",
        "を"
    ],
    "B",
    "お祭り (lễ hội) là một sự kiện được tổ chức ➔ Dùng trợ từ で:「浅草で お祭りが あります。」"
)

add_q("6", "1", P6_1,
    "Dịch câu sau: \"Ở Đại học FPT có diễn ra trận đấu bóng đá (サッカーの しあい).\"",
    [
        "FPT大学に サッカーの しあいが あります。",
        "FPT大学で サッカーの しあいが あります。",
        "FPT大学へ サッカーの しあいが あります。",
        "FPT大学は サッカーの しあいです。"
    ],
    "B",
    "Trận đấu bóng đá là sự kiện tổ chức tại trường ➔ Dùng trợ từ で:「FPT大学で サッカーの しあいが あります。」"
)

add_q("6", "1", P6_1,
    "Dịch câu sau: \"Ở nhà bạn Mai có một bữa tiệc (パーティー).\"",
    [
        "Maiさんの 家に パーティーが あります。",
        "Maiさんの 家で パーティーが あります。",
        "Maiさんの 家へ パーティーが あります。",
        "Maiさんの 家から パーティーが あります。"
    ],
    "B",
    "Bữa tiệc là sự kiện diễn ra tại nhà ➔ Dùng で:「Maiさんの 家で パーティーが あります。」"
)

add_q("6", "1", P6_1,
    "Lượng từ「〜枚 (〜まい)」trong tiếng Nhật dùng để đếm những vật có đặc điểm gì?",
    [
        "Những vật dài, hình trụ tròn (bút, chai nước...)",
        "Những vật mỏng, phẳng (giấy, vé, áo sơ mi, đĩa CD, tranh ảnh, bưu thiếp...)",
        "Các loại máy móc, xe cộ",
        "Các loại động vật nhỏ"
    ],
    "B",
    "「〜まい (枚)」là trợ số từ dùng để đếm các vật mỏng, dẹt, phẳng như: vé xem phim, áo, đĩa CD, tờ giấy, tem, ảnh..."
)

add_q("6", "1", P6_1,
    "Điền lượng từ vào câu sau:\n「映画の チケットが 2______ あります。」(Tôi có 2 tấm vé xem phim)",
    [
        "台 (だい)",
        "本 (ほん)",
        "枚 (まい)",
        "個 (こ)"
    ],
    "C",
    "Vé xem phim là vật mỏng, phẳng ➔ Dùng lượng từ 枚 (まい): 2まい (にまい)."
)

add_q("6", "1", P6_1,
    "Cách đọc số đếm lượng từ: \"4 chiếc áo sơ mi\" được phát âm là gì?",
    [
        "しまい",
        "よんまい",
        "よまい",
        "しちまい"
    ],
    "B",
    "4 vật mỏng đọc là よんまい (四枚). Tuyệt đối không đọc là しまい."
)

add_q("6", "1", P6_1,
    "Dịch câu sau sang tiếng Nhật: \"Hôm qua tôi đã mua 3 chiếc đĩa CD.\"",
    [
        "きのう CDを 3本(さんぼん) 買いました。",
        "きのう CDを 3枚(さんまい) 買いました。",
        "きのう CDを 3台(さんだい) 買いました。",
        "きのう CDを 3つ 買いました。"
    ],
    "B",
    "Đĩa CD đếm bằng 〜まい:「CDを 3枚(さんまい) 買いました。」"
)

add_q("6", "1", P6_1,
    "Hoàn thành câu theo slide bài học:\n「きのう シャツを 9______ 買いました。」(Hôm qua tôi đã mua 9 chiếc áo sơ mi)",
    [
        "まい (枚)",
        "だい (台)",
        "ほん (本)",
        "さつ (冊)"
    ],
    "A",
    "Áo sơ mi đếm bằng lượng từ 枚 (まい): きゅうまい (9枚)."
)

add_q("6", "1", P6_1,
    "Hoàn thành hội thoại mời đi xem concert:\nA:「コンサートの チケットが 2枚 あります。いっしょに ____________。」\nB:「いいですね。行きましょう。」",
    [
        "行きませんか",
        "行きましょうか",
        "行きましたか",
        "行かないでした"
    ],
    "A",
    "Khi có vé và muốn rủ bạn đi cùng:「いっしょに 行きませんか。」"
)

# ==============================================================================
# BÀI 6 - PHẦN 2: どちらがいいですか。 (So sánh hơn より, どちら, So sánh nhất 一番)
# ==============================================================================
P6_2 = "どちらがいいですか。"

add_q("6", "2", P6_2,
    "Cấu trúc so sánh hơn giữa 2 đối tượng「N1 は N2 より Adj です。」mang nghĩa là gì?",
    [
        "N1 không bằng N2 về tính chất Adj",
        "N1 hơn N2 về tính chất Adj (N1 có tính chất Adj hơn so với N2)",
        "N1 và N2 có tính chất Adj giống nhau",
        "N2 có tính chất Adj nhất"
    ],
    "B",
    "Mẫu câu「N1 は N2 より Adj です」dùng để so sánh hơn: chủ ngữ N1 hơn đối tượng mốc so sánh N2. Ví dụ: 車は バスより 速いです (Ô tô nhanh hơn xe buýt)."
)

add_q("6", "2", P6_2,
    "Dịch câu sau: \"Hokkaido mát hơn Osaka.\"",
    [
        "北海道は 大阪より すずしいです。",
        "大阪は 北海道より すずしいです。",
        "北海道より 大阪は すずしいです。",
        "北海道は 大阪が すずしいです。"
    ],
    "A",
    "Đối tượng hơn đặt trước は:「北海道は 大阪より すずしいです。」(Hokkaido mát hơn so với Osaka)."
)

add_q("6", "2", P6_2,
    "Dịch câu sau: \"Máy bay nhanh hơn tàu thủy (ふね).\"",
    [
        "飛行機は 船より はやいです。",
        "船は 飛行機より はやいです。",
        "飛行機より 船は はやいです。",
        "飛行機は 船が はやいです。"
    ],
    "A",
    "Máy bay (飛行機) nhanh hơn tàu thủy (船):「飛行機は 船より はやいです。」"
)

add_q("6", "2", P6_2,
    "Dịch câu sau: \"Trung Quốc (中国) đông dân hơn Nhật Bản (日本).\"",
    [
        "日本は 中国より 人が多いです。",
        "中国は 日本より 人が多いです。",
        "中国より 日本は 人が多いです。",
        "中国は 日本のほうが 人が多いです。"
    ],
    "B",
    "Trung Quốc hơn Nhật Bản về lượng người:「中国は 日本より 人が多いです。」"
)

add_q("6", "2", P6_2,
    "Dịch câu sau: \"Núi Phú Sĩ (3776m) thấp hơn đỉnh Everest (8800m).\"",
    [
        "エベレストは 富士山より 低いです。",
        "富士山は エベレストより 低いです。",
        "富士山は エベレストより 高いです。",
        "富士山のほうが エベレストより 高いです。"
    ],
    "B",
    "Phú Sĩ thấp hơn Everest:「富士山(ふじさん)は エベレストより 低(ひく)いです。」"
)

add_q("6", "2", P6_2,
    "Cấu trúc câu hỏi so sánh lựa chọn giữa 2 đối tượng là gì?",
    [
        "N1 と N2 と なにが Adj ですか。",
        "N1 と N2 と どちらが Adj ですか。",
        "N1 は N2 より どちらが Adj ですか。",
        "N1 と N2 と いつが Adj ですか。"
    ],
    "B",
    "Câu hỏi so sánh giữa 2 đối tượng:「N1 と N2 と どちらが Adj ですか。」(Giữa N1 và N2 cái nào Adj hơn?)."
)

add_q("6", "2", P6_2,
    "Khi trả lời câu hỏi lựa chọn「N1 と N2 と どちらが Adj ですか。」và bạn CHỌN N1 HƠN, mẫu câu trả lời là:",
    [
        "N1 より Adj です。",
        "N1 のほうが Adj です。",
        "N1 が 一番 Adj です。",
        "N1 は Adj です。"
    ],
    "B",
    "Chọn 1 trong 2 đối tượng dùng cụm「N1 のほうが Adj です」(Phía N1 thì... hơn)."
)

add_q("6", "2", P6_2,
    "Khi trả lời câu hỏi lựa chọn「N1 と N2 と どちらが Adj ですか。」và bạn thấy CẢ HAI ĐỀU NHƯ NHAU, mẫu câu trả lời là:",
    [
        "どちらも Adj です。",
        "どちらが Adj です。",
        "どれも Adj です。",
        "どちらは Adj です。"
    ],
    "A",
    "Cả hai đều cùng tính chất:「どちらも Adj です。」(Ví dụ: どちらも 好きです - Tôi thích cả hai)."
)

add_q("6", "2", P6_2,
    "Hoàn thành hội thoại so sánh lựa chọn:\nA:「タクシーと 電車と どちらが 速いですか。」\nB:「________________________。」(Taxi nhanh hơn)",
    [
        "タクシーより 速いです",
        "タクシーのほうが 速いです",
        "タクシーが 一番速いです",
        "タクシーは 速いです"
    ],
    "B",
    "Trả lời lựa chọn:「タクシーのほうが 速いです。」(Taxi thì nhanh hơn)."
)

add_q("6", "2", P6_2,
    "Hoàn thành hội thoại so sánh lựa chọn:\nA:「英語と 日本語と どちらが 難しいですか。」\nB:「________________________。」(Tiếng Nhật khó hơn)",
    [
        "日本語のほうが 難しいです",
        "日本語より 難しいです",
        "日本語が 一番難しいです",
        "どちらも 難しくないです"
    ],
    "A",
    "Chọn tiếng Nhật khó hơn:「日本語のほうが 難しいです。」"
)

add_q("6", "2", P6_2,
    "Hoàn thành hội thoại so sánh lựa chọn:\nA:「犬と 猫と どちらが 好きですか。」\nB:「________________________。」(Tôi thích cả hai)",
    [
        "犬のほうが 好きです",
        "どちらも 好きです",
        "猫より 好きです",
        "どちらが 好きです"
    ],
    "B",
    "Thích cả hai con:「どちらも 好きです。」"
)

add_q("6", "2", P6_2,
    "Cấu trúc so sánh nhất trong một phạm vi/tập hợp là gì?",
    [
        "N1(phạm vi) で N2 が 一番(いちばん) Adj です。",
        "N1(phạm vi) に N2 は 一番 Adj です。",
        "N1(phạm vi) より N2 が 一番 Adj です。",
        "N1(phạm vi) と N2 は 一番 Adj です。"
    ],
    "A",
    "Mẫu câu so sánh nhất:「N1(phạm vi) で N2 が 一番(いちばん) Adj です。」(Trong phạm vi N1 thì N2 là... nhất)."
)

add_q("6", "2", P6_2,
    "Dịch câu sau: \"Trên thế giới (世界 - せかい), nước Nga rộng nhất.\"",
    [
        "世界に ロシアが 一番広いです。",
        "世界で ロシアが 一番広いです。",
        "世界より ロシアが 一番広いです。",
        "世界は ロシアより 広いです。"
    ],
    "B",
    "Phạm vi so sánh dùng trợ từ で, đối tượng nhất dùng が + 一番:「世界で ロシアが 一番広いです。」"
)

add_q("6", "2", P6_2,
    "Dịch câu sau: \"Trong các môn thể thao (スポーツ), bóng đá là thú vị nhất.\"",
    [
        "スポーツで サッカーが 一番おもしろいです。",
        "スポーツに サッカーが 一番おもしろいです。",
        "スポーツより サッカーのほうが おもしろいです。",
        "スポーツで サッカーは おもしろいです。"
    ],
    "A",
    "Trong các môn thể thao (スポーツで) + bóng đá nhất (サッカーが 一番おもしろいです)."
)

add_q("6", "2", P6_2,
    "Dịch câu sau: \"Trong 1 năm (1年), tháng 12 là lạnh nhất.\"",
    [
        "1年で 12月が 一番寒いです。",
        "1年に 12月は 一番寒いです。",
        "1年より 12月のほうが 寒いです。",
        "1年で 12月が 寒くないです。"
    ],
    "A",
    "Trong 1 năm: 1年で + 12月が 一番寒いです."
)

add_q("6", "2", P6_2,
    "Để hỏi về ĐỒ VẬT trong câu hỏi so sánh nhất: \"Trong các loại hoa quả (果物), bạn thích quả gì nhất?\", câu tiếng Nhật đúng là:",
    [
        "果物で どこが 一番好きですか。",
        "果物で いつが 一番好きですか。",
        "果物で 何(なに)が 一番好きですか。",
        "果物で だれが 一番好きですか。"
    ],
    "C",
    "Hỏi về đồ vật, quả dùng「何(なに)が 一番好きですか。」."
)

add_q("6", "2", P6_2,
    "Để hỏi về THỜI GIAN trong câu hỏi so sánh nhất: \"Ở Hokkaido, khi nào là đẹp nhất?\", câu tiếng Nhật đúng là:",
    [
        "北海道は 何が 一番いいですか。",
        "北海道は いつが 一番いいですか。",
        "北海道は どこが 一番いいですか。",
        "北海道は だれが 一番いいですか。"
    ],
    "B",
    "Hỏi thời điểm, khi nào dùng từ để hỏi いつ:「北海道は いつが 一番いいですか。」"
)

add_q("6", "2", P6_2,
    "Để hỏi về NGƯỜI trong câu hỏi so sánh nhất: \"Trong các ca sĩ (歌手 - かしゅ), bạn thích ai nhất?\", câu tiếng Nhật đúng là:",
    [
        "歌手で だれが 一番好きですか。",
        "歌手で 何が 一番好きですか。",
        "歌手で どこが 一番好きですか。",
        "歌手で いつが 一番好きですか。"
    ],
    "A",
    "Hỏi về người dùng từ để hỏi だれ:「歌手で だれが 一番好きですか。」"
)

# ==============================================================================
# BÀI 6 - PHẦN 3: 約束 (Đã làm chưa もう〜ましたか, まだです, Đề xuất Nはどうですか, ね/よ)
# ==============================================================================
P6_3 = "約束"

add_q("6", "3", P6_3,
    "Cấu trúc「もう Vましたか。」dùng để hỏi điều gì?",
    [
        "Hỏi hành động V sẽ diễn ra khi nào",
        "Hỏi một hành động đã được hoàn thành hay chưa (\"Đã làm V chưa?\")",
        "Rủ người khác cùng làm V",
        "Hỏi tại sao không làm V"
    ],
    "B",
    "Phó từ「もう」đi với thể quá khứ「Vましたか」dùng để hỏi xem hành động đó đã hoàn thành chưa (\"Đã làm V rồi à / Đã làm V chưa?\")."
)

add_q("6", "3", P6_3,
    "Khi trả lời KHẲNG ĐỊNH cho câu hỏi「もう Vましたか。」(Đã làm V chưa?), mẫu câu trả lời là:",
    [
        "はい、もう Vました。",
        "はい、まだ Vました。",
        "はい、いま Vます。",
        "いいえ、もう Vました。"
    ],
    "A",
    "Đã làm rồi:「はい、もう Vました。」Ví dụ: はい、もう食べました (Vâng, tôi đã ăn rồi)."
)

add_q("6", "3", P6_3,
    "QUY TẮC BẮT BUỘC: Khi trả lời PHỦ ĐỊNH cho câu hỏi「もう Vましたか。」(chưa làm), câu trả lời chuẩn xác là:",
    [
        "いいえ、もう食べませんでした。",
        "いいえ、まだです。",
        "いいえ、食べませんでした。",
        "いいえ、まだ食べました。"
    ],
    "B",
    "Khi hành động chưa được thực hiện, BẮT BUỘC trả lời:「いいえ、まだです。」(Chưa, tôi vẫn chưa). Tuyệt đối không trả lời \"いいえ、もうVませんでした\"."
)

add_q("6", "3", P6_3,
    "Hoàn thành hội thoại:\nA:「もう 昼ごはんを食べましたか。」(Bạn đã ăn trưa chưa?)\nB:「いいえ、________。」",
    [
        "もうです",
        "まだです",
        "たべました",
        "たべませんでした"
    ],
    "B",
    "Chưa ăn trưa:「いいえ、まだです。」(Chưa, tôi vẫn chưa ăn)."
)

add_q("6", "3", P6_3,
    "Hoàn thành hội thoại:\nA:「田中さんは もう 起きましたか。」(Anh Tanaka đã thức dậy chưa?)\nB:「はい、________________。」(Đã dậy rồi)",
    [
        "もう 起きました",
        "まだ 起きました",
        "起きます",
        "起きませんでした"
    ],
    "A",
    "Đã dậy rồi:「はい、もう 起きました。」"
)

add_q("6", "3", P6_3,
    "SO SÁNH NGỮ PHÁP QUAN TRỌNG: Mẫu câu「N は どうですか。」ở BÀI 6.3 có ý nghĩa gì khác so với BÀI 4.2?",
    [
        "Bài 4.2 hỏi tính chất (N như thế nào?), còn Bài 6.3 dùng để ĐƯA RA GỢI Ý, ĐỀ XUẤT Ý KIẾN (Hay là N xem sao?)",
        "Bài 6.3 hỏi giá tiền, còn Bài 4.2 hỏi đường đi",
        "Cả hai bài hoàn toàn giống nhau không có gì khác",
        "Bài 6.3 chỉ dùng cho món ăn, còn Bài 4.2 chỉ dùng cho thời tiết"
    ],
    "A",
    "Ở Bài 4.2:「N は どうですか」dùng để hỏi đặc điểm/tính chất (\"N như thế nào?\"). Ở Bài 6.3:「N は どうですか」dùng để đưa ra gợi ý, đề xuất (\"Hay là N thì sao? / Thử N xem thế nào?\")."
)

add_q("6", "3", P6_3,
    "Hoàn thành hội thoại đưa ra gợi ý món ăn:\nA:「いっしょに 昼ごはんを食べませんか。」\nB:「いいですね。何を食べますか。」\nA:「日本料理は どうですか。」(Món Nhật thì sao?)\nB:「____________。行きましょう。」",
    [
        "おいしいです",
        "いいですよ",
        "まだです",
        "からいです"
    ],
    "B",
    "Đáp lại lời gợi ý món ăn:「いいですよ。行きましょう。」(Được đấy, đi thôi!)."
)

add_q("6", "3", P6_3,
    "Hoàn thành hội thoại gợi ý địa điểm du lịch:\nA:「もう4月ですね。どこに旅行しますか。」\nB:「東京は どうですか。」(Tokyo thì sao?)\nA:「いいですね。4月は桜がきれいですから。____________。」",
    [
        "そうしましょう",
        "そうでした",
        "そうしません",
        "そうでしたか"
    ],
    "A",
    "Đồng ý với gợi ý của đối phương:「いいですね。そうしましょう。」(Hay đấy, cùng làm thế nhé!)."
)

add_q("6", "3", P6_3,
    "Chức năng chính của trợ từ cuối câu「ね」trong giao tiếp là gì?",
    [
        "Đưa ra một thông tin hoàn toàn mới mà người nghe chưa biết",
        "Kêu gọi sự đồng tình hoặc xác nhận thông tin mà cả người nói và người nghe cùng biết (\"...nhỉ!\")",
        "Hỏi giá tiền của món hàng",
        "Chỉ sự bắt buộc phải thi hành"
    ],
    "B",
    "「ね」dùng khi cả hai người đều cùng biết hoặc cảm nhận được điều đó, nhằm tạo sự đồng cảm hoặc xác nhận lại (\"nhỉ!\")."
)

add_q("6", "3", P6_3,
    "Chức năng chính của trợ từ cuối câu「よ」trong giao tiếp là gì?",
    [
        "Hỏi xin sự giúp đỡ",
        "Cung cấp thông tin mới người nghe chưa biết, hoặc dùng để nhắc nhở, nhấn mạnh (\"...đấy / nhé!\")",
        "Kêu gọi sự đồng cảm",
        "Thừa nhận mình sai"
    ],
    "B",
    "「よ」dùng khi người nói muốn truyền đạt thông tin mới người nghe chưa biết, hoặc nhằm mục đích nhắc nhở, quả quyết (\"...đấy / nhé!\")."
)

add_q("6", "3", P6_3,
    "TÌNH HUỐNG: Đã muộn (12 giờ đêm) và bạn muốn nhắc nhở bạn cùng phòng đi ngủ vì người đó mải chơi không để ý giờ, bạn nói:",
    [
        "もう 12時ですね。",
        "もう 12時ですよ。",
        "もう 12時でしたか。",
        "まだ 12時ですね。"
    ],
    "B",
    "Dùng「よ」để thông báo thông tin mới và nhắc nhở người khác:「もう 12時ですよ。」(Đã 12 giờ rồi đấy!)."
)

add_q("6", "3", P6_3,
    "TÌNH HUỐNG: Hai bạn đang cùng đi dạo dưới trời nắng nóng, bạn quay sang trò chuyện để tìm kiếm sự đồng cảm:",
    [
        "きょうは あついですね。",
        "きょうは あついですよ。",
        "きょうは あつくないですね。",
        "きょうは さむいですね。"
    ],
    "A",
    "Cả hai cùng cảm nhận được cái nóng ➔ Dùng「ね」để tìm kiếm sự đồng tình:「きょうは あついですね。」(Hôm nay nóng nhỉ!)."
)

add_q("6", "3", P6_3,
    "TÌNH HUỐNG: Bạn giới thiệu với một người khách vừa tới thăm quê hương mình về rau sạch ở quê:",
    [
        "ここの野菜は おいしいですね。",
        "ここの野菜は おいしいですよ。",
        "ここの野菜は おいしくないですね。",
        "ここの野菜は おいしいでした。"
    ],
    "B",
    "Cung cấp thông tin mới cho người khách chưa biết ➔ Dùng「よ」:「ここの野菜は おいしいですよ。」(Rau ở đây ngon lắm đấy!)."
)

add_q("6", "3", P6_3,
    "Dịch câu sau: \"Dịp Tết (お正月) mời bạn đến nhà tôi chơi nhé. Cùng tổ chức tiệc Tết vui vẻ nhé!\"",
    [
        "お正月に 私のうちへ 来ませんか。いっしょに 楽しい お正月のパーティーを しましょう。",
        "お正月に 私のうちへ 来ました。いっしょに 楽しい お正月のパーティーを しました。",
        "お正月に 私のうちへ 来ますか。いっしょに 楽しい お正月のパーティーを しますか。",
        "お正月に 私のうちへ 行きませんか。いっしょに 楽しい お正月のパーティーを 行きましょう。"
    ],
    "A",
    "Lời mời đến nhà mình:「来ませんか」. Lời rủ cùng tổ chức tiệc:「パーティーを しましょう」."
)

add_q("6", "3", P6_3,
    "Hoàn thành câu theo bài đọc thư:\n\"Hanoino seikatsuwa omoshiroi desu____, benri desu. Demo, totemo isogashii desu.\"",
    [
        "ね",
        "よ",
        "か",
        "も"
    ],
    "A",
    "Cảm thán chia sẻ:「ハノイの生活は おもしろいですね。そして べんりです。」"
)

add_q("6", "3", P6_3,
    "Khi đồng ý làm theo một gợi ý, câu nào sau đây có nghĩa là \"Cùng làm như thế nhé!\":",
    [
        "そうでした。",
        "そうしましょう。",
        "そうしません。",
        "そうですよ。"
    ],
    "B",
    "Đồng ý với gợi ý:「そうしましょう。」(Hãy cùng làm như vậy đi!)."
)

# Output generation
out_file = "js/grammar_data.js"
full_content = """/**
 * KHO DỮ LIỆU CÂU HỎI NGỮ PHÁP TIẾNG NHẬT (BÀI 4 - 6)
 * Được biên soạn chi tiết theo toàn bộ giáo trình và bài tập:
 * - Bài 4: Phương hướng, Phương tiện, Thời gian, Tính từ đuôi い/な, Tồn tại にあります, Nối câu そして/が, Phó từ, Trợ từ ね
 * - Bài 5: Quá khứ Động từ, どこか/どこも, Làm cùng ai と/ひとりで, それから, Quá khứ Tính từ, どうでしたか, Lý do 〜から, 〜たい, Đi để làm gì に行きます
 * - Bài 6: Rủ rê 〜ませんか/〜ましょう, Từ chối 〜から, Sự kiện diễn ra であります, Lượng từ 〜まい, So sánh hơn より, So sánh lựa chọn どちら, So sánh nhất 一番, Đã làm chưa もう〜ましたか, Gợi ý Nはどうですか, Phân biệt ね và よ
 */

window.RAW_DATABASE_GRAMMAR = `
""" + "\n".join(questions) + """
`;

window.GRAMMAR_LESSON_PARTS = {
    "4": {
        "1": "どこ？ (Vị trí, Phương tiện, Thời gian)",
        "2": "どんなところ？ (Tính từ, Tồn tại, Nối câu)",
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
        "3": "約束 (Đã làm chưa もう, Gợi ý Nはどうですか, ね/よ)"
    }
};
"""

with open(out_file, "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Generated {len(questions)} grammar questions successfully in {out_file}!")
