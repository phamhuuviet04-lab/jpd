# -*- coding: utf-8 -*-
"""
Dữ liệu câu hỏi ngữ pháp Bài 5 - Dekiru Nihongo
Chia làm 2 dạng câu hỏi rõ ràng:
1. [HỎI NGỮ PHÁP]: Hỏi khái niệm, cấu trúc, quy tắc, cách trả lời theo chuẩn ngữ pháp
2. [DỊCH CÂU]: Dịch từ câu tiếng Việt sang tiếng Nhật tương ứng
"""

def register_lesson_5(add_pair):
    P5_1 = "しゅうまつ (Quá khứ Động từ, Đi đâu, と, それから)"
    P5_2 = "やすみのあとで (Quá khứ Tính từ, どうでしたか, Lý do 〜から)"
    P5_3 = "こんどのやすみに (ほしい, 〜たい, Mục đích di chuyển)"

    # ==============================================================================
    # PHẦN 1: しゅうまつ (9 cặp câu hỏi)
    # ==============================================================================

    # Cặp 1: Động từ quá khứ khẳng định Vました
    add_pair("5", "1", P5_1,
        "Để diễn đạt một hành động ĐÃ XẢY RA và kết thúc trong quá khứ, theo chuẩn ngữ pháp động từ tiếng Nhật đổi đuôi「ます」thành gì?",
        [
            "〜ません",
            "〜ました",
            "〜ませんでした",
            "〜ましょう"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Động từ thì quá khứ khẳng định: đổi đuôi「〜ます」thành「〜ました」(Ví dụ: べんきょうします ➔ べんきょうしました: đã học).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hôm qua tôi đã học tiếng Nhật ở thư viện.\"",
        [
            "きのう としょかんで にほんごを べんきょうします。",
            "きのう としょかんで にほんごを べんきょうしました。",
            "きのう としょかんに にほんごを べんきょうしませんでした。",
            "きのう としょかんで にほんごを べんきょうしたいです。"
        ],
        "B",
        "Hôm qua (quá khứ) ➔ động từ chia thì quá khứ:「きのう としょかんで にほんごを べんきょうしました。」"
    )

    # Cặp 2: Động từ quá khứ phủ định Vませんでした
    add_pair("5", "1", P5_1,
        "Để diễn đạt một hành động ĐÃ KHÔNG XẢY RA trong quá khứ, theo chuẩn ngữ pháp động từ tiếng Nhật đổi đuôi「ます」thành gì?",
        [
            "〜ません",
            "〜ました",
            "〜ませんでした",
            "〜ないでした"
        ],
        "C",
        "💡 Chuẩn ngữ pháp: Động từ thì quá khứ phủ định: đổi đuôi「〜ます」thành「〜ませんでした」(Ví dụ: はたらきます ➔ はたらきませんでした: đã không làm việc).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chủ nhật tuần trước tôi đã không làm việc.\"",
        [
            "せんしゅうの にちようび、はたらきません。",
            "せんしゅうの にちようび、はたらきませんでした。",
            "せんしゅうの にちようび、はたらきました。",
            "せんしゅうの にちようび、はたらきないでした。"
        ],
        "B",
        "Quá khứ phủ định (đã không làm):「せんしゅうの にちようび、はたらきませんでした。」"
    )

    # Cặp 3: Câu hỏi thì quá khứ Vましたか
    add_pair("5", "1", P5_1,
        "Khi được hỏi:「きのう なんじに ばんごはんを たべましたか。」, nếu bạn muốn trả lời là \"Hôm qua tôi đã ăn lúc 7 giờ\" thì câu nói chuẩn ngữ pháp là:",
        [
            "7じに たべます。",
            "7じに たべました。",
            "7じに たべたいです。",
            "7じに たべませんでした。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trả lời về hành động đã diễn ra trong quá khứ (ngày hôm qua) thì động từ phải chia đuôi「〜ました」➔「7じに たべました。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hôm qua bạn đã ăn tối lúc mấy giờ?\" - \"Tôi đã ăn lúc 7 giờ.\"",
        [
            "「きのう なんじに ばんごはんを たべましたか。」「7じに たべました。」",
            "「きのう なんじに ばんごはんを たべますか。」「7じに たべます。」",
            "「きのう なんじで ばんごはんを たべましたか。」「7じで たべました。」",
            "「きのう なんじに ばんごはんを たべたいですか。」「7じに たべたいです。」"
        ],
        "A",
        "Hỏi và trả lời hành động hôm qua:「きのう なんじに ばんごはんを たべましたか。」「7じに たべました。」"
    )

    # Cặp 4: Đại từ nghi vấn + か: どこか (đâu đó)
    add_pair("5", "1", P5_1,
        "Khi đối phương hỏi:「しゅうまつ、どこかへ いきましたか。」(Cuối tuần bạn có đi đâu đó không?), nếu bạn muốn trả lời là \"Có, tôi đã đi biển\" thì câu nói chuẩn ngữ pháp là:",
        [
            "はい、うみへ いきます。",
            "はい、うみへ いきました。",
            "いいえ、うみへ いきました。",
            "はい、どこも いきませんでした。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi được hỏi có đi đâu đó (どこかへ) không và bạn có đi, trả lời:「はい、[Địa điểm] へ いきました。」➔「はい、うみへ いきました。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cuối tuần trước bạn có đi đâu đó không?\" - \"Có, tôi đã đi biển.\"",
        [
            "「しゅうまつ、どこへ いきましたか。」「はい、うみへ いきました。」",
            "「しゅうまつ、どこかへ いきましたか。」「はい、うみへ いきました。」",
            "「しゅうまつ、どこも いきましたか。」「はい、うみへ いきました。」",
            "「しゅうまつ、どこかへ いきましたか。」「いいえ、うみへ いきました。」"
        ],
        "B",
        "Đi \"đâu đó\" dùng どこか (hoặc どこかへ):「しゅうまつ、どこかへ いきましたか。」「はい、うみへ いきました。」"
    )

    # Cặp 5: Phủ định hoàn toàn: どこも + Động từ phủ định
    add_pair("5", "1", P5_1,
        "Khi được hỏi:「しゅうまつ、どこかへ いきましたか。」, nếu bạn muốn trả lời là \"Tôi ở nhà, không đi đâu cả\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "うちに いました。どこかへ いきませんでした。",
            "うちに いました。どこも いきませんでした。",
            "うちに いました。どこでも いきませんでした。",
            "うちに いました。どこへ いきませんでした。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Phủ định hoàn toàn nơi chốn: Từ để hỏi どこ + trợ từ も + Động từ phủ định ➔「どこも いきませんでした。」(hoặc どこへも いきませんでした).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chủ nhật tôi đã ở nhà, không đi đâu cả.\"",
        [
            "にちようび、うちに いました。どこかへ いきませんでした。",
            "にちようび、うちに いました。どこも いきませんでした。",
            "にちようび、うちに いました。どこへ いきませんでした。",
            "にちようび、うちに いました。どこでも いきました。"
        ],
        "B",
        "\"Không đi đâu cả\" là:「どこも いきませんでした。」(hoặc どこへも いきませんでした)."
    )

    # Cặp 6: Phủ định hoàn toàn với đồ vật: なにも + Phủ định
    add_pair("5", "1", P5_1,
        "Khi được hỏi:「あさごはんを たべましたか。」, nếu bạn muốn trả lời là \"Vì bận nên tôi đã không ăn gì cả\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "いそがしかったですから、なにか たべませんでした。",
            "いそがしかったですから、なにも たべませんでした。",
            "いそがしいですから、なんでも たべませんでした。",
            "いそがしかったですから、なにも たべました。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Phủ định hoàn toàn đồ vật: なに + も + Động từ phủ định:「なにも たべませんでした。」(đã không ăn gì cả). Lý do quá khứ:「いそがしかったですから」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Sáng nay vì bận nên tôi đã không ăn gì cả.\"",
        [
            "けさ いそがしいですから、なにか たべませんでした。",
            "けさ いそがしかったですから、なにも たべませんでした。",
            "けさ いそがしいでしたから、なにも たべました。",
            "けさ いそがしくて、なんでも たべませんでした。"
        ],
        "B",
        "\"Hoàn toàn không ăn gì\":「なにも たべませんでした。」; lý do quá khứ: いそがしかったですから."
    )

    # Cặp 7: Làm cùng với ai: N(người) + と + V
    add_pair("5", "1", P5_1,
        "Khi được hỏi:「だれと ばんごはんを たべましたか。」, nếu bạn muốn trả lời là \"Tối qua tôi đã ăn cơm cùng với gia đình\" thì câu nói chuẩn ngữ pháp là:",
        [
            "かぞくに ごはんを たべました。",
            "かぞくで ごはんを たべました。",
            "かぞくと ごはんを たべました。",
            "かぞくを ごはんを たべました。"
        ],
        "C",
        "💡 Chuẩn ngữ pháp: Làm cùng ai thì dùng trợ từ と đi sau danh từ chỉ người: [Người] + と + Động từ ➔「かぞくと ごはんを たべました。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tối qua tôi đã ăn cơm cùng với gia đình.\"",
        [
            "きのうの ばん、かぞくに ごはんを たべました。",
            "きのうの ばん、かぞくで ごはんを たべました。",
            "きのうの ばん、かぞくと ごはんを たべました。",
            "きのうの ばん、かぞくを ごはんを たべました。"
        ],
        "C",
        "Cùng với gia đình dùng trợ từ と:「かぞくと ごはんを たべました。」"
    )

    # Cặp 8: Làm một mình: ひとりで
    add_pair("5", "1", P5_1,
        "Khi được hỏi:「だれと えいがをみに いきましたか。」, nếu bạn muốn trả lời là \"Tôi đã đi xem một mình\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "ひとりと みに いきました。",
            "ひとりで みに いきました。",
            "ひとりに みに いきました。",
            "ひとりを みに いきました。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Diễn đạt hành động làm \"một mình\": dùng cụm「ひとりで」, TUYỆT ĐỐI không dùng trợ từ と hay で thêm vào (không nói ひとりと) ➔「ひとりで みに いきました。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cuối tuần tôi đã đi xem phim một mình.\"",
        [
            "しゅうまつ、ひとりと えいがを みました。",
            "しゅうまつ、ひとりで えいがを みました。",
            "しゅうまつ、ひとりに えいがを みました。",
            "しゅうまつ、ひとりの えいがを みました。"
        ],
        "B",
        "\"Một mình\" là「ひとりで」:「ひとりで えいがを みました。」"
    )

    # Cặp 9: Liên từ nối tuần tự: それから (sau đó)
    add_pair("5", "1", P5_1,
        "Liên từ「それから、」(sau đó, tiếp theo) dùng để làm gì trong câu?",
        [
            "Giải thích nguyên nhân của hành động trước",
            "Nối các hành động diễn ra theo trình tự thời gian (hành động 1, sau đó là hành động 2)",
            "Biểu thị sự đối lập tương phản giữa hai câu",
            "Đặt điều kiện giả định"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「それから」dùng để nối tiếp các hành động tuần tự theo trình tự thời gian: làm A, sau đó / rồi thì làm B:「スーパーで かいものしました。それから、ともだちと りょうりしました。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hôm qua tôi đã đi mua sắm ở siêu thị, sau đó đã nấu ăn cùng bạn.\"",
        [
            "きのう スーパーで かいものしました。そして、ともだちと りょうりしました。",
            "きのう スーパーで かいものしました。それから、ともだちと りょうりしました。",
            "きのう スーパーで かいものしました。ですから、ともだちと りょうりしました。",
            "きのう スーパーで かいものしました。ですが、ともだちと りょうりしました。"
        ],
        "B",
        "Hành động tuần tự theo thời gian:「それから、ともだちと りょうりしました。」"
    )

    # ==============================================================================
    # PHẦN 2: やすみのあとで (9 cặp câu hỏi)
    # ==============================================================================

    # Cặp 10: Tính từ đuôi い quá khứ khẳng định: 〜かったです
    add_pair("5", "2", P5_2,
        "Quy tắc chia TÍNH TỪ ĐUÔI い sang thì QUÁ KHỨ KHẲNG ĐỊNH (đã...) là gì?",
        [
            "Bỏ đuôi い và thêm でした",
            "Bỏ đuôi い và thêm かったです",
            "Giữ nguyên đuôi い và thêm でした",
            "Đổi đuôi い thành かったでした"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ đuôi い thì quá khứ khẳng định: Bỏ「い」➔ thêm「かったです」(Ví dụ: たのしい ➔ たのしかったです: đã rất vui).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chuyến du lịch tuần trước đã rất vui.\"",
        [
            "せんしゅうの りょこうは とても たのしいでした。",
            "せんしゅうの りょこうは とても たのしかったです。",
            "せんしゅうの りょこうは とても たのしかったでした。",
            "せんしゅうの りょこうは とても たのしくないです。"
        ],
        "B",
        "Tính từ たのしい (vui) chuyển sang quá khứ là たのしかったです:「とても たのしかったです。」"
    )

    # Cặp 11: Tính từ đuôi い quá khứ phủ định: 〜くなかったです
    add_pair("5", "2", P5_2,
        "Khi được hỏi:「きのうのホテルは たかかったですか。」, nếu bạn muốn trả lời là \"Khách sạn hôm qua đã không đắt lắm\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "あまり たかいじゃなかったです。",
            "あまり たかくなかったです。",
            "あまり たかくないでした。",
            "あまり たかいでした。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ đuôi い thì quá khứ phủ định: Bỏ「い」➔ thêm「くなかったです」➔ たかい thành「たかくなかったです」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Khách sạn hôm qua đã không đắt lắm.\"",
        [
            "きのうの ホテルは あまり たかいじゃなかったです。",
            "きのうの ホテルは あまり たかくなかったです。",
            "きのうの ホテルは あまり たかくないでした。",
            "きのうの ホテルは あまり たかいでした。"
        ],
        "B",
        "Quá khứ phủ định của tính từ đuôi い: たかい ➔ たかくなかったです:「あまり たかくなかったです。」"
    )

    # Cặp 12: Ngoại lệ quá khứ của いい ➔ よかった
    add_pair("5", "2", P5_2,
        "Khi được hỏi:「きのうのりょこうのてんきはどうでしたか。」, nếu bạn muốn trả lời là \"Thời tiết hôm qua đã rất đẹp\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "とても いかったです。",
            "とても よかったです。",
            "とても いいでした。",
            "とても よいでした。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ「いい」có gốc là「よい」➔ Quá khứ khẳng định BẮT BUỘC là「よかったです」(TUYỆT ĐỐI không nói いかったです hay いいでした).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Thời tiết ngày hôm qua đã rất đẹp.\"",
        [
            "きのうの てんきは とても いかったです。",
            "きのうの てんきは とても よかったです。",
            "きのうの てんきは とても いいでした。",
            "きのうの てんきは とても よいでした。"
        ],
        "B",
        "Quá khứ của いい là よかったです:「きのうの てんきは とても よかったです。」"
    )

    # Cặp 13: Tính từ đuôi な quá khứ khẳng định: 〜でした
    add_pair("5", "2", P5_2,
        "Quy tắc chia TÍNH TỪ ĐUÔI な (hoặc Danh từ) sang thì QUÁ KHỨ KHẲNG ĐỊNH (đã...) là gì?",
        [
            "Bỏ な và thêm かったです",
            "Bỏ な và thêm でした",
            "Giữ nguyên な và thêm でした",
            "Bỏ な và thêm かったでした"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ đuôi な và Danh từ thì quá khứ khẳng định: Bỏ「な」➔ thêm「でした」(Ví dụ: にぎやか ➔ にぎやかでした: đã rất náo nhiệt).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bữa tiệc tối hôm qua đã rất náo nhiệt.\"",
        [
            "きのうの パーティーは とても にぎやかかったです。",
            "きのうの パーティーは とても にぎやかでした。",
            "きのうの パーティーは とても にぎやかなでした。",
            "きのうの パーティーは とても にぎやかかったでした。"
        ],
        "B",
        "にぎやか là tính từ đuôi な, quá khứ khẳng định là:「とても にぎやかでした。」"
    )

    # Cặp 14: Tính từ đuôi な quá khứ phủ định: 〜じゃなかったです
    add_pair("5", "2", P5_2,
        "Khi được hỏi:「まえの アパートは べんりでしたか。」, nếu bạn muốn trả lời là \"Phòng trọ trước đây đã không tiện lợi\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "いいえ、べんりくなかったです。",
            "いいえ、べんりじゃなかったです。",
            "いいえ、べんりないでした。",
            "いいえ、べんりでした。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ đuôi な thì quá khứ phủ định: Bỏ「な」➔ thêm「じゃなかったです」(hoặc「ではありませんでした」) ➔「べんりじゃなかったです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Phòng trọ trước đây của tôi đã không tiện lợi.\"",
        [
            "まえの アパートは べんりくなかったです。",
            "まえの アパートは べんりじゃなかったです。",
            "まえの アパートは べんりないでした。",
            "まえの アパートは べんりでした。"
        ],
        "B",
        "べんり là tính từ đuôi な, quá khứ phủ định là:「べんりじゃなかったです。」"
    )

    # Cặp 15: Hỏi cảm nhận sự kiện quá khứ: 〜は どうでしたか
    add_pair("5", "2", P5_2,
        "Khi được hỏi:「しゅうまつの りょこうは どうでしたか。」, nếu bạn muốn trả lời là \"Đã rất tuyệt vời / rất vui\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "とても いいです。",
            "とても よかったです。",
            "とても よいでした。",
            "とても いいでした。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Hỏi về trải nghiệm quá khứ「どうでしたか」➔ Trả lời dùng tính từ thì quá khứ:「とても よかったです。」(hoặc とても たのしかったです).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Kỳ nghỉ cuối tuần của bạn đã như thế nào?\" - \"Đã rất tuyệt vời.\"",
        [
            "「しゅうまつは どうですか。」「とても よかったです。」",
            "「しゅうまつは どうでしたか。」「とても よかったです。」",
            "「しゅうまつは どこでしたか。」「とても よかったです。」",
            "「しゅうまつは なんでしたか。」「とても よかったです。」"
        ],
        "B",
        "Hỏi kỳ nghỉ đã qua dùng thì quá khứ:「しゅうまつは どうでしたか。」, trả lời:「とても よかったです。」"
    )

    # Cặp 16: Giải thích lý do, nguyên nhân: 〜から (vì...)
    add_pair("5", "2", P5_2,
        "Trong tiếng Nhật, từ「〜から」đứng ở cuối một mệnh đề dùng để diễn đạt điều gì?",
        [
            "Biểu thị điểm xuất phát thời gian",
            "Biểu thị nguyên nhân, lý do (Vì... nên...)",
            "Biểu thị sự đối lập tương phản",
            "Biểu thị hành động tiếp theo"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Mệnh đề 1 + から, Mệnh đề 2: biểu thị \"Vì mệnh đề 1 nên dẫn đến kết quả mệnh đề 2\" (Ví dụ: かぜでしたから、かいしゃを やすみました: vì bị cảm nên nghỉ làm).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Vì hôm qua bị cảm sốt nên tôi đã nghỉ làm.\"",
        [
            "きのう かぜでしたから、かいしゃを やすみました。",
            "きのう かぜでしたそして、かいしゃを やすみました。",
            "きのう かぜでしたが、かいしゃを やすみました。",
            "きのう かぜですから、かいしゃを やすみます。"
        ],
        "A",
        "Nêu lý do quá khứ「かぜでしたから」+ kết quả「かいしゃを やすみました」."
    )

    # Cặp 17: Trả lời câu hỏi tại sao: どうしてですか ➔ 〜から です
    add_pair("5", "2", P5_2,
        "Khi đối phương hỏi:「どうしてきのう きませんでしたか。」, nếu bạn muốn trả lời là \"Vì hôm qua tôi có việc bận\" thì theo chuẩn ngữ pháp câu trả lời kết thúc bằng đuôi nào?",
        [
            "ようじが ありましたから です。",
            "ようじが ありましたですが。",
            "ようじが ありましたそして です。",
            "ようじが ありましたまで です。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Khi trả lời câu hỏi lý do「どうして〜」, câu trả lời giải thích lý do kết thúc bằng: [Lý do] + から です (hoặc ngắn gọn là 〜から) ➔「ようじがありましたから です。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tại sao hôm qua bạn không đến?\" - \"Vì hôm qua tôi có việc bận.\"",
        [
            "「どうして きのう きませんでしたか。」「ようじが ありましたから です。」",
            "「どうして きのう きませんでしたか。」「ようじが ありましたですが。」",
            "「どうして きのう きませんでしたか。」「ようじが ありますから。」",
            "「どこで きのう きませんでしたか。」「ようじが ありましたから です。」"
        ],
        "A",
        "Hỏi lý do:「どうして〜」; Trả lời lý do kết thúc bằng:「〜から です。」"
    )

    # Cặp 18: Kết hợp tính từ quá khứ và lý do: 〜かったですから
    add_pair("5", "2", P5_2,
        "Khi giải thích lý do bằng một tính từ đuôi い ở thì quá khứ (Ví dụ: \"Vì ngày hôm qua rất bận nên...\"), theo chuẩn ngữ pháp ta kết hợp như thế nào?",
        [
            "Tính từ đuôi い + から (Ví dụ: いそがしいから)",
            "Tính từ đuôi い bỏ い thêm かったですから (Ví dụ: いそがしかったですから)",
            "Tính từ đuôi い thêm でしたから (Ví dụ: いそがしいでしたから)",
            "Tính từ đuôi い bỏ い thêm くないですから"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Tính từ đuôi い quá khứ là「〜かったです」. Khi gắn thêm「から」để chỉ lý do trong quá khứ ➔「〜かったですから」(Ví dụ: いそがしかったですから、えいがを みませんでした).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Vì ngày hôm qua rất bận nên tôi đã không thể xem phim.\"",
        [
            "きのうは とても いそがしいですから、えいがを みませんでした。",
            "きのうは とても いそがしかったですから、えいがを みませんでした。",
            "きのうは とても いそがしいでしたから、えいがを みませんでした。",
            "きのうは とても いそがしくないですから、えいがを みませんでした。"
        ],
        "B",
        "Lý do tính từ quá khứ:「いそがしかったですから、えいがを みませんでした。」"
    )

    # ==============================================================================
    # PHẦN 3: こんどのやすみに (9 cặp câu hỏi)
    # ==============================================================================

    # Cặp 19: Muốn có cái gì (danh từ): N が ほしいです
    add_pair("5", "3", P5_3,
        "Mẫu câu「N が ほしいです。」dùng để biểu đạt điều gì và đi với trợ từ nào?",
        [
            "Mong muốn sở hữu một danh từ/đồ vật, đi với trợ từ が",
            "Mong muốn làm một hành động, đi với trợ từ を",
            "Yêu cầu người khác đưa đồ vật cho mình, đi với trợ từ に",
            "Khen ngợi một đồ vật đẹp, đi với trợ từ は"
        ],
        "A",
        "💡 Chuẩn ngữ pháp:「N が ほしいです」dùng để diễn đạt mong muốn sở hữu một danh từ (đồ vật, tiền bạc, người yêu...). Danh từ đi với trợ từ が ➔「あたらしい スマートフォンが ほしいです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bây giờ tôi muốn có một chiếc điện thoại thông minh mới.\"",
        [
            "いま あたらしい スマートフォンを ほしいです。",
            "いま あたらしい スマートフォンが ほしいです。",
            "いま あたらしい スマートフォンに ほしいです。",
            "いま あたらしい スマートフォンで ほしいです。"
        ],
        "B",
        "Muốn có danh từ đi với trợ từ が:「あたらしい スマートフォンが ほしいです。」"
    )

    # Cặp 20: Phủ định không muốn có: N は ほしくないです
    add_pair("5", "3", P5_3,
        "Khi được hỏi:「くるまが ほしいですか。」, nếu bạn muốn trả lời là \"Bây giờ tôi không muốn có ô tô\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "くるまは ほしいじゃないです。",
            "くるまは ほしくないです。",
            "くるまは ほしいくないです。",
            "くるまは ほしくありませんでした。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「ほしい」chia như tính từ đuôi い ➔ Thể phủ định \"không muốn có\" bỏ đuôi「い」thêm「くないです」➔「くるまは ほしくないです。」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bây giờ tôi không muốn có ô tô.\"",
        [
            "いま くるまは ほしいじゃないです。",
            "いま くるまは ほしくないです。",
            "いま くるまは ほしいくないです。",
            "いま くるまは ほしくありませんでした。"
        ],
        "B",
        "Không muốn có là:「くるまは ほしくないです。」(thường dùng trợ từ は thay cho が khi nhấn mạnh phủ định)."
    )

    # Cặp 21: Muốn làm hành động gì: V(bỏ ます) + たいです
    add_pair("5", "3", P5_3,
        "Để bày tỏ mong muốn, nguyện vọng làm một hành động nào đó của bản thân, theo chuẩn ngữ pháp ta đổi động từ đuôi「ます」thành gì?",
        [
            "V(bỏ ます) + たいです",
            "V(bỏ ます) + ほしいです",
            "V(nguyên thể) + たいです",
            "V(bỏ ます) + ますたい"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Muốn làm hành động V: Bỏ đuôi「ます」➔ thêm「たいです」(Ví dụ: りょこうします ➔ りょこうしたいです: muốn đi du lịch).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Kỳ nghỉ hè tới tôi muốn đi du lịch Nhật Bản.\"",
        [
            "こんどの なつやすみに にほんへ りょこうしたいです。",
            "こんどの なつやすみに にほんへ りょこうほしいです。",
            "こんどの なつやすみに にほんへ りょこうするたいです。",
            "こんどの なつやすみに にほんへ りょこうしたかったです。"
        ],
        "A",
        "Động từ りょこうします bỏ ます thêm たいです:「にほんへ りょこうしたいです。」"
    )

    # Cặp 22: Phủ định không muốn làm: V(bỏ ます) + たくないです
    add_pair("5", "3", P5_3,
        "Khi bạn bè hỏi:「なにか たべますか。」, nếu bạn muốn trả lời là \"Hôm nay tôi mệt nên không muốn ăn gì cả\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "きょうは つかれましたから、なにも たべたいじゃないです。",
            "きょうは つかれましたから、なにも たべたくないです。",
            "きょうは つかれましたから、なにか たべたくないです。",
            "きょうは つかれましたから、なんでも たべたいです。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Không muốn làm V: V(bỏ ます) + たくないです. Hoàn toàn không muốn ăn gì:「なにも たべたくないです。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hôm nay tôi mệt nên không muốn ăn gì cả.\"",
        [
            "きょうは つかれましたから、なにも たべたいじゃないです。",
            "きょうは つかれましたから、なにも たべたくないです。",
            "きょうは つかれましたから、なにか たべたくないです。",
            "きょうは つかれましたから、なんでも たべたいです。"
        ],
        "B",
        "Không muốn ăn gì cả:「なにも たべたくないです。」"
    )

    # Cặp 23: Quá khứ muốn làm: V(bỏ ます) + たかったです
    add_pair("5", "3", P5_3,
        "Khi muốn nói về một nguyện vọng trong quá khứ (\"đã từng rất muốn làm...\"), theo chuẩn ngữ pháp ta chia đuôi như thế nào?",
        [
            "V(bỏ ます) + たいでした",
            "V(bỏ ます) + たかったです",
            "V(bỏ ます) + ましたい",
            "V(bỏ ます) + たかったでした"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Thể quá khứ của たい: Bỏ「い」thêm「かったです」➔「Vたかったです」(Ví dụ: いきたかったです: đã muốn đi).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tuần trước tôi đã rất muốn đi xem hòa nhạc.\"",
        [
            "せんしゅう コンサートへ いきたいでした。",
            "せんしゅう コンサートへ いきたかったです。",
            "せんしゅう コンサートへ いきまましたい。",
            "せんしゅう コンサートへ いきたかったでした。"
        ],
        "B",
        "Quá khứ muốn đi là いきたかったです:「せんしゅう コンサートへ いきたかったです。」"
    )

    # Cặp 24: Hỏi mong muốn người khác: なにが / どこへ + たいですか
    add_pair("5", "3", P5_3,
        "Khi được hỏi:「こんどの やすみに どこへ いきたいですか。」, nếu bạn muốn trả lời là \"Tôi muốn đi Hokkaido\" thì câu nói chuẩn ngữ pháp là:",
        [
            "ほっかいどうへ いきたいです。",
            "ほっかいどうへ いきほしいです。",
            "ほっかいどうへ いきます。",
            "ほっかいどうへ いくたいです。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Trả lời về nơi mình muốn đi: [Địa điểm] + へ + いきたいです ➔「ほっかいどうへ いきたいです。」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Kỳ nghỉ tới bạn muốn đi đâu?\" - \"Tôi muốn đi Hokkaido.\"",
        [
            "「こんどの やすみに どこへ いきたいですか。」「ほっかいどうへ いきたいです。」",
            "「こんどの やすみに どこへ いきほしいですか。」「ほっかいどうへ いきほしいです。」",
            "「こんどの やすみに どこへ いきますか。」「ほっかいどうへ いきます。」",
            "「こんどの やすみに どこへ いくたいですか。」「ほっかいどうへ いくたいです。」"
        ],
        "A",
        "Hỏi muốn đi đâu:「どこへ いきたいですか。」, trả lời:「ほっかいどうへ いきたいです。」"
    )

    # Cặp 25: Đi đến đâu để làm gì: Địa điểm へ V(bỏ ます) に いきます
    add_pair("5", "3", P5_3,
        "Cấu trúc「[Địa điểm] へ [V bỏ ます] に いきます。」dùng để diễn đạt điều gì và trợ từ chỉ mục đích là gì?",
        [
            "Đi đến đâu để thực hiện một mục đích nào đó; trợ từ chỉ mục đích là に",
            "Đi đến đâu bằng phương tiện gì; trợ từ chỉ phương tiện là で",
            "Đi cùng với ai; trợ từ là と",
            "Thời gian bắt đầu đi; trợ từ là から"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Biểu thị mục đích di chuyển: [Địa điểm] へ + [V bỏ ます] + に + [いきます / きます / かえります] (Ví dụ: ふくを かいに いきます: đi mua quần áo).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi đi đến trung tâm thương mại để mua sắm quần áo.\"",
        [
            "デパートへ ふくを かいで いきます。",
            "デパートへ ふくを かいに いきます。",
            "デパートへ ふくを かうに いきます。",
            "デパートへ ふくを かいを いきます。"
        ],
        "B",
        "Động từ かいます bỏ ます thêm に:「デパートへ ふくを かいに いきます。」"
    )

    # Cặp 26: Đi đến đâu với mục đích là Danh từ: Địa điểm へ N に いきます
    add_pair("5", "3", P5_3,
        "Khi mục đích di chuyển là một danh từ chỉ hành động (ngắm hoa おはなみ, du lịch りょこう, trượt tuyết スキー), theo chuẩn ngữ pháp ta nối danh từ với trợ từ nào?",
        [
            "Danh từ + で + いきます",
            "Danh từ + に + いきます",
            "Danh từ + を + いきます",
            "Danh từ + へ + いきます"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Nếu mục đích là danh từ chỉ hành động/sự kiện: [Danh từ] + に + いきます (Ví dụ: おはなみに いきます: đi ngắm hoa).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chủ nhật tôi sẽ đi đến công viên để ngắm hoa anh đào (おはなみ).\"",
        [
            "にちようび、こうえんへ おはなみで いきます。",
            "にちようび、こうえんへ おはなみに いきます。",
            "にちようび、こうえんへ おはなみを いきます。",
            "にちようび、こうえんへ おはなみへ いきます。"
        ],
        "B",
        "Mục đích danh từ + に いきます:「こうえんへ おはなみに いきます。」"
    )

    # Cặp 27: Hỏi mục đích di chuyển: なにしに いきますか
    add_pair("5", "3", P5_3,
        "Khi được hỏi:「にほんへ なにをしに きましたか。」, nếu bạn muốn trả lời là \"Tôi đến để học kinh tế\" thì theo chuẩn ngữ pháp phải nói như thế nào?",
        [
            "けいざいを べんきょうしに きました。",
            "けいざいを べんきょうで きました。",
            "けいざいを べんきょうに きます。",
            "けいざいを べんきょうを きました。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Mục đích động từ: V(bỏ ます) + に きました ➔ べんきょうします bỏ ます thành べんきょうし ➔「けいざいを べんきょうしに きました。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bạn đến Nhật Bản để làm gì?\" - \"Tôi đến để học kinh tế.\"",
        [
            "「にほんへ なにしに きましたか。」「けいざいを べんきょうしに きました。」",
            "「にほんへ なにで きましたか。」「けいざいを べんきょうしに きました。」",
            "「にほんへ どこに きましたか。」「けいざいを べんきょうしに きました。」",
            "「にほんへ いつ きましたか。」「けいざいを べんきょうしに きました。」"
        ],
        "A",
        "Hỏi mục đích đến:「にほんへ なにしに きましたか。」, trả lời:「けいざいを べんきょうしに きました。」"
    )
