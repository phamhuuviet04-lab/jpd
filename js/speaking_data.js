/**
 * KHO DỮ LIỆU CÂU HỎI LUYỆN NÓI TIẾNG NHẬT (BÀI 4 - 7)
 * Đã chuyển hóa 100% từ Hán tự (Kanji) sang Hiragana & Katakana:
 * Giúp người học luyện phản xạ nói tự nhiên, chuẩn ngữ pháp Dekiru Nihongo mà không bị cản trở bởi chữ Hán.
 * 
 * Nội dung bao quát toàn bộ 34 cấu trúc câu hỏi giao tiếp theo giáo trình:
 * - Bài 4 (9 câu): Thời gian di chuyển (から〜まで), Phương tiện (で), Hỏi đặc điểm (どんなところ), Cảm nhận (どうですか), Tính từ (にぎやか, おおきい), Tồn tại (あります), Thời tiết (がつ・きせつ)
 * - Bài 5 (8 câu): Quá khứ động từ (なにをしましたか), Đi đâu (どこかへ), Làm cùng ai (だれと), Hỏi lý do (どうして〜から), Mong muốn sở hữu (ほしい), Sở thích (すき), Mong muốn hành động (〜たい), Mục đích di chuyển (〜にいきます)
 * - Bài 6 (8 câu): Rủ rê (〜ませんか・〜ましょう), Sự kiện diễn ra (であります), So sánh nhất (なに・だれ・どこ・なんがつがいちばん), So sánh hơn (どちらが), Đã làm chưa (もう〜ましたか / まだです)
 * - Bài 7 (9 câu): Vị trí vật / ĐH FPT (どこにありますか), Vị trí người / động vật (どこにいますか), Quanh đây có gì (ちかくになにがありますか), Dụng cụ (なにできりますか), Tập quán ăn uống (なにでごはんをたべますか), Đang làm gì (なにをしていますか・だれが〜ていますか)
 */

window.SPEAKING_LESSON_PARTS = {
    "4": {
        "1": "どこ？ (Vị trí, Phương tiện, Thời gian)",
        "2": "どんなところ？ (Đặc điểm, Tính từ, Tồn tại)",
        "3": "きせつ・りょうり (Thời tiết, Món ăn)"
    },
    "5": {
        "1": "しゅうまつ (Cuối tuần, Hành động quá khứ, Đi với ai)",
        "2": "やすみのあとで (Cảm nghĩ, Lý do どうして)",
        "3": "こんどのやすみに (Mong muốn ほしい・〜たい, Mục đích di chuyển)"
    },
    "6": {
        "1": "いっしょにいきませんか (Rủ rê 〜ませんか, Sự kiện であります)",
        "2": "どちらがいいですか (So sánh hơn, So sánh nhất いちばん)",
        "3": "やくそく (Đã làm chưa もう, Gợi ý, Hẹn ước)"
    },
    "7": {
        "1": "みちがわかりません (Vị trí ở đâu, Xung quanh có gì)",
        "2": "パーティーのじゅんび (Công cụ で, Đang làm gì 〜ています)",
        "3": "みんなでたのしいパーティー (Ai đang làm gì, Tập quán ăn uống)"
    }
};

