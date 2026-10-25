# -*- coding: utf-8 -*-
"""
Dữ liệu câu hỏi ngữ pháp Bài 4 - Dekiru Nihongo
Chia làm 2 dạng câu hỏi rõ ràng:
1. [HỎI NGỮ PHÁP]: Hỏi khái niệm, cấu trúc, quy tắc, ý nghĩa ngữ pháp
2. [DỊCH CÂU]: Dịch từ câu tiếng Việt sang tiếng Nhật tương ứng
"""

def register_lesson_4(add_pair):
    P4_1 = "どこ？ (Vị trí, Phương tiện, Thời gian)"
    P4_2 = "どんなところ？ (Tính từ, Tồn tại, Nối câu, Phủ định)"
    P4_3 = "季節・料理 (Phó từ, Trợ từ ね, Thời tiết)"

    # ==============================================================================
    # PHẦN 1: どこ？ (9 cặp câu hỏi)
    # ==============================================================================

    # Cặp 1: Vị trí thành phố / phương hướng
    add_pair("4", "1", P4_1,
        # Hỏi ngữ pháp là gì
        "Mẫu câu「Thành phố は đất nước の [hướng] です。」dùng để làm gì?",
        [
            "Nói về dân số của một thành phố",
            "Xác định vị trí phương hướng của thành phố thuộc một quốc gia",
            "Hỏi giá vé đi đến thành phố",
            "Miêu tả thời tiết của đất nước"
        ],
        "B",
        "Cấu trúc「Thành phố は đất nước の [hướng] です。」dùng để diễn đạt vị trí địa lý của thành phố nằm ở phía nào (đông, tây, nam, bắc, trung tâm) của đất nước đó.",
        # Dịch câu tiếng Việt qua
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Lạng Sơn ở phía bắc Việt Nam.\"",
        [
            "Lang Sonは ベトナムの きたです。",
            "Lang Sonは ベトナムの みなみです。",
            "Lang Sonは ベトナムの ひがしです。",
            "Lang Sonは ベトナムの にしです。"
        ],
        "A",
        "Phía bắc trong tiếng Nhật là きた (北). Câu dịch chuẩn là: Lang Sonは ベトナムの きたです。"
    )

    # Cặp 2: Phương hướng: Phía nam
    add_pair("4", "1", P4_1,
        "Trong tiếng Nhật, để nói về phương hướng \"Phía nam\", từ vựng nào sau đây là đúng?",
        [
            "きた (北)",
            "にし (西)",
            "みなみ (南)",
            "ひがし (東)"
        ],
        "C",
        "4 phương hướng cơ bản trong tiếng Nhật: きた (Bắc), みなみ (Nam), ひがし (Đông), にし (Tây).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cà Mau ở phía nam Việt Nam.\"",
        [
            "Cà Mauは ベトナムの きたです。",
            "Cà Mauは ベトナムの にしです。",
            "Cà Mauは ベトナムの みなみです。",
            "Cà Mauは ベトナムの まんなかです。"
        ],
        "C",
        "Phía nam là みなみ (南). Do đó câu đúng là: Cà Mauは ベトナムの みなみです。"
    )

    # Cặp 3: Vị trí chính giữa / miền Trung
    add_pair("4", "1", P4_1,
        "Để nói một địa điểm nằm ở \"chính giữa / miền trung\" của một đất nước, ta dùng từ vựng nào?",
        [
            "まんなか (真ん中)",
            "ちかく (近く)",
            "となり (隣)",
            "うしろ (後ろ)"
        ],
        "A",
        "「まんなか (真ん中)」nghĩa là chính giữa, trung tâm (miền Trung).",
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
        "Để hỏi \"Nhà của bạn ở đâu?\" một cách lịch sự trong tiếng Nhật, câu hỏi nào sau đây là đúng?",
        [
            "お家は なんですか。",
            "お家は だれですか。",
            "お家は どこですか。",
            "お家は どうですか。"
        ],
        "C",
        "「どこ」là từ để hỏi nơi chốn, vị trí. Thêm tiền tố「お」trước「家」để thể hiện sự lịch sự tôn trọng đối phương:「お家は どこですか。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Nhà bạn ở đâu?\" - \"Ở Hà Nội.\"",
        [
            "「お家は どこですか。」「ハノイです。」",
            "「お家は どうですか。」「ハノイです。」",
            "「お家は なんですか。」「ハノイです。」",
            "「お家は だれの ですか。」「ハノイです。」"
        ],
        "A",
        "Hỏi vị trí dùng「どこですか。」và trả lời trực tiếp tên địa danh「[Địa danh] です。」."
    )

    # Cặp 5: Trợ từ chỉ phương tiện di chuyển (で)
    add_pair("4", "1", P4_1,
        "Trong tiếng Nhật, để chỉ phương tiện giao thông dùng để di chuyển (Phương tiện + ? + 行きます), ta dùng trợ từ nào?",
        [
            "Trợ từ に",
            "Trợ từ で",
            "Trợ từ を",
            "Trợ từ へ"
        ],
        "B",
        "Trợ từ で đứng sau danh từ chỉ phương tiện/công cụ để biểu thị phương tiện di chuyển (Ví dụ: タクシーで 行きます).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi đi đến bệnh viện bằng taxi.\"",
        [
            "タクシーに びょういんへ 行きます。",
            "タクシーで びょういんへ 行きます。",
            "タクシーを びょういんへ 行きます。",
            "タクシーへ びょういんへ 行きます。"
        ],
        "B",
        "Phương tiện + で + Địa điểm + へ/に + 行きます. Câu đúng:「タクシーで びょういんへ 行きます。」"
    )

    # Cặp 6: Hỏi đi bằng phương tiện gì (なんで / なにで)
    add_pair("4", "1", P4_1,
        "Để hỏi \"Bạn đi đến [địa điểm] bằng phương tiện gì?\", cấu trúc câu hỏi nào sau đây là đúng?",
        [
            "どこで [địa điểm] へ 行きますか。",
            "なんで / なにで [địa điểm] へ 行きますか。",
            "だれで [địa điểm] へ 行きますか。",
            "いつで [địa điểm] へ 行きますか。"
        ],
        "B",
        "Dùng「なんで」hoặc「なにで」kết hợp với「〜へ 行きますか」để hỏi về phương tiện di chuyển.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bạn đi đến Nhật Bản bằng phương tiện gì?\" - \"Bằng máy bay.\"",
        [
            "「なんで 日本へ 行きますか。」「ひこうきで 行きます。」",
            "「どこで 日本へ 行きますか。」「ひこうきに 行きます。」",
            "「だれと 日本へ 行きますか。」「ひこうきで 行きます。」",
            "「いつ 日本へ 行きますか。」「ひこうきを 行きます。」"
        ],
        "A",
        "Hỏi phương tiện:「なんで 日本へ 行きますか。」, trả lời:「ひこうきで 行きます。」(bằng máy bay)."
    )

    # Cặp 7: Ngoại lệ đi bộ (あるいて 行きます)
    add_pair("4", "1", P4_1,
        "LƯU Ý NGỮ PHÁP ĐẶC BIỆT: Khi diễn đạt \"đi bộ đến trường / ga\", quy tắc dùng trợ từ nào sau đây là ĐÚNG?",
        [
            "あるきで えきへ 行きます。",
            "あるいて えきへ 行きます (Không dùng trợ từ で)",
            "あるいてで えきへ 行きます。",
            "あるくで えきへ 行きます。"
        ],
        "B",
        "Khi đi bộ, ta dùng thể te của động từ đi bộ là「あるいて 行きます」và TUYỆT ĐỐI KHÔNG dùng trợ từ で.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Mỗi ngày tôi đi bộ đến trường.\"",
        [
            "まいにち あるきで がっこうへ 行きます。",
            "まいにち あるいて がっこうへ 行きます。",
            "まいにち あるいてで がっこうへ 行きます。",
            "まいにち じてんしゃで がっこうへ あるきます。"
        ],
        "B",
        "Đi bộ đến trường là「あるいて がっこうへ 行きます」, không dùng trợ từ で."
    )

    # Cặp 8: Hỏi khoảng thời gian di chuyển (〜から 〜まで どのくらい)
    add_pair("4", "1", P4_1,
        "Mẫu câu「[Địa điểm 1] から [Địa điểm 2] まで どのくらい かかりますか。」có ý nghĩa ngữ pháp là gì?",
        [
            "Từ địa điểm 1 đến địa điểm 2 có những phương tiện nào?",
            "Từ địa điểm 1 đến địa điểm 2 mất khoảng bao lâu thời gian?",
            "Địa điểm 1 và địa điểm 2 nơi nào đẹp hơn?",
            "Tại sao bạn lại đi từ địa điểm 1 đến địa điểm 2?"
        ],
        "B",
        "「どのくらい かかりますか / どのくらいですか」dùng để hỏi về khoảng thời gian cần thiết để di chuyển từ điểm xuất phát (から) đến đích đến (まで).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Từ nhà đến trường mất khoảng bao lâu?\"",
        [
            "うちから がっこうまで どこですか。",
            "うちから がっこうまで どのくらい かかりますか。",
            "うちから がっこうまで なんで 行きますか。",
            "うちから がっこうまで いくらですか。"
        ],
        "B",
        "Mất khoảng bao lâu:「うちから がっこうまで どのくらい かかりますか。」(hoặc「どのくらいですか。」)."
    )

    # Cặp 9: Hậu tố ước lượng khoảng thời gian (〜くらい / 〜ぐらい) và giờ rưỡi
    add_pair("4", "1", P4_1,
        "Trong tiếng Nhật, để biểu thị mức độ ước lượng \"khoảng, chừng\", ta thêm hậu tố nào sau từ chỉ thời gian / số lượng?",
        [
            "Hậu tố 〜ごろ",
            "Hậu tố 〜から",
            "Hậu tố 〜くらい / 〜ぐらい",
            "Hậu tố 〜まで"
        ],
        "C",
        "〜くらい / 〜ぐらい dùng sau khoảng thời gian/lượng từ để nói \"khoảng chừng\" (Ví dụ: 30ぷんぐらい: khoảng 30 phút). Còn 〜ごろ dùng cho mốc thời gian cụ thể (3じごろ: khoảng 3 giờ).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Từ nhà đến công ty mất khoảng 1 tiếng rưỡi bằng tàu điện.\"",
        [
            "うちから 会社まで でんしゃで 1じかんはんぐらい です。",
            "うちから 会社まで でんしゃに 1じはんかんぐらい です。",
            "うちから 会社まで でんしゃで 1じかんごろ です。",
            "うちから 会社まで でんしゃを 1じかんはんまで です。"
        ],
        "A",
        "1 tiếng rưỡi là「1じかんはん (1時間半)」. Thêm「ぐらい」để chỉ khoảng:「でんしゃで 1じかんはんぐらい です。」"
    )

    # ==============================================================================
    # PHẦN 2: どんなところ？ (12 cặp câu hỏi)
    # ==============================================================================

    # Cặp 10: Hỏi tính chất đặc điểm: N は どうですか
    add_pair("4", "2", P4_2,
        "Trong Bài 4.2, câu hỏi「N は どうですか。」khi hỏi về nơi chốn, nhà cửa dùng để làm gì?",
        [
            "Hỏi N nằm ở phương hướng nào",
            "Hỏi giá tiền của N là bao nhiêu",
            "Hỏi về tính chất, đặc điểm cảm nhận về N (N trông như thế nào?)",
            "Rủ rê đối phương cùng đến N"
        ],
        "C",
        "Trong ngữ cảnh miêu tả nơi chốn,「N は どうですか。」dùng để hỏi tính chất, đặc điểm của N (Ví dụ: Nhà bạn thế nào? - Đẹp và rộng).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Nhà của bạn Suzuki như thế nào?\" - \"Rất yên tĩnh.\"",
        [
            "「すずきさんの家は どこですか。」「とても しずかです。」",
            "「すずきさんの家は どうですか。」「とても しずかです。」",
            "「すずきさんの家は なんですか。」「とても しずかです。」",
            "「すずきさんの家は だれですか。」「とても しずかです。」"
        ],
        "B",
        "Hỏi tính chất nhà:「すずきさんの家は どうですか。」; Trả lời:「とても しずかです。」(Rất yên tĩnh)."
    )

    # Cặp 11: Tính từ đuôi い bổ nghĩa cho danh từ
    add_pair("4", "2", P4_2,
        "Quy tắc ngữ pháp khi dùng TÍNH TỪ ĐUÔI い đứng trước để bổ nghĩa cho danh từ là gì?",
        [
            "Bỏ đuôi い rồi mới nối với danh từ",
            "Giữ nguyên đuôi い rồi đi trực tiếp với danh từ [Adj(い) + N]",
            "Phải thêm trợ từ な vào giữa tính từ và danh từ",
            "Phải thêm trợ từ の vào giữa tính từ và danh từ"
        ],
        "B",
        "Tính từ đuôi い giữ nguyên い khi đứng trước bổ nghĩa cho danh từ (Ví dụ: あたらしい へや: căn phòng mới, ひろい いえ: ngôi nhà rộng).",
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
        "Quy tắc ngữ pháp khi dùng TÍNH TỪ ĐUÔI な đứng trước để bổ nghĩa cho danh từ là gì?",
        [
            "Giữ nguyên và không cần thêm gì cả",
            "Bắt buộc phải giữ lại hoặc thêm「な」vào trước danh từ [Adj(な) + な + N]",
            "Bắt buộc phải thêm trợ từ「の」vào trước danh từ",
            "Bỏ chữ な đi và nối trực tiếp"
        ],
        "B",
        "Tính từ đuôi な khi đứng trước bổ nghĩa cho danh từ bắt buộc phải có chữ「な」: [Tính từ な] + な + Danh từ (Ví dụ: しずかな まち, にぎやかな まち).",
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
        "Cấu trúc câu hỏi「N1 は どんな N2 ですか。」có ý nghĩa ngữ pháp là gì?",
        [
            "N1 nằm ở vị trí nào của N2?",
            "N1 có giá bao nhiêu trong số các N2?",
            "N1 là một N2 như thế nào? (Hỏi bản chất, chủng loại, đặc tính của danh từ)",
            "N1 có bao nhiêu cái N2?"
        ],
        "C",
        "「どんな」là từ nghi vấn có nghĩa \"như thế nào\", luôn đi kèm trước danh từ để hỏi về tính chất, đặc điểm của danh từ đó (Ví dụ: どんな まちですか: thành phố như thế nào?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Công viên Midori là một nơi như thế nào?\" - \"Là một nơi rất đẹp.\"",
        [
            "「みどり公園は どこですか。」「きれいな ところです。」",
            "「みどり公園は どんなところですか。」「きれいな ところです。」",
            "「みどり公園は どうですか。」「きれい ところです。」",
            "「みどり公園は なんのところですか。」「きれいな ところです。」"
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
        "Cấu trúc tồn tại: Địa điểm + に + Danh từ (vô tri / công trình) + が + あります (Ở địa điểm có cái gì).",
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

    # Cặp 15: Hỏi ở địa điểm có cái gì: [Địa điểm] に 何が ありますか
    add_pair("4", "2", P4_2,
        "Để hỏi \"Ở [địa điểm] có cái gì / có những gì?\", cấu trúc câu hỏi tiếng Nhật nào sau đây là đúng?",
        [
            "[Địa điểm] で なにを しますか。",
            "[Địa điểm] に なにが ありますか。",
            "[Địa điểm] は なんですか。",
            "[Địa điểm] から なにが きますか。"
        ],
        "B",
        "Hỏi về đồ vật, công trình tồn tại ở nơi chốn:「[Địa điểm] に なにが ありますか。」(Ở... có cái gì?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ở gần nhà bạn có cái gì?\" - \"Có siêu thị và công viên.\"",
        [
            "「家の ちかくに 何が ありますか。」「スーパーと 公園が あります。」",
            "「家の ちかくで 何が ありますか。」「スーパーと 公園を あります。」",
            "「家の ちかくは 何ですか。」「スーパーと 公園に あります。」",
            "「家の ちかくに どこが ありますか。」「スーパーと 公園が あります。」"
        ],
        "A",
        "Địa điểm tồn tại:「家の ちかくに 何が ありますか。」, trả lời:「スーパーと 公園が あります。」"
    )

    # Cặp 16: Nối câu đồng thuận: そして (và, rồi thì)
    add_pair("4", "2", P4_2,
        "Liên từ「そして、」(và, thêm nữa) dùng để nối hai câu/mệnh đề có tính chất như thế nào?",
        [
            "Hai mệnh đề có ý nghĩa tương phản, trái ngược nhau (khen và chê)",
            "Hai mệnh đề có cùng hướng đánh giá (cùng khen hoặc cùng chê, bổ sung thông tin)",
            "Mệnh đề sau giải thích nguyên nhân cho mệnh đề trước",
            "Mệnh đề sau phủ định hoàn toàn mệnh đề trước"
        ],
        "B",
        "「そして、」dùng để liên kết 2 câu có tính chất bổ sung, cùng chiều (Ví dụ: Đẹp và yên tĩnh, Bẩn và chật hẹp).",
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
        "Trợ từ liên kết「〜が、」(nhưng...) dùng để nối hai mệnh đề có mối quan hệ như thế nào?",
        [
            "Hai mệnh đề có ý nghĩa đối lập, tương phản nhau (một vế khen, một vế chê)",
            "Hai mệnh đề hoàn toàn giống nhau",
            "Mệnh đề trước là lý do, mệnh đề sau là kết quả",
            "Chỉ dùng khi cả hai mệnh đề đều mang nghĩa phủ định"
        ],
        "A",
        "「〜が、」được đặt ở giữa câu mang nghĩa \"nhưng\", nối hai vế tương phản nhau (Ví dụ: Ngon nhưng đắt, Nhỏ nhưng sạch sẽ).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Đồ ăn của nhà hàng này rất ngon nhưng hơi đắt.\"",
        [
            "この店の 料理は とても おいしいです。そして、すこし 高いです。",
            "この店の 料理は とても おいしいですが、すこし 高いです。",
            "この店の 料理は とても おいしいですから、すこし 高いです。",
            "この店の 料理は とても おいしいと、すこし 高いです。"
        ],
        "B",
        "Một vế khen (rất ngon), một vế chê (hơi đắt) ➔ dùng trợ từ nối「が」(nhưng):「とても おいしいですが、すこし 高いです。」"
    )

    # Cặp 18: Phủ định tính từ đuôi い: 〜くないです
    add_pair("4", "2", P4_2,
        "Quy tắc ngữ pháp khi chuyển TÍNH TỪ ĐUÔI い sang THỂ PHỦ ĐỊNH (không...) là gì?",
        [
            "Bỏ đuôi い và thêm じゃないです",
            "Bỏ đuôi い và thêm くないです",
            "Giữ nguyên đuôi い và thêm ではないです",
            "Đổi đuôi い thành くありませんでした"
        ],
        "B",
        "Quy tắc phủ định tính từ đuôi い hiện tại: Bỏ đuôi「い」➔ thêm「くないです」(Ví dụ: ひろい ➔ ひろくないです, たかい ➔ たかくないです).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Căn phòng này không rộng.\"",
        [
            "このへやは ひろいじゃないです。",
            "このへやは ひろくないです。",
            "このへやは ひろいではないです。",
            "このへやは ひろくありませんでした。"
        ],
        "B",
        "Tính từ ひろい bỏ đuôi い thêm くないです:「このへやは ひろくないです。」"
    )

    # Cặp 19: Ngoại lệ phủ định của いい (tốt)
    add_pair("4", "2", P4_2,
        "NGOẠI LỆ QUAN TRỌNG: Thể phủ định của tính từ đặc biệt「いい」(tốt, đẹp) là gì?",
        [
            "いくないです",
            "よくないです",
            "いいじゃないです",
            "よかないです"
        ],
        "B",
        "Tính từ「いい」có nguồn gốc là「よい」. Mọi dạng biến đổi (phủ định, quá khứ) đều dựa trên「よい」➔ Phủ định là「よくないです」(TUYỆT ĐỐI không nói いくないです).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Thời tiết hôm nay không tốt lắm.\"",
        [
            "きょうの てんきは あまり いくないです。",
            "きょうの てんきは あまり よくないです。",
            "きょうの てんきは あまり いいじゃないです。",
            "きょうの てんきは あまり よいじゃないです。"
        ],
        "B",
        "Không tốt là「よくないです」. Kết hợp phó từ あまり:「きょうの てんきは あまり よくないです。」"
    )

    # Cặp 20: Phủ định tính từ đuôi な: 〜じゃないです
    add_pair("4", "2", P4_2,
        "Quy tắc ngữ pháp khi chuyển TÍNH TỪ ĐUÔI な sang THỂ PHỦ ĐỊNH thông thường (không...) là gì?",
        [
            "Bỏ đuôi な và thêm くないです",
            "Bỏ đuôi な và thêm じゃないです (hoặc ではありません)",
            "Giữ nguyên đuôi な và thêm ないです",
            "Thêm 不 (bất) vào đầu tính từ"
        ],
        "B",
        "Tính từ đuôi な phủ định: Bỏ「な」➔ thêm「じゃないです」(hoặc trang trọng là「ではありません」) (Ví dụ: しずか ➔ しずかじゃないです, にぎやか ➔ にぎやかじゃないです).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Thị trấn này không náo nhiệt.\"",
        [
            "このまちは にぎやかじゃないです。",
            "このまちは にぎやかくなないです。",
            "このまちは にぎやかないです。",
            "このまちは にぎやかでした。"
        ],
        "A",
        "にぎやか là tính từ đuôi な, phủ định là:「にぎやかじゃないです。」"
    )

    # Cặp 21: Phủ định tính từ đuôi な lịch sự: 〜ではありません
    add_pair("4", "2", P4_2,
        "Dạng phủ định trang trọng / lịch sự hơn của「〜じゃないです」với tính từ đuôi な và Danh từ là gì?",
        [
            "〜くないです",
            "〜ではありません",
            "〜でした",
            "〜ませんでした"
        ],
        "B",
        "Trong văn viết hoặc giao tiếp trang trọng,「〜じゃないです」được thay thế bằng「〜ではありません」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Nơi này hoàn toàn không tiện lợi chút nào (cách nói lịch sự).\"",
        [
            "ここは ぜんぜん べんりじゃないです。",
            "ここは ぜんぜん べんりではありません。",
            "ここは ぜんぜん べんりくないです。",
            "ここは ぜんぜん べんりでした。"
        ],
        "B",
        "Dạng lịch sự:「べんりではありません」. Kết hợp ぜんぜん:「ここは ぜんぜん べんりではありません。」"
    )

    # ==============================================================================
    # PHẦN 3: 季節・料理 (8 cặp câu hỏi)
    # ==============================================================================

    # Cặp 22: Trợ từ cảm thán đồng tình cuối câu ね
    add_pair("4", "3", P4_3,
        "Trợ từ「ね」ở cuối câu trong giao tiếp tiếng Nhật có chức năng ngữ pháp chính là gì?",
        [
            "Hỏi thông tin mới mà người nói hoàn toàn chưa biết",
            "Bày tỏ cảm xúc, tìm kiếm sự đồng cảm hoặc xác nhận thông tin từ người nghe",
            "Bắt buộc người nghe phải làm theo mệnh lệnh của mình",
            "Biểu thị sự nghi ngờ, không tin tưởng đối phương"
        ],
        "B",
        "Trợ từ「ね」đặt cuối câu dùng để tìm kiếm sự đồng tình, chia sẻ cảm xúc với đối phương (tương đương với \"... nhỉ, ... nhé\").",
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
        "Phó từ mức độ「とても」(rất) kết hợp với tính từ ở dạng nào và đứng ở vị trí nào?",
        [
            "Đứng trước tính từ và luôn đi với thể khẳng định",
            "Đứng sau tính từ và đi với thể phủ định",
            "Chỉ đi với động từ thể quá khứ",
            "Đứng ở cuối câu sau です"
        ],
        "A",
        "「とても」đứng trước tính từ/động từ để biểu thị mức độ cao \"rất...\", luôn đi với dạng khẳng định (Ví dụ: とても おいしいです: rất ngon).",
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
        "Phó từ「すこし」(một chút, hơi...) kết hợp với tính từ ở dạng nào?",
        [
            "Đi với tính từ thể khẳng định để diễn đạt mức độ nhẹ",
            "Bắt buộc phải đi với thể phủ định",
            "Chỉ đi với tính từ đuôi な",
            "Chỉ dùng trong câu hỏi nghi vấn"
        ],
        "A",
        "「すこし」(hoặc ちょっと trong khẩu ngữ) đi với dạng khẳng định để diễn đạt mức độ nhẹ \"hơi, một chút\" (Ví dụ: すこし さむいです: hơi lạnh).",
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
        "QUY TẮC BẮT BUỘC: Phó từ「あまり」(không... lắm) có quy tắc kết hợp ngữ pháp như thế nào?",
        [
            "Luôn luôn đi với tính từ / động từ ở thể khẳng định",
            "Luôn luôn đi với tính từ / động từ ở thể phủ định",
            "Có thể đi với cả khẳng định lẫn phủ định mà không đổi nghĩa",
            "Chỉ đi với danh từ chỉ số lượng"
        ],
        "B",
        "「あまり」bắt buộc phải đi với vị ngữ ở thể PHỦ ĐỊNH mang nghĩa \"không... lắm\" (Ví dụ: あまり さむくないです: không lạnh lắm).",
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
        "Phó từ「ぜんぜん」(hoàn toàn không...) có quy tắc kết hợp ngữ pháp như thế nào?",
        [
            "Bắt buộc đi với thể phủ định để nhấn mạnh mức độ phủ định 0%",
            "Luôn đi với câu khẳng định",
            "Chỉ đi với tính từ chỉ màu sắc",
            "Chỉ dùng khi hỏi ý kiến đối phương"
        ],
        "A",
        "「ぜんぜん」đi với thể phủ định biểu thị \"hoàn toàn không... chút nào\" (Ví dụ: ぜんぜん むずかしくないです: hoàn toàn không khó).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tiếng Nhật hoàn toàn không dễ chút nào.\"",
        [
            "日本語は ぜんぜん やさしいです。",
            "日本語は ぜんぜん かんたんじゃないです。",
            "日本語は とても かんたんじゃないです。",
            "日本語は あまり かんたんです。"
        ],
        "B",
        "ぜんぜん + Phủ định:「ぜんぜん かんたんじゃないです。」(hoàn toàn không đơn giản)."
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
        "Cấu trúc: Địa danh + は + Mùa (はる, なつ, あき, ふゆ) + Tính từ + です (Ví dụ: 日本は なつ、あついです: Nhật Bản vào mùa hè thì nóng).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Nhật Bản vào mùa hè thì rất nóng.\"",
        [
            "日本は なつ、とても あついです。",
            "日本は なつ、とても さむいです。",
            "日本は あき、とても あついです。",
            "日本は ふゆ、とても すずしいです。"
        ],
        "A",
        "Mùa hè là なつ (夏), nóng là あつい:「日本は なつ、とても あついです。」"
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
        "Dùng trợ từ の để xác định danh từ thời tiết/mùa thuộc địa điểm:「[Địa điểm] の [Mùa] は [Tính từ] です。」(Ví dụ: ハノイの あきは すずしいです).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Mùa thu của Hà Nội rất mát mẻ và dễ chịu.\"",
        [
            "ハノイの なつは とても すずしいです。",
            "ハノイの あきは とても すずしいです。",
            "ハノイの はるは とても さむいです。",
            "ハノイの ふゆは とても あついです。"
        ],
        "B",
        "Mùa thu là あき (秋), mát mẻ là すずしい (涼しい):「ハノイの あきは とても すずしいです。」"
    )

    # Cặp 29: Hỏi thời tiết theo mùa: [Mùa] は どうですか
    add_pair("4", "3", P4_3,
        "Để hỏi người khác \"Mùa xuân ở đất nước của bạn như thế nào?\", câu hỏi tiếng Nhật nào sau đây là đúng?",
        [
            "お国の はるは どこですか。",
            "お国の はるは どうですか。",
            "お国の はるは なんですか。",
            "お国の はるは だれですか。"
        ],
        "B",
        "Hỏi về đặc điểm thời tiết của một mùa:「[Địa điểm] の [Mùa] は どうですか。」(Mùa... ở... như thế nào?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Mùa xuân ở đất nước bạn như thế nào?\" - \"Ấm áp và rất đẹp.\"",
        [
            "「お国の はるは どうですか。」「あたたかくて、とても きれいです。」",
            "「お国の なつは どうですか。」「あたたかくて、とても きれいです。」",
            "「お国の ふゆは どうですか。」「さむくて、とても きれいです。」",
            "「お国の あきは どうですか。」「すずしくて、とても きれいです。」"
        ],
        "A",
        "Mùa xuân là はる, ấm áp là あたたかい:「お国の はるは どうですか。」「あたたかくて、とても きれいです。」"
    )
