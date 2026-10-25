# -*- coding: utf-8 -*-
"""
Dữ liệu câu hỏi ngữ pháp Bài 4 - Dekiru Nihongo
Chia làm 2 dạng câu hỏi rõ ràng:
1. [HỎI NGỮ PHÁP]: Hỏi khái niệm, cấu trúc, quy tắc, cách trả lời theo chuẩn ngữ pháp
2. [DỊCH CÂU]: Dịch từ câu tiếng Việt sang tiếng Nhật tương ứng
"""

def register_lesson_4(add_pair):
    P4_1 = "どこ？ (Vị trí, Phương tiện, Thời gian)"
    P4_2 = "どんなところ？ (Tính từ, Tồn tại, Nối câu, Phủ định)"
    P4_3 = "きせつ・りょうり (Phó từ, Trợ từ ね, Thời tiết)"

    # ==============================================================================
    # PHẦN 1: どこ？ (9 cặp câu hỏi)
    # ==============================================================================

    # Cặp 1: Vị trí thành phố / phương hướng
    add_pair("4", "1", P4_1,
        "Mẫu câu「Thành phố は đất nước の [hướng] です。」dùng để làm gì?",
        [
            "Nói về dân số của một thành phố",
            "Xác định vị trí phương hướng của thành phố thuộc một quốc gia",
            "Hỏi giá vé đi đến thành phố",
            "Miêu tả thời tiết của đất nước"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cấu trúc「Thành phố は đất nước の [hướng] です。」dùng để diễn đạt vị trí địa lý của thành phố nằm ở phía nào (đông, tây, nam, bắc, trung tâm) của đất nước đó. Ví dụ: Lang Sonは ベトナムの きたです。",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Lạng Sơn ở phía bắc Việt Nam.\"",
        [
            "Lang Sonは ベトナムの きたです。",
            "Lang Sonは ベトナムの みなみです。",
            "Lang Sonは ベトナムの ひがしです。",
            "Lang Sonは ベトナムの にしです。"
        ],
        "A",
        "Phía bắc trong tiếng Nhật là きた. Câu dịch chuẩn là: Lang Sonは ベトナムの きたです。"
    )

    # Cặp 2: Phương hướng: Phía nam
    add_pair("4", "1", P4_1,
        "Khi muốn nói về phương hướng \"Phía nam\" của một quốc gia, theo chuẩn ngữ pháp tiếng Nhật ta dùng từ vựng nào?",
        [
            "きた",
            "にし",
            "みなみ",
            "ひがし"
        ],
        "C",
        "💡 Chuẩn ngữ pháp: 4 phương hướng cơ bản trong tiếng Nhật: きた (Bắc), みなみ (Nam), ひがし (Đông), にし (Tây). Khi nói Cà Mau ở phía nam Việt Nam:「Cà Mauは ベトナムの みなみです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cà Mau ở phía nam Việt Nam.\"",
        [
            "Cà Mauは ベトナムの きたです。",
            "Cà Mauは ベトナムの にしです。",
            "Cà Mauは ベトナムの みなみです。",
            "Cà Mauは ベトナムの まんなかです。"
        ],
        "C",
        "Phía nam là みなみ. Do đó câu đúng là: Cà Mauは ベトナムの みなみです。"
    )

    # Cặp 3: Vị trí chính giữa / miền Trung
    add_pair("4", "1", P4_1,
        "Để nói một địa điểm nằm ở \"chính giữa / miền trung\" của một đất nước, theo chuẩn ngữ pháp ta dùng từ vựng nào?",
        [
            "まんなか",
            "ちかく",
            "となり",
            "うしろ"
        ],
        "A",
        "💡 Chuẩn ngữ pháp:「まんなか」nghĩa là chính giữa, trung tâm (miền Trung). Ví dụ: Nghệ An là miền Trung Việt Nam:「Nghệ Anは ベトナムの まんなかです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Nghệ An ở miền Trung (chính giữa) Việt Nam.\"",
        [
            "Nghệ Anは ベトナムの ひがしです。",
            "Nghệ Anは ベトナムの まんなかです。",
            "Nghệ Anは ベトナムの きたです。",
            "Nghệ Anは ベトナムの にしです。"
        ],
        "B",
        "Miền Trung/chính giữa là まんなか. Câu đúng: Nghệ Anは ベトナムの まんなかです。"
    )

    # Cặp 4: Hỏi vị trí nơi chốn lịch sự
    add_pair("4", "1", P4_1,
        "Khi đối phương hỏi lịch sự:「おうちは どこですか。」(Nhà của bạn ở đâu?), nếu bạn muốn trả lời là \"Nhà tôi ở Hà Nội\" thì theo chuẩn ngữ pháp phải trả lời như thế nào?",
        [
            "おうちは なんですか。",
            "ハノイです。",
            "おうちは だれですか。",
            "おうちは どうですか。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi trả lời câu hỏi vị trí「どこですか。」, nếu bạn muốn trả lời là ở đâu thì trả lời trực tiếp:「[Tên địa danh] です。」➔「ハノイです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Nhà bạn ở đâu?\" - \"Ở Hà Nội.\"",
        [
            "「おうちは どこですか。」「ハノイです。」",
            "「おうちは どうですか。」「ハノイです。」",
            "「おうちは なんですか。」「ハノイです。」",
            "「おうちは だれの ですか。」「ハノイです。」"
        ],
        "A",
        "Hỏi vị trí dùng「どこですか。」và trả lời trực tiếp tên địa danh「[Địa danh] です。」."
    )

    # Cặp 5: Trợ từ chỉ phương tiện di chuyển (で)
    add_pair("4", "1", P4_1,
        "Trong tiếng Nhật, để chỉ phương tiện giao thông dùng để di chuyển (Phương tiện + ? + いきます), theo chuẩn ngữ pháp ta dùng trợ từ nào?",
        [
            "Trợ từ に",
            "Trợ từ で",
            "Trợ từ を",
            "Trợ từ へ"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trợ từ で đứng sau danh từ chỉ phương tiện/công cụ để biểu thị phương tiện di chuyển: [Phương tiện] + で + いきます (Ví dụ: タクシーで いきます).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi đi đến bệnh viện bằng taxi.\"",
        [
            "タクシーに びょういんへ いきます。",
            "タクシーで びょういんへ いきます。",
            "タクシーを びょういんへ いきます。",
            "タクシーへ びょういんへ いきます。"
        ],
        "B",
        "Phương tiện + で + Địa điểm + へ/に + いきます. Câu đúng:「タクシーで びょういんへ いきます。」"
    )

    # Cặp 6: Hỏi đi bằng phương tiện gì (なんで / なにで)
    add_pair("4", "1", P4_1,
        "Khi được hỏi:「なんで にほんへ いきますか。」(Bạn đi Nhật bằng gì?), nếu bạn muốn trả lời là \"Tôi đi bằng máy bay\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "ひこうきを いきます。",
            "ひこうきで いきます。",
            "ひこうきに いきます。",
            "ひこうきへ いきます。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Đi bằng phương tiện gì thì dùng trợ từ で: [Phương tiện] + で + いきます ➔「ひこうきで いきます。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bạn đi đến Nhật Bản bằng phương tiện gì?\" - \"Bằng máy bay.\"",
        [
            "「なんで にほんへ いきますか。」「ひこうきで いきます。」",
            "「どこで にほんへ いきますか。」「ひこうきに いきます。」",
            "「だれと にほんへ いきますか。」「ひこうきで いきます。」",
            "「いつ にほんへ いきますか。」「ひこうきを いきます。」"
        ],
        "A",
        "Hỏi phương tiện:「なんで にほんへ いきますか。」, trả lời:「ひこうきで いきます。」(bằng máy bay)."
    )

    # Cặp 7: Ngoại lệ đi bộ (あるいて いきます)
    add_pair("4", "1", P4_1,
        "Khi được hỏi:「なんで がっこうへ いきますか。」, nếu bạn muốn trả lời là \"Tôi đi bộ đến trường\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "あるきで がっこうへ いきます。",
            "あるいて がっこうへ いきます。",
            "あるいてで がっこうへ いきます。",
            "あるくで がっこうへ いきます。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi muốn trả lời là \"đi bộ\", bắt buộc dùng thể te của động từ đi bộ là「あるいて いきます」và TUYỆT ĐỐI KHÔNG dùng trợ từ で.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Mỗi ngày tôi đi bộ đến trường.\"",
        [
            "まいにち あるきで がっこうへ いきます。",
            "まいにち あるいて がっこうへ いきます。",
            "まいにち あるいてで がっこうへ いきます。",
            "まいにち じてんしゃで がっこうへ あるきます。"
        ],
        "B",
        "Đi bộ đến trường là「あるいて がっこうへ いきます」, không dùng trợ từ で."
    )

    # Cặp 8: Hỏi khoảng thời gian di chuyển (〜から 〜まで どのくらい)
    add_pair("4", "1", P4_1,
        "Khi được hỏi:「うちから がっこうまで どのくらい かかりますか。」, nếu bạn muốn trả lời là \"Mất khoảng 30 phút bằng xe buýt\" thì câu nói chuẩn ngữ pháp là:",
        [
            "バスで 30ぷんぐらい かかります。",
            "バスに 30ぷんぐらい かかります。",
            "バスで 30ぷんごろ かかります。",
            "バスを 30ぷんまで かかります。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trả lời về phương tiện (バスで) + thời lượng ước lượng (30ぷんぐらい) + かかります (hoặc です):「バスで 30ぷんぐらい かかります。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Từ nhà đến trường mất khoảng bao lâu?\"",
        [
            "うちから がっこうまで どこですか。",
            "うちから がっこうまで どのくらい かかりますか。",
            "うちから がっこうまで なんで いきますか。",
            "うちから がっこうまで いくらですか。"
        ],
        "B",
        "Mất khoảng bao lâu:「うちから がっこうまで どのくらい かかりますか。」(hoặc「どのくらいですか。」)."
    )

    # Cặp 9: Hậu tố ước lượng khoảng thời gian (〜くらい / 〜ぐらい) và giờ rưỡi
    add_pair("4", "1", P4_1,
        "Trong tiếng Nhật, để biểu thị mức độ ước lượng \"khoảng, chừng\", theo chuẩn ngữ pháp ta thêm hậu tố nào sau từ chỉ thời gian / số lượng?",
        [
            "Hậu tố 〜ごろ",
            "Hậu tố 〜から",
            "Hậu tố 〜くらい / 〜ぐらい",
            "Hậu tố 〜まで"
        ],
        "C",
        "💡 Chuẩn ngữ pháp: 〜くらい / 〜ぐらい dùng sau khoảng thời gian/lượng từ để nói \"khoảng chừng\" (Ví dụ: 1じかんはんぐらい: khoảng 1 tiếng rưỡi). Còn 〜ごろ chỉ dùng cho mốc thời gian cụ thể (3じごろ: khoảng 3 giờ).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Từ nhà đến công ty mất khoảng 1 tiếng rưỡi bằng tàu điện.\"",
        [
            "うちから かいしゃまで でんしゃで 1じかんはんぐらい です。",
            "うちから かいしゃまで でんしゃに 1じはんかんぐらい です。",
            "うちから かいしゃまで でんしゃで 1じかんごろ です。",
            "うちから かいしゃまで でんしゃを 1じかんはんまで です。"
        ],
        "A",
        "1 tiếng rưỡi là「1じかんはん (1じかんはん)」. Thêm「ぐらい」để chỉ khoảng:「でんしゃで 1じかんはんぐらい です。」"
    )

    # ==============================================================================
    # PHẦN 2: どんなところ？ (12 cặp câu hỏi)
    # ==============================================================================

    # Cặp 10: Hỏi tính chất đặc điểm: N は どうですか
    add_pair("4", "2", P4_2,
        "Khi được hỏi:「すずきさんの うちは どうですか。」(Nhà của bạn Suzuki thế nào?), nếu bạn muốn trả lời là \"Rất yên tĩnh\" thì câu nói chuẩn ngữ pháp là:",
        [
            "とても しずかなです。",
            "とても しずかです。",
            "とても しずかでした。",
            "とても しずかくないです。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ đuôi な khi làm vị ngữ đứng trước です thì bỏ な ➔「とても しずかです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Nhà của bạn Suzuki như thế nào?\" - \"Rất yên tĩnh.\"",
        [
            "「すずきさんの うちは どこですか。」「とても しずかです。」",
            "「すずきさんの うちは どうですか。」「とても しずかです。」",
            "「すずきさんの うちは なんですか。」「とても しずかです。」",
            "「すずきさんの うちは だれですか。」「とても しずかです。」"
        ],
        "B",
        "Hỏi tính chất nhà:「すずきさんの うちは どうですか。」; Trả lời:「とても しずかです。」(Rất yên tĩnh)."
    )

    # Cặp 11: Tính từ đuôi い bổ nghĩa cho danh từ
    add_pair("4", "2", P4_2,
        "Khi muốn diễn đạt \"căn phòng mới và rộng rãi\", theo chuẩn ngữ pháp khi dùng tính từ đuôi い bổ nghĩa cho danh từ へや ta làm thế nào?",
        [
            "Bỏ đuôi い rồi mới nối với danh từ",
            "Giữ nguyên đuôi い rồi đi trực tiếp với danh từ [Adj(い) + N]",
            "Phải thêm trợ từ な vào giữa tính từ và danh từ",
            "Phải thêm trợ từ の vào giữa tính từ và danh từ"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ đuôi い giữ nguyên い khi đứng trước bổ nghĩa cho danh từ: [Tính từ い] + [Danh từ] ➔「あたらしい ひろい へや」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Đây là một căn phòng mới và rộng rãi.\"",
        [
            "これは あたらしな ひろい へやです。",
            "これは あたらしい ひろい へやです。",
            "これは あたらしく ひろな へやです。",
            "これは あたらし ひろい へやです。"
        ],
        "B",
        "Cả あたらしい và ひろい đều là tính từ đuôi い, giữ nguyên い bổ nghĩa cho へや:「あたらしい ひろい へや」."
    )

    # Cặp 12: Tính từ đuôi な bổ nghĩa cho danh từ
    add_pair("4", "2", P4_2,
        "Khi muốn diễn đạt \"thành phố náo nhiệt\", theo chuẩn ngữ pháp khi dùng tính từ đuôi な (にぎやか) đứng trước bổ nghĩa cho danh từ まち ta phải làm thế nào?",
        [
            "Giữ nguyên và không cần thêm gì cả",
            "Bắt buộc phải thêm「な」vào trước danh từ [Adj(な) + な + N]",
            "Bắt buộc phải thêm trợ từ「の」vào trước danh từ",
            "Bỏ chữ な đi và nối trực tiếp"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ đuôi な khi đứng trước bổ nghĩa cho danh từ bắt buộc phải có chữ「な」➔「にぎやかな まち」(thành phố náo nhiệt).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tokyo là một thành phố náo nhiệt.\"",
        [
            "とうきょうは にぎやか まちです。",
            "とうきょうは にぎやかで まちです。",
            "とうきょうは にぎやかな まちです。",
            "とうきょうは にぎやかの まちです。"
        ],
        "C",
        "にぎやか là tính từ đuôi な, khi bổ nghĩa cho danh từ まち phải có な:「にぎやかな まちです。」"
    )

    # Cặp 13: Cấu trúc hỏi loại nơi chốn: N1 は どんな N2 ですか
    add_pair("4", "2", P4_2,
        "Khi được hỏi:「みどりこうえんは どんなところですか。」, nếu bạn muốn trả lời là \"Là một nơi rất đẹp\" thì theo chuẩn ngữ pháp tính từ đuôi な phải nói như thế nào?",
        [
            "きれい ところです。",
            "きれいな ところです。",
            "きれいの ところです。",
            "きれいに ところです。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi tính từ đuôi な đứng trước bổ nghĩa cho danh từ ところ (nơi chốn), bắt buộc phải có chữ な ➔「きれいな ところです。」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Công viên Midori là một nơi như thế nào?\" - \"Là một nơi rất đẹp.\"",
        [
            "「みどりこうえんは どこですか。」「きれいな ところです。」",
            "「みどりこうえんは どんなところですか。」「きれいな ところです。」",
            "「みどりこうえんは どうですか。」「きれい ところです。」",
            "「みどりこうえんは なんのところですか。」「きれいな ところです。」"
        ],
        "B",
        "Nơi như thế nào là「どんなところですか。」; きれい là tính từ đuôi な nên bổ nghĩa là「きれいな ところです。」"
    )

    # Cặp 14: Mẫu câu tồn tại ở địa điểm: [Địa điểm] に [Vật/Công trình] が あります
    add_pair("4", "2", P4_2,
        "Mẫu câu「[Địa điểm] に [Vật vô tri / Công trình] が あります。」dùng để diễn đạt điều gì?",
        [
            "Địa điểm đó làm việc gì",
            "Tại địa điểm đó có sự hiện diện / tồn tại của đồ vật, công trình, nơi chốn nào",
            "Ai đó đang đi về phía địa điểm",
            "Thời gian mở cửa của địa điểm"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cấu trúc tồn tại tĩnh: Địa điểm + に + Danh từ (vô tri / công trình) + が + あります (Ở địa điểm có cái gì). Ví dụ: まちに ふるい おてらが あります。",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ở trong thị trấn của tôi có một ngôi chùa cổ.\"",
        [
            "わたしの まちに ふるい おてらが あります。",
            "わたしの まちで ふるい おてらが あります。",
            "わたしの まちに ふるい おてらを あります。",
            "わたしの まちは ふるい おてらに あります。"
        ],
        "A",
        "Địa điểm tồn tại dùng trợ từ に, đối tượng tồn tại dùng が:「まちに ふるい おてらが あります。」"
    )

    # Cặp 15: Hỏi ở địa điểm có cái gì: [Địa điểm] に なにが ありますか
    add_pair("4", "2", P4_2,
        "Khi được hỏi:「うちの ちかくに なにが ありますか。」, nếu bạn muốn trả lời là \"Có siêu thị và công viên\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "スーパーと こうえんを あります。",
            "スーパーと こうえんが あります。",
            "スーパーと こうえんで あります。",
            "スーパーと こうえんに あります。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trong mẫu câu tồn tại [Địa điểm] に [Vật] が あります, danh từ tồn tại bắt buộc đi với trợ từ が ➔「スーパーと こうえんが あります。」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ở gần nhà bạn có cái gì?\" - \"Có siêu thị và công viên.\"",
        [
            "「うちの ちかくに なにが ありますか。」「スーパーと こうえんが あります。」",
            "「うちの ちかくで なにが ありますか。」「スーパーと こうえんを あります。」",
            "「うちの ちかくは なんですか。」「スーパーと こうえんに あります。」",
            "「うちの ちかくに どこが ありますか。」「スーパーと こうえんが あります。」"
        ],
        "A",
        "Địa điểm tồn tại:「うちの ちかくに なにが ありますか。」, trả lời:「スーパーと こうえんが あります。」"
    )

    # Cặp 16: Nối câu đồng thuận: そして (và, rồi thì)
    add_pair("4", "2", P4_2,
        "Khi muốn nối 2 câu cùng một hướng khen ngợi \"Khách sạn này đẹp, và lại còn yên tĩnh nữa\", theo chuẩn ngữ pháp ta dùng liên từ nào?",
        [
            "Liên từ が、",
            "Liên từ そして、",
            "Liên từ から、",
            "Liên từ でも、"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「そして、」(và, thêm nữa) dùng để liên kết 2 câu có tính chất bổ sung, cùng chiều khen ngợi hoặc cùng chiều chê:「きれいです。そして、しずかです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Khách sạn này đẹp, và lại còn yên tĩnh nữa.\"",
        [
            "このホテルは きれいです。が、しずかです。",
            "このホテルは きれいです。そして、しずかです。",
            "このホテルは きれいです。から、しずかです。",
            "このホテルは きれいです。でも、しずかです。"
        ],
        "B",
        "Hai vế cùng là điểm tốt (khen):「きれいです。そして、しずかです。」"
    )

    # Cặp 17: Trợ từ nối tương phản: 〜が、 (nhưng...)
    add_pair("4", "2", P4_2,
        "Khi muốn diễn đạt ý tương phản giữa 2 vế câu \"Món ăn này rất ngon nhưng hơi đắt\", theo chuẩn ngữ pháp ta dùng trợ từ nối nào?",
        [
            "Trợ từ 〜そして",
            "Trợ từ 〜ですが、(hoặc 〜が、)",
            "Trợ từ 〜から",
            "Trợ từ 〜と"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「〜が、」được đặt ở giữa câu mang nghĩa \"nhưng\", nối hai vế tương phản nhau (một vế khen, một vế chê):「とても おいしいですが、すこし たかいです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Đồ ăn của nhà hàng này rất ngon nhưng hơi đắt.\"",
        [
            "このみせの りょうりは とても おいしいです。そして、すこし たかいです。",
            "このみせの りょうりは とても おいしいですが、すこし たかいです。",
            "このみせの りょうりは とても おいしいですから、すこし たかいです。",
            "このみせの りょうりは とても おいしいと、すこし たかいです。"
        ],
        "B",
        "Một vế khen (rất ngon), một vế chê (hơi đắt) ➔ dùng trợ từ nối「が」(nhưng):「とても おいしいですが、すこし たかいです。」"
    )

    # Cặp 18: Phủ định tính từ đuôi い: 〜くないです
    add_pair("4", "2", P4_2,
        "Khi muốn diễn đạt phủ định \"Căn phòng này không rộng\", theo chuẩn ngữ pháp tính từ đuôi い (ひろい) được chia như thế nào?",
        [
            "Bỏ đuôi い và thêm じゃありません",
            "Bỏ đuôi い và thêm くないです",
            "Giữ nguyên đuôi い và thêm ではありません",
            "Đổi đuôi い thành くありませんでした"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Phủ định tính từ đuôi い hiện tại: Bỏ đuôi「い」➔ thêm「くないです」➔ ひろい thành「ひろくないです」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Căn phòng này không rộng.\"",
        [
            "このへやは ひろいじゃありません。",
            "このへやは ひろくないです。",
            "このへやは ひろいではありません。",
            "このへやは ひろくありませんでした。"
        ],
        "B",
        "Tính từ ひろい bỏ đuôi い thêm くないです:「このへやは ひろくないです。」"
    )

    # Cặp 19: Ngoại lệ phủ định của いい (tốt)
    add_pair("4", "2", P4_2,
        "Khi được hỏi:「きょうの てんきは どうですか。」, nếu bạn muốn trả lời là \"Thời tiết hôm nay không tốt lắm\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "きょうの てんきは あまり いくないです。",
            "きょうの てんきは あまり よくないです。",
            "きょうの てんきは あまり いいじゃありません。",
            "きょうの てんきは あまり よいじゃありません。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ「いい」có nguồn gốc là「よい」➔ Khi muốn trả lời phủ định \"không tốt\", chuẩn ngữ pháp BẮT BUỘC là「よくないです」(TUYỆT ĐỐI không nói いくないです).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Thời tiết hôm nay không tốt lắm.\"",
        [
            "きょうの てんきは あまり いくないです。",
            "きょうの てんきは あまり よくないです。",
            "きょうの てんきは あまり いいじゃありません。",
            "きょうの てんきは あまり よいじゃありません。"
        ],
        "B",
        "Không tốt là「よくないです」. Kết hợp phó từ あまり:「きょうの てんきは あまり よくないです。」"
    )

    # Cặp 20: Phủ định tính từ đuôi な: 〜じゃありません
    add_pair("4", "2", P4_2,
        "Khi được hỏi:「このまちは にぎやかですか。」, nếu bạn muốn trả lời là \"Không, thị trấn này không náo nhiệt\" thì theo chuẩn ngữ pháp (lịch sự, trang trọng) phải nói như thế nào?",
        [
            "いいえ、にぎやかじゃありません。",
            "いいえ、にぎやかくなないです。",
            "いいえ、にぎやかないです。",
            "いいえ、にぎやかでした。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Tính từ đuôi な khi chia phủ định: Bỏ「な」➔ thêm「じゃありません」(cách nói lịch sự, trang trọng hơn một chút so với「じゃないです」) ➔「いいえ、にぎやかじゃありません。」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Thị trấn này không náo nhiệt.\"",
        [
            "このまちは にぎやかじゃありません。",
            "このまちは にぎやかくなないです。",
            "このまちは にぎやかないです。",
            "このまちは にぎやかでした。"
        ],
        "A",
        "にぎやか là tính từ đuôi な, thể phủ định chuẩn lịch sự, trang trọng là:「このまちは にぎやかじゃありません。」"
    )

    # Cặp 21: Phủ định tính từ đuôi な trang trọng nhất / văn viết: 〜ではありません
    add_pair("4", "2", P4_2,
        "Dạng phủ định trang trọng hơn / văn viết (thay thế cho「〜じゃありません」) với tính từ đuôi な và Danh từ là gì?",
        [
            "〜くないです",
            "〜ではありません",
            "〜でした",
            "〜ませんでした"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trong văn viết hoặc hoàn cảnh trang trọng nhất,「〜じゃありません」được thay thế bằng dạng「〜ではありません」(Ví dụ: べんりではありません).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật theo phong cách trang trọng nhất / văn viết: \"Nơi này hoàn toàn không tiện lợi chút nào.\"",
        [
            "ここは ぜんぜん べんりないです。",
            "ここは ぜんぜん べんりではありません。",
            "ここは ぜんぜん べんりくないです。",
            "ここは ぜんぜん べんりでした。"
        ],
        "B",
        "Dạng lịch sự:「べんりではありません」. Kết hợp ぜんぜん:「ここは ぜんぜん べんりではありません。」"
    )

    # ==============================================================================
    # PHẦN 3: きせつ・りょうり (8 cặp câu hỏi)
    # ==============================================================================

    # Cặp 22: Trợ từ cảm thán đồng tình cuối câu ね
    add_pair("4", "3", P4_3,
        "Khi thấy trời nóng và bạn muốn chia sẻ cảm thán với người bên cạnh để tìm kiếm sự đồng cảm (\"Hôm nay trời nóng thật đấy nhỉ!\"), theo chuẩn ngữ pháp ta dùng trợ từ cuối câu nào?",
        [
            "Trợ từ よ",
            "Trợ từ ね",
            "Trợ từ か",
            "Trợ từ も"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trợ từ「ね」đặt cuối câu dùng để tìm kiếm sự đồng tình, chia sẻ cảm xúc với đối phương (tương đương với \"... nhỉ, ... nhé\"):「きょうは あついですね。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hôm nay trời nóng thật đấy nhỉ!\"",
        [
            "きょうは あついですよ。",
            "きょうは あついですね。",
            "きょうは あついですか。",
            "きょうは あついです。"
        ],
        "B",
        "Chia sẻ cảm thán về thời tiết dùng trợ từ ね:「きょうは あついですね。」"
    )

    # Cặp 23: Phó từ mức độ cao: とても (rất)
    add_pair("4", "3", P4_3,
        "Khi muốn diễn đạt mức độ cao khẳng định \"Món lẩu này rất ngon\", theo chuẩn ngữ pháp ta dùng phó từ nào đứng trước tính từ?",
        [
            "Phó từ あまり",
            "Phó từ とても",
            "Phó từ ぜんぜん",
            "Phó từ すこし"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「とても」đứng trước tính từ để biểu thị mức độ cao \"rất...\", luôn đi với dạng khẳng định ➔「とても おいしいです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Món lẩu này rất ngon.\"",
        [
            "このなべは あまり おいしいです。",
            "このなべは とても おいしいです。",
            "このなべは ぜんぜん おいしいです。",
            "このなべは すこし おいしくないです。"
        ],
        "B",
        "\"Rất ngon\" là「とても おいしいです。」"
    )

    # Cặp 24: Phó từ mức độ nhẹ: すこし (hơi, một chút)
    add_pair("4", "3", P4_3,
        "Khi muốn diễn đạt mức độ nhẹ khẳng định \"Thời tiết hôm nay hơi lạnh một chút\", theo chuẩn ngữ pháp ta dùng phó từ nào?",
        [
            "Phó từ とても",
            "Phó từ すこし",
            "Phó từ あまり",
            "Phó từ ぜんぜん"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「すこし」(một chút, hơi...) đi với dạng khẳng định để diễn đạt mức độ nhẹ ➔「すこし さむいです。」(hơi lạnh một chút).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Thời tiết hôm nay hơi lạnh một chút.\"",
        [
            "きょうは とても さむいです。",
            "きょうは すこし さむいです。",
            "きょうは あまり さむいです。",
            "きょうは ぜんぜん さむいです。"
        ],
        "B",
        "\"Hơi lạnh một chút\" dùng phó từ すこし:「きょうは すこし さむいです。」"
    )

    # Cặp 25: Phó từ phủ định nhẹ: あまり + Phủ định
    add_pair("4", "3", P4_3,
        "Khi được hỏi:「ふゆは さむいですか。」(Mùa đông có lạnh không?), nếu bạn muốn trả lời là \"Không lạnh lắm\" thì theo chuẩn ngữ pháp bắt buộc phải nói như thế nào?",
        [
            "あまり さむいです。",
            "あまり さむくないです。",
            "とても さむくないです。",
            "ぜんぜん さむいです。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Phó từ「あまり」(không... lắm) BẮT BUỘC phải đi cùng với vị ngữ ở thể PHỦ ĐỊNH ➔「あまり さむくないです。」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Mùa đông ở quê tôi không lạnh lắm.\"",
        [
            "わたしの くには ふゆが あまり さむいです。",
            "わたしの くには ふゆが あまり さむくないです。",
            "わたしの くには ふゆが ぜんぜん さむいです。",
            "わたしの くには ふゆが とても さむくないです。"
        ],
        "B",
        "Phó từ あまり đi kèm vị ngữ phủ định:「あまり さむくないです。」(không lạnh lắm)."
    )

    # Cặp 26: Phó từ phủ định tuyệt đối: ぜんぜん + Phủ định
    add_pair("4", "3", P4_3,
        "Khi được hỏi:「にほんごは かんたんですか。」(Tiếng Nhật có đơn giản không?), nếu bạn muốn trả lời là \"Hoàn toàn không đơn giản chút nào\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "ぜんぜん かんたんです。",
            "ぜんぜん かんたんじゃありません。",
            "あまり かんたんです。",
            "とても かんたんじゃありません。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Phó từ「ぜんぜん」(hoàn toàn không...) BẮT BUỘC kết hợp với thể PHỦ ĐỊNH ➔「ぜんぜん かんたんじゃありません。」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tiếng Nhật hoàn toàn không dễ chút nào.\"",
        [
            "にほんごは ぜんぜん やさしいです。",
            "にほんごは ぜんぜん かんたんじゃありません。",
            "にほんごは とても かんたんじゃありません。",
            "にほんごは あまり かんたんです。"
        ],
        "B",
        "ぜんぜん + Phủ định:「ぜんぜん かんたんじゃありません。」(hoàn toàn không đơn giản)."
    )

    # Cặp 27: Cấu trúc miêu tả thời tiết theo mùa: Địa điểm は Mùa, Adj です
    add_pair("4", "3", P4_3,
        "Mẫu câu「N(quốc gia/thành phố) は [thời gian/mùa]、Adj です。」dùng để diễn đạt điều gì?",
        [
            "Nói về dân số theo mùa của địa điểm",
            "Miêu tả đặc điểm thời tiết của một nơi vào một khoảng thời gian/mùa cụ thể",
            "Hỏi chi phí đi du lịch vào mùa đó",
            "Rủ bạn bè đi chơi vào mùa hè"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cấu trúc: [Địa danh] は [Mùa]、[Tính từ] です (Ví dụ: にほんは なつ、とても あついです: Nhật Bản vào mùa hè thì rất nóng).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Nhật Bản vào mùa hè thì rất nóng.\"",
        [
            "にほんは なつ、とても あついです。",
            "にほんは なつ、とても さむいです。",
            "にほんは あき、とても あついです。",
            "にほんは ふゆ、とても すずしいです。"
        ],
        "A",
        "Mùa hè là なつ (なつ), nóng là あつい:「にほんは なつ、とても あついです。」"
    )

    # Cặp 28: Cấu trúc sở hữu mùa: [Địa điểm] の [Mùa] は Adj です
    add_pair("4", "3", P4_3,
        "Ngoài mẫu「N は [mùa]、Adj です」, cấu trúc nào sau đây cũng dùng để nói về thời tiết của một nơi theo mùa?",
        [
            "[Địa điểm] で [Mùa] を Adj です。",
            "[Địa điểm] の [Mùa] は Adj です。",
            "[Địa điểm] に [Mùa] が Adj です。",
            "[Địa điểm] から [Mùa] まで Adj です。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Dùng trợ từ の để xác định danh từ thời tiết/mùa thuộc địa điểm:「[Địa điểm] の [Mùa] は [Tính từ] です。」(Ví dụ: ハノイの あきは すずしいです).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Mùa thu của Hà Nội rất mát mẻ và dễ chịu.\"",
        [
            "ハノイの なつは とても すずしいです。",
            "ハノイの あきは とても すずしいです。",
            "ハノイの はるは とても さむいです。",
            "ハノイの ふゆは とても あついです。"
        ],
        "B",
        "Mùa thu là あき (あき), mát mẻ là すずしい (すずしい):「ハノイの あきは とても すずしいです。」"
    )

    # Cặp 29: Hỏi thời tiết theo mùa: [Mùa] は どうですか
    add_pair("4", "3", P4_3,
        "Khi người khác hỏi:「おくにの はるは どうですか。」, nếu bạn muốn trả lời là \"Mùa xuân ấm áp và rất đẹp\" thì câu nói chuẩn ngữ pháp là:",
        [
            "あたたかくて、とても きれいです。",
            "あたたかいで、とても きれいです。",
            "あたたかくて、とても きれいなです。",
            "あたたかいと、とても きれいです。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Nối 2 tính từ tương đồng: Tính từ đuôi い đổi đuôi「い」➔「くて」(あたたかくて) rồi nối tiếp với「とても きれいです。」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Mùa xuân ở đất nước bạn như thế nào?\" - \"Ấm áp và rất đẹp.\"",
        [
            "「おくにの はるは どうですか。」「あたたかくて、とても きれいです。」",
            "「おくにの なつは どうですか。」「あたたかくて、とても きれいです。」",
            "「おくにの ふゆは どうですか。」「さむくて、とても きれいです。」",
            "「おくにの あきは どうですか。」「すずしくて、とても きれいです。」"
        ],
        "A",
        "Mùa xuân là はる, ấm áp là あたたかい:「おくにの はるは どうですか。」「あたたかくて、とても きれいです。」"
    )