window.RAW_DATABASE_SPEAKING = `
Câu 1 [BÀI 4 - PHẦN 1: どこ？ (Vị trí, Phương tiện, Thời gian)] [LUYỆN NÓI]
うちから がっこうまで どのくらいですか。
  A. 30ぷんくらいです。  ✓
  B. バスで いきます。
  C. がっこうは おおきいです。
  D. 8じからです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Từ nhà bạn đến trường mất khoảng bao lâu?"
💬 Dịch câu trả lời: "Mất khoảng 30 phút."
🌟 Cách trả lời khác để luyện nói:
• あるいて 15ふんくらいです。(Đi bộ mất khoảng 15 phút.)
• でんしゃで 1じかんくらい かかります。(Đi bằng tàu điện mất khoảng 1 tiếng.)
• ちかいですから、すぐですよ。(Vì gần nên đến ngay thôi.)
💡 Mẹo giao tiếp: Khi hỏi khoảng thời gian di chuyển, dùng「どのくらいですか」. Trả lời bằng [khoảng thời gian] +「くらい / ぐらいです」hoặc「〜かかります」.
────────────────────────────────────────────────────────────
Câu 2 [BÀI 4 - PHẦN 1: どこ？ (Vị trí, Phương tiện, Thời gian)] [LUYỆN NÓI]
ハノイから ダナンまで ひこうきで どのくらいですか。
  A. 1じかん20ぷんくらいです。  ✓
  B. ひこうきの きっぷを かいました。
  C. ダナンは きれいな まちです。
  D. ともだちと いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Từ Hà Nội đến Đà Nẵng bằng máy bay mất khoảng bao lâu?"
💬 Dịch câu trả lời: "Mất khoảng 1 tiếng 20 phút."
🌟 Cách trả lời khác để luyện nói:
• くるまで 14じかんくらい かかります。(Đi ô tô mất khoảng 14 tiếng.)
• しんかんせんで 2じかんはんくらいです。(Đi shinkansen mất khoảng 2 tiếng rưỡi.)
💡 Mẹo giao tiếp: Cấu trúc「[Nơi xuất phát]から [Nơi đến]まで [Phương tiện]で どのくらいですか」. Trợ từ「で」dùng chỉ phương tiện di chuyển.
────────────────────────────────────────────────────────────
Câu 3 [BÀI 4 - PHẦN 2: どんなところ？ (Đặc điểm, Tính từ, Tồn tại)] [LUYỆN NÓI]
ベトナムは どんな くにですか。
  A. たべものが おいしくて、ひとが しんせつな くにです。  ✓
  B. ベトナムへ いきたいです。
  C. はい、ベトナムです。
  D. ハノイに あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Việt Nam là một đất nước như thế nào?"
💬 Dịch câu trả lời: "Là đất nước đồ ăn ngon và con người thân thiện."
🌟 Cách trả lời khác để luyện nói:
• あつくて、にぎやかな くにです。(Là một đất nước nóng và náo nhiệt.)
• きれいで、しずかな くにですよ。(Là đất nước đẹp và thanh bình đấy.)
💡 Mẹo giao tiếp:「どんな＋Danh từ」dùng hỏi đặc điểm, bản chất. Câu trả lời thường dùng tính từ bổ nghĩa cho danh từ「[Tính từ] + Nです」hoặc nối tính từ bằng「〜くて / 〜で」.
────────────────────────────────────────────────────────────
Câu 4 [BÀI 4 - PHẦN 2: どんなところ？ (Đặc điểm, Tính từ, Tồn tại)] [LUYỆN NÓI]
ナムさんの まちは どんな ところですか。
  A. みどりが おおくて、しずかな ところです。  ✓
  B. わたしの まちは ハノイの きたです。
  C. いいえ、まちじゃありません。
  D. らいしゅう、まちへ かえります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Quê / Thành phố của Nam là một nơi như thế nào?"
💬 Dịch câu trả lời: "Là nơi nhiều cây xanh và yên tĩnh."
🌟 Cách trả lời khác để luyện nói:
• にぎやかですが、ちょっと うるさいところです。(Náo nhiệt nhưng là nơi hơi ồn ào một chút.)
• うみが きれいで、さかなが おいしいところですよ。(Là nơi biển đẹp và cá rất ngon đấy.)
💡 Mẹo giao tiếp: Khi được hỏi về quê hương, hãy nêu từ 1 đến 2 nét đặc trưng nổi bật (thiên nhiên, nhịp sống, ẩm thực) kèm cảm xúc của mình.
────────────────────────────────────────────────────────────
Câu 5 [BÀI 4 - PHẦN 3: きせつ・りょうり (Thời tiết, Món ăn)] [LUYỆN NÓI]
ベトナムの りょうりは どうですか。
  A. おいしいですが、ちょっと からいです。  ✓
  B. きのう フォーを たべました。
  C. まいにち りょうりを つくります。
  D. レストランで たべます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Món ăn Việt Nam thì thế nào?"
💬 Dịch câu trả lời: "Ngon nhưng hơi cay một chút."
🌟 Cách trả lời khác để luyện nói:
• とても おいしいですよ。フォーが すきです。(Rất ngon đấy ạ. Mình thích phở.)
• あまいですが、たべやすいです。(Hơi ngọt một chút nhưng rất dễ ăn.)
💡 Mẹo giao tiếp:「〜はどうですか」dùng hỏi cảm nhận, ấn tượng trực tiếp về đồ ăn hoặc trải nghiệm. Dùng「〜が」(nhưng) để nối 2 vế tính từ tương phản.
────────────────────────────────────────────────────────────
Câu 6 [BÀI 4 - PHẦN 2: どんなところ？ (Đặc điểm, Tính từ, Tồn tại)] [LUYỆN NÓI]
リンさんの まちは にぎやかですか。
  A. いいえ、あまり にぎやかじゃありません。しずかです。  ✓
  B. はい、しずかです。
  C. いいえ、とても にぎやかです。
  D. まちに デパートが あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của Linh có náo nhiệt / sầm uất không?"
💬 Dịch câu trả lời: "Không, không náo nhiệt lắm. Rất yên tĩnh."
🌟 Cách trả lời khác để luyện nói:
• はい、とても にぎやかですよ。(Vâng, rất náo nhiệt đấy ạ.)
• ひるは にぎやかですが、よるは しずかです。(Ban ngày thì náo nhiệt nhưng ban đêm thì yên tĩnh.)
💡 Mẹo giao tiếp: Phủ định của tính từ đuôi な:「〜じゃありません / 〜ではありません」. Thường kết hợp với phó từ「あまり」(không... lắm).
────────────────────────────────────────────────────────────
Câu 7 [BÀI 4 - PHẦN 2: どんなところ？ (Đặc điểm, Tính từ, Tồn tại)] [LUYỆN NÓI]
ホアンさんの まちは おおきいですか。
  A. いいえ、あまり おおきくないです。ちいさい まちです。  ✓
  B. はい、ちいさいです。
  C. いいえ、おおきいじゃありません。
  D. まちに やまが あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của Hoàng có lớn không?"
💬 Dịch câu trả lời: "Không, không lớn lắm. Là một thị trấn nhỏ."
🌟 Cách trả lời khác để luyện nói:
• はい、とても おおきいまちですよ。(Vâng, là một thành phố rất lớn đấy.)
• あまり おおきくないですが、とても べんりです。(Không lớn lắm nhưng rất tiện lợi.)
💡 Mẹo giao tiếp: Phủ định của tính từ đuôi い: bỏ「い」thay bằng「〜くないです」(おおきい ➔ おおきくないです).
────────────────────────────────────────────────────────────
Câu 8 [BÀI 4 - PHẦN 2: どんなところ？ (Đặc điểm, Tính từ, Tồn tại)] [LUYỆN NÓI]
マイさんの まちに おてらが ありますか。
  A. はい、ふるい おてらが ありますよ。  ✓
  B. はい、おてらへ いきます。
  C. いいえ、おてらが います。
  D. おてらは あしたです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở quê / thành phố của Mai có chùa không?"
💬 Dịch câu trả lời: "Vâng, có một ngôi chùa cổ kính đấy."
🌟 Cách trả lời khác để luyện nói:
• いいえ、おてらは ありませんが、きょうかいが あります。(Không, không có chùa nhưng có nhà thờ.)
• はい、ゆうめいな おてらが ありますよ。(Vâng, có một ngôi chùa rất nổi tiếng đấy.)
💡 Mẹo giao tiếp: Tồn tại của vật thể, công trình, danh lam:「[Nơi chốn]に [Vật]が あります」. Khẳng định dùng「あります」, phủ định dùng「ありません」.
────────────────────────────────────────────────────────────
Câu 9 [BÀI 4 - PHẦN 3: きせつ・りょうり (Thời tiết, Món ăn)] [LUYỆN NÓI]
ハノイは 7がつ、あついですか。
  A. はい、とても あついです。あめも よく ふります。  ✓
  B. はい、7がつに いきます。
  C. いいえ、あついです。
  D. ハノイは ベトナムの まちです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hà Nội vào tháng 7 có nóng không?"
💬 Dịch câu trả lời: "Vâng, rất nóng. Mưa cũng hay rơi nữa."
🌟 Cách trả lời khác để luyện nói:
• はい、とても むしあついですよ。(Vâng, oi bức lắm đấy.)
• いいえ、あまり あつくないです。すずしいですよ。(Không, không nóng lắm đâu. Mát mẻ lắm.)
💡 Mẹo giao tiếp: Mẫu câu hỏi thời tiết theo thời gian:「[Địa điểm]は [Tháng / Mùa]、[Tính từ]ですか」. Trả lời có thể thêm chi tiết thời tiết như mưa (あめ), nắng (いいてんき).
────────────────────────────────────────────────────────────
Câu 10 [BÀI 5 - PHẦN 1: しゅうまつ (Cuối tuần, Hành động quá khứ, Đi với ai)] [LUYỆN NÓI]
きのう、ナムさんは なにを しましたか。
  A. うちで にほんごを べんきょうしました。それから、えいがを みました。  ✓
  B. あした べんきょうします。
  C. きのうは げつようびです。
  D. どこへも いきません。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua Nam đã làm gì thế?"
💬 Dịch câu trả lời: "Mình đã học tiếng Nhật ở nhà. Sau đó, mình xem phim."
🌟 Cách trả lời khác để luyện nói:
• ともだちと カフェで おしゃべりしました。(Tôi đã tán gẫu với bạn ở quán cà phê.)
• いちにちじゅう うちで ゆっくり やすみました。(Tôi đã ở nhà thong thả nghỉ ngơi cả ngày.)
💡 Mẹo giao tiếp: Hỏi hành động quá khứ dùng「なにをしましたか」. Trả lời chia động từ đuôi「〜ました」. Dùng「それから」(sau đó) để kể tiếp hành động thứ hai.
────────────────────────────────────────────────────────────
Câu 11 [BÀI 5 - PHẦN 1: しゅうまつ (Cuối tuần, Hành động quá khứ, Đi với ai)] [LUYỆN NÓI]
きのう どこかへ いきましたか。
  A. いいえ、どこへも いきませんでした。うちに いました。  ✓
  B. はい、どこへも いきました。
  C. きのう いきます。
  D. にちようびでした。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua bạn có đi đâu không?"
💬 Dịch câu trả lời: "Không, tôi không đi đâu cả. Tôi đã ở nhà."
🌟 Cách trả lời khác để luyện nói:
• はい、スーパーへ かいものに いきました。(Có, tôi đã đi siêu thị mua sắm.)
• はい、ともだちの うちへ あそびに いきました。(Có, tôi đã đến nhà bạn chơi.)
💡 Mẹo giao tiếp:「どこかへ」(đi đâu đó không - câu hỏi Có/Không). Nếu không đi đâu, cấu trúc phủ định tuyệt đối là:「いいえ、どこへも いきませんでした」.
────────────────────────────────────────────────────────────
Câu 12 [BÀI 5 - PHẦN 1: しゅうまつ (Cuối tuần, Hành động quá khứ, Đi với ai)] [LUYỆN NÓI]
せんしゅう、リンさんは だれと ばんごはんを たべましたか。
  A. クラスの ともだちと たべました。  ✓
  B. ひとりで たべません。
  C. レストランで たべました。
  D. ラーメンを たべました。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tuần trước Linh đã đi ăn tối cùng ai thế?"
💬 Dịch câu trả lời: "Mình đã ăn cùng bạn bè trong lớp."
🌟 Cách trả lời khác để luyện nói:
• かぞくと いっしょに たべました。(Tôi đã ăn cùng với gia đình.)
• だれとも たべませんでした。ひとりで たべました。(Tôi không ăn cùng ai cả. Tôi đã ăn một mình.)
💡 Mẹo giao tiếp: Hỏi làm việc cùng ai dùng「だれと」. Nếu làm một mình thì dùng「ひとりで」(chú ý không dùng trợ từ と sau ひとり).
────────────────────────────────────────────────────────────
Câu 13 [BÀI 5 - PHẦN 2: やすみのあとで (Cảm nghĩ, Lý do どうして)] [LUYỆN NÓI]
アンさんは きのう どうして がっこうへ いきませんでしたか。
  A. ねつが ありましたから。  ✓
  B. はい、いきませんでした。
  C. バスで いきましたから。
  D. がっこうは ちかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "An ơi, hôm qua sao bạn không đi học thế?"
💬 Dịch câu trả lời: "Tại vì tôi bị sốt."
🌟 Cách trả lời khác để luyện nói:
• あたまが いたかったですから。(Vì tôi đã bị đau đầu.)
• ようじが ありましたから。(Vì tôi có việc bận.)
💡 Mẹo giao tiếp: Hỏi lý do bằng「どうして」. Câu trả lời giải thích lý do luôn kết thúc bằng「〜から / 〜からです」(vì...).
────────────────────────────────────────────────────────────
Câu 14 [BÀI 5 - PHẦN 3: こんどのやすみに (Mong muốn ほしい・〜たい, Mục đích di chuyển)] [LUYỆN NÓI]
いま、トゥアンさんは なにが いちばん ほしいですか。
  A. あたらしい ノートパソコンが ほしいです。  ✓
  B. にほんへ いきたいです。
  C. パソコンを かいました。
  D. いいえ、ほしくないです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hiện giờ Tuấn muốn có thứ gì nhất?"
💬 Dịch câu trả lời: "Mình muốn có một chiếc máy tính xách tay mới."
🌟 Cách trả lời khác để luyện nói:
• くるまが いちばん ほしいです。(Tôi muốn có ô tô nhất.)
• じかんが ほしいですね。(Tôi muốn có thời gian đấy.)
💡 Mẹo giao tiếp:「[Danh từ] が ほしいです」dùng để biểu đạt mong muốn sở hữu một đồ vật/vật chất. Không dùng「ほしい」cho hành động (động từ).
────────────────────────────────────────────────────────────
Câu 15 [BÀI 5 - PHẦN 3: こんどのやすみに (Mong muốn ほしい・〜たい, Mục đích di chuyển)] [LUYỆN NÓI]
いま、マイさんは なにが いちばん すきですか。
  A. にほんの アニメが いちばん すきです。  ✓
  B. サッカーを します。
  C. きのう アニメを みました。
  D. はい、すきです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hiện tại Mai thích cái gì nhất?"
💬 Dịch câu trả lời: "Mình thích anime Nhật Bản nhất."
🌟 Cách trả lời khác để luyện nói:
• バドミントンが いちばん すきです。(Tôi thích cầu lông nhất.)
• ベトナムの たべものが だいすきです。(Tôi cực kỳ thích đồ ăn Việt Nam.)
💡 Mẹo giao tiếp: Cấu trúc hỏi sở thích nổi bật nhất:「なにが いちばん すきですか」. Trả lời:「[Danh từ]が いちばん すきです」.
────────────────────────────────────────────────────────────
Câu 16 [BÀI 5 - PHẦN 3: こんどのやすみに (Mong muốn ほしい・〜たい, Mục đích di chuyển)] [LUYỆN NÓI]
いま、ナムさんは おかねが たくさん あります。なにを したいですか。
  A. せかいじゅうを りょこうしたいです。  ✓
  B. おかねが ほしいです。
  C. ぎんこうへ いきました。
  D. おかねが ありません。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Bây giờ Nam có rất nhiều tiền. Bạn muốn làm gì?"
💬 Dịch câu trả lời: "Tôi muốn đi du lịch vòng quanh thế giới."
🌟 Cách trả lời khác để luyện nói:
• りょうしんに おおきな うちを かってあげたいです。(Tôi muốn mua nhà to cho bố mẹ.)
• にほんへ りゅうがくしたいです。(Tôi muốn đi du học Nhật Bản.)
💡 Mẹo giao tiếp: Biểu đạt mong muốn làm hành động gì của bản thân: chia động từ sang thể「V-たいです」(V-ます bỏ ます thêm たいです).
────────────────────────────────────────────────────────────
Câu 17 [BÀI 5 - PHẦN 3: こんどのやすみに (Mong muốn ほしい・〜たい, Mục đích di chuyển)] [LUYỆN NÓI]
フンさんは あした なにを しに いきますか。
  A. まちへ ふくを かいに いきます。  ✓
  B. ふくを きています。
  C. きのう かいものに いきました。
  D. あした がっこうです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ngày mai Hưng đi làm gì thế?"
💬 Dịch câu trả lời: "Mình lên phố để mua quần áo."
🌟 Cách trả lời khác để luyện nói:
• ともだちと えいがを みに いきます。(Tôi đi để xem phim cùng bạn.)
• おいしいものを たべに いきますよ。(Tôi đi để ăn đồ ngon đấy.)
💡 Mẹo giao tiếp: Biểu đạt mục đích di chuyển:「[Địa điểm]へ [V-bỏ ます / Danh từ]に いきます」. Từ để hỏi mục đích là「なにを しに いきますか」.
────────────────────────────────────────────────────────────
Câu 18 [BÀI 6 - PHẦN 1: いっしょにいきませんか (Rủ rê 〜ませんか, Sự kiện であります)] [LUYỆN NÓI]
こんばん、いっしょに ごはんを たべませんか。
  A. いいですね。ぜひ たべましょう！  ✓
  B. はい、たべました。
  C. いいえ、たべます。
  D. ごはんは おいしいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tối nay cùng đi ăn cơm với mình không?"
💬 Dịch câu trả lời: "Hay quá! Nhất định cùng đi ăn nhé!"
🌟 Cách trả lời khác để luyện nói:
• ええ、いきましょう！なにを たべますか。(Được chứ, đi thôi! Ăn món gì đây?)
• すみません、こんばんは ちょっと ようじが ありますから...(Xin lỗi, tối nay mình có chút việc bận mất rồi...)
💡 Mẹo giao tiếp: Mời mọc, rủ rê lịch sự dùng「〜ませんか」. Nhận lời vui vẻ dùng「いいですね。〜ましょう」. Từ chối khéo léo dùng「ちょっと...＋Lý do＋から」.
────────────────────────────────────────────────────────────
Câu 19 [BÀI 6 - PHẦN 1: いっしょにいきませんか (Rủ rê 〜ませんか, Sự kiện であります)] [LUYỆN NÓI]
にちようび、FPTだいがくで なにが ありますか。
  A. おんがくの フェスティバルが ありますよ。  ✓
  B. だいがくに としょかんが あります。
  C. だいがくで べんきょうします。
  D. はい、あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Chủ nhật này ở Đại học FPT có sự kiện gì thế?"
💬 Dịch câu trả lời: "Có lễ hội âm nhạc đấy."
🌟 Cách trả lời khác để luyện nói:
• サッカーの しあいが あります。(Có trận thi đấu bóng đá.)
• にほんごの スピーチコンテストが ありますよ。(Có cuộc thi hùng biện tiếng Nhật đấy.)
💡 Mẹo giao tiếp: Trợ từ「で」đi với động từ「あります」dùng để diễn tả một sự kiện, hoạt động, lễ hội diễn ra hoặc được tổ chức tại địa điểm đó.
────────────────────────────────────────────────────────────
Câu 20 [BÀI 6 - PHẦN 2: どちらがいいですか (So sánh hơn, So sánh nhất いちばん)] [LUYỆN NÓI]
ベトナムりょうりで なにが いちばん おいしいですか。
  A. フォーが いちばん おいしいです。  ✓
  B. まいにち フォーを たべます。
  C. りょうりを つくります。
  D. きのう フォーを たべました。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong các món ăn Việt Nam, món nào ngon nhất?"
💬 Dịch câu trả lời: "Phở là ngon nhất."
🌟 Cách trả lời khác để luyện nói:
• ブンチャーが いちばん すきですね。(Tôi thích bún chả nhất đấy.)
• フォーが いちばん おいしいと おもいますよ。(Tôi nghĩ phở là ngon nhất đấy.)
💡 Mẹo giao tiếp: So sánh nhất đồ vật:「[Nhóm/Phạm vi]で なにが いちばん [Tính từ]ですか」. Trả lời:「[Vật]が いちばん [Tính từ]です」. Thêm「とおもいます」(tôi nghĩ là) để câu nói thêm tự nhiên.
────────────────────────────────────────────────────────────
Câu 21 [BÀI 6 - PHẦN 2: どちらがいいですか (So sánh hơn, So sánh nhất いちばん)] [LUYỆN NÓI]
クラスで だれが いちばん せが たかいですか。
  A. ナムさんが いちばん せが たかいです。  ✓
  B. ナムさんは がくせいです。
  C. クラスは 30にんです。
  D. はい、せが たかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong lớp học, ai là người cao nhất?"
💬 Dịch câu trả lời: "Nam là người cao nhất."
🌟 Cách trả lời khác để luyện nói:
• フンさんですよ。1メートル80あります。(Là Hưng đấy, bạn ấy cao 1 mét 80.)
• たなかせんせいが いちばん せがたかいです。(Thầy Tanaka là người cao nhất.)
💡 Mẹo giao tiếp: Chiều cao con người dùng cụm tính từ「せが たかい」. Khi so sánh nhất:「[Tên người]さんが いちばん せが たかいです」. Tuyệt đối không lược bỏ「せが」vì「たかい」đơn độc mang nghĩa đắt tiền hoặc độ cao địa hình.
────────────────────────────────────────────────────────────
Câu 22 [BÀI 6 - PHẦN 2: どちらがいいですか (So sánh hơn, So sánh nhất いちばん)] [LUYỆN NÓI]
ベトナムで どこが いちばん にぎやかですか。
  A. ホーチミンしが いちばん にぎやかです。  ✓
  B. ハノイへ いきました。
  C. ホーチミンしに あります。
  D. きれいな ところです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở Việt Nam nơi nào sầm uất / náo nhiệt nhất?"
💬 Dịch câu trả lời: "Thành phố Hồ Chí Minh là náo nhiệt nhất."
🌟 Cách trả lời khác để luyện nói:
• ハノイの きゅうしがいが いちばん にぎやかですよ。(Khu phố cổ Hà Nội là náo nhiệt nhất đấy.)
• だいとしが いちばん にぎやかですね。(Các thành phố lớn là náo nhiệt nhất.)
💡 Mẹo giao tiếp: So sánh nhất về nơi chốn:「[Phạm vi]で どこが いちばん [Tính từ]ですか」. Trả lời:「[Địa điểm]が いちばん [Tính từ]です」.
────────────────────────────────────────────────────────────
Câu 23 [BÀI 6 - PHẦN 2: どちらがいいですか (So sánh hơn, So sánh nhất いちばん)] [LUYỆN NÓI]
にほんで なんがつが いちばん さむいですか。
  A. 1がつが いちばん さむいです。  ✓
  B. ふゆが すきです。
  C. さむくないです。
  D. ゆきが ふります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở Nhật Bản tháng mấy là lạnh nhất?"
💬 Dịch câu trả lời: "Tháng 1 là lạnh nhất."
🌟 Cách trả lời khác để luyện nói:
• 2がつですね。ゆきがたくさん ふりますよ。(Tháng 2 đấy, tuyết rơi nhiều lắm.)
• ハノイでは 6がつが いちばん あついです。(Ở Hà Nội thì tháng 6 là nóng nhất.)
💡 Mẹo giao tiếp: So sánh nhất「いちばん」yêu cầu chọn một mốc thời gian đỉnh điểm nhất:「[Tháng]が いちばん [Tính từ]です」.
────────────────────────────────────────────────────────────
Câu 24 [BÀI 6 - PHẦN 2: どちらがいいですか (So sánh hơn, So sánh nhất いちばん)] [LUYỆN NÓI]
いぬと ねこと どちらが すきですか。
  A. ねこの ほうが すきです。  ✓
  B. いぬの ほうが たかいです。
  C. ねこが いちばんです。
  D. はい、すきです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Giữa chó và mèo bạn thích con nào hơn?"
💬 Dịch câu trả lời: "Mình thích mèo hơn."
🌟 Cách trả lời khác để luyện nói:
• どちらも だいすきです！(Cả hai con mình đều rất thích!)
• いぬのほうが すきですね。かわいいですから。(Mình thích chó hơn đấy, vì chúng đáng yêu.)
💡 Mẹo giao tiếp: So sánh lựa chọn giữa 2 đối tượng:「Aと Bと どちらが [Tính từ]ですか」. Trả lời chọn 1 bên:「[A/B]の ほうが [Tính từ]です」. Nếu thích cả hai:「どちらも [Tính từ]です」.
────────────────────────────────────────────────────────────
Câu 25 [BÀI 6 - PHẦN 3: やくそく (Đã làm chưa もう, Gợi ý, Hẹn ước)] [LUYỆN NÓI]
もう ひるごはんを たべましたか。
  A. いいえ、まだです。いまから たべます。  ✓
  B. いいえ、たべませんでした。
  C. はい、たべません。
  D. ひるごはんは ラーメンです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Bạn đã ăn trưa chưa?"
💬 Dịch câu trả lời: "Chưa, tôi vẫn chưa ăn. Bây giờ tôi mới đi ăn đây."
🌟 Cách trả lời khác để luyện nói:
• はい、もう たべました。おなかが いっぱいです。(Vâng, tôi ăn rồi. No bụng rồi.)
• まだです。いっしょに たべにいきませんか。(Chưa ăn. Cùng đi ăn với mình không?)
💡 Mẹo giao tiếp: Cấu trúc hỏi việc đã làm chưa:「もう V-ましたか」. Khẳng định:「はい、もう V-ました」. Phủ định KHÔNG dùng「〜ませんでした」, mà chuẩn ngữ pháp giao tiếp là:「いいえ、まだです」(Chưa, vẫn chưa).
────────────────────────────────────────────────────────────
Câu 26 [BÀI 7 - PHẦN 1: みちがわかりません (Vị trí ở đâu, Xung quanh có gì)] [LUYỆN NÓI]
FPTだいがくは どこに ありますか。
  A. ハノイの ホアラックに あります。  ✓
  B. だいがくに がくせいが います。
  C. ホアラックに います。
  D. バスで いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trường Đại học FPT nằm ở đâu thế?"
💬 Dịch câu trả lời: "Nằm ở Hòa Lạc, Hà Nội."
🌟 Cách trả lời khác để luyện nói:
• ハノイと ダナンと ホーチミンしなどに あります。(Có ở Hà Nội, Đà Nẵng, TP.HCM, v.v.)
• えきから バスで 30ぷんくらいの ところに あります。(Nằm ở nơi cách ga khoảng 30 phút đi xe buýt.)
💡 Mẹo giao tiếp: Vị trí của địa điểm, công trình vô tri dùng động từ「あります」:「[Địa điểm]に あります」. Câu hỏi vị trí:「どこに ありますか」.
────────────────────────────────────────────────────────────
Câu 27 [BÀI 7 - PHẦN 1: みちがわかりません (Vị trí ở đâu, Xung quanh có gì)] [LUYỆN NÓI]
ナムさんは どこに いますか。
  A. 2かいの きょうしつに いますよ。  ✓
  B. きょうしつに あります。
  C. ナムさんは がくせいです。
  D. きのう あいました。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Bạn Nam đang ở đâu thế?"
💬 Dịch câu trả lời: "Bạn ấy đang ở lớp học tầng 2 đấy."
🌟 Cách trả lời khác để luyện nói:
• しょくいんしつに います。せんせいと はなしています。(Bạn ấy đang ở phòng giáo viên, nói chuyện với thầy cô.)
• としょかんに いますよ。(Cậu ấy đang ở thư viện đấy.)
💡 Mẹo giao tiếp: Vị trí của con người hoặc động vật sống: dùng động từ「います」:「[Địa điểm]に います」. Không dùng「あります」cho người hoặc động vật.
────────────────────────────────────────────────────────────
Câu 28 [BÀI 7 - PHẦN 1: みちがわかりません (Vị trí ở đâu, Xung quanh có gì)] [LUYỆN NÓI]
えきの ちかくに なにが ありますか。
  A. コンビニや ぎんこうなどが あります。  ✓
  B. えきへ いきます。
  C. えきは おおきいです。
  D. でんしゃが います。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở gần nhà ga có những gì thế?"
💬 Dịch câu trả lời: "Có những thứ như cửa hàng tiện lợi, ngân hàng."
🌟 Cách trả lời khác để luyện nói:
• スーパーや カフェが ありますよ。(Có siêu thị và quán cà phê đấy.)
• こうえんが あります。とても しずかですよ。(Có công viên. Rất yên tĩnh đấy.)
💡 Mẹo giao tiếp: Hỏi sự vật quanh một địa điểm:「[Nơi chốn]の ちかくに なにが ありますか」. Dùng「Aや B（など）が あります」để liệt kê đại diện các tiện ích.
────────────────────────────────────────────────────────────
Câu 29 [BÀI 7 - PHẦN 1: みちがわかりません (Vị trí ở đâu, Xung quanh có gì)] [LUYỆN NÓI]
ナムさんの うちの ちかくに なにが ありますか。
  A. おおきな こうえんと スーパーが あります。  ✓
  B. わたしの うちは ハノイです。
  C. うちへ かえります。
  D. はい、ちかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Gần nhà Nam có những gì thế?"
💬 Dịch câu trả lời: "Có một công viên lớn và siêu thị."
🌟 Cách trả lời khác để luyện nói:
• なにも ありません。いなかですから、とても しずかです。(Chẳng có gì cả. Vì là vùng quê nên rất yên bình.)
• おいしい レストランが たくさん ありますよ。(Có rất nhiều nhà hàng ngon đấy.)
💡 Mẹo giao tiếp: Giới thiệu quang cảnh xung quanh nơi mình ở:「[Danh từ]の ちかくに [Công trình]が あります」.
────────────────────────────────────────────────────────────
Câu 30 [BÀI 7 - PHẦN 2: パーティーのじゅんび (Công cụ で, Đang làm gì 〜ています)] [LUYỆN NÓI]
なにで りんごを きりますか。
  A. ナイフで きります。  ✓
  B. スーパーで かいました。
  C. きのう たべました。
  D. りんごは あかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Bạn cắt quả táo bằng cái gì thế?"
💬 Dịch câu trả lời: "Tôi cắt bằng dao."
🌟 Cách trả lời khác để luyện nói:
• ほうちょうで きりますよ。(Tôi cắt bằng dao làm bếp đấy.)
• てで かわを むきます。(Tôi bóc vỏ bằng tay.)
💡 Mẹo giao tiếp: Hỏi công cụ, dụng cụ làm việc gì:「なにで [Hành động]か」. Trả lời:「[Dụng cụ]で [Hành động]ます」. Trợ từ「で」chỉ công cụ / phương tiện.
────────────────────────────────────────────────────────────
Câu 31 [BÀI 7 - PHẦN 2: パーティーのじゅんび (Công cụ で, Đang làm gì 〜ています)] [LUYỆN NÓI]
ベトナムじんは フォークと ナイフで ごはんを たべますか。
  A. いいえ、はしで たべます。  ✓
  B. はい、フォークで たべます。
  C. ごはんを たべません。
  D. レストランで たべます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Việt Nam có ăn cơm bằng dao và nĩa không?"
💬 Dịch câu trả lời: "Không, người Việt ăn bằng đũa."
🌟 Cách trả lời khác để luyện nói:
• いいえ、はしや スプーンで たべます。(Không, chúng tôi ăn bằng đũa hoặc thìa.)
• せいようりょうりを たべるとき、フォークと ナイフを つかいます。(Khi ăn món Tây mới dùng dao và nĩa.)
💡 Mẹo giao tiếp: Trợ từ「で」chỉ dụng cụ ăn uống:「はしで」(bằng đũa),「スプーンで」(bằng thìa),「てで」(bằng tay).
────────────────────────────────────────────────────────────
Câu 32 [BÀI 7 - PHẦN 3: みんなでたのしいパーティー (Ai đang làm gì, Tập quán ăn uống)] [LUYỆN NÓI]
インドじんは なにで ごはんを たべますか。
  A. てで たべます。  ✓
  B. はしで たべます。
  C. カレーを たべます。
  D. うちで たべます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Ấn Độ ăn cơm bằng gì?"
💬 Dịch câu trả lời: "Họ ăn bằng tay."
🌟 Cách trả lời khác để luyện nói:
• にほんじんは はしで たべます。(Người Nhật ăn bằng đũa.)
• アメリカじんは フォークと スプーンと ナイフで たべます。(Người Mỹ ăn bằng nĩa, thìa và dao.)
💡 Mẹo giao tiếp: Điểm văn hóa trong Bài 7 Dekiru Nihongo: Các quốc gia có dụng cụ ăn uống đặc trưng: はし (Nhật, Việt), て (Ấn Độ), フォークとナイフ (Phương Tây).
────────────────────────────────────────────────────────────
Câu 33 [BÀI 7 - PHẦN 2: パーティーのじゅんび (Công cụ で, Đang làm gì 〜ています)] [LUYỆN NÓI]
ナムさんは いま、なにを していますか。
  A. へやで にほんごを べんきょうしています。  ✓
  B. きのう べんきょうしました。
  C. がくせいです。
  D. あした べんきょうします。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hiện giờ Nam đang làm gì thế?"
💬 Dịch câu trả lời: "Bạn ấy đang học tiếng Nhật ở trong phòng."
🌟 Cách trả lời khác để luyện nói:
• ともだちと でんわで はなしていますよ。(Cậu ấy đang nói chuyện điện thoại với bạn đấy.)
• へやで レポートを かいています。(Bạn ấy đang viết báo cáo ở trong phòng.)
💡 Mẹo giao tiếp: Diễn tả hành động đang diễn ra tại thời điểm nói: chia động từ sang thể tiếp diễn「V-ています」(V thể て + います).
────────────────────────────────────────────────────────────
Câu 34 [BÀI 7 - PHẦN 3: みんなでたのしいパーティー (Ai đang làm gì, Tập quán ăn uống)] [LUYỆN NÓI]
だれが ギターを ひいていますか。
  A. ケンさんが ひいていますよ。  ✓
  B. ギターを ひきます。
  C. おんがくしつに あります。
  D. きのう ひきました。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ai đang chơi đàn ghi-ta thế?"
💬 Dịch câu trả lời: "Anh Ken đang chơi đấy."
🌟 Cách trả lời khác để luyện nói:
• リンさんが うたいながら ひいています。(Chị Linh vừa hát vừa đàn đấy.)
• だれも ひいていませんよ。ラジオの おとです。(Chẳng có ai chơi đâu. Là tiếng đài radio đấy.)
💡 Mẹo giao tiếp: Từ để hỏi chủ ngữ「だれ」luôn đi với trợ từ「が」(だれが 〜ていますか). Câu trả lời nêu tên chủ ngữ đi với「が」:「[Người]さんが 〜ています」.
────────────────────────────────────────────────────────────
`;
