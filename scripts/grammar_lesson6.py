# -*- coding: utf-8 -*-
"""
Dữ liệu câu hỏi ngữ pháp Bài 6 - Dekiru Nihongo
Chia làm 2 dạng câu hỏi rõ ràng:
1. [HỎI NGỮ PHÁP]: Hỏi khái niệm, cấu trúc, quy tắc, cách trả lời theo chuẩn ngữ pháp
2. [DỊCH CÂU]: Dịch từ câu tiếng Việt sang tiếng Nhật tương ứng
"""

def register_lesson_6(add_pair):
    P6_1 = "いっしょにいきませんか (Rủ rê 〜ませんか, 〜ましょう, であります, 〜まい)"
    P6_2 = "どちらがいいですか。 (So sánh hơn より, どちら, いちばん)"
    P6_3 = "やくそく (Đã làm chưa もう, Gợi ý Nはどうですか, ね/よ, そうしましょう)"

    # ==============================================================================
    # PHẦN 1: いっしょにいきませんか (9 cặp câu hỏi)
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
        "💡 Chuẩn ngữ pháp:「〜ませんか」là mẫu câu rủ rê, mời mọc lịch sự: \"Cùng làm... với tôi không?\" (Ví dụ: いっしょに えいがを みませんか: cùng đi xem phim với tôi không?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cuối tuần cùng đi xem phim với tôi không?\"",
        [
            "しゅうまつ いっしょに えいがを みませんか。",
            "しゅうまつ いっしょに えいがを みましょう。",
            "しゅうまつ いっしょに えいがを みてください。",
            "しゅうまつ いっしょに えいがを みたいですか。"
        ],
        "A",
        "Lời rủ rê lịch sự:「しゅうまつ いっしょに えいがを みませんか。」"
    )

    # Cặp 2: Đồng ý lời rủ rê / Khởi xướng cùng làm: Vましょう
    add_pair("6", "1", P6_1,
        "Khi được rủ:「いっしょに コーヒーを のみませんか。」, nếu bạn muốn ĐỒNG Ý và hào hứng đề xuất đi ngay thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "いいですね。のみません。",
            "いいですね。のみましょう。",
            "いいですね。のみたいです。",
            "いいですね。のみます。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi đồng ý với lời rủ rê và khởi xướng cùng đi làm hành động, ta dùng「Vましょう」➔「いいですね。のみましょう。」(Được đấy, cùng uống nhé!).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ý kiến hay đấy, chúng ta cùng đi uống cà phê nhé!\"",
        [
            "いいですね。コーヒーを のみませんか。",
            "いいですね。コーヒーを のみましょう。",
            "いいですね。コーヒーを のみたいです。",
            "いいですね。コーヒーを のみます。"
        ],
        "B",
        "Đồng ý và rủ cùng thực hiện ngay:「いいですね。コーヒーを のみましょう。」"
    )

    # Cặp 3: Từ chối khéo lời rủ rê: すみません、ちょっと… [Lý do] から
    add_pair("6", "1", P6_1,
        "Khi ai đó rủ bạn đi chơi, nếu bạn muốn TỪ CHỐI KHÉO vì ngày mai có việc bận thì theo chuẩn ngữ pháp và văn hóa giao tiếp phải nói như thế nào?",
        [
            "「いやです。(Tôi ghét)」",
            "「すみません、あしたは ちょっと ようじが ありますから…」",
            "「ぜったいに いきません。(Tuyệt đối không đi)」",
            "「なぜですか。(Tại sao lại rủ tôi)」"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cách từ chối khéo léo, lịch sự: Nói「すみません、ちょっと…」rồi nêu lý do kết thúc bằng「〜から」➔「すみません、あしたは ちょっと ようじが ありますから…」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Xin lỗi, ngày mai tôi có chút việc bận rồi (nên không đi được).\"",
        [
            "すみません、あしたは ようじが ありますから…",
            "すみません、あしたは ようじが ありますですが…",
            "すみません、あしたは ようじが ありますそして…",
            "すみません、あしたは ようじが ありませんから…"
        ],
        "A",
        "Từ chối khéo có lý do:「すみません、あしたは ようじが ありますから…」"
    )

    # Cặp 4: Từ chối vì có hẹn trước: やくそくがありますから
    add_pair("6", "1", P6_1,
        "Khi bạn bè rủ:「にちようび、サッカーを しませんか。」, nếu bạn muốn từ chối vì \"đã có hẹn với bạn bè rồi\" thì câu nói chuẩn ngữ pháp là:",
        [
            "すみません、しごとが ありますから。",
            "すみません、ともだちと やくそくが ありますから。",
            "すみません、じかんが ありますから。",
            "すみません、おかねが ありますから。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cuộc hẹn trước, lời hứa là「やくそく」. Giải thích lý do từ chối:「すみません、ともだちと やくそくが ありますから。」(vì tôi có hẹn với bạn rồi).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chủ nhật cùng đi đá bóng không?\" - \"Xin lỗi, tôi có hẹn với bạn rồi.\"",
        [
            "「にちようび、サッカーを しませんか。」「すみません、ともだちと やくそくが ありますから。」",
            "「にちようび、サッカーを しませんか。」「すみません、ともだちと やくそくが ありませんから。」",
            "「にちようび、サッカーを しませんか。」「いいですね、ともだちと やくそくが ありますから。」",
            "「にちようび、サッカーを しましょうか。」「すみません、ともだちに やくそくが ありますから。」"
        ],
        "A",
        "Hội thoại rủ rê và từ chối vì có hẹn:「にちようび、サッカーを しませんか。」「すみません、ともだちと やくそくが ありますから。」"
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
        "💡 Chuẩn ngữ pháp: Với sự kiện/hoạt động diễn ra (lễ hội, concert, kỳ thi, tiệc tùng): [Địa điểm] + で + [Sự kiện] + が あります (Ví dụ: あさくさこうえんで おまつりが あります).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Vào thứ Bảy tuần này, ở công viên Asakusa có lễ hội hoa anh đào.\"",
        [
            "こんどの どようび、あさくさこうえんに おまつりが あります。",
            "こんどの どようび、あさくさこうえんで おまつりが あります。",
            "こんどの どようび、あさくさこうえんを おまつりが あります。",
            "こんどの どようび、あさくさこうえんへ おまつりが あります。"
        ],
        "B",
        "Lễ hội diễn ra tại công viên ➔ dùng trợ từ で:「あさくさこうえんで おまつりが あります。」"
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
        "💡 Chuẩn ngữ pháp: Tồn tại tĩnh (đồ vật, toà nhà, chùa chiền) dùng [Địa điểm] + に; Tổ chức sự kiện (lễ hội, thi cử, tiệc tùng, hòa nhạc) dùng [Địa điểm] + で ➔「だいがくで テストが あります。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ngày mai ở trường đại học có kỳ thi tiếng Nhật.\"",
        [
            "あした だいがくに にほんごの テストが あります。",
            "あした だいがくで にほんごの テストが あります。",
            "あした だいがくを にほんごの テストが あります。",
            "あした だいがくへ にほんごの テストが あります。"
        ],
        "B",
        "Kỳ thi là một sự kiện diễn ra ➔ dùng trợ từ で:「だいがくで にほんごの テストが あります。」"
    )

    # Cặp 7: Lượng từ đếm vật mỏng phẳng: 〜まい
    add_pair("6", "1", P6_1,
        "Lượng từ「〜まい」trong tiếng Nhật dùng để đếm những đồ vật có đặc điểm như thế nào?",
        [
            "Đếm người và động vật nhỏ",
            "Đếm các vật mỏng, phẳng như vé xem phim, áo sơ mi, tờ giấy, đĩa CD",
            "Đếm các loại xe cộ và máy móc",
            "Đếm các vật dài hình trụ như cây bút, cái chai"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Lượng từ「〜まい」chuyên dùng để đếm các vật mỏng, phẳng: vé (チケット), áo sơ mi (シャツ), giấy (かみ), đĩa CD, ảnh (しゃしん)...",
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

    # Cặp 8: Số đếm kết hợp lượng từ 〜まい (1まい, 2まい...)
    add_pair("6", "1", P6_1,
        "Cách đọc số đếm lượng từ cho 1 tấm vé (1まい) và 3 chiếc áo sơ mi (3まい) trong tiếng Nhật là gì?",
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
            "きのう みせで シャツを 3まい かいまました。",
            "きのう みせで シャツを 3ほん かいまました。",
            "きのう みせで シャツを 3さつ かいまました。",
            "きのう みせで シャツを 3こ かいまました。"
        ],
        "A",
        "Áo sơ mi đếm bằng まい:「シャツを 3まい かいまました。」"
    )

    # Cặp 9: Rủ rê dựa trên số lượng có sẵn
    add_pair("6", "1", P6_1,
        "Khi bạn có sẵn 2 tấm vé xem phim và muốn rủ đối phương cùng đi xem, câu nói chuẩn ngữ pháp giao tiếp là gì?",
        [
            "チケットが ありますから、おかねを ください。",
            "えいがの チケットが 2まい あります。いっしょに いきませんか。",
            "チケットを かいまました。ひとりで いきます。",
            "チケットが ありません。いきましょう。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Nêu số lượng vé có sẵn [Danh từ] + が + [Số lượng] + あります kết hợp rủ rê「いっしょに いきませんか。」(Tôi có 2 tấm vé. Cùng đi với tôi không?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi có 2 tấm vé xem phim. Cùng đi xem với tôi không?\"",
        [
            "えいがの チケットが 2まい あります。いっしょに いきませんか。",
            "えいがの チケットが 2まい あります。いっしょに いきましょうか。",
            "えいがの チケットが 2まい あります。ひとりで いきます。",
            "えいがの チケットが 2まい あります。みたくないです。"
        ],
        "A",
        "Câu mời rủ chuẩn:「えいがの チケットが 2まい あります。いっしょに いきませんか。」"
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
        "💡 Chuẩn ngữ pháp: Cấu trúc: N1 は N2 より Adj です = \"N1 thì [Tính từ] hơn N2\" (Đối tượng đứng trước は là đối tượng có tính chất cao hơn). Ví dụ: しんかんせんは でんしゃより はやいです。",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tàu Shinkansen nhanh hơn tàu điện thông thường.\"",
        [
            "しんかんせんは でんしゃより はやいです。",
            "でんしゃは しんかんせんより はやいです。",
            "しんかんせんは でんしゃほど はやいです。",
            "しんかんせんのほうが でんしゃが はやいです。"
        ],
        "A",
        "N1 (Shinkansen) nhanh hơn N2 (tàu thường):「しんかんせんは でんしゃより はやいです。」"
    )

    # Cặp 11: So sánh hơn về tính chất: [Đối tượng 1] は [Đối tượng 2] より [Tính từ]
    add_pair("6", "2", P6_2,
        "Trong câu so sánh hơn「とうきょうは きょうとより にぎやかです。」, thành phố nào náo nhiệt hơn?",
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
            "きょうとは とうきょうより にぎやかです。",
            "とうきょうは きょうとより にぎやかです。",
            "とうきょうは きょうとと にぎやかです。",
            "とうきょうより きょうとのほうが にぎやかです。"
        ],
        "B",
        "Tokyo hơn Kyoto:「とうきょうは きょうとより にぎやかです。」"
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
        "Khi được hỏi:「えいごと にほんごと どちらが むずかしいですか。」, nếu bạn muốn trả lời là \"Tiếng Nhật khó hơn\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "にほんごの ほうが むずかしいです。",
            "えいごの ほうが むずかしいです。",
            "にほんごより むずかしいです。",
            "どちらも むずかしいです。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Khi trả lời câu hỏi lựa chọn và bạn chọn một phía hơn, mẫu câu chuẩn là: [Đối tượng] + の ほうが + [Tính từ] です ➔「にほんごの ほうが むずかしいです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tiếng Nhật và tiếng Anh, tiếng Nhật khó hơn.\"",
        [
            "にほんごの ほうが むずかしいです。",
            "えいごの ほうが むずかしいです。",
            "にほんごより むずかしいです。",
            "どちらも むずかしいです。"
        ],
        "A",
        "Chọn tiếng Nhật khó hơn:「にほんごの ほうが むずかしいです。」"
    )

    # Cặp 14: Trả lời cả hai đều như nhau: どちらも Adj です
    add_pair("6", "2", P6_2,
        "Khi được hỏi:「いぬと ねこと どちらが すきですか。」, nếu bạn muốn trả lời là \"Cả hai con tôi đều thích cả\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "いぬの ほうが すきです。",
            "どちらも すきです。",
            "どちらが すきです。",
            "どちらの ほうが すきです。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi cả hai đối tượng đều như nhau: dùng「どちらも + Tính từ」➔「どちらも すきです。」(Cả hai con tôi đều thích).",
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

    # Cặp 15: So sánh nhất trong một phạm vi: [Phạm vi] で N が いちばん Adj です
    add_pair("6", "2", P6_2,
        "Cấu trúc so sánh nhất trong một phạm vi / tập hợp theo chuẩn ngữ pháp là gì?",
        [
            "[Phạm vi] に N が いちばん Adj です。",
            "[Phạm vi] で N が いちばん Adj です。",
            "[Phạm vi] を N が いちばん Adj です。",
            "[Phạm vi] より N が いちばん Adj です。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cấu trúc so sánh nhất: [Phạm vi/Tập hợp] + で + [Danh từ] + が + いちばん + [Tính từ] + です (Trong phạm vi..., N là... nhất). Ví dụ: 1ねんで 7がつが いちばん あついです。",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Trong một năm, tháng 7 là nóng nhất.\"",
        [
            "1ねんで 7がつが いちばん あついです。",
            "1ねんに 7がつが いちばん あついです。",
            "1ねんより 7がつが いちばん あついです。",
            "1ねんのほうが 7がつが いちばん あついです。"
        ],
        "A",
        "Phạm vi thời gian dùng trợ từ で:「1ねんで 7がつが いちばん あついです。」"
    )

    # Cặp 16: Từ để hỏi về đồ vật trong so sánh nhất: なにが いちばん
    add_pair("6", "2", P6_2,
        "Khi được hỏi:「にほんりょうりで なにが いちばん すきですか。」, nếu bạn muốn trả lời là \"Tôi thích món sushi nhất\" thì câu trả lời chuẩn ngữ pháp là:",
        [
            "すしが いちばん すきです。",
            "すしは いちばん すきです。",
            "すしの ほうが すきです。",
            "すしより すきです。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trả lời so sánh nhất: [Đối tượng] + が + いちばん + [Tính từ] です ➔「すしが いちばん すきです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Trong các món ăn Nhật Bản, bạn thích món nào nhất?\"",
        [
            "にほんりょうりで だれが いちばん すきですか。",
            "にほんりょうりで なにが いちばん すきですか。",
            "にほんりょうりで どこが いちばん すきですか。",
            "にほんりょうりで いつが いちばん すきですか。"
        ],
        "B",
        "Hỏi về món ăn dùng なにが いちばん:「にほんりょうりで なにが いちばん すきですか。」"
    )

    # Cặp 17: Từ để hỏi về thời gian trong so sánh nhất: いつが いちばん
    add_pair("6", "2", P6_2,
        "Khi được hỏi:「にほんは いつが いちばん きれいですか。」, nếu bạn muốn trả lời là \"Mùa xuân là đẹp nhất\" thì câu nói chuẩn ngữ pháp là:",
        [
            "はるが いちばん きれいです。",
            "はるの ほうが きれいです。",
            "はるより きれいです。",
            "はるは どちらも きれいです。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trả lời câu hỏi so sánh nhất「いつが いちばん〜」: [Thời điểm] + が + いちばん + [Tính từ] です ➔「はるが いちばん きれいです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ở Nhật Bản, mùa nào (khi nào) là đẹp nhất?\"",
        [
            "にほんは どこが いちばん きれいですか。",
            "にほんは いつが いちばん きれいですか。",
            "にほんは だれが いちばん きれいですか。",
            "にほんは なにが いちばん きれいですか。"
        ],
        "B",
        "Hỏi về thời điểm dùng いつが いちばん:「にほんは いつが いちばん きれいですか。」"
    )

    # Cặp 18: Từ để hỏi về nơi chốn trong so sánh nhất: どこが いちばん
    add_pair("6", "2", P6_2,
        "Khi được hỏi:「おくにで どこが いちばん ゆうめいですか。」, nếu bạn muốn trả lời là \"Vịnh Hạ Long là nổi tiếng nhất\" thì câu trả lời chuẩn ngữ pháp là:",
        [
            "ハロンわんが いちばん ゆうめいです。",
            "ハロンわんの ほうが ゆうめいです。",
            "ハロンわんより ゆうめいです。",
            "ハロンわんは どちらも ゆうめいです。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trả lời so sánh nhất nơi chốn: [Địa danh] + が + いちばん + ゆうめいです ➔「ハロンわんが いちばん ゆうめいです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ở đất nước của bạn, nơi nào là nổi tiếng nhất?\"",
        [
            "おくにで どこが いちばん ゆうめいですか。",
            "おくにで いつが いちばん ゆうめいですか。",
            "おくにで なにが いちばん ゆうめいですか。",
            "おくにで だれが いちばん ゆうめいですか。"
        ],
        "A",
        "Hỏi địa điểm dùng どこが いちばん:「おくにで どこが いちばん ゆうめいですか。」"
    )

    # ==============================================================================
    # PHẦN 3: やくそく (9 cặp câu hỏi)
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
        "💡 Chuẩn ngữ pháp:「もう Vましたか」dùng để kiểm tra tiến độ xem hành động đã hoàn tất hay chưa: \"Bạn đã làm V chưa / rồi phải không?\". Ví dụ: もう しゅくだいを しましたか。",
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
        "Khi được hỏi:「もう ひるごはんを たべましたか。」, nếu bạn muốn trả lời khẳng định là \"Vâng, tôi đã ăn rồi\" thì câu nói chuẩn ngữ pháp là:",
        [
            "はい、まだ たべました。",
            "はい、もう たべました。",
            "いいえ、もう たべました。",
            "はい、これから たべました。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trả lời khẳng định cho「もう Vましたか」:「はい、もう Vました。」➔「はい、もう たべました。」(Vâng, tôi đã ăn rồi).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Vâng, tôi đã ăn cơm trưa rồi.\"",
        [
            "はい、まだ ひるごはんを たべました。",
            "はい、もう ひるごはんを たべました。",
            "いいえ、もう ひるごはんを たべました。",
            "はい、ひるごはんを たべたいです。"
        ],
        "B",
        "\"Vâng, tôi đã ăn rồi\":「はい、もう たべました。」"
    )

    # Cặp 21: Quy tắc bắt buộc khi trả lời phủ định: いいえ、まだです
    add_pair("6", "3", P6_3,
        "QUY TẮC BẮT BUỘC: Khi được hỏi「もう ひこうきの チケットを かいまましたか。」, nếu bạn muốn trả lời là \"Chưa, tôi vẫn chưa mua\" thì theo chuẩn ngữ pháp BẮT BUỘC phải nói như thế nào?",
        [
            "いいえ、かいませんでした (Sai ngữ pháp nghiêm trọng)",
            "いいえ、まだです。(Hoặc: いいえ、まだ かっていません)",
            "いいえ、もう かいません。",
            "いいえ、ぜんぜん かいまました。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Đối với câu hỏi「もう Vましたか」, nếu chưa làm thì BẮT BUỘC trả lời「いいえ、まだです」(Chưa, tôi chưa làm). Tuyệt đối KHÔNG trả lời「いいえ、Vませんでした」vì câu đó mang nghĩa là bạn đã không mua và từ chối không mua nữa.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bạn đã mua vé máy bay chưa?\" - \"Chưa, tôi vẫn chưa mua.\"",
        [
            "「もう ひこうきの チケットを かいまましたか。」「いいえ、かいませんでした。」",
            "「もう ひこうきの チケットを かいまましたか。」「いいえ、まだです。」",
            "「もう ひこうきの チケットを かいまましたか。」「はい、まだです。」",
            "「もう ひこうきの チケットを かいまましたか。」「いいえ、もう かいまました。」"
        ],
        "B",
        "Chưa làm phải trả lời:「いいえ、まだです。」(Chưa, tôi chưa làm)."
    )

    # Cặp 22: Gợi ý, đề xuất phương án: N は どうですか
    add_pair("6", "3", P6_3,
        "Khi cùng bạn bè bàn「なにを たべますか。」, nếu bạn muốn GỢI Ý ĐỀ XUẤT \"Món sushi thì sao / thế nào?\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
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
            "ひるごはんを たべませんか。すしは どうですか。",
            "ひるごはんを たべましょう。すしは どこですか。",
            "ひるごはんを たべましたか。すしは なんですか。",
            "ひるごはんを たべたいです。すしは だれですか。"
        ],
        "A",
        "Đưa ra gợi ý món ăn:「すしは どうですか。」(Món sushi thì sao?)."
    )

    # Cặp 23: Đề xuất địa điểm du lịch: N は どうですか
    add_pair("6", "3", P6_3,
        "Khi bàn bạc kế hoạch đi chơi「どこに りょこうしますか。」, nếu bạn muốn GỢI Ý \"Đi Kyoto thì thế nào?\" thì câu nói chuẩn ngữ pháp là:",
        [
            "きょうとは どうですか。",
            "きょうとは どこですか。",
            "きょうとは なんですか。",
            "きょうとは だれですか。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trong bối cảnh bàn kế hoạch du lịch, dùng「[Địa điểm] は どうですか」để gợi ý địa điểm:「きょうとは どうですか。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Sắp đến kỳ nghỉ rồi. Đi du lịch Kyoto thì thế nào?\"",
        [
            "もうすぐ やすみですね。きょうとは どうですか。",
            "もうすぐ やすみですね。きょうとは どこですか。",
            "もうすぐ やすみですね。きょうとは なんですか。",
            "もうすぐ やすみですね。きょうとは だれですか。"
        ],
        "A",
        "Gợi ý địa điểm du lịch:「きょうとは どうですか。」"
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
        "💡 Chuẩn ngữ pháp: Trợ từ「ね」dùng khi cả người nói và người nghe cùng nhìn thấy hoặc cùng chia sẻ một trải nghiệm chung (đồng cảm, đồng thuận):「とうきょうの せいかつは おもしろいですね。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cuộc sống ở Tokyo thật là thú vị và tiện lợi nhỉ!\"",
        [
            "とうきょうの せいかつは おもしろいですね。そして、べんりです。",
            "とうきょうの せいかつは おもしろいですよ。そして、べんりです。",
            "とうきょうの せいかつは おもしろいですか。そして、べんりです。",
            "とうきょうの せいかつは おもしろいでした。そして、べんりです。"
        ],
        "A",
        "Chia sẻ cảm xúc đồng cảm dùng trợ từ ね:「とうきょうの せいかつは おもしろいですね。」"
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
        "💡 Chuẩn ngữ pháp: Trợ từ「よ」dùng khi người nói muốn truyền đạt một thông tin mới mà đối phương chưa biết:「あのみせは おいしくて、やすいですよ。」(Quán kia đồ ăn ngon và rẻ lắm đấy nhé!).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Quán ăn kia đồ ăn ngon và rẻ lắm đấy nhé! (cho người chưa biết)\"",
        [
            "あのみせは おいしくて、やすいですね。",
            "あのみせは おいしくて、やすいですよ。",
            "あのみせは おいしくて、やすいですか。",
            "あのみせは おいしくて、やすいでした。"
        ],
        "B",
        "Cung cấp thông tin mới cho người nghe dùng trợ từ よ:「おいしくて、やすいですよ。」"
    )

    # Cặp 26: Tình huống phân biệt ね và よ trong thực tế
    add_pair("6", "3", P6_3,
        "Khi thấy đã muộn (12 giờ đêm) và bạn muốn NHẮC NHỞ bạn cùng phòng đi ngủ vì người đó chưa để ý giờ thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "もう 12じですね。ねましょう。",
            "もう 12じですよ。ねましょう。",
            "もう 12じですか。ねましょう。",
            "もう 12じでした。ねましょう。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Nhắc nhở người chưa để ý giờ (thông tin mới với người đó) ➔ BẮT BUỘC dùng trợ từ「よ」:「もう 12じですよ。ねましょう。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Đã 12 giờ đêm rồi đấy, đi ngủ thôi nào! (nhắc nhở người đang mải chơi chưa để ý giờ)\"",
        [
            "もう 12じですね。ねましょう。",
            "もう 12じですよ。ねましょう。",
            "もう 12じですか。ねましょう。",
            "もう 12じでした。ねましょう。"
        ],
        "B",
        "Nhắc nhở người chưa để ý giờ (thông tin mới với người đó) ➔ dùng trợ từ よ:「もう 12じですよ。ねましょう。」"
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
