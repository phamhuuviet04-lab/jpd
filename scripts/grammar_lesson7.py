# -*- coding: utf-8 -*-
"""
Dữ liệu câu hỏi ngữ pháp Bài 7 - Dekiru Nihongo
Chia làm 2 dạng câu hỏi rõ ràng:
1. [HỎI NGỮ PHÁP]: Hỏi khái niệm, cấu trúc, quy tắc, cách dùng trợ từ và chia động từ
2. [DỊCH CÂU]: Dịch từ câu tiếng Việt sang tiếng Nhật tương ứng
"""

def register_lesson_7(add_pair):
    P7_1 = "みちが わかりません (Vị trí, Chỉ đường, を/へ, Vてください)"
    P7_2 = "パーティーの じゅんび (Công cụ で, Cho/Nhận に, Ngôn ngữ で)"
    P7_3 = "みんなで たのしい パーティー (Hành động đang tiếp diễn Vています, だれが, Vましょうか)"

    # ==============================================================================
    # PHẦN 1: みちが わかりません (9 cặp câu hỏi = 18 câu)
    # ==============================================================================

    # Cặp 1: Vị trí không gian tương đối: N1 の [vị trí] に あります
    add_pair("7", "1", P7_1,
        "Để miêu tả vị trí của một đồ vật hoặc công trình so với một vật làm mốc, cấu trúc chuẩn trong tiếng Nhật là gì?",
        [
            "N1 の [vị trí] で N2 が あります",
            "N1 の [vị trí] に N2 が あります",
            "N1 の [vị trí] を N2 が あります",
            "N1 の [vị trí] へ N2 が あります"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Cấu trúc chỉ vị trí tồn tại của đồ vật/công trình:「N1 の [vị trí] に N2 が あります」hoặc「N2 は N1 の [vị trí] に あります」. Trong đó vị trí gồm: まえ (trước), うしろ (sau), なか (trong), そと (ngoài), となり (bên cạnh), うえ (trên), した (dưới).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Trạm xe buýt ở phía trước cửa hàng tiện lợi.\"",
        [
            "バスていは コンビニの まえに あります。",
            "バスていは コンビニの まえで あります。",
            "バスていは コンビニの まえを あります。",
            "バスていは コンビニの まえへ あります。"
        ],
        "A",
        "Vị trí tồn tại của vật mốc:「バスていは コンビニの まえに あります。」"
    )

    # Cặp 2: Phân biệt あります vs います
    add_pair("7", "1", P7_1,
        "Quy tắc phân biệt động từ tồn tại「あります」và「います」trong tiếng Nhật là gì?",
        [
            "「あります」chỉ dùng cho thời gian,「います」chỉ dùng cho tiền bạc",
            "「あります」dùng cho đồ vật vô tri, thực vật, công trình; còn「います」bắt buộc dùng cho sinh vật sống có thể tự chuyển động (người, động vật)",
            "「あります」dùng cho người lớn,「います」dùng cho trẻ em và đồ chơi",
            "Hai động từ này hoàn toàn giống nhau, dùng thay thế cho nhau tùy ý"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「あります」dùng cho đồ vật vô tri, công trình, cây cối, địa điểm; còn「います」dùng cho người và động vật (những đối tượng sống có ý chí và tự di chuyển). Ví dụ:「たなかさんは とけいの したに います。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Anh Tanaka đang ở dưới cái đồng hồ.\"",
        [
            "たなかさんは とけいの したに あります。",
            "たなかさんは とけいの したに います。",
            "たなかさんは とけいの したで います。",
            "たなかさんは とけいの したを あります。"
        ],
        "B",
        "Tanaka là người nên dùng います:「たなかさんは とけいの したに います。」"
    )

    # Cặp 3: Vị trí ở giữa hai vật: N1 と N2 の あいだ
    add_pair("7", "1", P7_1,
        "Khi muốn nói một địa điểm nằm ở \"chính giữa hai địa điểm N1 và N2\", ta dùng cụm từ chỉ vị trí nào?",
        [
            "N1 と N2 の となり に あります",
            "N1 と N2 の あいだ に あります",
            "N1 と N2 の まんなか を あります",
            "N1 と N2 の ちかく へ あります"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Vị trí ở giữa hai vật/địa điểm là:「N1 と N2 の あいだ に あります」(nằm ở khoảng giữa N1 và N2).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Ngân hàng nằm ở giữa siêu thị và bưu điện.\"",
        [
            "ぎんこうは スーパーと ゆうびんきょくの となりに あります。",
            "ぎんこうは スーパーと ゆうびんきょくの あいだに あります。",
            "ぎんこうは スーパーと ゆうびんきょくの なかに あります。",
            "ぎんこうは スーパーと ゆうびんきょくの まえに あります。"
        ],
        "B",
        "Ở giữa hai vật dùng あいだ:「ぎんこうは スーパーと ゆうびんきょくの あいだに あります。」"
    )

    # Cặp 4: Phân biệt となり vs ちかく
    add_pair("7", "1", P7_1,
        "Từ「となり」và「ちかく」khác nhau như thế nào khi miêu tả vị trí?",
        [
            "「となり」là ở xa,「ちかく」là ở ngay bên cạnh sát vách",
            "「となり」là bên cạnh sát vách (cùng dãy/tiếp giáp), còn「ちかく」là khu vực lân cận, gần xung quanh",
            "「となり」chỉ dùng cho người,「ちかく」chỉ dùng cho đồ vật",
            "Hai từ này có nghĩa hoàn toàn giống nhau và cách dùng như nhau"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「となり」(bên cạnh) chỉ vị trí tiếp giáp ngay kề sát bên cạnh. Còn「ちかく」(gần) chỉ một phạm vi khoảng cách gần trong khu vực xung quanh:「さくらえきの ちかくに スーパーが あります。」",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Gần ga Sakura có siêu thị.\"",
        [
            "さくらえきの となりに スーパーが あります。",
            "さくらえきの ちかくに スーパーが あります。",
            "さくらえきの まえに スーパーが います。",
            "さくらえきの なかに スーパーが います。"
        ],
        "B",
        "Gần địa điểm nào đó dùng ちかく:「さくらえきの ちかくに スーパーが あります。」"
    )

    # Cặp 5: Động từ chuyển động qua không gian với trợ từ を
    add_pair("7", "1", P7_1,
        "Điền trợ từ thích hợp vào chỗ trống để chỉ hành động băng qua cây cầu:「あのはし（　）わたります。」",
        [
            "で",
            "を",
            "に",
            "へ"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trợ từ「を」đi kèm với các động từ chuyển động (わたります: băng qua, あるきます: đi bộ, とおります: đi ngang qua) để chỉ không gian/đoạn đường mà chuyển động xuyên qua:「はしを わたります」(qua cầu),「みちを わたります」(qua đường).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Xin hãy đi qua cây cầu kia.\"",
        [
            "あのはしで わたってください。",
            "あのはしを わたってください。",
            "あのはしに わたってください。",
            "あのはしへ わたってください。"
        ],
        "B",
        "Chuyển động qua không gian dùng trợ từ を:「あのはしを わたってください。」"
    )

    # Cặp 6: Trợ từ chỉ hướng rẽ: へ / に まがります
    add_pair("7", "1", P7_1,
        "Điền trợ từ thích hợp vào câu chỉ hướng rẽ:「ひとつめの かどを みぎ（　）まがってください。」",
        [
            "を",
            "へ",
            "で",
            "から"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Để chỉ hướng rẽ (quẹo), ta dùng trợ từ「へ」hoặc「に」sau phương hướng:「みぎへ / みぎに まがります」(rẽ sang phải),「ひだりへ / ひだりに まがります」(rẽ sang trái). Còn ngã rẽ/khúc quanh xuyên qua dùng trợ từ「を」:「かどを みぎへ まがります」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Hãy rẽ phải ở góc cua đầu tiên.\"",
        [
            "ひとつめの かどに みぎを まがってください。",
            "ひとつめの かどを みぎへ まがってください。",
            "ひとつめの かどで みぎから まがってください。",
            "ひとつめの かどへ みぎで まがってください。"
        ],
        "B",
        "Góc rẽ đi qua dùng を, hướng rẽ dùng へ:「ひとつめの かどを みぎへ まがってください。」"
    )

    # Cặp 7: Mẫu câu chỉ dẫn hành động: Vてください
    add_pair("7", "1", P7_1,
        "Khi muốn hướng dẫn người khác đi đường \"Hãy đi thẳng con đường này\", câu nói chuẩn ngữ pháp là:",
        [
            "このみちを まっすぐ いきます。",
            "このみちを まっすぐ いってください。",
            "このみちを まっすぐ いきたいです。",
            "このみちを まっすぐ いきませんか。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Thể「Vてください」dùng để yêu cầu, chỉ dẫn hoặc nhờ vả đối phương thực hiện một hành động một cách lịch sự:「まっすぐ いってください」(Hãy đi thẳng).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Xin hãy đi thẳng con đường này.\"",
        [
            "このみちを まっすぐ いきます。",
            "このみちを まっすぐ いってください。",
            "このみちを まっすぐ いきました。",
            "このみちを まっすぐ いきましょう。"
        ],
        "B",
        "Chỉ dẫn lịch sự dùng Vてください:「このみちを まっすぐ いってください。」"
    )

    # Cặp 8: Mở đầu hỏi đường lịch sự dùng 〜が
    add_pair("7", "1", P7_1,
        "Khi bắt đầu hỏi đường người lạ: \"Xin lỗi, tôi muốn đến nhà ga nhưng... (không biết đường)\", người Nhật thường dùng từ nối nào ở cuối vế mở đầu?",
        [
            "すみませんが、えきへ いきたいですから、…",
            "すみませんが、えきへ いきたいですが、…",
            "すみませんが、えきへ いきたいそして、…",
            "すみませんが、えきへ いきたいですからして、…"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi mở đầu câu chuyện để hỏi thông tin hoặc nhờ vả, người Nhật dùng trợ từ nối「〜が」(nhưng / với ý đệm nhẹ nhàng):「すみませんが、えきへ いきたいですが、…」(Xin lỗi, tôi muốn đến ga nhưng mà...).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Xin lỗi, tôi không biết đường...\"",
        [
            "すみません、みちが わかりませんから…",
            "すみません、みちが わかりませんが…",
            "すみません、みちが わかりますですが…",
            "すみません、みちが わかりませんそして…"
        ],
        "B",
        "Mở lời nhờ vả / báo tình huống đệm nhẹ:「すみません、みちが わかりませんが…」"
    )

    # Cặp 9: Đi đón ai đó: むかえに いきます
    add_pair("7", "1", P7_1,
        "Khi nói \"Tôi sẽ đi ra tận cổng soát vé để đón bạn\", cụm từ chỉ mục đích di chuyển chuẩn là:",
        [
            "かいさつまで むかえに いきます。",
            "かいさつまで むかえを いきます。",
            "かいさつまで むかえで いきます。",
            "かいさつまで むかえから いきます。"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Cấu trúc mục đích di chuyển:「[Hành động thể Vます bỏ ます] に いきます」➔ Đón ai là「むかえに いきます」. Đến địa điểm nào đón:「[Địa điểm] まで むかえに いきます」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi sẽ đi đến cổng soát vé để đón bạn.\"",
        [
            "かいさつまで むかえに いきます。",
            "かいさつまで むかえを いきます。",
            "かいさつまで むかえで いきます。",
            "かいさつまで むかえから いきます。"
        ],
        "A",
        "Đi đón ở cổng soát vé:「かいさつまで むかえに いきます。」"
    )

    # ==============================================================================
    # PHẦN 2: パーティーの じゅんび (9 cặp câu hỏi = 18 câu)
    # ==============================================================================

    # Cặp 10: Trợ từ で chỉ công cụ: [Công cụ] で V
    add_pair("7", "2", P7_2,
        "Điền trợ từ thích hợp vào chỗ trống để chỉ dụng cụ cắt bánh:「ナイフ（　）パンを きります。」",
        [
            "を",
            "で",
            "に",
            "へ"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trợ từ「で」đứng sau danh từ chỉ dụng cụ, công cụ hoặc phương tiện thực hiện hành động:「[Dụng cụ] で [Hành động] を します」. Ví dụ:「ナイフで きります」(cắt bằng dao),「はさみで きります」(cắt bằng kéo).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cắt bánh mì bằng dao.\"",
        [
            "ナイフを パンで きります。",
            "ナイフで パンを きります。",
            "ナイフに パンを きります。",
            "ナイフへ パンで きります。"
        ],
        "B",
        "Dụng cụ cắt dùng trợ từ で:「ナイフで パンを きります。」"
    )

    # Cặp 11: Phương thức ăn uống dùng で
    add_pair("7", "2", P7_2,
        "Câu nào dưới đây dùng đúng trợ từ để miêu tả \"Người Nhật ăn cơm bằng đũa\"?",
        [
            "にほんじんは はしを ごはんを たべます。",
            "にほんじんは はしで ごはんを たべます。",
            "にほんじんは はしに ごはんを たべます。",
            "にほんじんは はしへ ごはんを たべます。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Dụng cụ dùng để ăn uống đi với trợ từ「で」:「はしで ごはんを たべます」(ăn bằng đũa),「フォークと ナイフで ごはんを たべます」(ăn bằng nĩa và dao),「てで ごはんを たべます」(ăn bằng tay).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Người Nhật ăn cơm bằng đũa.\"",
        [
            "にほんじんは はしを ごはんを たべます。",
            "にほんじんは はしで ごはんを たべます。",
            "にほんじんは はしに ごはんを たべます。",
            "にほんじんは はしから ごはんを たべます。"
        ],
        "B",
        "Ăn bằng đũa dùng はしで:「にほんじんは はしで ごはんを たべます。」"
    )

    # Cặp 12: Ngôn ngữ biểu đạt dùng trợ từ で
    add_pair("7", "2", P7_2,
        "Khi muốn hỏi một từ hoặc một vật \"Bằng tiếng Nhật là gì?\", ta dùng mẫu câu chuẩn nào?",
        [
            "これは にほんごを なんですか。",
            "これは にほんごで なんですか。",
            "これは にほんごに なんですか。",
            "これは にほんごへ なんですか。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trợ từ「で」dùng sau danh từ chỉ ngôn ngữ để biểu thị phương tiện diễn đạt:「にほんごで なんですか」(bằng tiếng Nhật là gì?),「ベトナムごで いいます」(nói bằng tiếng Việt),「えいごで てがみを かきます」(viết thư bằng tiếng Anh).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cái này bằng tiếng Nhật là gì vậy?\"",
        [
            "これは にほんごを なんですか。",
            "これは にほんごで なんですか。",
            "これは にほんごに なんですか。",
            "これは にほんごから なんですか。"
        ],
        "B",
        "Bằng tiếng Nhật là gì:「これは にほんごで なんですか。」"
    )

    # Cặp 13: Cho / tặng ai cái gì: [Người nhận] に [Vật] を あげます
    add_pair("7", "2", P7_2,
        "Trong mẫu câu tặng quà:「わたしは ともだち（　）はなを あげます。」, trợ từ đứng sau người nhận quà là trợ từ nào?",
        [
            "で",
            "に",
            "を",
            "へ"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trong cấu trúc cho/tặng ai cái gì:「[Người tặng] は [Người nhận] に [Vật] を あげます」, người nhận đối tượng bắt buộc đi với trợ từ「に」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi tặng hoa cho bạn bè.\"",
        [
            "わたしは ともだちで はなを あげます。",
            "わたしは ともだちに はなを あげます。",
            "わたしは ともだちを はなに あげます。",
            "わたしは ともだちから はなを あげます。"
        ],
        "B",
        "Tặng cho ai dùng trợ từ に:「わたしは ともだちに はなを あげます。」"
    )

    # Cặp 14: Nhận từ ai cái gì: [Người cho] に / から [Vật] を もらいます
    add_pair("7", "2", P7_2,
        "Khi bạn nhận một món quà từ bạn bè:「わたしは ともだち（　）プレゼントを もらいました。」, trợ từ có thể điền vào chỗ trống là gì?",
        [
            "で hoặc を",
            "に hoặc から",
            "へ hoặc で",
            "まで hoặc を"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Trong cấu trúc nhận cái gì từ ai:「[Người nhận] は [Người cho] に (hoặc から) [Vật] を もらいます」. Trợ từ「に」hoặc「から」chỉ nguồn gốc xuất phát của món đồ được nhận.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi đã nhận được quà từ bạn bè.\"",
        [
            "わたしは ともだちで プレゼントを もらいました。",
            "わたしは ともだちに プレゼントを もらいました。",
            "わたしは ともだちを プレゼントに もらいました。",
            "わたしは ともだちへ プレゼントを もらいました。"
        ],
        "B",
        "Nhận từ ai dùng に hoặc から:「わたしは ともだちに プレゼントを もらいました。」"
    )

    # Cặp 15: Cho mượn (かします) vs Đi mượn (かります)
    add_pair("7", "2", P7_2,
        "Phân biệt cặp động từ「かします」và「かります」trong tiếng Nhật:",
        [
            "「かします」nghĩa là đi mượn từ người khác,「かります」nghĩa là cho người khác mượn",
            "「かします」nghĩa là cho người khác mượn,「かります」nghĩa là mượn từ người khác",
            "Cả hai từ đều có nghĩa là mua bán đồ dùng",
            "「かします」chỉ dùng cho tiền,「かります」chỉ dùng cho sách vở"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「[Người cho mượn] は [Người mượn] に [Đồ vật] を かします」(cho ai mượn). Ngược lại:「[Người mượn] は [Người cho mượn] に / から [Đồ vật] を かります」(mượn từ ai).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi cho bạn tôi mượn cây bút.\"",
        [
            "わたしは ともだちから ペンを かします。",
            "わたしは ともだちに ペンを かします。",
            "わたしは ともだちで ペンを かります。",
            "わたしは ともだちを ペンに かします。"
        ],
        "B",
        "Cho ai mượn dùng に かします:「わたしは ともだちに ペンを かします。」"
    )

    # Cặp 16: Dạy cho ai (おしえます) vs Học từ ai (ならいます)
    add_pair("7", "2", P7_2,
        "Khi nói \"Tôi dạy tiếng Việt cho bạn bè\", câu chuẩn ngữ pháp là:",
        [
            "わたしは ともだちに ベトナムごを ならいます。",
            "わたしは ともだちに ベトナムごを おしえます。",
            "わたしは ともだちから ベトナムごを おしえます。",
            "わたしは ともだちで ベトナムごを ならいます。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Dạy cho ai dùng「[Người học] に おしえます」. Ngược lại, học từ ai dùng「[Người dạy] に / から ならいます」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi dạy tiếng Việt cho bạn bè.\"",
        [
            "わたしは ともだちに ベトナムごを ならいます。",
            "わたしは ともだちに ベトナムごを おしえます。",
            "わたしは ともだちで ベトナムごを おしえます。",
            "わたしは ともだちを ベトナムごに ならいます。"
        ],
        "B",
        "Dạy cho người khác dùng に おしえます:「わたしは ともだちに ベトナムごを おしえます。」"
    )

    # Cặp 17: Cho vào (いれます) vs Lấy ra (だします)
    add_pair("7", "2", P7_2,
        "Điền cặp trợ từ thích hợp vào hai câu sau:\n1. れいぞうこ（　）ジュースを いれます。(Cho vào)\n2. れいぞうこ（　）ジュースを だします。(Lấy ra)",
        [
            "1. で  /  2. を",
            "1. に  /  2. から",
            "1. を  /  2. に",
            "1. へ  /  2. で"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Đưa vật vào bên trong một nơi:「[Nơi chốn] に いれます」(đích đến vào bên trong dùng に). Ngược lại, lấy vật ra khỏi một nơi:「[Nơi chốn] から だします」(xuất phát điểm ra ngoài dùng から).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Cho nước ngọt vào tủ lạnh.\"",
        [
            "れいぞうこで ジュースを いれます。",
            "れいぞうこに ジュースを いれます。",
            "れいぞうこから ジュースを いれます。",
            "れいぞうこを ジュースに いれます。"
        ],
        "B",
        "Cho vào tủ lạnh dùng に いれます:「れいぞうこに ジュースを いれます。」"
    )

    # Cặp 18: Lời nhờ vả lịch sự khi chuẩn bị tiệc và đáp lại: すみませんが、Vてください ➔ いいですよ
    add_pair("7", "2", P7_2,
        "Khi muốn nhờ bạn bè giúp chuẩn bị bữa tiệc một cách lịch sự, bạn nói gì và bạn của bạn sẽ vui vẻ đáp lại như thế nào?",
        [
            "「すみませんが、てつだって ください。」「いいですよ。」",
            "「てつだいませんか。」「けっこうです。」",
            "「てつだいたいですか。」「はい、そうです。」",
            "「てつだって ください。」「いいえ、いやです。」"
        ],
        "A",
        "💡 Chuẩn ngữ pháp: Lời nhờ vả lịch sự:「すみませんが、Vてください」(Xin lỗi, xin bạn hãy giúp...). Người được nhờ vui vẻ nhận lời đáp:「いいですよ。」(Được chứ! / Sẵn lòng!).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Xin lỗi, hãy giúp tôi một tay nhé!\" - \"Được chứ!\"",
        [
            "「すみませんが、てつだって ください。」「いいですよ。」",
            "「すみませんが、てつだいませんか。」「いいですね。」",
            "「すみませんが、てつだいましたか。」「いいですよ。」",
            "「すみませんが、てつだいたいです。」「そうですね。」"
        ],
        "A",
        "Nhờ giúp đỡ và nhận lời:「すみませんが、てつだって ください。」「いいですよ。」"
    )

    # ==============================================================================
    # PHẦN 3: みんなで たのしい パーティー (9 cặp câu hỏi = 18 câu)
    # ==============================================================================

    # Cặp 19: Thể hiện tại tiếp diễn Vています
    add_pair("7", "3", P7_3,
        "Để diễn tả một hành động ĐANG DIỄN RA tại thời điểm nói trong tiếng Nhật, ta dùng dạng động từ nào?",
        [
            "Vます",
            "Vています",
            "Vました",
            "Vたいです"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Động từ chia sang thể て kết hợp với「います」(Vています) dùng để diễn tả hành động đang diễn ra ngay tại thời điểm nói:「いま おさらを あらっています」(Bây giờ tôi đang rửa bát).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bây giờ anh Park đang rửa bát.\"",
        [
            "いま パクさんは おさらを あらいます。",
            "いま パクさんは おさらを あらっています。",
            "いま パクさんは おさらを あらいました。",
            "いま パクさんは おさらを あらいたいです。"
        ],
        "B",
        "Hành động đang diễn ra dùng Vています:「いま パクさんは おさらを あらっています。」"
    )

    # Cặp 20: Phân biệt Vます vs Vています
    add_pair("7", "3", P7_3,
        "Điểm khác nhau cơ bản giữa câu「コーヒーを のみます」và「コーヒーを のんでいます」là gì?",
        [
            "「のみます」chỉ quá khứ đã uống xong,「のんでいます」chỉ việc chưa làm",
            "「のみます」diễn tả thói quen hoặc hành động sẽ làm, còn「のんでいます」nhấn mạnh hành động ĐANG DIỄN RA ngay lúc nói",
            "「のみます」chỉ dùng cho buổi sáng,「のんでいます」chỉ dùng cho buổi tối",
            "Hai câu này hoàn toàn giống nhau, không có sự khác biệt"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「Vます」nói về thói quen lặp đi lặp lại hoặc hành động tương lai (まいあさ コーヒーを のみます: mỗi sáng tôi đều uống cà phê). Còn「Vています」diễn tả hành động đang tiến hành ngay tại thời điểm nói (いま コーヒーを のんでいます: bây giờ tôi đang uống cà phê).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bây giờ tôi đang uống cà phê.\"",
        [
            "いま わたしは コーヒーを のみます。",
            "いま わたしは コーヒーを のんでいます。",
            "いま わたしは コーヒーを のみました。",
            "いま わたしは コーヒーを のみたいです。"
        ],
        "B",
        "Đang uống cà phê dùng のんでいます:「いま わたしは コーヒーを のんでいます。」"
    )

    # Cặp 21: Động từ chơi nhạc cụ: ひきます (đang chơi: ひいています)
    add_pair("7", "3", P7_3,
        "Với các nhạc cụ dây hoặc phím như đàn piano (ピアノ), đàn guitar (ギター), tiếng Nhật dùng động từ nào để diễn tả việc chơi đàn?",
        [
            "あそびます (あそんでいます)",
            "ひきます (ひいています)",
            "します (しています)",
            "とります (とっています)"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Chơi nhạc cụ dây/phím (piano, guitar) dùng động từ「ひきます」➔ Đang chơi đàn là「ひいています」:「ピアノを ひいています」(đang chơi piano),「ギターを ひいています」(đang chơi guitar).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chị Maria đang chơi đàn piano.\"",
        [
            "マリアさんは ピアノを します。",
            "マリアさんは ピアノを ひいています。",
            "マリアさんは ピアノを あそんでいます。",
            "マリアさんは ピアノを とっています。"
        ],
        "B",
        "Đang chơi đàn piano dùng ピアノを ひいています:「マリアさんは ピアノを ひいています。」"
    )

    # Cặp 22: Động từ liên quan đến điện thoại: でんわを しています / かけています
    add_pair("7", "3", P7_3,
        "Để nói ai đó \"đang nói chuyện điện thoại / đang gọi điện thoại\", cụm từ chuẩn ngữ pháp là:",
        [
            "でんわを はなします",
            "でんわを しています (hoặc でんわを かけています)",
            "でんわを きいています",
            "でんわを みています"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Nói chuyện điện thoại là「でんわを します」➔ Đang nói chuyện điện thoại là「でんわを しています」. Gọi điện thoại là「でんわを かけます」➔ Đang gọi điện là「でんわを かけています」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Chị Anna đang nói chuyện điện thoại.\"",
        [
            "アンナさんは でんわを します。",
            "アンナさんは でんわを しています。",
            "アンナさんは でんわを かけました。",
            "アンナさんは でんわを きいています。"
        ],
        "B",
        "Đang nói chuyện điện thoại dùng でんわを しています:「アンナさんは でんわを しています。」"
    )

    # Cặp 23: Cụm từ hát một bài hát: うたを うたっています
    add_pair("7", "3", P7_3,
        "Cụm từ biểu thị hành động \"đang hát (bài hát)\" trong tiếng Nhật là:",
        [
            "うたを いっています",
            "うたを うたっています",
            "うたを はなしています",
            "うたを きいています"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Danh từ bài hát là「うた」, động từ hát là「うたいます」. Cụm từ hát bài hát:「うたを うたいます」➔ Đang hát:「うたを うたっています」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Anh Nishikawa đang hát.\"",
        [
            "にしかわさんは うたを いっています。",
            "にしかわさんは うたを うたっています。",
            "にしかわさんは うたを はなしています。",
            "にしかわさんは うたを きいています。"
        ],
        "B",
        "Đang hát dùng うたを うたっています:「にしかわさんは うたを うたっています。」"
    )

    # Cặp 24: Hỏi đang làm gì: 〜さんは なにを していますか
    add_pair("7", "3", P7_3,
        "Khi muốn hỏi đối phương hoặc người khác \"Bây giờ bạn đang làm gì đấy?\", mẫu câu hỏi chuẩn là:",
        [
            "いま なにを しますか。",
            "いま なにを していますか。",
            "いま なにを しましたか。",
            "いま なにを したいですか。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Để hỏi hành động đang diễn ra tại thời điểm hiện tại:「なにを していますか。」(Đang làm gì thế?). Trả lời bằng:「[Hành động thể て] います。」.",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Bây giờ bạn đang làm gì vậy?\"",
        [
            "いま なにを しますか。",
            "いま なにを していますか。",
            "いま なにを しましたか。",
            "いま なにを しませんか。"
        ],
        "B",
        "Hỏi đang làm gì dùng なにを していますか:「いま なにを していますか。」"
    )

    # Cặp 25: Hỏi ai đang làm gì với trợ từ が: だれが Vていますか
    add_pair("7", "3", P7_3,
        "Khi hỏi \"Ai đang chơi đàn guitar thế?\", trợ từ đi sau từ để hỏi「だれ」bắt buộc phải là gì?",
        [
            "だれは ギターを ひいていますか。",
            "だれが ギターを ひいていますか。",
            "だれを ギターを ひいていますか。",
            "だれに ギターを ひいていますか。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi từ để hỏi (như だれ - ai, なに - cái gì) làm chủ ngữ của câu, BẮT BUỘC dùng trợ từ「が」, tuyệt đối không dùng「は」. Trong câu trả lời, chủ ngữ cũng đi với「が」:「メアリーンさんが ギターを ひいています。」",
        "Dịch đoạn đối thoại sau sang tiếng Nhật: \"Ai đang chơi guitar vậy?\" - \"Maryn đang chơi đấy.\"",
        [
            "「だれは ギターを ひいていますか。」「メアリーンさんは ひいています。」",
            "「だれが ギターを ひいていますか。」「メアリーンさんが ひいています。」",
            "「だれを ギターを ひいていますか。」「メアリーンさんを ひいています。」",
            "「だれに ギターを ひいていますか。」「メアリーンさんに ひいています。」"
        ],
        "B",
        "Hỏi chủ ngữ với だれ dùng trợ từ が:「だれが ギターを ひいていますか。」「メアリーンさんが ひいています。」"
    )

    # Cặp 26: Đề nghị làm giúp đối phương: Vましょうか
    add_pair("7", "3", P7_3,
        "Mẫu câu「Vましょうか。」dùng trong hoàn cảnh giao tiếp nào?",
        [
            "Hỏi xin phép đối phương cho mình làm việc gì",
            "Người nói chủ động đề nghị làm giúp một hành động cho đối phương (\"Tôi làm giúp bạn nhé?\")",
            "Bắt buộc đối phương phải làm việc gì cho mình",
            "Hỏi xem đối phương đã hoàn thành công việc hay chưa"
        ],
        "B",
        "💡 Chuẩn ngữ pháp:「Vましょうか。」dùng khi người nói chủ động đề nghị giúp đỡ đối phương:「てつだいましょうか。」(Tôi giúp một tay nhé?),「もちましょうか。」(Tôi xách giúp bạn nhé?),「しゃしんを とりましょうか。」(Tôi chụp ảnh giúp bạn nhé?).",
        "Dịch câu tiếng Việt sau sang tiếng Nhật: \"Tôi xách hành lý giúp bạn nhé?\"",
        [
            "にもつを もちますか。",
            "にもつを もちましょうか。",
            "にもつを もちたいですか。",
            "にもつを もってください。"
        ],
        "B",
        "Chủ động đề nghị giúp xách đồ:「にもつを もちましょうか。」"
    )

    # Cặp 27: Cách đáp lại lời đề nghị giúp đỡ Vましょうか
    add_pair("7", "3", P7_3,
        "Khi ai đó đề nghị giúp bạn:「まどを あけましょうか。」(Tôi mở cửa sổ giúp bạn nhé?), nếu bạn muốn ĐỒNG Ý và nhờ họ giúp, theo chuẩn lịch sự bạn sẽ đáp như thế nào?",
        [
            "いいえ、けっこうです。",
            "ええ、おねがいします。",
            "いいえ、あけません。",
            "ええ、あけましょう。"
        ],
        "B",
        "💡 Chuẩn ngữ pháp: Khi đồng ý nhận sự giúp đỡ từ lời đề nghị「Vましょうか」, câu đáp lịch sự chuẩn mực là:「ええ、おねがいします。」(Vâng, nhờ bạn / làm ơn giúp tôi). Nếu từ chối lịch sự thì nói:「いいえ、けっこうです。」(Không cần đâu, tôi ổn rồi).",
        "Dịch đoạn đối thoại sau sang tiếng Nhật: \"Tôi mở cửa sổ giúp bạn nhé?\" - \"Vâng, nhờ bạn nhé.\"",
        [
            "「まどを あけましょうか。」「いいえ、けっこうです。」",
            "「まどを あけましょうか。」「ええ、おねがいします。」",
            "「まどを あけませんか。」「ええ、そうしましょう。」",
            "「まどを あけてください。」「いいですよ。」"
        ],
        "B",
        "Đồng ý nhận giúp đỡ từ Vましょうか:「ええ、おねがいします。」"
    )
