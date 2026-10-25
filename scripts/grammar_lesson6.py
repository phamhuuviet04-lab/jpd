# -*- coding: utf-8 -*-
"""
Dữ liệu câu hỏi ngữ pháp Bài 6 - Dekiru Nihongo
Chia làm 2 dạng câu hỏi rõ ràng:
1. [HỎI NGỮ PHÁP]: Hỏi khái niệm, cấu trúc, quy tắc, ý nghĩa ngữ pháp
2. [DỊCH CÂU]: Dịch từ câu tiếng Việt sang tiếng Nhật tương ứng
"""

def register_lesson_6(add_pair):
    P6_1 = "一緒に行きませんか (Rủ rê 〜ませんか, 〜ましょう, であります, 〜まい)"
    P6_2 = "どちらがいいですか。 (So sánh hơn より, どちら, 一番)"
    P6_3 = "約束 (Đã làm chưa もう, Gợi ý Nはどうですか, ね/よ, そうしましょう)"

    # ==============================================================================
    # PHẦN 1: 一緒に行きませんか (9 cặp câu hỏi)
    # ==============================================================================

    # Cặp 1: Lời rủ rê, mời mọc lịch sự: Vませんか
    add_pair("6", "1", P6_1,
        "Mẫu câu「Vませんか。」dùng để làm gì trong giao tiếp tiếng Nhật?",
        [
            "Hỏi xem đối phương có thể làm được việc gì không",
            "Dùng để rủ rê, mời mọc đối phương cùng làm một hành động với mình một cách lịch sự",
            "Hỏi xin phép đối phương cho mình làm việc gì",
            "Mệnh lệnh bắt buộc đối phương phải làm"
        ],
        "B",
        "「〜ませんか」là mẫu câu rủ rê, mời mọc lịch sự: \"Cùng làm... với tôi không?\" (Ví dụ: いっしょに えいがを 見に行きませんか).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cuối tuần cùng đi xem phim với tôi không?\"",
        [
            "しゅうまつ いっしょに えいがを 見ませんか。",
            "しゅうまつ いっしょに えいがを 見ましょう。",
            "しゅうまつ いっしょに えいがを 見てください。",
            "しゅうまつ いっしょに えいがを 見たいですか。"
        ],
        "A",
        "Lời rủ rê lịch sự:「しゅうまつ いっしょに えいがを 見ませんか。」"
    )

    # Cặp 2: Đồng ý lời rủ rê / Khởi xướng cùng làm: Vましょう
    add_pair("6", "1", P6_1,
        "Mẫu câu「Vましょう。」dùng trong hoàn cảnh giao tiếp nào?",
        [
            "Chỉ dùng khi ra lệnh cho cấp dưới",
            "Dùng để hào hứng đồng ý với một lời rủ rê, hoặc chủ động khởi xướng đề xuất: \"Chúng ta hãy cùng làm... nhé!\"",
            "Dùng khi từ chối một lời đề nghị",
            "Dùng để diễn tả một thói quen hàng ngày"
        ],
        "B",
        "「〜ましょう」dùng để đồng ý lời rủ rê:「いいですね。行きましょう」(Được đấy, cùng đi nào!) hoặc khởi xướng:「食べましょう」(Cùng ăn nào!).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ý kiến hay đấy, chúng ta cùng đi uống cà phê nhé!\"",
        [
            "いいですね。コーヒーを 飲みませんか。",
            "いいですね。コーヒーを 飲みましょう。",
            "いいですね。コーヒーを 飲みたいです。",
            "いいですね。コーヒーを 飲みます。"
        ],
        "B",
        "Đồng ý và rủ cùng thực hiện ngay:「いいですね。コーヒーを 飲みましょう。」"
    )

    # Cặp 3: Từ chối khéo lời rủ rê: すみません、ちょっと… [Lý do] から
    add_pair("6", "1", P6_1,
        "Khi muốn từ chối khéo một lời rủ rê mà không gây mất lòng đối phương, người Nhật thường sử dụng mẫu câu nào?",
        [
            "「嫌です。(Tôi ghét)」",
            "「すみません、ちょっと… [Lý do] から。」",
            "「絶対に行きません。(Tuyệt đối không đi)」",
            "「なぜですか。(Tại sao lại rủ tôi)」"
        ],
        "B",
        "Cách từ chối khéo léo, lịch sự của người Nhật: Nói「すみません、ちょっと…」(Xin lỗi, tôi hơi kẹt một chút...) rồi nêu lý do kết thúc bằng「〜から」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Xin lỗi, ngày mai tôi có chút việc bận rồi (nên không đi được).\"",
        [
            "すみません、あしたは 用事(ようじ)が ありますから…",
            "すみません、あしたは 用事(ようじ)が ありますですが…",
            "すみません、あしたは 用事(ようじ)が ありますそして…",
            "すみません、あしたは 用事(ようじ)が ありませんから…"
        ],
        "A",
        "Từ chối khéo có lý do:「すみません、あしたは 用事(ようじ)が ありますから…」"
    )

    # Cặp 4: Từ chối vì có hẹn trước: 約束がありますから
    add_pair("6", "1", P6_1,
        "Để giải thích lý do từ chối lời mời là \"vì tôi có hẹn trước rồi\", câu tiếng Nhật nào sau đây là đúng?",
        [
            "すみません、しごとが ありますから。",
            "すみません、約束(やくそく)が ありますから。",
            "すみません、時間が ありますから。",
            "すみません、お金が ありますから。"
        ],
        "B",
        "Cuộc hẹn trước, lời hứa là「約束 (やくそく)」. Giải thích lý do từ chối:「約束が ありますから。」(vì tôi có hẹn trước rồi).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chủ nhật cùng đi đá bóng không?\" - \"Xin lỗi, tôi có hẹn với bạn rồi.\"",
        [
            "「日曜日、サッカーを しませんか。」「すみません、ともだちと 約束が ありますから。」",
            "「日曜日、サッカーを しませんか。」「すみません、ともだちと 約束が ありませんから。」",
            "「日曜日、サッカーを しませんか。」「いいですね、ともだちと 約束が ありますから。」",
            "「日曜日、サッカーを しましょうか。」「すみません、ともだちに 約束が ありますから。」"
        ],
        "A",
        "Hội thoại rủ rê và từ chối vì có hẹn:「日曜日、サッカーを しませんか。」「すみません、ともだちと 約束が ありますから。」"
    )

    # Cặp 5: Sự kiện, lễ hội diễn ra tại địa điểm: Địa điểm で Sự kiện が あります
    add_pair("6", "1", P6_1,
        "Khi muốn diễn đạt một sự kiện, buổi hòa nhạc hay lễ hội DIỄN RA tại một địa điểm, ta dùng trợ từ nào đi sau địa điểm đó?",
        [
            "Trợ từ に",
            "Trợ từ で",
            "Trợ từ を",
            "Trợ từ へ"
        ],
        "B",
        "Với sự kiện/hoạt động diễn ra (lễ hội, concert, kỳ thi, tiệc tùng): [Địa điểm] + で + [Sự kiện] + が あります.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Vào thứ Bảy tuần này, ở công viên Asakusa có lễ hội hoa anh đào.\"",
        [
            "こんどの 土曜日、浅草公園に お祭りが あります。",
            "こんどの 土曜日、浅草公園で お祭りが あります。",
            "こんどの 土曜日、浅草公園をお祭りが あります。",
            "こんどの 土曜日、浅草公園へ お祭りが あります。"
        ],
        "B",
        "Lễ hội diễn ra tại công viên ➔ dùng trợ từ で:「浅草公園で お祭りが あります。」"
    )

    # Cặp 6: Phân biệt trợ từ に và で khi đi với あります
    add_pair("6", "1", P6_1,
        "PHÂN BIỆT TRỢ TỪ: Điểm khác biệt về mặt ngữ pháp giữa「Địa điểm に あります」và「Địa điểm で あります」là gì?",
        [
            "Hai cấu trúc hoàn toàn giống nhau, dùng thay thế tự do",
            "「に あります」dùng cho đồ vật, công trình tồn tại tĩnh; còn「で あります」dùng cho sự kiện, hoạt động tổ chức diễn ra",
            "「で あります」chỉ dùng cho thời gian",
            "「に あります」chỉ dùng cho người và động vật"
        ],
        "B",
        "Quy tắc vàng: Tồn tại tĩnh (đồ vật, toà nhà, chùa chiền) dùng [Địa điểm] + に; Tổ chức sự kiện (lễ hội, thi cử, tiệc tùng, hòa nhạc) dùng [Địa điểm] + で.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ngày mai ở trường đại học có kỳ thi tiếng Nhật.\"",
        [
            "あした 大学に 日本語の テストが あります。",
            "あした 大学で 日本語の テストが あります。",
            "あした 大学を 日本語の テストが あります。",
            "あした 大学へ 日本語の テストが あります。"
        ],
        "B",
        "Kỳ thi là một sự kiện diễn ra ➔ dùng trợ từ で:「大学で 日本語の テストが あります。」"
    )

    # Cặp 7: Lượng từ đếm vật mỏng phẳng: 〜枚 (〜まい)
    add_pair("6", "1", P6_1,
        "Lượng từ「〜枚 (〜まい)」trong tiếng Nhật dùng để đếm những đồ vật có đặc điểm như thế nào?",
        [
            "Đếm người và động vật nhỏ",
            "Đếm các vật mỏng, phẳng như vé xem phim, áo sơ mi, tờ giấy, đĩa CD",
            "Đếm các loại xe cộ và máy móc",
            "Đếm các vật dài hình trụ như cây bút, cái chai"
        ],
        "B",
        "Lượng từ「〜まい (枚)」chuyên dùng để đếm các vật mỏng, phẳng: vé (チケット), áo (シャツ), giấy (かみ), đĩa CD, ảnh (しゃしん)...",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi có 2 tấm vé xem buổi hòa nhạc.\"",
        [
            "コンサートの チケットが 2ほん あります。",
            "コンサートの チケットが 2まい あります。",
            "コンサートの チケットが 2だい あります。",
            "コンサートの チケットが 2さつ あります。"
        ],
        "B",
        "Vé là vật mỏng phẳng, đếm bằng まい:「チケットが 2まい あります。」"
    )

    # Cặp 8: Số đếm kết hợp lượng từ 〜枚 (1枚, 2枚...)
    add_pair("6", "1", P6_1,
        "Cách đọc số đếm lượng từ cho 1 tấm vé (1枚) và 3 chiếc áo sơ mi (3枚) trong tiếng Nhật là gì?",
        [
            "ひとつ / みっつ",
            "いちまい / さんまい",
            "いっぽん / さんぼん",
            "いちだい / さんだい"
        ],
        "B",
        "Đếm lượng từ 〜まい: 1まい (いちまい), 2まい (にまい), 3まい (さんまい), 4まい (よんまい)...",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hôm qua tôi đã mua 3 chiếc áo sơ mi ở cửa hàng.\"",
        [
            "きのう 店で シャツを 3まい 買いました。",
            "きのう 店で シャツを 3ほん 買いました。",
            "きのう 店で シャツを 3さつ 買いました。",
            "きのう 店で シャツを 3こ 買いました。"
        ],
        "A",
        "Áo sơ mi đếm bằng まい:「シャツを 3まい 買いました。」"
    )

    # Cặp 9: Rủ rê dựa trên số lượng có sẵn
    add_pair("6", "1", P6_1,
        "Khi bạn có sẵn vé và muốn mời bạn đi cùng xem, cấu trúc hội thoại chuẩn thường dùng là gì?",
        [
            "チケットが ありますから、お金を ください。",
            "チケットが 2枚 あります。いっしょに 行きませんか。",
            "チケットを 買いました。ひとりで行きます。",
            "チケットが ありません。行きましょう。"
        ],
        "B",
        "Mẫu giao tiếp thực tế Dekiru Nihongo: Nêu số lượng vé có sẵn + Rủ rê bằng「いっしょに 行きませんか。」(Tôi có 2 tấm vé. Cùng đi với tôi không?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi có 2 tấm vé xem phim. Cùng đi xem với tôi không?\"",
        [
            "えいがの チケットが 2まい あります。いっしょに 行きませんか。",
            "えいがの チケットが 2まい あります。いっしょに 行きましょうか。",
            "えいがの チケットが 2まい あります。ひとりで 行きます。",
            "えいがの チケットが 2まい あります。見たくないです。"
        ],
        "A",
        "Câu mời rủ chuẩn:「えいがの チケットが 2まい あります。いっしょに 行きませんか。」"
    )

    # ==============================================================================
    # PHẦN 2: どちらがいいですか。 (9 cặp câu hỏi)
    # ==============================================================================

    # Cặp 10: So sánh hơn giữa 2 đối tượng: N1 は N2 より Adj です
    add_pair("6", "2", P6_2,
        "Cấu trúc so sánh hơn giữa hai đối tượng「N1 は N2 より Adj です。」mang ý nghĩa là gì?",
        [
            "N1 và N2 ngang bằng nhau về tính chất",
            "N1 thì [Tính từ] hơn so với N2",
            "N2 thì [Tính từ] hơn so với N1",
            "Cả N1 và N2 đều không đạt tính chất đó"
        ],
        "B",
        "Cấu trúc: N1 は N2 より Adj です = \"N1 thì [Tính từ] hơn N2\" (Đối tượng đứng trước は là đối tượng có tính chất cao hơn).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tàu Shinkansen nhanh hơn tàu điện thông thường.\"",
        [
            "新幹線は でんしゃより はやいです。",
            "でんしゃは 新幹線より はやいです。",
            "新幹線は でんしゃほど はやいです。",
            "新幹線のほうが でんしゃが はやいです。"
        ],
        "A",
        "N1 (Shinkansen) nhanh hơn N2 (tàu thường):「新幹線は でんしゃより はやいです。」"
    )

    # Cặp 11: So sánh hơn về tính chất: [Đối tượng 1] は [Đối tượng 2] より [Tính từ]
    add_pair("6", "2", P6_2,
        "Trong câu so sánh hơn「ハノイは ダナンより にぎやかです。」, thành phố nào náo nhiệt hơn?",
        [
            "Đà Nẵng náo nhiệt hơn",
            "Hà Nội náo nhiệt hơn",
            "Cả hai thành phố đều yên tĩnh",
            "Không xác định được"
        ],
        "B",
        "Chủ ngữ đi với trợ từ「は」là đối tượng được khẳng định có tính chất nổi trội hơn so với đối tượng sau「より」➔ Hà Nội náo nhiệt hơn.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tokyo náo nhiệt hơn Kyoto.\"",
        [
            "京都は 東京より にぎやかです。",
            "東京は 京都より にぎやかです。",
            "東京は 京都と にぎやかです。",
            "東京より 京都のほうが にぎやかです。"
        ],
        "B",
        "Tokyo hơn Kyoto:「東京は 京都より にぎやかです。」"
    )

    # Cặp 12: Câu hỏi so sánh lựa chọn: N1 と N2 と どちらが Adj ですか
    add_pair("6", "2", P6_2,
        "Cấu trúc câu hỏi so sánh lựa chọn giữa 2 đối tượng là gì?",
        [
            "N1 や N2 や どれが Adj ですか。",
            "N1 と N2 と どちらが Adj ですか。",
            "N1 から N2 まで なにが Adj ですか。",
            "N1 も N2 も どこが Adj ですか。"
        ],
        "B",
        "Mẫu câu hỏi lựa chọn giữa 2 đối tượng:「N1 と N2 と どちら (hoặc どっち) が Adj ですか。」(N1 và N2, cái nào... hơn?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Thịt bò và thịt cá, món nào ngon hơn?\"",
        [
            "ぎゅうにくと さかなと どれが おいしいですか。",
            "ぎゅうにくと さかなと どちらが おいしいですか。",
            "ぎゅうにくや さかなや なにが おいしいですか。",
            "ぎゅうにくと さかなと どこが おいしいですか。"
        ],
        "B",
        "So sánh lựa chọn giữa 2 thứ dùng「どちらが」:「ぎゅうにくと さかなと どちらが おいしいですか。」"
    )

    # Cặp 13: Trả lời chọn một đối tượng hơn: N の ほうが Adj です
    add_pair("6", "2", P6_2,
        "Khi trả lời câu hỏi lựa chọn「N1 と N2 と どちらが Adj ですか。」và bạn CHỌN N1 HƠN, mẫu câu trả lời chuẩn là gì?",
        [
            "N1 の ほうが Adj です。",
            "N1 より Adj です。",
            "N1 は どちらも Adj です。",
            "N1 が 一番 Adj です。"
        ],
        "A",
        "Khi lựa chọn một phía hơn trong 2 đối tượng, ta dùng mẫu「[Đối tượng] の ほうが Adj です。」(Phía... hơn).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tiếng Nhật và tiếng Anh, tiếng Nhật khó hơn.\"",
        [
            "日本語の ほうが むずかしいです。",
            "英語の ほうが むずかしいです。",
            "日本語より むずかしいです。",
            "どちらも むずかしいです。"
        ],
        "A",
        "Chọn tiếng Nhật khó hơn:「日本語の ほうが むずかしいです。」"
    )

    # Cặp 14: Trả lời cả hai đều như nhau: どちらも Adj です
    add_pair("6", "2", P6_2,
        "Khi trả lời câu hỏi lựa chọn giữa 2 đối tượng và bạn thấy CẢ HAI ĐỀU NHƯ NHAU, mẫu câu trả lời là gì?",
        [
            "どちらが Adj です。",
            "どちらも Adj です。",
            "どちらの ほうが Adj です。",
            "どれも Adj です。"
        ],
        "B",
        "Khi cả hai đều như nhau:「どちらも + Tính từ khẳng định / phủ định」(Cả hai đều...; Ví dụ: どちらも すきです: cả hai tôi đều thích).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chó và mèo, con nào tôi cũng thích cả.\"",
        [
            "いぬの ほうが すきです。",
            "いぬと ねこと どちらも すきです。",
            "ねこの ほうが すきです。",
            "どちらが すきです。"
        ],
        "B",
        "Cả hai đều thích:「いぬと ねこと どちらも すきです。」"
    )

    # Cặp 15: So sánh nhất trong một phạm vi: [Phạm vi] で N が 一番 Adj です
    add_pair("6", "2", P6_2,
        "Cấu trúc so sánh nhất trong một phạm vi / tập hợp là gì?",
        [
            "[Phạm vi] に N が 一番 Adj です。",
            "[Phạm vi] で N が 一番 Adj です。",
            "[Phạm vi] を N が 一番 Adj です。",
            "[Phạm vi] より N が 一番 Adj です。"
        ],
        "B",
        "Cấu trúc so sánh nhất: [Phạm vi/Tập hợp] + で + [Danh từ] + が + 一番 (いちばん) + [Tính từ] + です (Trong phạm vi..., N là... nhất).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Trong một năm, tháng 7 là nóng nhất.\"",
        [
            "1年で 7月が 一番 あついです。",
            "1年に 7月が 一番 あついです。",
            "1年より 7月が 一番 あついです。",
            "1年のほうが 7月が 一番 あついです。"
        ],
        "A",
        "Phạm vi thời gian dùng trợ từ で:「1年で 7月が 一番 あついです。」"
    )

    # Cặp 16: Từ để hỏi về đồ vật trong so sánh nhất: 何が 一番
    add_pair("6", "2", P6_2,
        "Để hỏi về ĐỒ VẬT / MÓN ĂN trong câu hỏi so sánh nhất, từ để hỏi nào được sử dụng?",
        [
            "だれが 一番〜",
            "何(なに)が 一番〜",
            "どこが 一番〜",
            "いつが 一番〜"
        ],
        "B",
        "Hỏi về đồ vật, món ăn dùng từ để hỏi「何 (なに)」:「[Phạm vi] で 何が 一番 Adj ですか。」(Trong..., cái gì là... nhất?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Trong các món ăn Nhật Bản, bạn thích món nào nhất?\"",
        [
            "日本料理で だれが 一番 好きですか。",
            "日本料理で 何(なに)が 一番 好きですか。",
            "日本料理で どこが 一番 好きですか。",
            "日本料理で いつが 一番 好きですか。"
        ],
        "B",
        "Hỏi về món ăn dùng 何が 一番:「日本料理で 何が 一番 好きですか。」"
    )

    # Cặp 17: Từ để hỏi về thời gian trong so sánh nhất: いつが 一番
    add_pair("6", "2", P6_2,
        "Để hỏi về THỜI ĐIỂM / MÙA trong câu hỏi so sánh nhất, từ để hỏi nào được sử dụng?",
        [
            "どこが 一番〜",
            "いつが 一番〜",
            "だれが 一番〜",
            "なにが 一番〜"
        ],
        "B",
        "Hỏi về thời gian, thời điểm dùng「いつ」:「1年で いつが 一番 さむいですか。」(Trong 1 năm, khi nào là lạnh nhất?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ở Nhật Bản, mùa nào (khi nào) là đẹp nhất?\"",
        [
            "日本は どこが 一番 きれいですか。",
            "日本は いつが 一番 きれいですか。",
            "日本は だれが 一番 きれいですか。",
            "日本は なにが 一番 きれいですか。"
        ],
        "B",
        "Hỏi về thời điểm dùng いつが 一番:「日本は いつが 一番 きれいですか。」"
    )

    # Cặp 18: Từ để hỏi về nơi chốn trong so sánh nhất: どこが 一番
    add_pair("6", "2", P6_2,
        "Để hỏi về NƠI CHỐN / ĐỊA ĐIỂM trong câu hỏi so sánh nhất, từ để hỏi nào được sử dụng?",
        [
            "どこが 一番〜",
            "いつが 一番〜",
            "なにが 一番〜",
            "だれが 一番〜"
        ],
        "A",
        "Hỏi về địa điểm nơi chốn dùng「どこ」:「世界で どこが 一番 ひろいですか。」(Trên thế giới, nơi nào là rộng nhất?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ở đất nước của bạn, nơi nào là nổi tiếng nhất?\"",
        [
            "お国で どこが 一番 有名(ゆうめい)ですか。",
            "お国で いつが 一番 有名(ゆうめい)ですか。",
            "お国で なにが 一番 有名(ゆうめい)ですか。",
            "お国で だれが 一番 有名(ゆうめい)ですか。"
        ],
        "A",
        "Hỏi địa điểm dùng どこが 一番:「お国で どこが 一番 有名ですか。」"
    )

    # ==============================================================================
    # PHẦN 3: 約束 (9 cặp câu hỏi)
    # ==============================================================================

    # Cặp 19: Hỏi đã làm việc gì chưa: もう Vましたか
    add_pair("6", "3", P6_3,
        "Cấu trúc「もう Vましたか。」dùng để hỏi điều gì?",
        [
            "Hỏi xem ai đó có muốn làm việc gì trong tương lai không",
            "Hỏi xem một hành động nào đó đã được hoàn thành hay chưa (Đã làm... chưa?)",
            "Hỏi tần suất làm việc gì",
            "Hỏi lý do tại sao chưa làm việc gì"
        ],
        "B",
        "「もう Vましたか」dùng để kiểm tra tiến độ, hành động đã hoàn tất chưa: \"Bạn đã làm V chưa / rồi phải không?\".",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bạn đã làm bài tập về nhà chưa?\"",
        [
            "もう しゅくだいを しましたか。",
            "まだ しゅくだいを しましたか。",
            "しゅくだいを したいですか。",
            "しゅくだいを しませんか。"
        ],
        "A",
        "\"Đã làm bài tập chưa\":「もう しゅくだいを しましたか。」"
    )

    # Cặp 20: Trả lời khẳng định đã làm rồi: はい、もう Vました
    add_pair("6", "3", P6_3,
        "Khi trả lời KHẲNG ĐỊNH cho câu hỏi「もう Vましたか。」(Đã làm rồi), mẫu câu trả lời chuẩn là gì?",
        [
            "はい、まだ Vました。",
            "はい、もう Vました。",
            "いいえ、もう Vました。",
            "はい、これから Vました。"
        ],
        "B",
        "Trả lời khẳng định:「はい、もう Vました。」(Vâng, tôi đã làm rồi; Ví dụ: はい、もう 食べました).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Vâng, tôi đã ăn cơm trưa rồi.\"",
        [
            "はい、まだ ひるごはんを 食べました。",
            "はい、もう ひるごはんを 食べました。",
            "いいえ、もう ひるごはんを 食べました。",
            "はい、ひるごはんを 食べたいです。"
        ],
        "B",
        "\"Vâng, tôi đã ăn rồi\":「はい、もう 食べました。」"
    )

    # Cặp 21: Quy tắc bắt buộc khi trả lời phủ định: いいえ、まだです
    add_pair("6", "3", P6_3,
        "QUY TẮC BẮT BUỘC: Khi trả lời PHỦ ĐỊNH cho câu hỏi「もう Vましたか。」(Chưa làm), câu trả lời chuẩn xác là gì?",
        [
            "いいえ、Vませんでした (Sai ngữ pháp nghiêm trọng)",
            "いいえ、まだです。(Hoặc: いいえ、まだ Vていません)",
            "いいえ、もう Vません。",
            "いいえ、ぜんぜん Vました。"
        ],
        "B",
        "LƯU Ý ĐẶC BIỆT: Đối với「もう Vましたか」, nếu chưa làm thì BẮT BUỘC trả lời「いいえ、まだです」(Chưa, tôi chưa làm). Tuyệt đối KHÔNG trả lời「いいえ、Vませんでした」vì câu đó có nghĩa là \"tôi đã không làm và sẽ không làm nữa\".",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bạn đã mua vé máy bay chưa?\" - \"Chưa, tôi vẫn chưa mua.\"",
        [
            "「もう ひこうきの チケットを 買いましたか。」「いいえ、買いませんでした。」",
            "「もう ひこうきの チケットを 買いましたか。」「いいえ、まだです。」",
            "「もう ひこうきの チケットを 買いましたか。」「はい、まだです。」",
            "「もう ひこうきの チケットを 買いましたか。」「いいえ、もう 買いました。」"
        ],
        "B",
        "Chưa làm phải trả lời:「いいえ、まだです。」(Chưa, tôi chưa làm)."
    )

    # Cặp 22: Gợi ý, đề xuất phương án: N は どうですか
    add_pair("6", "3", P6_3,
        "SO SÁNH NGỮ PHÁP QUAN TRỌNG: Mẫu câu「N は どうですか。」ở BÀI 6.3 có ý nghĩa gì khác so với BÀI 4.2?",
        [
            "Không có gì khác biệt, cả hai đều dùng để miêu tả phòng ốc",
            "Ở Bài 4.2 dùng để hỏi tính chất đặc điểm nơi chốn, còn ở Bài 6.3 dùng để đưa ra GỢI Ý, ĐỀ XUẤT một giải pháp/món ăn (\"Phương án N thì sao?\")",
            "Ở Bài 6.3 chỉ dùng để hỏi giá tiền",
            "Ở Bài 6.3 chỉ dùng để từ chối lời mời"
        ],
        "B",
        "Ở Bài 6.3,「N は どうですか」mang chức năng đề xuất/gợi ý một ý kiến: \"Ăn sushi thì sao?\" (Ví dụ: なにを食べますか。➔ すしは どうですか).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Trưa nay cùng đi ăn nhé. Món sushi thì sao/thế nào?\"",
        [
            "ひるごはんを 食べませんか。すしは どうですか。",
            "ひるごはんを 食べましょう。すしは どこですか。",
            "ひるごはんを 食べましたか。すしは なんですか。",
            "ひるごはんを 食べたいです。すしは だれですか。"
        ],
        "A",
        "Đưa ra gợi ý món ăn:「すしは どうですか。」(Món sushi thì sao?)."
    )

    # Cặp 23: Đề xuất địa điểm du lịch: N は どうですか
    add_pair("6", "3", P6_3,
        "Khi bàn bạc kế hoạch đi chơi và một người đề xuất:「東京は どうですか。」, câu này mang ý nghĩa gì?",
        [
            "Tokyo là một nơi như thế nào?",
            "Đi Tokyo thì thế nào / có được không? (Đưa ra gợi ý về địa điểm)",
            "Tokyo ở đâu?",
            "Tokyo có đông dân không?"
        ],
        "B",
        "Trong bối cảnh bàn kế hoạch,「[Địa điểm] は どうですか」nghĩa là \"Đi địa điểm đó thì thế nào/sao?\".",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Sắp đến kỳ nghỉ rồi. Đi du lịch Kyoto thì thế nào?\"",
        [
            "もうすぐ 休みですね。京都は どうですか。",
            "もうすぐ 休みですね。京都は どこですか。",
            "もうすぐ 休みですね。京都は なんですか。",
            "もうすぐ 休みですね。京都は だれですか。"
        ],
        "A",
        "Gợi ý địa điểm du lịch:「京都は どうですか。」"
    )

    # Cặp 24: Trợ từ cuối câu ね (Đồng cảm, tìm kiếm sự đồng thuận)
    add_pair("6", "3", P6_3,
        "Chức năng chính của trợ từ cuối câu「ね」trong hội thoại giao tiếp là gì?",
        [
            "Thông báo thông tin mới mà đối phương hoàn toàn chưa biết",
            "Bày tỏ sự đồng cảm, tìm kiếm sự đồng thuận hoặc xác nhận thông tin mà CẢ HAI BÊN CÙNG BIẾT",
            "Bày tỏ sự phản đối kịch liệt",
            "Chỉ dùng khi tức giận"
        ],
        "B",
        "Trợ từ「ね」dùng khi người nói và người nghe cùng nhìn thấy hoặc cùng biết một sự việc (đồng cảm, đồng thuận, chia sẻ cảm xúc).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cuộc sống ở Tokyo thật là thú vị và tiện lợi nhỉ!\"",
        [
            "東京の 生活は おもしろいですね。そして、べんりです。",
            "東京の 生活は おもしろいですよ。そして、べんりです。",
            "東京の 生活は おもしろいですか。そして、べんりです。",
            "東京の 生活は おもしろいでした。そして、べんりです。"
        ],
        "A",
        "Chia sẻ cảm xúc đồng cảm dùng trợ từ ね:「東京の 生活は おもしろいですね。」"
    )

    # Cặp 25: Trợ từ cuối câu よ (Cung cấp thông tin mới, nhắc nhở)
    add_pair("6", "3", P6_3,
        "Chức năng chính của trợ từ cuối câu「よ」trong giao tiếp tiếng Nhật là gì?",
        [
            "Tìm kiếm sự đồng tình từ người khác",
            "Cung cấp thông tin mới mà người nghe CHƯA BIẾT, hoặc nhấn mạnh nhắc nhở đối phương với sự quả quyết",
            "Hỏi ý kiến của đối phương",
            "Dùng khi chào tạm biệt"
        ],
        "B",
        "Trợ từ「よ」dùng khi người nói muốn truyền đạt một thông tin mới mà đối phương chưa biết, hoặc nhắc nhở, cảnh báo (Ví dụ: この映画は おもしろいですよ: Phim này hay lắm đấy nhé!).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Quán ăn kia đồ ăn ngon và rẻ lắm đấy nhé! (cho người chưa biết)\"",
        [
            "あの店は おいしくて、やすいですね。",
            "あの店は おいしくて、やすいですよ。",
            "あの店は おいしくて、やすいですか。",
            "あの店は おいしくて、やすいでした。"
        ],
        "B",
        "Cung cấp thông tin mới cho người nghe dùng trợ từ よ:「おいしくて、やすいですよ。」"
    )

    # Cặp 26: Tình huống phân biệt ね và よ trong thực tế
    add_pair("6", "3", P6_3,
        "PHÂN BIỆT THỰC HÀNH: Khi bạn và người kia đang cùng đứng dưới trời mưa to, bạn quay sang trò chuyện thì nên dùng trợ từ nào?",
        [
            "Dùng trợ từ「よ」vì trời đang mưa",
            "Dùng trợ từ「ね」(Ví dụ: すごい雨ですね) vì cả hai người đều đang cùng nhìn thấy và trải nghiệm trời mưa",
            "Dùng trợ từ「か」",
            "Không dùng trợ từ nào cả"
        ],
        "B",
        "Khi cả hai người cùng chứng kiến sự việc (trời mưa to) ➔ dùng「ね」(すごい雨ですね: Mưa to quá nhỉ). Nếu đối phương ở trong phòng không biết bên ngoài đang mưa ➔ dùng「よ」(雨が 降っていますよ: Trời đang mưa đấy nhé).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Đã 12 giờ đêm rồi đấy, đi ngủ thôi nào! (nhắc nhở người đang mải chơi chưa để ý giờ)\"",
        [
            "もう 12じですね。寝ましょう。",
            "もう 12じですよ。寝ましょう。",
            "もう 12じですか。寝ましょう。",
            "もう 12じでした。寝ましょう。"
        ],
        "B",
        "Nhắc nhở người chưa để ý giờ (thông tin mới với người đó) ➔ dùng trợ từ よ:「もう 12じですよ。寝ましょう。」"
    )

    # Cặp 27: Đồng ý làm theo một gợi ý: そうしましょう
    add_pair("6", "3", P6_3,
        "Khi đồng ý làm theo một gợi ý / kế hoạch của người khác, câu tiếng Nhật nào sau đây có nghĩa là \"Cùng làm như thế nhé!\":",
        [
            "そうでした。",
            "そうしましょう。",
            "そうしません。",
            "そうですよ。"
        ],
        "B",
        "「そうしましょう。」(Hãy cùng làm như vậy nhé!) dùng để đồng ý một cách nhiệt tình với một gợi ý, đề xuất vừa được đưa ra.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hay quá, chúng ta hãy cùng làm như vậy nhé!\"",
        [
            "いいですね。そうでした。",
            "いいですね。そうしましょう。",
            "いいですね。そうしません。",
            "いいですね。そうですよ。"
        ],
        "B",
        "Đồng ý với gợi ý đề xuất:「いいですね。そうしましょう。」"
    )
