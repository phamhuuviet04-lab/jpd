# -*- coding: utf-8 -*-
"""
Dữ liệu câu hỏi ngữ pháp Bài 6 - Dekiru Nihongo
Chia làm 2 dạng câu hỏi rõ ràng:
1. [HỎI NGỮ PHÁP]: Hỏi khái niệm, cấu trúc, quy tắc, cách trả lời theo chuẩn ngữ pháp
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
        "💡 Chuẩn ngữ pháp:「〜ませんか」là mẫu câu rủ rê, mời mọc lịch sự: \"Cùng làm... với tôi không?\" (Ví dụ: いっしょに えいがを 見ませんか: cùng đi xem phim với tôi không?).",
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
        "Khi được rủ:「いっしょに コーヒーを 飲みませんか。」, nếu bạn muốn ĐỒNG Ý và hào hứng đề xuất đi ngay thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "いいですね。飲みません。",
            "いいですね。飲みましょう。",
            "いいですね。飲みたいです。",
            "いいですね。飲みます。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi đồng ý với lời rủ rê và khởi xướng cùng đi làm hành động, ta dùng「Vましょう」➔「いいですね。飲みましょう。」(Được đấy, cùng uống nhé!).",
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
        "Khi ai đó rủ bạn đi chơi, nếu bạn muốn TỪ CHỐI KHÉO vì ngày mai có việc bận thì theo chuẩn ngữ pháp và văn hóa giao tiếp phải nói như thế nào?",
        [
            "「嫌です。(Tôi ghét)」",
            "「すみません、あしたは ちょっと 用事(ようじ)が ありますから…」",
            "「絶対に行きません。(Tuyệt đối không đi)」",
            "「なぜですか。(Tại sao lại rủ tôi)」"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cách từ chối khéo léo, lịch sự: Nói「すみません、ちょっと…」rồi nêu lý do kết thúc bằng「〜から」➔「すみません、あしたは ちょっと 用事がありますから…」",
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
        "Khi bạn bè rủ:「日曜日、サッカーを しませんか。」, nếu bạn muốn từ chối vì \"đã có hẹn với bạn bè rồi\" thì câu nói chuẩn ngữ pháp là:",
        [
            "すみません、しごとが ありますから。",
            "すみません、ともだちと 約束(やくそく)が ありますから。",
            "すみません、時間が ありますから。",
            "すみません、お金が ありますから。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cuộc hẹn trước, lời hứa là「約束 (やくそく)」. Giải thích lý do từ chối:「すみません、ともだちと 約束が ありますから。」(vì tôi có hẹn với bạn rồi).",
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
        "Khi muốn diễn đạt một sự kiện, buổi hòa nhạc hay lễ hội DIỄN RA tại một địa điểm, theo chuẩn ngữ pháp ta dùng trợ từ nào đi sau địa điểm đó?",
        [
            "Trợ từ に",
            "Trợ từ で",
            "Trợ từ を",
            "Trợ từ へ"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Với sự kiện/hoạt động diễn ra (lễ hội, concert, kỳ thi, tiệc tùng): [Địa điểm] + で + [Sự kiện] + が あります (Ví dụ: 浅草公園で お祭りが あります).",
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
        "PHÂN BIỆT TRỢ TỪ: Điểm khác biệt về mặt chuẩn ngữ pháp giữa「Địa điểm に あります」và「Địa điểm で あります」là gì?",
        [
            "Hai cấu trúc hoàn toàn giống nhau, dùng thay thế tự do",
            "「に あります」dùng cho đồ vật, công trình tồn tại tĩnh; còn「で あります」dùng cho sự kiện, hoạt động tổ chức diễn ra",
            "「で あります」chỉ dùng cho thời gian",
            "「に あります」chỉ dùng cho người và động vật"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tồn tại tĩnh (đồ vật, toà nhà, chùa chiền) dùng [Địa điểm] + に; Tổ chức sự kiện (lễ hội, thi cử, tiệc tùng, hòa nhạc) dùng [Địa điểm] + で ➔「大学で テストが あります。」",
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
        "💡 Chuẩn ngữ pháp: Lượng từ「〜まい (枚)」chuyên dùng để đếm các vật mỏng, phẳng: vé (チケット), áo sơ mi (シャツ), giấy (かみ), đĩa CD, ảnh (しゃしん)...",
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
        "💡 Chuẩn ngữ pháp: Đếm lượng từ 〜まい: 1まい (いちまい), 2まい (にまい), 3まい (さんまい), 4まい (よんまい)...",
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
        "Khi bạn có sẵn 2 tấm vé xem phim và muốn rủ đối phương cùng đi xem, câu nói chuẩn ngữ pháp giao tiếp là gì?",
        [
            "チケットが ありますから、お金を ください。",
            "えいがの チケットが 2枚 あります。いっしょに 行きませんか。",
            "チケットを 買いました。ひとりで 行きます。",
            "チケットが ありません。行きましょう。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Nêu số lượng vé có sẵn [Danh từ] + が + [Số lượng] + あります kết hợp rủ rê「いっしょに 行きませんか。」(Tôi có 2 tấm vé. Cùng đi với tôi không?).",
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
        "💡 Chuẩn ngữ pháp: Cấu trúc: N1 は N2 より Adj です = \"N1 thì [Tính từ] hơn N2\" (Đối tượng đứng trước は là đối tượng có tính chất cao hơn). Ví dụ: 新幹線は でんしゃより はやいです。",
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
        "Trong câu so sánh hơn「東京は 京都より にぎやかです。」, thành phố nào náo nhiệt hơn?",
        [
            "Kyoto náo nhiệt hơn",
            "Tokyo náo nhiệt hơn",
            "Cả hai thành phố đều yên tĩnh",
            "Không xác định được"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Đối tượng đi với trợ từ「は」là đối tượng được khẳng định có tính chất nổi trội hơn so với đối tượng sau「より」➔ Tokyo náo nhiệt hơn Kyoto.",
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
        "Cấu trúc câu hỏi so sánh lựa chọn giữa 2 đối tượng theo chuẩn ngữ pháp là gì?",
        [
            "N1 や N2 や どれが Adj ですか。",
            "N1 と N2 と どちらが Adj ですか。",
            "N1 から N2 まで なにが Adj ですか。",
            "N1 も N2 も どこが Adj ですか。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Mẫu câu hỏi lựa chọn giữa 2 đối tượng:「N1 と N2 と どちら (hoặc どっち) が Adj ですか。」(N1 và N2, cái nào... hơn?).",
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
        "Khi được hỏi:「英語と 日本語と どちらが 難しいですか。」, nếu bạn muốn trả lời là \"Tiếng Nhật khó hơn\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "日本語の ほうが 難しいです。",
            "英語の ほうが 難しいです。",
            "日本語より 難しいです。",
            "どちらも 難しいです。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Khi trả lời câu hỏi lựa chọn và bạn chọn một phía hơn, mẫu câu chuẩn là: [Đối tượng] + の ほうが + [Tính từ] です ➔「日本語の ほうが 難しいです。」",
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
        "Khi được hỏi:「犬と 猫と どちらが 好きですか。」, nếu bạn muốn trả lời là \"Cả hai con tôi đều thích cả\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "犬の ほうが 好きです。",
            "どちらも 好きです。",
            "どちらが 好きです。",
            "どちらの ほうが 好きです。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi cả hai đối tượng đều như nhau: dùng「どちらも + Tính từ」➔「どちらも 好きです。」(Cả hai con tôi đều thích).",
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
        "Cấu trúc so sánh nhất trong một phạm vi / tập hợp theo chuẩn ngữ pháp là gì?",
        [
            "[Phạm vi] に N が 一番 Adj です。",
            "[Phạm vi] で N が 一番 Adj です。",
            "[Phạm vi] を N が 一番 Adj です。",
            "[Phạm vi] より N が 一番 Adj です。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cấu trúc so sánh nhất: [Phạm vi/Tập hợp] + で + [Danh từ] + が + 一番 (いちばん) + [Tính từ] + です (Trong phạm vi..., N là... nhất). Ví dụ: 1年で 7月が 一番 あついです。",
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
        "Khi được hỏi:「日本料理で 何が 一番 好きですか。」, nếu bạn muốn trả lời là \"Tôi thích món sushi nhất\" thì câu trả lời chuẩn ngữ pháp là:",
        [
            "すしが 一番 好きです。",
            "すしは 一番 好きです。",
            "すしの ほうが 好きです。",
            "すしより 好きです。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trả lời so sánh nhất: [Đối tượng] + が + 一番 + [Tính từ] です ➔「すしが 一番 好きです。」",
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
        "Khi được hỏi:「日本は いつが 一番 きれいですか。」, nếu bạn muốn trả lời là \"Mùa xuân là đẹp nhất\" thì câu nói chuẩn ngữ pháp là:",
        [
            "春が 一番 きれいです。",
            "春の ほうが きれいです。",
            "春より きれいです。",
            "春は どちらも きれいです。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trả lời câu hỏi so sánh nhất「いつが 一番〜」: [Thời điểm] + が + 一番 + [Tính từ] です ➔「春が 一番 きれいです。」",
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
        "Khi được hỏi:「お国で どこが 一番 有名ですか。」, nếu bạn muốn trả lời là \"Vịnh Hạ Long là nổi tiếng nhất\" thì câu trả lời chuẩn ngữ pháp là:",
        [
            "ハロンわんが 一番 有名です。",
            "ハロンわんの ほうが 有名です。",
            "ハロンわんより 有名です。",
            "ハロンわんは どちらも 有名です。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trả lời so sánh nhất nơi chốn: [Địa danh] + が + 一番 + 有名です ➔「ハロンわんが 一番 有名です。」",
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
        "💡 Chuẩn ngữ pháp:「もう Vましたか」dùng để kiểm tra tiến độ xem hành động đã hoàn tất hay chưa: \"Bạn đã làm V chưa / rồi phải không?\". Ví dụ: もう 宿題を しましたか。",
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
        "Khi được hỏi:「もう 昼ごはんを食べましたか。」, nếu bạn muốn trả lời khẳng định là \"Vâng, tôi đã ăn rồi\" thì câu nói chuẩn ngữ pháp là:",
        [
            "はい、まだ 食べました。",
            "はい、もう 食べました。",
            "いいえ、もう 食べました。",
            "はい、これから 食べました。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trả lời khẳng định cho「もう Vましたか」:「はい、もう Vました。」➔「はい、もう 食べました。」(Vâng, tôi đã ăn rồi).",
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
        "QUY TẮC BẮT BUỘC: Khi được hỏi「もう 飛行機のチケットを 買いましたか。」, nếu bạn muốn trả lời là \"Chưa, tôi vẫn chưa mua\" thì theo chuẩn ngữ pháp BẮT BUỘC phải nói như thế nào?",
        [
            "いいえ、買いませんでした (Sai ngữ pháp nghiêm trọng)",
            "いいえ、まだです。(Hoặc: いいえ、まだ 買っていません)",
            "いいえ、もう 買いません。",
            "いいえ、ぜんぜん 買いました。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Đối với câu hỏi「もう Vましたか」, nếu chưa làm thì BẮT BUỘC trả lời「いいえ、まだです」(Chưa, tôi chưa làm). Tuyệt đối KHÔNG trả lời「いいえ、Vませんでした」vì câu đó mang nghĩa là bạn đã không mua và từ chối không mua nữa.",
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
        "Khi cùng bạn bè bàn「何を食べますか。」, nếu bạn muốn GỢI Ý ĐỀ XUẤT \"Món sushi thì sao / thế nào?\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "すしは どこですか。",
            "すしは どうですか。",
            "すしは なんですか。",
            "すしは だれですか。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Ở Bài 6.3, mẫu câu「[Danh từ] は どうですか。」mang chức năng đưa ra đề xuất, gợi ý giải pháp: \"Phương án/món... thì thế nào/sao?\" ➔「すしは どうですか。」",
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
        "Khi bàn bạc kế hoạch đi chơi「どこに旅行しますか。」, nếu bạn muốn GỢI Ý \"Đi Kyoto thì thế nào?\" thì câu nói chuẩn ngữ pháp là:",
        [
            "京都は どうですか。",
            "京都は どこですか。",
            "京都は なんですか。",
            "京都は だれですか。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trong bối cảnh bàn kế hoạch du lịch, dùng「[Địa điểm] は どうですか」để gợi ý địa điểm:「京都は どうですか。」",
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
        "Khi cùng bạn dạo phố Tokyo và muốn chia sẻ cảm thán đồng cảm (\"Cuộc sống ở Tokyo thật thú vị và tiện lợi nhỉ!\"), theo chuẩn ngữ pháp ta dùng trợ từ cuối câu nào?",
        [
            "Trợ từ よ",
            "Trợ từ ね",
            "Trợ từ か",
            "Trợ từ も"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trợ từ「ね」dùng khi cả người nói và người nghe cùng nhìn thấy hoặc cùng chia sẻ một trải nghiệm chung (đồng cảm, đồng thuận):「東京の 生活は おもしろいですね。」",
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
        "💡 Chuẩn ngữ pháp: Trợ từ「よ」dùng khi người nói muốn truyền đạt một thông tin mới mà đối phương chưa biết:「あの店は おいしくて、やすいですよ。」(Quán kia đồ ăn ngon và rẻ lắm đấy nhé!).",
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
        "Khi thấy đã muộn (12 giờ đêm) và bạn muốn NHẮC NHỞ bạn cùng phòng đi ngủ vì người đó chưa để ý giờ thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "もう 12じですね。寝ましょう。",
            "もう 12じですよ。寝ましょう。",
            "もう 12じですか。寝ましょう。",
            "もう 12じでした。寝ましょう。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Nhắc nhở người chưa để ý giờ (thông tin mới với người đó) ➔ BẮT BUỘC dùng trợ từ「よ」:「もう 12じですよ。寝ましょう。」",
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
        "Khi đối phương đưa ra một gợi ý kế hoạch hay và bạn muốn ĐỒNG Ý \"Hay quá, chúng ta hãy cùng làm như vậy nhé!\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "いいですね。そうでした。",
            "いいですね。そうしましょう。",
            "いいですね。そうしません。",
            "いいですね。そうですよ。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi đồng ý nhiệt tình với một gợi ý đề xuất:「いいですね。そうしましょう。」(Hay quá, chúng ta cùng làm như vậy đi!).",
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
