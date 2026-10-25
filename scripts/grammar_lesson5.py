# -*- coding: utf-8 -*-
"""
Dữ liệu câu hỏi ngữ pháp Bài 5 - Dekiru Nihongo
Chia làm 2 dạng câu hỏi rõ ràng:
1. [HỎI NGỮ PHÁP]: Hỏi khái niệm, cấu trúc, quy tắc, ý nghĩa ngữ pháp
2. [DỊCH CÂU]: Dịch từ câu tiếng Việt sang tiếng Nhật tương ứng
"""

def register_lesson_5(add_pair):
    P5_1 = "週末 (Quá khứ Động từ, Đi đâu, と, それから)"
    P5_2 = "休みの後で (Quá khứ Tính từ, どうでしたか, Lý do 〜から)"
    P5_3 = "今度の休みに (ほしい, 〜たい, Mục đích di chuyển)"

    # ==============================================================================
    # PHẦN 1: 週末 (9 cặp câu hỏi)
    # ==============================================================================

    # Cặp 1: Động từ quá khứ khẳng định Vました
    add_pair("5", "1", P5_1,
        "Để diễn đạt một hành động ĐÃ XẢY RA và kết thúc trong quá khứ, động từ tiếng Nhật đổi đuôi「ます」thành gì?",
        [
            "〜ません",
            "〜ました",
            "〜ませんでした",
            "〜ましょう"
        ],
        "B",
        "Động từ thì quá khứ khẳng định: đổi đuôi「〜ます」thành「〜ました」(Ví dụ: たべます ➔ たべました, べんきょうします ➔ べんきょうしました).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hôm qua tôi đã học tiếng Nhật ở thư viện.\"",
        [
            "きのう としょかんで 日本語を 勉強します。",
            "きのう としょかんで 日本語を 勉強しました。",
            "きのう としょかんに 日本語を 勉強しませんでした。",
            "きのう としょかんで 日本語を 勉強したいです。"
        ],
        "B",
        "Hôm qua (quá khứ) ➔ động từ chia thì quá khứ:「きのう としょかんで 日本語を 勉強しました。」"
    )

    # Cặp 2: Động từ quá khứ phủ định Vませんでした
    add_pair("5", "1", P5_1,
        "Để diễn đạt một hành động ĐÃ KHÔNG XẢY RA trong quá khứ, động từ tiếng Nhật đổi đuôi「ます」thành gì?",
        [
            "〜ません",
            "〜ました",
            "〜ませんでした",
            "〜ないでした"
        ],
        "C",
        "Động từ thì quá khứ phủ định: đổi đuôi「〜ます」thành「〜ませんでした」(Ví dụ: いきません ➔ いきませんでした: đã không đi).",
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
        "Cấu trúc câu hỏi thì quá khứ「Vましたか。」dùng để làm gì?",
        [
            "Hỏi ai đó có kế hoạch làm việc gì trong tương lai không",
            "Hỏi ai đó đã thực hiện hành động nào đó trong quá khứ chưa / phải không",
            "Rủ ai đó cùng làm việc gì với mình",
            "Hỏi xin phép đối phương cho mình làm việc gì"
        ],
        "B",
        "「Vましたか。」dùng để hỏi về hành động trong quá khứ: \"Bạn đã làm... phải không / đã làm... chưa?\".",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hôm qua bạn đã ăn tối lúc mấy giờ?\"",
        [
            "きのう なんじに ばんごはんを 食べますか。",
            "きのう なんじに ばんごはんを 食べましたか。",
            "きのう なんじで ばんごはんを 食べましたか。",
            "きのう なんじを ばんごはんを 食べませんでしたか。"
        ],
        "B",
        "Hỏi hành động hôm qua:「きのう なんじに ばんごはんを 食べましたか。」"
    )

    # Cặp 4: Đại từ nghi vấn + か: どこか (đâu đó)
    add_pair("5", "1", P5_1,
        "Khi thêm「か」vào sau từ để hỏi nơi chốn「どこ」thành「どこか」, nó mang ý nghĩa ngữ pháp gì?",
        [
            "Hỏi chính xác địa điểm cụ thể nào đó",
            "Trở thành từ phiếm định có nghĩa là \"đâu đó / một nơi nào đó\" (không xác định cụ thể)",
            "Nghĩa là hoàn toàn không đi nơi nào cả",
            "Nghĩa là tất cả mọi nơi"
        ],
        "B",
        "Từ để hỏi + か biểu thị ý nghĩa không xác định (phiếm định): どこか (đâu đó), なにか (cái gì đó), だれか (ai đó), いつか (lúc nào đó).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cuối tuần trước bạn có đi đâu đó không?\"",
        [
            "せんしゅうの しゅうまつ、どこへ 行きましたか。",
            "せんしゅうの しゅうまつ、どこかへ 行きましたか。",
            "せんしゅうの しゅうまつ、どこも 行きましたか。",
            "せんしゅうの しゅうまつ、どこでも 行きましたか。"
        ],
        "B",
        "Đi \"đâu đó\" dùng どこか (hoặc どこかへ):「しゅうまつ、どこか(へ) 行きましたか。」"
    )

    # Cặp 5: Phủ định hoàn toàn: どこも + Động từ phủ định
    add_pair("5", "1", P5_1,
        "Cấu trúc「どこも + Động từ quá khứ phủ định (Vませんでした)」mang ý nghĩa ngữ pháp gì?",
        [
            "Đã đi đến rất nhiều nơi",
            "Phủ định hoàn toàn: \"Đã không đi đâu cả / chẳng đi đâu\"",
            "Đã đi đến một nơi nào đó",
            "Không biết phải đi đâu"
        ],
        "B",
        "Từ để hỏi + も + Thể phủ định biểu thị phủ định hoàn toàn: どこも いきませんでした (hoàn toàn không đi đâu cả).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chủ nhật tôi đã ở nhà, không đi đâu cả.\"",
        [
            "日曜日、うちに いました。どこかへ 行きませんでした。",
            "日曜日、うちに いました。どこも 行きませんでした。",
            "日曜日、うちに いました。どこへ 行きませんでした。",
            "日曜日、うちに いました。どこでも 行きました。"
        ],
        "B",
        "\"Không đi đâu cả\" là:「どこも 行きませんでした。」(hoặc どこへも 行きませんでした)."
    )

    # Cặp 6: Phủ định hoàn toàn với đồ vật: なにも + Phủ định
    add_pair("5", "1", P5_1,
        "Để diễn đạt ý phủ định hoàn toàn: \"hoàn toàn không ăn / không uống gì cả\", cấu trúc ngữ pháp nào sau đây là đúng?",
        [
            "なにか 食べませんでした",
            "なにも 食べませんでした",
            "なんの 食べませんでした",
            "なんでも 食べませんでした"
        ],
        "B",
        "「なにも + Động từ phủ định」nghĩa là \"không làm cái gì cả / không ăn gì cả\".",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Sáng nay vì bận nên tôi đã không ăn gì cả.\"",
        [
            "けさ いそがしいですから、なにか 食べませんでした。",
            "けさ いそがしかったですから、なにも 食べませんでした。",
            "けさ いそがしいでしたから、なにも 食べました。",
            "けさ いそがしくて、なんでも 食べませんでした。"
        ],
        "B",
        "\"Hoàn toàn không ăn gì\":「なにも 食べませんでした。」; lý do quá khứ: いそがしかったですから."
    )

    # Cặp 7: Làm cùng với ai: N(người) + と + V
    add_pair("5", "1", P5_1,
        "Trong tiếng Nhật, trợ từ nào đi sau danh từ chỉ người để biểu thị làm hành động CÙNG VỚI người đó?",
        [
            "Trợ từ に",
            "Trợ từ で",
            "Trợ từ と",
            "Trợ từ を"
        ],
        "C",
        "Trợ từ と dùng để chỉ đối tượng cùng thực hiện hành động (Ví dụ: ともだちと ごはんを たべます: ăn cơm cùng bạn bè).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tối qua tôi đã ăn cơm cùng với gia đình.\"",
        [
            "きのうの ばん、かぞくに ごはんを 食べました。",
            "きのうの ばん、かぞくで ごはんを 食べました。",
            "きのうの ばん、かぞくと ごはんを 食べました。",
            "きのうの ばん、かぞくを ごはんを 食べました。"
        ],
        "C",
        "Cùng với gia đình dùng trợ từ と:「かぞくと ごはんを 食べました。」"
    )

    # Cặp 8: Làm một mình: ひとりで
    add_pair("5", "1", P5_1,
        "Để diễn đạt ý \"làm hành động một mình\" (ví dụ: đi du lịch một mình), quy tắc ngữ pháp nào sau đây là đúng?",
        [
            "ひとりと 行きます",
            "ひとりで 行きます (không dùng thêm trợ từ と)",
            "ひとりに 行きます",
            "ひとりを 行きます"
        ],
        "B",
        "Cụm từ「ひとりで」đã mang nghĩa \"một mình\", không dùng trợ từ と (tuyệt đối không nói ひとりと).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cuối tuần tôi đã đi xem phim một mình.\"",
        [
            "しゅうまつ、ひとりと えいがを 見ました。",
            "しゅうまつ、ひとりで えいがを 見ました。",
            "しゅうまつ、ひとりに えいがを 見ました。",
            "しゅうまつ、ひとりの えいがを 見ました。"
        ],
        "B",
        "\"Một mình\" là「ひとりで」:「ひとりで えいがを 見ました。」"
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
        "「それから」dùng để nối tiếp các hành động theo trình tự thời gian (làm A, sau đó / rồi thì làm B).",
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
    # PHẦN 2: 休みの後で (9 cặp câu hỏi)
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
        "Tính từ đuôi い thì quá khứ khẳng định: Bỏ「い」➔ thêm「かったです」(Ví dụ: たのしい ➔ たのしかったです, あつい ➔ あつかったです).",
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
        "Quy tắc chia TÍNH TỪ ĐUÔI い sang thì QUÁ KHỨ PHỦ ĐỊNH (đã không...) là gì?",
        [
            "Bỏ đuôi い và thêm くなかったです",
            "Bỏ đuôi い và thêm くないでした",
            "Bỏ đuôi い và thêm じゃなかったです",
            "Giữ nguyên đuôi い và thêm ありませんでした"
        ],
        "A",
        "Tính từ đuôi い thì quá khứ phủ định: Bỏ「い」➔ thêm「くなかったです」(Ví dụ: さむい ➔ さむくなかったです, たかい ➔ たかくなかったです).",
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
        "NGOẠI LỆ QUAN TRỌNG: Thể quá khứ khẳng định và phủ định của tính từ đặc biệt「いい」(tốt, đẹp) là gì?",
        [
            "いかったです / いくなかったです",
            "よかった / よくなかった (dạng lịch sự: よかったです / よくなかったです)",
            "いいでした / いいじゃなかったです",
            "よかったです / よくないでした"
        ],
        "B",
        "Tính từ「いい」được biến đổi từ gốc「よい」➔ Quá khứ khẳng định là「よかったです」, quá khứ phủ định là「よくなかったです」.",
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
        "Tính từ đuôi な và Danh từ thì quá khứ khẳng định: Bỏ「な」➔ thêm「でした」(Ví dụ: しずか ➔ しずかでした, ひま ➔ ひまでした).",
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
        "Quy tắc chia TÍNH TỪ ĐUÔI な (hoặc Danh từ) sang thì QUÁ KHỨ PHỦ ĐỊNH (đã không...) thông thường là gì?",
        [
            "Bỏ な và thêm くなかったです",
            "Bỏ な và thêm じゃなかったです (hoặc ではありませんでした)",
            "Giữ nguyên な và thêm なかったです",
            "Bỏ な và thêm じゃないでした"
        ],
        "B",
        "Tính từ đuôi な quá khứ phủ định: Bỏ「な」➔ thêm「じゃなかったです」(Ví dụ: べんり ➔ べんりじゃなかったです).",
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
        "Mẫu câu hỏi「[Sự kiện / Chuyến đi] は どうでしたか。」dùng để làm gì?",
        [
            "Hỏi sự kiện diễn ra ở đâu",
            "Hỏi cảm nhận, đánh giá về một sự việc, trải nghiệm ĐÃ DIỄN RA trong quá khứ",
            "Hỏi chi phí của chuyến đi",
            "Hỏi thời gian diễn ra sự kiện"
        ],
        "B",
        "「〜は どうでしたか。」dùng để hỏi cảm nhận về một việc đã kết thúc trong quá khứ: \"... đã như thế nào? / có vui không?\".",
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
        "Mệnh đề 1 + から, Mệnh đề 2: biểu thị \"Vì mệnh đề 1 nên dẫn đến kết quả mệnh đề 2\".",
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
        "Khi được hỏi lý do bằng「どうしてですか。」(Tại sao vậy?), câu trả lời giải thích lý do kết thúc bằng đuôi nào?",
        [
            "Kết thúc bằng 〜ですが。",
            "Kết thúc bằng 〜から です。",
            "Kết thúc bằng 〜そして です。",
            "Kết thúc bằng 〜まで です。"
        ],
        "B",
        "Khi trả lời câu hỏi lý do「どうしてですか」, câu trả lời kết thúc bằng「[Lý do] から です。」(\"Vì... ạ\").",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tại sao hôm qua bạn không đến?\" - \"Vì hôm qua tôi có việc bận.\"",
        [
            "「どうして きのう 来ませんでしたか。」「用事(ようじ)が ありましたから です。」",
            "「どうして きのう 来ませんでしたか。」「用事(ようじ)が ありましたですが。」",
            "「どうして きのう 来ませんでしたか。」「用事(ようじ)が ありますから。」",
            "「どこで きのう 来ませんでしたか。」「用事(ようじ)が ありましたから です。」"
        ],
        "A",
        "Hỏi lý do:「どうして〜」; Trả lời lý do kết thúc bằng:「〜から です。」"
    )

    # Cặp 18: Kết hợp tính từ quá khứ và lý do: 〜かったですから
    add_pair("5", "2", P5_2,
        "Khi giải thích lý do bằng một tính từ đuôi い ở thì quá khứ (Ví dụ: \"Vì hôm qua trời nóng...\"), ta kết hợp ngữ pháp như thế nào?",
        [
            "Tính từ đuôi い + から (Ví dụ: あついから)",
            "Tính từ đuôi い bỏ い thêm かったですから (Ví dụ: あつかったですから)",
            "Tính từ đuôi い thêm でしたから (Ví dụ: あついでしたから)",
            "Tính từ đuôi い bỏ い thêm くないですから"
        ],
        "B",
        "Tính từ đuôi い thì quá khứ là「〜かったです」. Khi gắn thêm「から」để chỉ lý do, ta được「〜かったですから」(Ví dụ: いそがしかったですから: vì đã bận).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Vì ngày hôm qua rất bận nên tôi đã không thể xem phim.\"",
        [
            "きのうは とても いそがしいですから、えいがを 見ませんでした。",
            "きのうは とても いそがしかったですから、えいがを 見ませんでした。",
            "きのうは とても いそがしいでしたから、えいがを 見ませんでした。",
            "きのうは とても いそがしくないですから、えいがを 見ませんでした。"
        ],
        "B",
        "Lý do tính từ quá khứ:「いそがしかったですから、えいがを 見ませんでした。」"
    )

    # ==============================================================================
    # PHẦN 3: 今度の休みに (9 cặp câu hỏi)
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
        "「N が ほしいです」dùng để diễn đạt mong muốn sở hữu một danh từ (vật, tiền, người yêu, bạn bè...). Danh từ đi với trợ từ が.",
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
        "Vì「ほしい」được chia như một tính từ đuôi い, thể phủ định \"không muốn có\" được chia như thế nào?",
        [
            "ほしいじゃないです",
            "ほしくないです",
            "ほしいくないです",
            "ほしくありませんでした"
        ],
        "B",
        "「ほしい」là tính từ đuôi い ➔ Phủ định bỏ「い」thêm「くないです」thành「ほしくないです」(không muốn có).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bây giờ tôi không muốn có ô tô.\"",
        [
            "いま 車は ほしいじゃないです。",
            "いま 車は ほしくないです。",
            "いま 車は ほしいくないです。",
            "いま 車は ほしくありませんでした。"
        ],
        "B",
        "Không muốn có là:「車は ほしくないです。」(thường dùng trợ từ は thay cho が khi nhấn mạnh phủ định)."
    )

    # Cặp 21: Muốn làm hành động gì: V(bỏ ます) + たいです
    add_pair("5", "3", P5_3,
        "Để bày tỏ mong muốn, nguyện vọng làm một hành động nào đó của bản thân, ta đổi động từ đuôi「ます」thành gì?",
        [
            "V(bỏ ます) + たいです",
            "V(bỏ ます) + ほしいです",
            "V(nguyên thể) + たいです",
            "V(bỏ ます) + ますたい"
        ],
        "A",
        "Muốn làm V: Bỏ đuôi「ます」➔ thêm「たいです」(Ví dụ: 行きます ➔ 行きたいです: muốn đi; 食べます ➔ 食べたいです: muốn ăn).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Kỳ nghỉ hè tới tôi muốn đi du lịch Nhật Bản.\"",
        [
            "こんどの なつやすみに 日本へ りょこうしたいです。",
            "こんどの なつやすみに 日本へ りょこうほしいです。",
            "こんどの なつやすみに 日本へ りょこうするたいです。",
            "こんどの なつやすみに 日本へ りょこうしたかったです。"
        ],
        "A",
        "Động từ りょこうします bỏ ます thêm たいです:「日本へ りょこうしたいです。」"
    )

    # Cặp 22: Phủ định không muốn làm: V(bỏ ます) + たくないです
    add_pair("5", "3", P5_3,
        "Để diễn đạt \"không muốn làm\" một hành động nào đó, đuôi động từ được chia như thế nào?",
        [
            "V(bỏ ます) + たいじゃないです",
            "V(bỏ ます) + たくないです",
            "V(bỏ ます) + ないたいです",
            "V(bỏ ます) + ませんたい"
        ],
        "B",
        "Đuôi「たい」chia tương tự như tính từ đuôi い ➔ Phủ định bỏ「い」thêm「くないです」thành「Vたくないです」(không muốn làm).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hôm nay tôi mệt nên không muốn ăn gì cả.\"",
        [
            "きょうは つかれましたから、なにも 食べたいじゃないです。",
            "きょうは つかれましたから、なにも 食べたくないです。",
            "きょうは つかれましたから、なにか 食べたくないです。",
            "きょうは つかれましたから、なんでも 食べたいです。"
        ],
        "B",
        "Không muốn ăn gì cả:「なにも 食べたくないです。」"
    )

    # Cặp 23: Quá khứ muốn làm: V(bỏ ます) + たかったです
    add_pair("5", "3", P5_3,
        "Khi muốn nói về một nguyện vọng trong quá khứ (\"đã từng rất muốn làm...\"), cấu trúc ngữ pháp chia đuôi như thế nào?",
        [
            "V(bỏ ます) + たいでした",
            "V(bỏ ます) + たかったです",
            "V(bỏ ます) + ましたい",
            "V(bỏ ます) + たかったでした"
        ],
        "B",
        "Thể quá khứ của たい: Bỏ「い」thêm「かったです」thành「Vたかったです」(đã muốn làm).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tuần trước tôi đã rất muốn đi xem hòa nhạc.\"",
        [
            "せんしゅう コンサートへ 行きたいでした。",
            "せんしゅう コンサートへ 行きたかったです。",
            "せんしゅう コンサートへ 行きましたい。",
            "せんしゅう コンサートへ 行きたかったでした。"
        ],
        "B",
        "Quá khứ muốn đi là 行きたかったです:「せんしゅう コンサートへ 行きたかったです。」"
    )

    # Cặp 24: Hỏi mong muốn người khác: 何が / どこへ + たいですか
    add_pair("5", "3", P5_3,
        "Để hỏi người khác muốn làm gì hoặc muốn đi đâu vào kỳ nghỉ, mẫu câu hỏi nào sau đây là đúng?",
        [
            "何が したいですか。 / どこへ 行きたいですか。",
            "何が ほしいですか。 / どこへ 行きほしいですか。",
            "何が しますか。 / どこへ 行きますか。",
            "何が してたいですか。 / どこへ 行くたいですか。"
        ],
        "A",
        "Hỏi mong muốn làm hành động:「何が / 何を したいですか。」(Bạn muốn làm gì?);「どこへ 行きたいですか。」(Bạn muốn đi đâu?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Kỳ nghỉ tới bạn muốn đi đâu?\" - \"Tôi muốn đi Hokkaido.\"",
        [
            "「こんどの 休みに どこへ 行きたいですか。」「北海道へ 行きたいです。」",
            "「こんどの 休みに どこへ 行きほしいですか。」「北海道へ 行きほしいです。」",
            "「こんどの 休みに どこへ 行きますか。」「北海道へ 行きます。」",
            "「こんどの 休みに どこへ 行くたいですか。」「北海道へ 行くたいです。」"
        ],
        "A",
        "Hỏi muốn đi đâu:「どこへ 行きたいですか。」, trả lời:「北海道へ 行きたいです。」"
    )

    # Cặp 25: Đi đến đâu để làm gì: Địa điểm へ V(bỏ ます) に 行きます
    add_pair("5", "3", P5_3,
        "Cấu trúc「[Địa điểm] へ [V bỏ ます] に 行きます。」dùng để diễn đạt điều gì và trợ từ chỉ mục đích là gì?",
        [
            "Đi đến đâu để thực hiện một mục đích nào đó; trợ từ chỉ mục đích là に",
            "Đi đến đâu bằng phương tiện gì; trợ từ chỉ phương tiện là で",
            "Đi cùng với ai; trợ từ là と",
            "Thời gian bắt đầu đi; trợ từ là から"
        ],
        "A",
        "Cấu trúc biểu thị mục đích di chuyển: [Địa điểm] へ + [V bỏ ます / Danh từ] + に + [行きます / 来ます / 帰ります] (Đi/đến/về đâu để làm gì).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi đi đến trung tâm thương mại để mua sắm quần áo.\"",
        [
            "デパートへ ふくを 買いで 行きます。",
            "デパートへ ふくを 買いに 行きます。",
            "デパートへ ふくを 買うに 行きます。",
            "デパートへ ふくを 買いを 行きます。"
        ],
        "B",
        "Động từ 買います bỏ ます thêm に:「デパートへ ふくを 買いに 行きます。」"
    )

    # Cặp 26: Đi đến đâu với mục đích là Danh từ: Địa điểm へ N に 行きます
    add_pair("5", "3", P5_3,
        "Khi mục đích di chuyển là một danh từ chỉ hành động (ngắm hoa お花見, du lịch りょこう, trượt tuyết スキー), ta nối danh từ với trợ từ nào?",
        [
            "Danh từ + で + 行きます",
            "Danh từ + に + 行きます",
            "Danh từ + を + 行きます",
            "Danh từ + へ + 行きます"
        ],
        "B",
        "Nếu mục đích là danh từ chỉ hành động/sự kiện: [Danh từ] + に + 行きます (Ví dụ: お花見に 行きます: đi ngắm hoa; りょこうに 行きます: đi du lịch).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chủ nhật tôi sẽ đi đến công viên để ngắm hoa anh đào (お花見).\"",
        [
            "日曜日、公園へ お花見で 行きます。",
            "日曜日、公園へ お花見に 行きます。",
            "日曜日、公園へ お花見を 行きます。",
            "日曜日、公園へ お花見へ 行きます。"
        ],
        "B",
        "Mục đích danh từ + に 行きます:「公園へ お花見に 行きます。」"
    )

    # Cặp 27: Hỏi mục đích di chuyển: なにしに 行きますか
    add_pair("5", "3", P5_3,
        "Để hỏi \"Bạn đi đến [địa điểm] để làm gì?\", cấu trúc câu hỏi ngữ pháp tiếng Nhật nào sau đây là đúng?",
        [
            "[Địa điểm] へ なにで 行きますか。",
            "[Địa điểm] へ なにしに 行きますか (hoặc 何を しに 行きますか)。",
            "[Địa điểm] へ だれと 行きますか。",
            "[Địa điểm] へ いつ 行きますか。"
        ],
        "B",
        "Hỏi mục đích di chuyển:「なにをしに (hoặc なにしに) 行きますか。」(Đi để làm cái gì?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bạn đến Nhật Bản để làm gì?\" - \"Tôi đến để học kinh tế.\"",
        [
            "「日本へ なにしに 来ましたか。」「けいざいを 勉強しに 来ました。」",
            "「日本へ なにで 来ましたか。」「けいざいを 勉強しに 来ました。」",
            "「日本へ どこに 来ましたか。」「けいざいを 勉強しに 来ました。」",
            "「日本へ いつ 来ましたか。」「けいざいを 勉強しに 来ました。」"
        ],
        "A",
        "Hỏi mục đích đến:「日本へ なにしに 来ましたか。」, trả lời:「けいざいを 勉強しに 来ました。」"
    )
