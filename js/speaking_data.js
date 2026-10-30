/**
 * KHO DỮ LIỆU CÂU HỎI LUYỆN NÓI NGỮ PHÁP TIẾNG NHẬT JPD123 (BÀI 4 - 7)
 * SỔ TAY ÔN THI SPEAKING JPD123 - TỔNG HỢP BÀI 4 → BÀI 7 (32 DẠNG CÂU HỎI · 61 VÍ DỤ)
 * Đối chiếu “Đề cương FE SPEAKING JPD123 – Ms Thuỷ” với SGK Shokyu JPD123 (Bài 4–7).
 * Nguyên tắc: Mỗi câu hỏi chỉ có MỘT lượt trả lời đầu tiên (giữ cả 2 ý nếu người đối thoại nói liền nhau trong 1 lượt).
 */

window.SPEAKING_LESSON_PARTS = {
    "4": {
        "1": "Dạng 1: Hỏi mất bao lâu giữa hai địa điểm (どのくらい)",
        "2": "Dạng 2: Hỏi thời gian di chuyển bằng phương tiện (でどのくらい)",
        "3": "Dạng 3: Hỏi địa điểm / thành phố / đại học / quốc gia như thế nào (どんな～)",
        "4": "Dạng 4: Hỏi thành phố của bạn như thế nào (どんなところ)",
        "5": "Dạng 5: Hỏi nhận xét / đặc điểm về một nơi (どうですか)",
        "6": "Dạng 6: Hỏi thành phố có nhộn nhịp không (にぎやかですか)",
        "7": "Dạng 7: Hỏi thành phố có lớn không (おおきいですか)",
        "8": "Dạng 8: Hỏi nơi bạn sống có nhà thờ / chùa / núi không (～がありますか)"
    },
    "5": {
        "1": "Dạng 1: Hỏi hôm qua / tuần trước đã làm gì (なにをしましたか)",
        "2": "Dạng 2: Hỏi hôm qua có đi đâu không (どこかへいきましたか)",
        "3": "Dạng 3: Hỏi tuần trước làm việc gì với ai (だれと～ましたか)",
        "4": "Dạng 4: Hỏi vì sao hôm qua không đến trường (どうして～から)",
        "5": "Dạng 5: Hỏi hiện tại muốn thứ gì nhất (なにがいちばんほしいですか)",
        "6": "Dạng 6: Hỏi loại trái cây thích nhất (くだもので なにがいちばんすき)",
        "7": "Dạng 7: Hỏi nếu có nhiều tiền thì muốn làm gì (なにをしたいですか)",
        "8": "Dạng 8: Hỏi ngày mai đi để làm gì (なにをしにいきますか)"
    },
    "6": {
        "1": "Dạng 1: Rủ người khác cùng làm gì (～ませんか・～ましょう)",
        "2": "Dạng 2: Hỏi ở đâu có sự kiện gì (でなにがありますか)",
        "3": "Dạng 3: Hỏi thứ gì đứng đầu trong một nhóm (なにがいちばん)",
        "4": "Dạng 4: Hỏi người nào đứng đầu trong một nhóm (だれがいちばん)",
        "5": "Dạng 5: Hỏi nơi nào đứng đầu trong một nhóm (どこがいちばん)",
        "6": "Dạng 6: Hỏi tháng nào đứng đầu theo một đặc điểm (なんがつがいちばん)",
        "7": "Dạng 7: So sánh hai đối tượng (～と～とどちらが・～のほうが)"
    },
    "7": {
        "1": "Dạng 1: Hỏi nhà / trường / vật ở đâu (どこにありますか)",
        "2": "Dạng 2: Hỏi người / mèo / chó ở đâu (どこにいますか)",
        "3": "Dạng 3: Hỏi gần địa điểm nào đó có gì (ちかくになにがありますか)",
        "4": "Dạng 4: Hỏi gần nhà bạn có gì (うちのちかくになにがありますか)",
        "5": "Dạng 5: Hỏi cắt đồ ăn bằng gì (なにできりますか)",
        "6": "Dạng 6: Hỏi người Việt có ăn cơm bằng dao nĩa không (フォークとナイフで)",
        "7": "Dạng 7: Hỏi người các nước ăn cơm bằng gì (なにでごはんをたべますか)",
        "8": "Dạng 8: Hỏi một người đang làm gì (なにをしていますか)",
        "9": "Dạng 9: Hỏi ai đang thực hiện một hành động (だれが～ていますか)"
    }
};

/**
 * QUY TẮC KIỂM TRA CẤU TRÚC CHO 32 DẠNG SPEAKING
 * Bám sát SGK và Đề cương Ms Thuỷ; kiểm tra đúng cấu trúc ngữ pháp và tính linh hoạt từ vựng.
 */
window.SPEAKING_STRUCTURE_RULES = {
    // === BÀI 4 ===
    "4_1": {
        title: "Dạng 1: Hỏi mất bao lâu giữa hai địa điểm",
        pattern: "～から～までどのくらいですか。",
        structure: "[Thời gian] + くらい / ぐらい (です) HOẶC [Thời gian] + です",
        examples: ["2じかんはん くらいです。", "12じかん くらいです。", "30ぷんくらいです。", "1じかんです。"],
        validate: (norm) => {
            const hasTimeUnit = /(じかん|ふん|ぷん|にち|かげつ|しゅうかん|ねん)/.test(norm);
            const hasEnding = /(くらい|ぐらい|です|はん)/.test(norm);
            return hasTimeUnit && (hasEnding || norm.length >= 4);
        },
        errorMessage: "Cần nêu khoảng thời gian di chuyển kèm 'くらい/ぐらいです' hoặc 'です' (Ví dụ: 2じかんはん くらいです, 12じかん くらいです, 1じかんです)."
    },
    "4_2": {
        title: "Dạng 2: Hỏi thời gian di chuyển bằng phương tiện",
        pattern: "～から～まで～でどのくらいですか。",
        structure: "[Thời gian] (くらい / ぐらい) です",
        examples: ["2じかんはん です。", "2じかんはん くらいです。", "1じかんです。"],
        validate: (norm) => {
            const hasTimeUnit = /(じかん|ふん|ぷん|にち|かげつ|しゅうかん|ねん)/.test(norm);
            const hasEnding = /(です|くらい|ぐらい|はん)/.test(norm);
            return hasTimeUnit && (hasEnding || norm.length >= 4);
        },
        errorMessage: "Cần trả lời thời gian di chuyển kết thúc bằng 'です' hoặc 'くらいです' (Ví dụ: 2じかんはん です, 1じかんくらいです)."
    },
    "4_3": {
        title: "Dạng 3: Hỏi địa điểm / thành phố / đại học / quốc gia như thế nào",
        pattern: "～はどんなところ／まち／だいがく／くにですか。",
        structure: "[Tính từ] + [Danh từ] です (kèm đặc điểm) HOẶC [Tính từ] です",
        examples: ["にぎやかなまちです。ひとが おおいです。", "にぎやかなまちです。", "おおきいだいがくです。", "きれいなくにです。", "いいところです。"],
        validate: (norm) => {
            const hasNounMod = /.+な(まち|ところ|だいがく|くに)/.test(norm) || /.+い(まち|ところ|だいがく|くに)/.test(norm);
            const hasDesu = /(です|でした)$/.test(norm);
            const hasAdjWords = /(にぎやか|きれい|おおきい|ちいさい|しずか|いい|たのしい|ふるい|あたらし|あつい|さむい|すずし|おおい|すくない|ゆうめい)/.test(norm);
            return (hasNounMod && hasDesu) || (hasAdjWords && hasDesu) || hasNounMod || /ひとがおおい/.test(norm);
        },
        errorMessage: "Cần dùng tính từ miêu tả danh từ (Tính từ な + な + N / Tính từ い + N) kết thúc bằng 'です' (Ví dụ: にぎやかなまちです。ひとが おおいです, おおきいだいがくです)."
    },
    "4_4": {
        title: "Dạng 4: Hỏi thành phố của bạn như thế nào",
        pattern: "～さんのまちはどんなところですか。",
        structure: "[Tính từ / Đặc điểm] + ところです (kèm bổ sung) HOẶC [Tính từ] です",
        examples: ["にぎやかなところです。そして、ひとが おおいです。", "にぎやかなところです。", "ひとが おおいところです。", "しずかなところです。", "きれいです。"],
        validate: (norm) => {
            const hasTokoro = /ところ(です)?/.test(norm) || /まち(です)?/.test(norm);
            const hasAdj = /(にぎやか|きれい|おおきい|ちいさい|しずか|いい|たのしい|ふるい|あたらし|おおい|すくない|ゆうめい)/.test(norm);
            const hasDesu = /(です|でした)$/.test(norm);
            return (hasTokoro && hasAdj) || (hasTokoro && norm.length >= 5) || (hasAdj && hasDesu);
        },
        errorMessage: "Cần kết thúc bằng '...ところです' (hoặc '...まちです') miêu tả đặc điểm nơi đó (Ví dụ: にぎやかなところです。そして、ひとが おおいです, ひとがおおいところです)."
    },
    "4_5": {
        title: "Dạng 5: Hỏi nhận xét / đặc điểm về một nơi",
        pattern: "～はどうですか。",
        structure: "[Tính từ] です (hoặc phủ định [Tính từ] くないです / じゃありません)",
        examples: ["きれいです。", "おおきいです。", "しずかです。", "おいしいです。"],
        validate: (norm) => {
            const hasDesu = /(です|でした|くないです|じゃありま|ではない)/.test(norm);
            const hasAdj = /(きれい|おおきい|ちいさい|しずか|にぎやか|いい|たのしい|おいしい|すずしい|あつい|さむい|ふるい|あたらし|ゆうめい|べんり)/.test(norm);
            return (hasAdj && hasDesu) || (hasDesu && norm.length >= 4);
        },
        errorMessage: "Cần trả lời trực tiếp bằng tính từ cảm nhận + 'です' (Ví dụ: きれいです, おおきいです, おいしいです)."
    },
    "4_6": {
        title: "Dạng 6: Hỏi thành phố có nhộn nhịp không",
        pattern: "～さんのまちはにぎやかですか。",
        structure: "Khẳng định: はい、にぎやかです • Phủ định: いいえ、にぎやかじゃありません。しずかです (hoặc いいえ、しずかです)",
        examples: ["はい、にぎやかです。", "いいえ、にぎやかじゃありません。しずかです。", "いいえ、にぎやかじゃありません。", "いいえ、しずかです。"],
        validate: (norm) => {
            const isAffirm = /はい.*(にぎやか|そう)/.test(norm) || norm === 'にぎやかです';
            const isNeg = /いいえ.*(しずか|にぎやかじゃ|にぎやかでは|ちがい)/.test(norm) || /にぎやかじゃありま/.test(norm) || norm === 'しずかです';
            return isAffirm || isNeg;
        },
        errorMessage: "Cần trả lời: 'はい、にぎやかです' (Có, nhộn nhịp) hoặc 'いいえ、にぎやかじゃありません。しずかです' / 'いいえ、しずかです' (Không, không nhộn nhịp. Yên tĩnh)."
    },
    "4_7": {
        title: "Dạng 7: Hỏi thành phố có lớn không",
        pattern: "～さんのまちはおおきいですか。",
        structure: "Khẳng định: はい、おおきいです • Phủ định: いいえ、おおきくないです。ちいさいです (hoặc いいえ、ちいさいです)",
        examples: ["はい、おおきいです。", "いいえ、おおきくないです。ちいさいです。", "いいえ、おおきくないです。", "いいえ、ちいさいです。"],
        validate: (norm) => {
            const isAffirm = /はい.*おおきい/.test(norm) || norm === 'おおきいです';
            const isNeg = /いいえ.*(ちいさい|おおきくない)/.test(norm) || /おおきくない/.test(norm) || norm === 'ちいさいです';
            return isAffirm || isNeg;
        },
        errorMessage: "Cần trả lời: 'はい、おおきいです' (Có, lớn) hoặc 'いいえ、おおきくないです。ちいさいです' / 'いいえ、ちいさいです' (Không, không lớn. Nhỏ)."
    },
    "4_8": {
        title: "Dạng 8: Hỏi nơi bạn sống có nhà thờ / chùa / núi không",
        pattern: "～さんのまちに～がありますか。",
        structure: "Khẳng định: はい、あります • Phủ định: いいえ、ありません",
        examples: ["はい、あります。", "いいえ、ありません。", "はい、おてらがあります。", "いいえ、やまはありません。"],
        validate: (norm) => {
            const isAffirm = /はい.*ありま/.test(norm) || norm === 'あります';
            const isNeg = /いいえ.*ありま/.test(norm) || norm === 'ありません' || norm === 'ないです';
            return isAffirm || isNeg;
        },
        errorMessage: "Cần trả lời: 'はい、あります' (Có) hoặc 'いいえ、ありません' (Không có)."
    },

    // === BÀI 5 ===
    "5_1": {
        title: "Dạng 1: Hỏi hôm qua / tuần trước đã làm gì",
        pattern: "きのう／せんしゅう、～さんはなにをしましたか。",
        structure: "[Hành động] ました (kết hợp それから、[Hành động] ました)",
        examples: ["ともだちのいえへ いきました。それから、ゲームを しました。", "ともだちのいえへ いきました。", "ゲームを しました。", "そうじを しました。", "にほんごを べんきょうしました。"],
        validate: (norm) => {
            return /ました/.test(norm);
        },
        errorMessage: "Cần chia động từ thì quá khứ kết thúc bằng '～ました' (Ví dụ: ともだちのいえへ いきました。それから、ゲームを しました, ゲームを しました, そうじを しました)."
    },
    "5_2": {
        title: "Dạng 2: Hỏi hôm qua có đi đâu không",
        pattern: "きのうどこかへいきましたか。",
        structure: "Khẳng định: はい、[Địa điểm]へ いきました (kèm hành động) • Phủ định: いいえ、どこへも いきませんでした (kèm hoạt động ở nhà)",
        examples: ["はい、デパートへ いきました。デパートで かいものしました。", "はい、デパートへ いきました。", "いいえ、どこへも いきませんでした。うちで テレビを みました。", "いいえ、どこも いきませんでした。"],
        validate: (norm) => {
            const isAffirm = /はい.*(へ|に)?.*いきました/.test(norm) || /デパート.*いきました/.test(norm);
            const isNeg = /いいえ.*(どこ.*いきませんでした|どこへも|どこも)/.test(norm) || /どこ(へ|に)?も.*いきませんでした/.test(norm);
            return isAffirm || isNeg;
        },
        errorMessage: "Khẳng định: 'はい、デパートへ いきました。デパートで かいものしました' • Phủ định: 'いいえ、どこへも いきませんでした。うちで テレビを みました' (hoặc 'どこも いきませんでした')."
    },
    "5_3": {
        title: "Dạng 3: Hỏi tuần trước làm việc gì với ai",
        pattern: "せんしゅう、～さんはだれと～ましたか。",
        structure: "[Người] と ... ました (hoặc ひとりで ... ました)",
        examples: ["ともだちと デパートで かいものしました。", "かぞくと レストランで しょくじしました。", "ともだちと たべました。", "ひとりで べんきょうしました。"],
        validate: (norm) => {
            return /(と|ひとりで).*ました/.test(norm);
        },
        errorMessage: "Cần dùng trợ từ 'と' sau người cùng làm hoặc 'ひとりで' kèm động từ đuôi '～ました' (Ví dụ: ともだちと デパートで かいものしました, かぞくと レストランで しょくじしました)."
    },
    "5_4": {
        title: "Dạng 4: Hỏi vì sao hôm qua không đến trường",
        pattern: "～さんはきのうどうしてがっこうへいきませんでしたか。",
        structure: "[Lý do] + から (hoặc からです / からでした)",
        examples: ["かぜでしたから。", "あめでしたから。", "びょうきですから。", "ようじが ありましたから。"],
        validate: (norm) => {
            return /から/.test(norm);
        },
        errorMessage: "Khi hỏi 'どうして' (tại sao), câu trả lời bắt buộc kết thúc bằng '～から' hoặc '～からです' để nêu lý do (Ví dụ: かぜでしたから, あめでしたから)."
    },
    "5_5": {
        title: "Dạng 5: Hỏi hiện tại muốn thứ gì nhất",
        pattern: "いま、～さんはなにがいちばんほしいですか。",
        structure: "[Đồ vật] が (いちばん) ほしいです",
        examples: ["おかねが いちばん ほしいです。", "じてんしゃが いちばん ほしいです。", "くるまが ほしいです。", "パソコンが ほしいです。"],
        validate: (norm) => {
            return /ほしい/.test(norm);
        },
        errorMessage: "Mong muốn sở hữu một vật dùng cấu trúc: '[Đồ vật] が (いちばん) ほしいです' (Ví dụ: おかねが いちばん ほしいです, じてんしゃが いちばん ほしいです)."
    },
    "5_6": {
        title: "Dạng 6: Hỏi loại trái cây thích nhất",
        pattern: "くだもので なにが いちばん すきですか。",
        structure: "[Tên trái cây] が (いちばん) すきです",
        examples: ["りんごが いちばん すきです。", "バナナが いちばん すきです。", "すいかが すきです。"],
        validate: (norm) => {
            return /すき/.test(norm);
        },
        errorMessage: "Hỏi sở thích nhất trong nhóm dùng cấu trúc: '[Tên quả] が (いちばん) すきです' (Ví dụ: りんごが いちばん すきです, バナナが いちばん すきです)."
    },
    "5_7": {
        title: "Dạng 7: Hỏi nếu có nhiều tiền thì muốn làm gì",
        pattern: "いま、おかねがたくさんあります。なにをしたいですか。",
        structure: "[Hành động] たいです (Động từ thể muốn: V-たいです)",
        examples: ["りょこうしたいです。", "くるまを かいたいです。", "いえを かいたいです。", "あそびたいです。"],
        validate: (norm) => {
            return /たい(です)?$/.test(norm) || /たい/.test(norm);
        },
        errorMessage: "Diễn tả mong muốn làm hành động gì dùng động từ đuôi '～たいです' (Ví dụ: りょこうしたいです, くるまを かいたいです)."
    },
    "5_8": {
        title: "Dạng 8: Hỏi ngày mai đi để làm gì",
        pattern: "～さんはあしたなにをしにいきますか。",
        structure: "[V bỏ ます / Danh từ hành động] に いきます",
        examples: ["えいがを みに いきます。", "かいものに いきます。", "ごはんを たべに いきます。", "あそびに いきます。"],
        validate: (norm) => {
            return /に\s*いきま/.test(norm) || /に\s*いく/.test(norm);
        },
        errorMessage: "Diễn tả mục đích đi đâu dùng: '[Động từ bỏ ます / Danh từ hành động] に いきます' (Ví dụ: えいがを みに いきます, かいものに いきます)."
    },

    // === BÀI 6 ===
    "6_1": {
        title: "Dạng 1: Rủ người khác cùng làm gì",
        pattern: "こんばん、いっしょに～ませんか。",
        structure: "Đồng ý: はい、いいですね。～ましょう • Từ chối: すみません。こんばん は ちょっと……。ようじが ありますから (hoặc いいえ、ちょっと……)",
        examples: [
            "はい、いいですね。たべましょう。",
            "すみません。こんばん は ちょっと……。ようじが ありますから。",
            "すみません。こんばん は ちょっと……。",
            "いいえ、ちょっと……。",
            "たべましょう。"
        ],
        validate: (norm) => {
            const isAgree = /ましょう/.test(norm) || /いいですね/.test(norm);
            const isDecline = /ちょっと/.test(norm) || /すみません/.test(norm) || /ようじが/.test(norm);
            return isAgree || isDecline;
        },
        errorMessage: "Rủ rê '～ませんか': Đồng ý dùng 'はい、いいですね。～ましょう' • Từ chối lịch sự dùng 'すみません。こんばん は ちょっと……。ようじが ありますから' (hoặc 'いいえ、ちょっと……')."
    },
    "6_2": {
        title: "Dạng 2: Hỏi ở đâu có sự kiện gì",
        pattern: "～でなにがありますか。",
        structure: "[Sự kiện] が あります",
        examples: ["サッカーの しあいが あります。", "おまつりが あります。", "セールが あります。", "パーティーが あります。"],
        validate: (norm) => {
            return /ありま/.test(norm);
        },
        errorMessage: "Sự kiện diễn ra ở đâu dùng: '[Sự kiện] が あります' (Ví dụ: サッカーの しあいが あります, おまつりが あります, セールが あります)."
    },
    "6_3": {
        title: "Dạng 3: Hỏi thứ gì đứng đầu trong một nhóm",
        pattern: "～でなにがいちばんAですか。",
        structure: "[Vật] が (いちばん) [Tính từ] です",
        examples: ["りんごが いちばん すきです。", "フォーが いちばん おいしいです。", "くるまが やすいです。"],
        validate: (norm) => {
            return /が/.test(norm) && /(です|だ)$/.test(norm);
        },
        errorMessage: "So sánh nhất đồ vật dùng: '[Vật] が (いちばん) [Tính từ] です' (Ví dụ: りんごが いちばん すきです)."
    },
    "6_4": {
        title: "Dạng 4: Hỏi người nào đứng đầu trong một nhóm",
        pattern: "～でだれがいちばんAですか。",
        structure: "[Người] (さん)? が (いちばん) [Tính từ] です",
        examples: ["ソン・トゥンM-TPが いちばん すきです。", "ソン・トゥンが いちばん すきです。", "ナムさんが いちばん せが たかいです。", "たなかさんが すきです。"],
        validate: (norm) => {
            return /が/.test(norm) && /(です|だ)$/.test(norm);
        },
        errorMessage: "So sánh nhất con người dùng: '[Tên người] が (いちばん) [Tính từ] です' (Ví dụ: ソン・トゥンM-TPが いちばん すきです)."
    },
    "6_5": {
        title: "Dạng 5: Hỏi nơi nào đứng đầu trong một nhóm",
        pattern: "～でどこがいちばんAですか。",
        structure: "[Địa điểm] が (いちばん) [Tính từ] です",
        examples: ["ロシアが いちばん ひろいです。", "ベトナムが いちばん すきです。", "ホーチミンしが いちばん にぎやかです。"],
        validate: (norm) => {
            return /が/.test(norm) && /(です|だ)$/.test(norm);
        },
        errorMessage: "So sánh nhất nơi chốn dùng: '[Địa điểm] が (いちばん) [Tính từ] です' (Ví dụ: ロシアが いちばん ひろいです)."
    },
    "6_6": {
        title: "Dạng 6: Hỏi tháng nào đứng đầu theo một đặc điểm",
        pattern: "～でなんがつがいちばんAですか。",
        structure: "[Số]がつ が (いちばん) [Tính từ] です",
        examples: ["12がつが いちばん さむいです。", "1がつが いちばん さむいです。", "8がつが いちばん あついです。"],
        validate: (norm) => {
            return /(がつ|月).*が/.test(norm) || (/(がつ|月)/.test(norm) && /です$/.test(norm));
        },
        errorMessage: "So sánh nhất tháng trong năm: '[Số]がつ が (いちばん) [Tính từ] です' (Ví dụ: 12がつが いちばん さむいです, 1がつが いちばん さむいです)."
    },
    "6_7": {
        title: "Dạng 7: So sánh hai đối tượng",
        pattern: "～と～とどちらがAですか。",
        structure: "[A / B] の ほうが [Tính từ] です",
        examples: ["Bコースのほうが りょうりが おおいです。", "もみじのほうが やすいです。", "ねこのほうが すきです。"],
        validate: (norm) => {
            return /の\s*ほう\s*が/.test(norm) || /のほうが/.test(norm);
        },
        errorMessage: "So sánh 2 đối tượng (～と～とどちらが...): Câu trả lời bắt buộc dùng cấu trúc '[Đối tượng] の ほうが [Tính từ] です' (Ví dụ: Bコースのほうが りょうりが おおいです, もみじのほうが やすいです)."
    },

    // === BÀI 7 ===
    "7_1": {
        title: "Dạng 1: Hỏi nhà / trường / vật ở đâu",
        pattern: "～さんのうち／FPTだいがくはどこにありますか。",
        structure: "[Vị trí] に あります",
        examples: ["コンビニの まえに あります。", "ホアラックに あります。", "あそこに あります。", "えきの ちかくに あります。"],
        validate: (norm) => {
            return /に\s*ありま/.test(norm);
        },
        errorMessage: "Hỏi vị trí của đồ vật / địa điểm: dùng động từ 'あります' đi với trợ từ 'に' -> '[Vị trí] に あります' (Ví dụ: コンビニの まえに あります)."
    },
    "7_2": {
        title: "Dạng 2: Hỏi người / mèo / chó ở đâu",
        pattern: "～さん／ねこ／いぬはどこにいますか。",
        structure: "[Vị trí] に います",
        examples: ["とけいの したに います。", "へやに います。", "あそこに います。", "きょうしつに います。"],
        validate: (norm) => {
            return /に\s*いま/.test(norm);
        },
        errorMessage: "Hỏi vị trí người / động vật: dùng động từ 'います' đi với trợ từ 'に' -> '[Vị trí] に います' (Ví dụ: とけいの したに います, へやに います)."
    },
    "7_3": {
        title: "Dạng 3: Hỏi gần địa điểm nào đó có gì",
        pattern: "～のちかくになにがありますか。",
        structure: "[Công trình / Vật] が あります",
        examples: ["スーパーが あります。", "ぎんこうが あります。", "コンビニが あります。", "こうえんが あります。"],
        validate: (norm) => {
            return /が\s*ありま/.test(norm) || /ありま/.test(norm);
        },
        errorMessage: "Xung quanh có vật/công trình gì dùng: '[Danh từ] が あります' (Ví dụ: スーパーが あります, ぎんこうが あります)."
    },
    "7_4": {
        title: "Dạng 4: Hỏi gần nhà bạn có gì",
        pattern: "～さんのうちのちかくになにがありますか。",
        structure: "[Cảnh quan / Công trình] が あります",
        examples: ["やまが あります。", "かわが あります。", "きょうかいが あります。", "スーパーが あります。"],
        validate: (norm) => {
            return /が\s*ありま/.test(norm) || /ありま/.test(norm);
        },
        errorMessage: "Giới thiệu quanh nhà có gì dùng: '[Cảnh quan/Vật] が あります' (Ví dụ: やまが あります, かわが あります, きょうかいが あります)."
    },
    "7_5": {
        title: "Dạng 5: Hỏi cắt đồ ăn bằng gì",
        pattern: "なにでパン／やさい／りんごをきりますか。",
        structure: "[Dụng cụ] で きります",
        examples: ["ナイフで きります。", "はさみで きります。"],
        validate: (norm) => {
            return /で\s*きりま/.test(norm) || (/で/.test(norm) && /きり/.test(norm));
        },
        errorMessage: "Công cụ cắt dùng trợ từ 'で' + 'きります' -> '[Dụng cụ] で きります' (Ví dụ: ナイフで きります)."
    },
    "7_6": {
        title: "Dạng 6: Hỏi người Việt có ăn cơm bằng dao nĩa không",
        pattern: "ベトナムじんはフォークとナイフでごはんをたべますか。",
        structure: "いいえ、はしで ごはんを たべます (hoặc いいえ、はしで たべます)",
        examples: ["いいえ、はしで ごはんを たべます。", "いいえ、はしで たべます。"],
        validate: (norm) => {
            return /いいえ/.test(norm) && (/はし/.test(norm) || /たべま/.test(norm));
        },
        errorMessage: "Cần trả lời phủ định và nêu dụng cụ ăn: 'いいえ、はしで ごはんを たべます' (Không, ăn bằng đũa)."
    },
    "7_7": {
        title: "Dạng 7: Hỏi người các nước ăn cơm bằng gì",
        pattern: "～じんはなにでごはんをたべますか。",
        structure: "[Dụng cụ / Tay] で (ごはんを) たべます",
        examples: ["はしで ごはんを たべます。", "フォークと ナイフで ごはんを たべます。", "てで ごはんを たべます。", "はしで たべます。"],
        validate: (norm) => {
            return /で.*たべま/.test(norm);
        },
        errorMessage: "Dụng cụ dùng bữa: '[Dụng cụ/Tay] で ごはんを たべます' (Ví dụ: はしで ごはんを たべます, フォークと ナイフで ごはんを たべます, てで ごはんを たべます)."
    },
    "7_8": {
        title: "Dạng 8: Hỏi một người đang làm gì",
        pattern: "～さんはなにをしていますか。",
        structure: "[Hành động] ています / でいます (thì hiện tại tiếp diễn)",
        examples: ["でんわを しています。", "おさらを あらっています。", "ピアノを ひいています。", "うたを うたっています。", "ほんを よんでいます。"],
        validate: (norm) => {
            return /(ています|でいます)/.test(norm);
        },
        errorMessage: "Hành động đang diễn ra tại thời điểm nói: động từ thể tiếp diễn đuôi '～ています' (Ví dụ: でんわを しています, おさらを あらっています, ピアノを ひいています, うたを うたっています)."
    },
    "7_9": {
        title: "Dạng 9: Hỏi ai đang thực hiện một hành động",
        pattern: "だれが～ていますか。",
        structure: "[Tên người] (さん)? が ... ています / でいます",
        examples: ["メアリーンさんが ギターを ひいています。", "にしかわさんが うたを うたっています。", "アンナさんが でんわを かけています。", "たなかさんが ひいています。"],
        validate: (norm) => {
            return /が.*(ています|でいます)/.test(norm);
        },
        errorMessage: "Hỏi ai đang làm việc gì (だれが...): trả lời '[Tên người]さんが ... ています' (Ví dụ: メアリーンさんが ギターを ひいています, にしかわさんが うたを うたっています, アンナさんが でんわを かけています)."
    }
};

window.RAW_DATABASE_SPEAKING = `
Câu 1 [BÀI 4 - PHẦN 1: Hỏi mất bao lâu giữa hai địa điểm] [LUYỆN NÓI]
とうきょうから ソウルまで どのくらいですか。
  A. 2じかんはん くらいです。  ✓
  B. バスで いきます。
  C. おおきいです。
  D. 8じからです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Từ Tokyo đến Seoul mất bao lâu?"
💬 Dịch câu trả lời: "Khoảng 2 tiếng rưỡi."
💡 Mẹo ngữ pháp: Hỏi thời gian di chuyển:「～から～まで どのくらいですか」. Trả lời: [Thời gian] +「くらい / ぐらいです」hoặc [Thời gian] +「です」.
────────────────────────────────────────────────────────────
Câu 2 [BÀI 4 - PHẦN 1: Hỏi mất bao lâu giữa hai địa điểm] [LUYỆN NÓI]
とうきょうから ローマまで どのくらいですか。
  A. 12じかん くらいです。  ✓
  B. ひこうきを かいました。
  C. きれいです。
  D. ともだちと いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Từ Tokyo đến Rome mất bao lâu?"
💬 Dịch câu trả lời: "Khoảng 12 tiếng."
💡 Mẹo ngữ pháp: Hỏi thời gian di chuyển giữa 2 điểm:「どのくらいですか」. Trả lời:「12じかん くらいです」.
────────────────────────────────────────────────────────────
Câu 3 [BÀI 4 - PHẦN 2: Hỏi thời gian di chuyển bằng phương tiện] [LUYỆN NÓI]
とうきょうから ソウルまで ひこうきで どのくらいですか。
  A. 2じかんはん です。  ✓
  B. ひこうきが あります。
  C. 2じかんに いきます。
  D. でんしゃです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Đi máy bay từ Tokyo đến Seoul mất bao lâu?"
💬 Dịch câu trả lời: "2 tiếng rưỡi."
💡 Mẹo ngữ pháp: Ghi nhớ:「で」đứng sau phương tiện (ひこうきで = bằng máy bay). Trả lời: [Thời gian] +「です」(hoặc「くらいです」).
────────────────────────────────────────────────────────────
Câu 4 [BÀI 4 - PHẦN 3: Hỏi địa điểm / thành phố / đại học / quốc gia như thế nào] [LUYỆN NÓI]
ハノイは どんなまちですか。
  A. にぎやかなまちです。ひとが おおいです。  ✓
  B. まちへ いきます。
  C. ハノイです。
  D. ベトナムに あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hà Nội là thành phố thế nào?"
💬 Dịch câu trả lời: "Là thành phố nhộn nhịp, đông người."
💡 Mẹo ngữ pháp: Ghi nhớ: どんな + danh từ; にぎやか → にぎやかな + danh từ (にぎやかなまちです。ひとが おおいです).
────────────────────────────────────────────────────────────
Câu 5 [BÀI 4 - PHẦN 3: Hỏi địa điểm / thành phố / đại học / quốc gia như thế nào] [LUYỆN NÓI]
FPTだいがくは どんなだいがくですか。
  A. おおきいだいがくです。  ✓
  B. がくせいです。
  C. だいがくへ いきます。
  D. べんきょうします。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Đại học FPT như thế nào?"
💬 Dịch câu trả lời: "Là trường đại học lớn."
💡 Mẹo ngữ pháp: Ghi nhớ: Tính từ đuôi い bổ nghĩa trực tiếp cho danh từ:「おおきいだいがくです」.
────────────────────────────────────────────────────────────
Câu 6 [BÀI 4 - PHẦN 4: Hỏi thành phố của bạn như thế nào] [LUYỆN NÓI]
あなたのまちは どんなところですか。
  A. にぎやかなところです。そして、ひとが おおいです。  ✓
  B. まちです。
  C. きたに あります。
  D. ともだちが います。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố bạn thế nào?"
💬 Dịch câu trả lời: "Là nơi nhộn nhịp và đông người."
💡 Mẹo ngữ pháp: Ghi nhớ: Mẫu trong đề dùng ～さんのまち; khi luyện có thể thay bằng tên bạn học. Nối 2 ý miêu tả bằng「そして」(và):「にぎやかなところです。そして、ひとが おおいです」.
────────────────────────────────────────────────────────────
Câu 7 [BÀI 4 - PHẦN 4: Hỏi thành phố của bạn như thế nào] [LUYỆN NÓI]
あなたのまちは どんなところですか。
  A. ひとが おおいところです。  ✓
  B. ひとが いません。
  C. まちへ かえります。
  D. ちかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố bạn thế nào?"
💬 Dịch câu trả lời: "Là nơi đông người."
💡 Mẹo ngữ pháp: Dùng cụm định ngữ miêu tả đặc điểm nơi chốn:「ひとが おおいところです」(nơi đông người).
────────────────────────────────────────────────────────────
Câu 8 [BÀI 4 - PHẦN 5: Hỏi nhận xét / đặc điểm về một nơi] [LUYỆN NÓI]
ハノイは どうですか。
  A. きれいです。  ✓
  B. まちです。
  C. ハノイに いきます。
  D. ベトナムです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hà Nội thế nào?"
💬 Dịch câu trả lời: "Đẹp."
💡 Mẹo ngữ pháp: Ghi nhớ:「どんな」+ danh từ, còn「どう」đứng độc lập khi hỏi nhận xét, cảm nhận. Trả lời trực tiếp bằng tính từ:「きれいです」.
────────────────────────────────────────────────────────────
Câu 9 [BÀI 4 - PHẦN 5: Hỏi nhận xét / đặc điểm về một nơi] [LUYỆN NÓI]
FPTだいがくは どうですか。
  A. おおきいです。  ✓
  B. だいがくです。
  C. いきました。
  D. あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Đại học FPT thế nào?"
💬 Dịch câu trả lời: "Lớn."
💡 Mẹo ngữ pháp: Trả lời trực tiếp cảm nhận với「どうですか」:「おおきいです」.
────────────────────────────────────────────────────────────
Câu 10 [BÀI 4 - PHẦN 6: Hỏi thành phố có nhộn nhịp không] [LUYỆN NÓI]
あなたのまちは にぎやかですか。
  A. はい、にぎやかです。  ✓
  B. いいえ、にぎやかです。
  C. まちです。
  D. いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của bạn có nhộn nhịp không?"
💬 Dịch câu trả lời: "Có, nhộn nhịp."
💡 Mẹo ngữ pháp: Trả lời khẳng định tính từ đuôi な:「はい、にぎやかです」.
────────────────────────────────────────────────────────────
Câu 11 [BÀI 4 - PHẦN 6: Hỏi thành phố có nhộn nhịp không] [LUYỆN NÓI]
あなたのまちは にぎやかですか。
  A. いいえ、にぎやかじゃありません。しずかです。  ✓
  B. はい、しずかです。
  C. にぎやかでした。
  D. まちに あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của bạn có nhộn nhịp không?"
💬 Dịch câu trả lời: "Không, thành phố không nhộn nhịp. Thành phố yên tĩnh."
💡 Mẹo ngữ pháp: Trả lời phủ định tính từ đuôi な và nêu tính từ đối lập trong cùng một lượt đáp:「いいえ、にぎやかじゃありません。しずかです」.
────────────────────────────────────────────────────────────
Câu 12 [BÀI 4 - PHẦN 7: Hỏi thành phố có lớn không] [LUYỆN NÓI]
あなたのまちは おおきいですか。
  A. はい、おおきいです。  ✓
  B. いいえ、おおきいです。
  C. まちが あります。
  D. おおきくありませんでした。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của bạn có lớn không?"
💬 Dịch câu trả lời: "Có, lớn."
💡 Mẹo ngữ pháp: Trả lời khẳng định tính từ đuôi い:「はい、おおきいです」.
────────────────────────────────────────────────────────────
Câu 13 [BÀI 4 - PHẦN 7: Hỏi thành phố có lớn không] [LUYỆN NÓI]
あなたのまちは おおきいですか。
  A. いいえ、おおきくないです。ちいさいです。  ✓
  B. はい、ちいさいです。
  C. おおきいでした。
  D. まちです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của bạn có lớn không?"
💬 Dịch câu trả lời: "Không, thành phố không lớn, mà nhỏ."
💡 Mẹo ngữ pháp: Trả lời phủ định tính từ đuôi い (おおきくないです) và bổ sung tính từ trái nghĩa (ちいさいです) trong cùng một lượt đáp:「いいえ、おおきくないです。ちいさいです」.
────────────────────────────────────────────────────────────
Câu 14 [BÀI 4 - PHẦN 8: Hỏi nơi bạn sống có nhà thờ / chùa / núi không] [LUYỆN NÓI]
あなたのまちに おてらが ありますか。
  A. はい、あります。  ✓
  B. おてらへ いきます。
  C. いいえ、います。
  D. きのうです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở thành phố bạn có chùa không?"
💬 Dịch câu trả lời: "Có."
💡 Mẹo ngữ pháp: Ghi nhớ: Đề nêu きょうかい (nhà thờ), おてら (chùa), やま (núi). Vật vô tri và công trình dùng「あります」:「はい、あります」.
────────────────────────────────────────────────────────────
Câu 15 [BÀI 4 - PHẦN 8: Hỏi nơi bạn sống có nhà thờ / chùa / núi không] [LUYỆN NÓI]
あなたのまちに やまが ありますか。
  A. いいえ、ありません。  ✓
  B. はい、ありません。
  C. やまへ いきます。
  D. たかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Có núi không?"
💬 Dịch câu trả lời: "Không có."
💡 Mẹo ngữ pháp: Phủ định của「あります」là「ありません」(Không có).
────────────────────────────────────────────────────────────
Câu 16 [BÀI 5 - PHẦN 1: Hỏi hôm qua / tuần trước đã làm gì] [LUYỆN NÓI]
きのう、なにをしましたか。
  A. ともだちのいえへ いきました。それから、ゲームを しました。  ✓
  B. ともだちのいえへ いきます。
  C. あした いきます。
  D. ともだちです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua làm gì?"
💬 Dịch câu trả lời: "Tôi đến nhà bạn. Sau đó, tôi chơi game."
💡 Mẹo ngữ pháp: Ghi nhớ: Thời quá khứ khẳng định: ～ました. Nối 2 ý liên tiếp trong cùng một lượt nói bằng「それから」(sau đó):「ともだちのいえへ いきました。それから、ゲームを しました」.
────────────────────────────────────────────────────────────
Câu 17 [BÀI 5 - PHẦN 1: Hỏi hôm qua / tuần trước đã làm gì] [LUYỆN NÓI]
きのう、なにをしましたか。
  A. ゲームを しました。  ✓
  B. ゲームを します。
  C. ゲームが ほしいです。
  D. おもしろいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua bạn đã làm gì?"
💬 Dịch câu trả lời: "Tôi chơi game."
💡 Mẹo ngữ pháp: Trả lời ngắn gọn thời quá khứ khẳng định:「ゲームを しました」.
────────────────────────────────────────────────────────────
Câu 18 [BÀI 5 - PHẦN 1: Hỏi hôm qua / tuần trước đã làm gì] [LUYỆN NÓI]
せんしゅう、なにをしましたか。
  A. そうじを しました。  ✓
  B. そうじを します。
  C. へやです。
  D. きれいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tuần trước làm gì?"
💬 Dịch câu trả lời: "Tôi dọn dẹp."
💡 Mẹo ngữ pháp:「せんしゅう」(tuần trước) chia quá khứ khẳng định:「そうじを しました」.
────────────────────────────────────────────────────────────
Câu 19 [BÀI 5 - PHẦN 2: Hỏi hôm qua có đi đâu không] [LUYỆN NÓI]
きのう どこかへ いきましたか。
  A. はい、デパートへ いきました。デパートで かいものしました。  ✓
  B. はい、いきませんでした。
  C. デパートが あります。
  D. かいものします。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua có đi đâu không?"
💬 Dịch câu trả lời: "Có, tôi đến cửa hàng bách hóa và mua sắm ở đó."
💡 Mẹo ngữ pháp: Ghi nhớ: どこか = nơi nào đó; で sau địa điểm diễn ra hành động. Giữ cả 2 ý trong cùng một lượt đáp theo SGK:「はい、デパートへ いきました。デパートで かいものしました」.
────────────────────────────────────────────────────────────
Câu 20 [BÀI 5 - PHẦN 2: Hỏi hôm qua có đi đâu không] [LUYỆN NÓI]
きのう どこかへ いきましたか。
  A. いいえ、どこへも いきませんでした。うちで テレビを みました。  ✓
  B. はい、どこへも いきませんでした。
  C. どこかへ いきました。
  D. うちです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua có đi đâu không?"
💬 Dịch câu trả lời: "Không, tôi không đi đâu cả. Tôi xem TV ở nhà."
💡 Mẹo ngữ pháp: Ghi nhớ: どこも + phủ định = không nơi nào. Trả lời phủ định và bổ sung hoạt động tại nhà trong cùng lượt nói:「いいえ、どこへも いきませんでした。うちで テレビを みました」.
────────────────────────────────────────────────────────────
Câu 21 [BÀI 5 - PHẦN 3: Hỏi tuần trước làm việc gì với ai] [LUYỆN NÓI]
せんしゅう、だれと かいものしましたか。
  A. ともだちと デパートで かいものしました。  ✓
  B. ともだちが かいものしました。
  C. デパートへ いきました。
  D. にちようびでした。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tuần trước mua sắm với ai?"
💬 Dịch câu trả lời: "Với bạn bè tại cửa hàng bách hóa."
💡 Mẹo ngữ pháp: Ghi nhớ: だれと = với ai; で sau địa điểm diễn ra hành động:「ともだちと デパートで かいものしました」.
────────────────────────────────────────────────────────────
Câu 22 [BÀI 5 - PHẦN 3: Hỏi tuần trước làm việc gì với ai] [LUYỆN NÓI]
せんしゅう、だれと しょくじしましたか。
  A. かぞくと レストランで しょくじしました。  ✓
  B. かぞくが しょくじしました。
  C. レストランです。
  D. おいしかったです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tuần trước ăn cùng ai?"
💬 Dịch câu trả lời: "Với gia đình tại nhà hàng."
💡 Mẹo ngữ pháp: Trợ từ「と」(cùng với ai) và「で」(tại đâu):「かぞくと レストランで しょくじしました」.
────────────────────────────────────────────────────────────
Câu 23 [BÀI 5 - PHẦN 4: Hỏi vì sao hôm qua không đến trường] [LUYỆN NÓI]
きのう どうして がっこうへ いきませんでしたか。
  A. かぜでしたから。  ✓
  B. かぜでした。
  C. がっこうへ いきますから。
  D. バスで いきました。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Vì sao hôm qua bạn không đến trường?"
💬 Dịch câu trả lời: "Vì bị cảm."
💡 Mẹo ngữ pháp: Ghi nhớ: Dùng ～から để nêu lý do, khác から chỉ điểm bắt đầu ở Bài 4:「かぜでしたから」.
────────────────────────────────────────────────────────────
Câu 24 [BÀI 5 - PHẦN 4: Hỏi vì sao hôm qua không đến trường] [LUYỆN NÓI]
きのう どうして がっこうへ いきませんでしたか。
  A. あめでしたから。  ✓
  B. あめです。
  C. いきませんでしたから。
  D. あした いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Vì sao hôm qua bạn không đến trường?"
💬 Dịch câu trả lời: "Vì trời mưa."
💡 Mẹo ngữ pháp: Nêu lý do thời tiết quá khứ bằng「～でしたから」:「あめでしたから」(bởi vì trời đã mưa).
────────────────────────────────────────────────────────────
Câu 25 [BÀI 5 - PHẦN 5: Hỏi hiện tại muốn thứ gì nhất] [LUYỆN NÓI]
いま、なにが いちばん ほしいですか。
  A. おかねが いちばん ほしいです。  ✓
  B. おかねを かいます。
  C. おかねが あります。
  D. ほしくないです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hiện tại bạn muốn có thứ gì nhất?"
💬 Dịch câu trả lời: "Tôi muốn tiền nhất."
💡 Mẹo ngữ pháp: Ghi nhớ: ほしいです = muốn có một vật. Cấu trúc: [Đồ vật] +「が いちばん ほしいです」.
────────────────────────────────────────────────────────────
Câu 26 [BÀI 5 - PHẦN 5: Hỏi hiện tại muốn thứ gì nhất] [LUYỆN NÓI]
いま、なにが いちばん ほしいですか。
  A. じてんしゃが いちばん ほしいです。  ✓
  B. じてんしゃで いきます。
  C. じてんしゃを のります。
  D. あたらしかったです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hiện tại bạn muốn có thứ gì nhất?"
💬 Dịch câu trả lời: "Tôi muốn xe đạp nhất."
💡 Mẹo ngữ pháp:「[Đồ vật]が いちばん ほしいです」:「じてんしゃが いちばん ほしいです」.
────────────────────────────────────────────────────────────
Câu 27 [BÀI 5 - PHẦN 6: Hỏi loại trái cây thích nhất] [LUYỆN NÓI]
くだもので なにが いちばん すきですか。
  A. りんごが いちばん すきです。  ✓
  B. りんごを たべました。
  C. くだものを かいました。
  D. あかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong các loại trái cây, bạn thích gì nhất?"
💬 Dịch câu trả lời: "Tôi thích táo nhất."
💡 Mẹo ngữ pháp: Trong nhóm: [Nhóm] +「で なにが いちばん すきですか」➔「りんごが いちばん すきです」.
────────────────────────────────────────────────────────────
Câu 28 [BÀI 5 - PHẦN 6: Hỏi loại trái cây thích nhất] [LUYỆN NÓI]
くだもので なにが いちばん すきですか。
  A. バナナが いちばん すきです。  ✓
  B. バナナを かいます。
  C. きいろいです。
  D. すきじゃありません。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong các loại trái cây, bạn thích gì nhất?"
💬 Dịch câu trả lời: "Tôi thích chuối nhất."
💡 Mẹo ngữ pháp: Trả lời quả thích nhất:「バナナが いちばん すきです」.
────────────────────────────────────────────────────────────
Câu 29 [BÀI 5 - PHẦN 7: Hỏi nếu có nhiều tiền thì muốn làm gì] [LUYỆN NÓI]
おかねが たくさん あります。なにを したいですか。
  A. りょこうしたいです。  ✓
  B. りょこうしました。
  C. おかねが ほしいです。
  D. ぎんこうへ いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Bây giờ bạn có nhiều tiền. Bạn muốn làm gì?"
💬 Dịch câu trả lời: "Tôi muốn đi du lịch."
💡 Mẹo ngữ pháp: Ghi nhớ: Động từ dạng ～たいです diễn tả muốn làm việc gì (りょこうします ➔ りょこうしたいです).
────────────────────────────────────────────────────────────
Câu 30 [BÀI 5 - PHẦN 7: Hỏi nếu có nhiều tiền thì muốn làm gì] [LUYỆN NÓI]
おかねが たくさん あります。なにを したいですか。
  A. くるまを かいたいです。  ✓
  B. くるまを かいました。
  C. くるまが あります。
  D. たかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Bây giờ bạn có nhiều tiền. Bạn muốn làm gì?"
💬 Dịch câu trả lời: "Tôi muốn mua ô tô."
💡 Mẹo ngữ pháp: Động từ thể muốn: かいます ➔ かいたいです:「くるまを かいたいです」.
────────────────────────────────────────────────────────────
Câu 31 [BÀI 5 - PHẦN 8: Hỏi ngày mai đi để làm gì] [LUYỆN NÓI]
あした なにを しに いきますか。
  A. えいがを みに いきます。  ✓
  B. えいがを みました。
  C. えいがかんへ いきます。
  D. おもしろいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ngày mai bạn đi để làm gì?"
💬 Dịch câu trả lời: "Tôi đi xem phim."
💡 Mẹo ngữ pháp: Ghi nhớ: Động từ bỏ ます + にいきます để nói mục đích đi: みます ➔「えいがを みに いきます」.
────────────────────────────────────────────────────────────
Câu 32 [BÀI 5 - PHẦN 8: Hỏi ngày mai đi để làm gì] [LUYỆN NÓI]
あした なにを しに いきますか。
  A. かいものに いきます。  ✓
  B. かいものしました。
  C. デパートです。
  D. あしたです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ngày mai bạn đi để làm gì?"
💬 Dịch câu trả lời: "Tôi đi mua sắm."
💡 Mẹo ngữ pháp: Danh từ hành động + にいきます:「かいものに いきます」.
────────────────────────────────────────────────────────────
Câu 33 [BÀI 6 - PHẦN 1: Rủ người khác cùng làm gì] [LUYỆN NÓI]
こんばん、いっしょに ごはんを たべませんか。
  A. はい、いいですね。たべましょう。  ✓
  B. はい、たべました。
  C. ごはんを たべます。
  D. おいしいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tối nay cùng ăn cơm nhé?"
💬 Dịch câu trả lời: "Được, hay đấy. Cùng ăn nhé."
💡 Mẹo ngữ pháp: Ghi nhớ: ～ませんか dùng để rủ rê; ～ましょう để cùng làm:「はい、いいですね。たべましょう」.
────────────────────────────────────────────────────────────
Câu 34 [BÀI 6 - PHẦN 1: Rủ người khác cùng làm gì] [LUYỆN NÓI]
こんばん、いっしょに ごはんを たべませんか。
  A. すみません。こんばん は ちょっと……。ようじが ありますから。  ✓
  B. いいえ、たべません。
  C. たべましょう。
  D. こんばんは。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tối nay cùng ăn cơm nhé?"
💬 Dịch câu trả lời: "Xin lỗi, tối nay tôi không tiện vì có việc bận."
💡 Mẹo ngữ pháp: Ghi nhớ: ～ませんか dùng để rủ rê. Từ chối lịch sự bằng「すみません。こんばん は ちょっと……」và nêu lý do「ようじが ありますから」(vì có việc bận).
────────────────────────────────────────────────────────────
Câu 35 [BÀI 6 - PHẦN 2: Hỏi ở đâu có sự kiện gì] [LUYỆN NÓI]
FPTだいがくで なにが ありますか。
  A. サッカーの しあいが あります。  ✓
  B. がくせいが います。
  C. としょかんが あります。
  D. べんきょうします。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở đại học FPT có gì?"
💬 Dịch câu trả lời: "Có trận bóng đá."
💡 Mẹo ngữ pháp: Ghi nhớ: で chỉ nơi diễn ra sự kiện; あります dùng cho sự kiện:「サッカーの しあいが あります」.
────────────────────────────────────────────────────────────
Câu 36 [BÀI 6 - PHẦN 2: Hỏi ở đâu có sự kiện gì] [LUYỆN NÓI]
ハノイで なにが ありますか。
  A. おまつりが あります。  ✓
  B. ハノイへ いきます。
  C. きれいです。
  D. ひとが います。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở Hà Nội có gì?"
💬 Dịch câu trả lời: "Có lễ hội."
💡 Mẹo ngữ pháp: Sự kiện diễn ra ở đâu: [Địa điểm] +「で」+ [Sự kiện] +「が あります」:「おまつりが あります」.
────────────────────────────────────────────────────────────
Câu 37 [BÀI 6 - PHẦN 2: Hỏi ở đâu có sự kiện gì] [LUYỆN NÓI]
あさくさで なにが ありますか。
  A. セールが あります。  ✓
  B. あさくさへ いきました。
  C. にぎやかです。
  D. おてらです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở Asakusa có gì?"
💬 Dịch câu trả lời: "Có đợt giảm giá."
💡 Mẹo ngữ pháp:「セールが あります」(Có đợt giảm giá / đợt sale).
────────────────────────────────────────────────────────────
Câu 38 [BÀI 6 - PHẦN 3: Hỏi thứ gì đứng đầu trong một nhóm] [LUYỆN NÓI]
くだもので なにが いちばん すきですか。
  A. りんごが いちばん すきです。  ✓
  B. りんごを かいました。
  C. くだものです。
  D. あかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong trái cây, thích loại nào nhất?"
💬 Dịch câu trả lời: "Táo."
💡 Mẹo ngữ pháp: Ghi nhớ: A là tính từ phù hợp, ví dụ すき, やすい, おおきい:「りんごが いちばん すきです」.
────────────────────────────────────────────────────────────
Câu 39 [BÀI 6 - PHẦN 4: Hỏi người nào đứng đầu trong một nhóm] [LUYỆN NÓI]
かしゅで だれが いちばん すきですか。
  A. ソン・トゥンM-TPが いちばん すきです。  ✓
  B. うたを うたいます。
  C. かしゅです。
  D. おんがくを ききます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong các ca sĩ, bạn thích ai nhất?"
💬 Dịch câu trả lời: "Sơn Tùng M-TP."
💡 Mẹo ngữ pháp: Ghi nhớ: Ví dụ ca sĩ trong đề cương là Sơn Tùng M-TP:「ソン・トゥンM-TPが いちばん すきです」.
────────────────────────────────────────────────────────────
Câu 40 [BÀI 6 - PHẦN 5: Hỏi nơi nào đứng đầu trong một nhóm] [LUYỆN NÓI]
せかいで どこが いちばん ひろいですか。
  A. ロシアが いちばん ひろいです。  ✓
  B. ロシアへ いきます。
  C. ひろくないです。
  D. くにです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trên thế giới, nơi nào rộng nhất?"
💬 Dịch câu trả lời: "Nga rộng nhất."
💡 Mẹo ngữ pháp: So sánh nhất nơi chốn:「せかいで どこが いちばん ひろいですか」➔「ロシアが いちばん ひろいです」.
────────────────────────────────────────────────────────────
Câu 41 [BÀI 6 - PHẦN 6: Hỏi tháng nào đứng đầu theo một đặc điểm] [LUYỆN NÓI]
1ねんで なんがつが いちばん さむいですか。
  A. 12がつが いちばん さむいです。  ✓
  B. ふゆが すきです。
  C. さむくないです。
  D. ゆきです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong một năm, tháng nào lạnh nhất?"
💬 Dịch câu trả lời: "Tháng 12."
💡 Mẹo ngữ pháp: Ghi nhớ: Câu hỏi đã được bổ sung か ở cuối khi luyện nói:「12がつが いちばん さむいです」.
────────────────────────────────────────────────────────────
Câu 42 [BÀI 6 - PHẦN 7: So sánh hai đối tượng] [LUYỆN NÓI]
Aコースと Bコースと どちらが りょうりが おおいですか。
  A. Bコースのほうが りょうりが おおいです。  ✓
  B. Aコースが すきです。
  C. りょうりを たべます。
  D. おいしいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Giữa suất A và B, suất nào nhiều món hơn?"
💬 Dịch câu trả lời: "Suất B."
💡 Mẹo ngữ pháp: Ghi nhớ: Đề cương chủ yếu đưa đáp án ở mục này; câu hỏi ví dụ được dựng theo đáp án mẫu:「Bコースのほうが りょうりが おおいです」.
────────────────────────────────────────────────────────────
Câu 43 [BÀI 6 - PHẦN 7: So sánh hai đối tượng] [LUYỆN NÓI]
さくらと もみじと どちらが やすいですか。
  A. もみじのほうが やすいです。  ✓
  B. さくらが やすいです。
  C. たかいです。
  D. きれいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Giữa Sakura và Momiji, cái nào rẻ hơn?"
💬 Dịch câu trả lời: "Momiji."
💡 Mẹo ngữ pháp: Cấu trúc so sánh hơn:「[A/B]の ほうが [Tính từ] です」(もみじのほうが やすいです).
────────────────────────────────────────────────────────────
Câu 44 [BÀI 7 - PHẦN 1: Hỏi nhà / trường / vật ở đâu] [LUYỆN NÓI]
バスていは どこに ありますか。
  A. コンビニの まえに あります。  ✓
  B. バスが います。
  C. バスに のります。
  D. あした いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trạm xe buýt ở đâu?"
💬 Dịch câu trả lời: "Ở phía trước cửa hàng tiện lợi."
💡 Mẹo ngữ pháp: Ghi nhớ: Dùng あります cho đồ vật, công trình và địa điểm:「コンビニの まえに あります」.
────────────────────────────────────────────────────────────
Câu 45 [BÀI 7 - PHẦN 2: Hỏi người / mèo / chó ở đâu] [LUYỆN NÓI]
たなかさんは どこに いますか。
  A. とけいの したに います。  ✓
  B. とけいの したに あります。
  C. たなかさんです。
  D. きのう あいました。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Anh/chị Tanaka ở đâu?"
💬 Dịch câu trả lời: "Ở dưới đồng hồ."
💡 Mẹo ngữ pháp: Ghi nhớ: Dùng います cho người và động vật:「とけいの したに います」.
────────────────────────────────────────────────────────────
Câu 46 [BÀI 7 - PHẦN 3: Hỏi gần địa điểm nào đó có gì] [LUYỆN NÓI]
さくらえきの ちかくに なにが ありますか。
  A. スーパーが あります。  ✓
  B. えきへ いきます。
  C. おおきいです。
  D. でんしゃです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Gần ga Sakura có gì?"
💬 Dịch câu trả lời: "Có siêu thị."
💡 Mẹo ngữ pháp: Ghi nhớ: Đề có hai câu trả lời; câu hỏi minh họa được khôi phục theo mẫu:「スーパーが あります」.
────────────────────────────────────────────────────────────
Câu 47 [BÀI 7 - PHẦN 3: Hỏi gần địa điểm nào đó có gì] [LUYỆN NÓI]
きっさてんの ちかくに なにが ありますか。
  A. ぎんこうが あります。  ✓
  B. コーヒーを のみます。
  C. きっさてんです。
  D. ちかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Gần quán cà phê có gì?"
💬 Dịch câu trả lời: "Có ngân hàng."
💡 Mẹo ngữ pháp: Gần địa điểm có công trình gì:「ぎんこうが あります」(Có ngân hàng).
────────────────────────────────────────────────────────────
Câu 48 [BÀI 7 - PHẦN 4: Hỏi gần nhà bạn có gì] [LUYỆN NÓI]
あなたの うちの ちかくに なにが ありますか。
  A. やまが あります。  ✓
  B. うちへ かえります。
  C. やまへ いきます。
  D. たかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Gần nhà bạn có gì?"
💬 Dịch câu trả lời: "Có núi."
💡 Mẹo ngữ pháp: Ghi nhớ: Đề còn gợi ý きょうかい (nhà thờ):「やまが あります」.
────────────────────────────────────────────────────────────
Câu 49 [BÀI 7 - PHẦN 4: Hỏi gần nhà bạn có gì] [LUYỆN NÓI]
あなたの うちの ちかくに なにが ありますか。
  A. かわが あります。  ✓
  B. かわへ いきます。
  C. みずです。
  D. さかなが います。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Gần nhà bạn có gì?"
💬 Dịch câu trả lời: "Có sông."
💡 Mẹo ngữ pháp: Giới thiệu cảnh quan xung quanh nơi ở:「かわが あります」(Có sông).
────────────────────────────────────────────────────────────
Câu 50 [BÀI 7 - PHẦN 5: Hỏi cắt đồ ăn bằng gì] [LUYỆN NÓI]
なにで パンを きりますか。
  A. ナイフで きります。  ✓
  B. パンを たべました。
  C. パンやさんで かいました。
  D. おいしいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Cắt bánh mì bằng gì?"
💬 Dịch câu trả lời: "Bằng dao."
💡 Mẹo ngữ pháp: Ghi nhớ: で chỉ công cụ:「ナイフで きります」.
────────────────────────────────────────────────────────────
Câu 51 [BÀI 7 - PHẦN 6: Hỏi người Việt có ăn cơm bằng dao nĩa không] [LUYỆN NÓI]
ベトナムじんは フォークと ナイフで ごはんを たべますか。
  A. いいえ、はしで ごはんを たべます。  ✓
  B. はい、ナイフで たべます。
  C. たべません。
  D. レストランです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Việt có ăn cơm bằng dao nĩa không?"
💬 Dịch câu trả lời: "Không, (theo ví dụ trong đề) ăn bằng đũa."
💡 Mẹo ngữ pháp: Ghi nhớ: Đây là câu trả lời ví dụ trong đề, không phải khẳng định mọi người đều như vậy:「いいえ、はしで ごはんを たべます」.
────────────────────────────────────────────────────────────
Câu 52 [BÀI 7 - PHẦN 7: Hỏi người các nước ăn cơm bằng gì] [LUYỆN NÓI]
にほんじんと ベトナムじんは なにで ごはんを たべますか。
  A. はしで ごはんを たべます。  ✓
  B. スプーンです。
  C. ごはんを たべました。
  D. おいしいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Nhật và người Việt ăn cơm bằng dụng cụ gì?"
💬 Dịch câu trả lời: "Theo ví dụ: người Nhật và người Việt ăn bằng đũa."
💡 Mẹo ngữ pháp: Ghi nhớ: Đây là những câu mẫu trong đề; thói quen ăn uống thực tế đa dạng:「はしで ごはんを たべます」.
────────────────────────────────────────────────────────────
Câu 53 [BÀI 7 - PHẦN 7: Hỏi người các nước ăn cơm bằng gì] [LUYỆN NÓI]
アメリカじんは なにで ごはんを たべますか。
  A. フォークと ナイフで ごはんを たべます。  ✓
  B. はしで たべます。
  C. パンを たべます。
  D. アメリカです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Mỹ ăn cơm bằng dụng cụ gì?"
💬 Dịch câu trả lời: "Theo ví dụ: người Mỹ dùng nĩa và dao."
💡 Mẹo ngữ pháp: Dụng cụ ăn uống người Mỹ:「フォークと ナイフで ごはんを たべます」.
────────────────────────────────────────────────────────────
Câu 54 [BÀI 7 - PHẦN 7: Hỏi người các nước ăn cơm bằng gì] [LUYỆN NÓI]
インドじんは なにで ごはんを たべますか。
  A. てで ごはんを たべます。  ✓
  B. はしで たべます。
  C. カレーです。
  D. てが あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Ấn ăn cơm bằng dụng cụ gì?"
💬 Dịch câu trả lời: "Theo ví dụ: người Ấn dùng tay."
💡 Mẹo ngữ pháp: Điểm văn hóa Bài 7:「てで ごはんを たべます」(Ăn bằng tay).
────────────────────────────────────────────────────────────
Câu 55 [BÀI 7 - PHẦN 8: Hỏi một người đang làm gì] [LUYỆN NÓI]
アンナさんは なにを していますか。
  A. でんわを しています。  ✓
  B. でんわを しました。
  C. でんわです。
  D. ともだちです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Anna đang làm gì?"
💬 Dịch câu trả lời: "Anna đang nói chuyện điện thoại."
💡 Mẹo ngữ pháp: Ghi nhớ: Các động tác khác trong đề: nói chuyện, hút thuốc, vẽ tranh, chơi guitar. Động từ tiếp diễn đuôi「～ています」:「でんわを しています」.
────────────────────────────────────────────────────────────
Câu 56 [BÀI 7 - PHẦN 8: Hỏi một người đang làm gì] [LUYỆN NÓI]
パクさんは なにを していますか。
  A. おさらを あらっています。  ✓
  B. おさらを あらいました。
  C. おさらです。
  D. だいどころです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Park đang làm gì?"
💬 Dịch câu trả lời: "Park đang rửa bát."
💡 Mẹo ngữ pháp: Hành động đang tiếp diễn: あらいます ➔ あらっています:「おさらを あらっています」.
────────────────────────────────────────────────────────────
Câu 57 [BÀI 7 - PHẦN 8: Hỏi một người đang làm gì] [LUYỆN NÓI]
マリアさんは なにを していますか。
  A. ピアノを ひいています。  ✓
  B. ピアノを ひきました。
  C. ピアノが あります。
  D. おんがくです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Maria đang làm gì?"
💬 Dịch câu trả lời: "Maria đang chơi đàn piano."
💡 Mẹo ngữ pháp: Chơi nhạc cụ: ひきます ➔ ひいています:「ピアノを ひいています」.
────────────────────────────────────────────────────────────
Câu 58 [BÀI 7 - PHẦN 8: Hỏi một người đang làm gì] [LUYỆN NÓI]
にしかわさんは なにを していますか。
  A. うたを うたっています。  ✓
  B. うたを うたいました。
  C. うたです。
  D. かしゅです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Nishikawa đang làm gì?"
💬 Dịch câu trả lời: "Nishikawa đang hát."
💡 Mẹo ngữ pháp: Hát bài hát: うたいます ➔ うたっています:「うたを うたっています」.
────────────────────────────────────────────────────────────
Câu 59 [BÀI 7 - PHẦN 9: Hỏi ai đang thực hiện một hành động] [LUYỆN NÓI]
だれが ギターを ひいていますか。
  A. メアリーンさんが ギターを ひいています。  ✓
  B. ギターを ひきます。
  C. メアリーンさんです。
  D. おんがくしつです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ai đang chơi guitar?"
💬 Dịch câu trả lời: "Maryn."
💡 Mẹo ngữ pháp: Ghi nhớ: Câu hỏi được minh hoạ từ các hoạt động và hình ở trang 8–9. Trả lời:「メアリーンさんが ギターを ひいています」.
────────────────────────────────────────────────────────────
Câu 60 [BÀI 7 - PHẦN 9: Hỏi ai đang thực hiện một hành động] [LUYỆN NÓI]
だれが うたを うたっていますか。
  A. にしかわさんが うたを うたっています。  ✓
  B. うたを うたいました。
  C. にしかわさんです。
  D. かしゅです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ai đang hát?"
💬 Dịch câu trả lời: "Nishikawa."
💡 Mẹo ngữ pháp: Hỏi chủ ngữ hành động:「だれが」➔「にしかわさんが うたを うたっています」.
────────────────────────────────────────────────────────────
Câu 61 [BÀI 7 - PHẦN 9: Hỏi ai đang thực hiện một hành động] [LUYỆN NÓI]
だれが でんわを かけていますか。
  A. アンナさんが でんわを かけています。  ✓
  B. でんわを かけました。
  C. アンナさんです。
  D. いまです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ai đang gọi điện?"
💬 Dịch câu trả lời: "Anna."
💡 Mẹo ngữ pháp:「アンナさんが でんわを かけています」.
────────────────────────────────────────────────────────────
`;

/**
 * TỔNG HỢP TỪ VỰNG CẦN THUỘC & NGỮ PHÁP TRỌNG TÂM (SỔ TAY BÀI 4 - 7)
 * Tiện ích hỗ trợ tra cứu trực tiếp theo tài liệu đề cương Ms Thuỷ và SGK Shokyu JPD123.
 */
window.SPEAKING_HANDBOOK_VOCAB_GRAMMAR = {
    "4": {
        title: "BÀI 4: Địa điểm, đặc điểm và thời gian di chuyển",
        vocab: [
            { jp: "どのくらい", vi: "bao lâu" },
            { jp: "～から", vi: "từ" },
            { jp: "～まで", vi: "đến" },
            { jp: "～で", vi: "bằng (phương tiện)" },
            { jp: "じかん", vi: "giờ / tiếng" },
            { jp: "はん", vi: "rưỡi" },
            { jp: "くらい", vi: "khoảng" },
            { jp: "ひこうき", vi: "máy bay" },
            { jp: "どんな", vi: "như thế nào (trước danh từ)" },
            { jp: "どう", vi: "như thế nào" },
            { jp: "ところ", vi: "nơi, địa điểm" },
            { jp: "まち", vi: "thành phố, thị trấn" },
            { jp: "だいがく", vi: "đại học" },
            { jp: "くに", vi: "đất nước" },
            { jp: "きれい", vi: "đẹp, sạch" },
            { jp: "にぎやか", vi: "nhộn nhịp" },
            { jp: "しずか", vi: "yên tĩnh" },
            { jp: "おおきい", vi: "to, lớn" },
            { jp: "ちいさい", vi: "nhỏ" },
            { jp: "ひとが おおい", vi: "đông người" },
            { jp: "きょうかい", vi: "nhà thờ" },
            { jp: "おてら", vi: "chùa" },
            { jp: "やま", vi: "núi" },
            { jp: "あります / ありません", vi: "có / không có" }
        ],
        grammar: [
            { pattern: "AからBまで", usage: "Từ A đến B", example: "とうきょうから ソウルまで" },
            { pattern: "Phương tiện + で", usage: "Bằng phương tiện", example: "ひこうきで" },
            { pattern: "どんな + danh từ", usage: "Hỏi đặc điểm / loại", example: "どんなまちですか" },
            { pattern: "Tính từ な + danh từ", usage: "Miêu tả danh từ", example: "にぎやかなまち" },
            { pattern: "Tính từ い + danh từ", usage: "Miêu tả danh từ", example: "おおきいだいがく" },
            { pattern: "Địa điểm に + N が あります", usage: "Có địa điểm / vật ở đâu", example: "まちに おてらが あります" }
        ]
    },
    "5": {
        title: "BÀI 5: Việc đã làm, mong muốn và mục đích",
        vocab: [
            { jp: "きのう", vi: "hôm qua" },
            { jp: "せんしゅう", vi: "tuần trước" },
            { jp: "あした", vi: "ngày mai" },
            { jp: "いま", vi: "bây giờ" },
            { jp: "なに", vi: "cái gì" },
            { jp: "どこか", vi: "nơi nào đó" },
            { jp: "どこも (phủ định)", vi: "không nơi nào" },
            { jp: "だれと", vi: "với ai" },
            { jp: "どうして", vi: "tại sao" },
            { jp: "ともだち", vi: "bạn bè" },
            { jp: "かぞく", vi: "gia đình" },
            { jp: "がっこう", vi: "trường học" },
            { jp: "いえ", vi: "nhà" },
            { jp: "デパート", vi: "cửa hàng bách hóa" },
            { jp: "レストラン", vi: "nhà hàng" },
            { jp: "ゲーム", vi: "trò chơi" },
            { jp: "そうじ", vi: "dọn dẹp" },
            { jp: "しょくじ", vi: "bữa ăn; ăn uống" },
            { jp: "かいもの", vi: "mua sắm" },
            { jp: "かぜ", vi: "cảm lạnh" },
            { jp: "びょうき", vi: "bệnh" },
            { jp: "あめ", vi: "mưa" },
            { jp: "おかね", vi: "tiền" },
            { jp: "じてんしゃ", vi: "xe đạp" },
            { jp: "りんご", vi: "táo" },
            { jp: "バナナ", vi: "chuối" },
            { jp: "りょこう", vi: "du lịch" },
            { jp: "えいが", vi: "phim" },
            { jp: "くるま", vi: "ô tô" },
            { jp: "ほしい", vi: "muốn có" },
            { jp: "いちばん", vi: "nhất" },
            { jp: "たくさん", vi: "nhiều" }
        ],
        grammar: [
            { pattern: "Vました", usage: "Động từ quá khứ khẳng định", example: "ゲームを しました" },
            { pattern: "Vませんでした", usage: "Động từ quá khứ phủ định", example: "いきませんでした" },
            { pattern: "だれと + V", usage: "Làm với ai", example: "ともだちと かいものしました" },
            { pattern: "Lý do + から", usage: "Bởi vì / vì", example: "かぜでしたから" },
            { pattern: "Nがほしいです", usage: "Muốn có thứ gì", example: "おかねが ほしいです" },
            { pattern: "Vたいです", usage: "Muốn làm hành động", example: "りょこうしたいです" },
            { pattern: "V bỏ ます + にいきます", usage: "Đi để làm gì", example: "えいがを みに いきます" },
            { pattern: "Nhóm で + なにが いちばん", usage: "Hỏi cái thích nhất trong nhóm", example: "くだもので なにが いちばん すきですか" }
        ]
    },
    "6": {
        title: "BÀI 6: Rủ rê, sự kiện và so sánh",
        vocab: [
            { jp: "こんばん", vi: "tối nay" },
            { jp: "いっしょに", vi: "cùng nhau" },
            { jp: "ごはん", vi: "cơm, bữa ăn" },
            { jp: "たべます", vi: "ăn" },
            { jp: "いいですね", vi: "hay đấy" },
            { jp: "ちょっと……", vi: "hơi khó / từ chối lịch sự" },
            { jp: "サッカー", vi: "bóng đá" },
            { jp: "しあい", vi: "trận đấu" },
            { jp: "おまつり", vi: "lễ hội" },
            { jp: "セール", vi: "giảm giá" },
            { jp: "かしゅ", vi: "ca sĩ" },
            { jp: "くだもの", vi: "trái cây" },
            { jp: "りんご", vi: "táo" },
            { jp: "せかい", vi: "thế giới" },
            { jp: "ロシア", vi: "Nga" },
            { jp: "ひろい", vi: "rộng" },
            { jp: "さむい", vi: "lạnh" },
            { jp: "なんがつ", vi: "tháng mấy" },
            { jp: "いちばん", vi: "nhất" },
            { jp: "どちら", vi: "cái nào (trong hai)" },
            { jp: "～のほうが", vi: "phía A... hơn" },
            { jp: "りょうり", vi: "món ăn" },
            { jp: "おおい", vi: "nhiều" },
            { jp: "やすい", vi: "rẻ" }
        ],
        grammar: [
            { pattern: "Vませんか", usage: "Rủ người khác cùng làm", example: "いっしょに たべませんか" },
            { pattern: "Vましょう", usage: "Đề nghị cùng làm", example: "たべましょう" },
            { pattern: "Địa điểm で + sự kiện が あります", usage: "Sự kiện diễn ra ở đâu", example: "ハノイで おまつりが あります" },
            { pattern: "Nhóm で + nghi vấn + いちばん", usage: "Ai/cái gì/nơi nào nhất", example: "かしゅで だれが いちばん すきですか" },
            { pattern: "AとBとどちらが～", usage: "So sánh A với B", example: "AとBと どちらが やすいですか" },
            { pattern: "Aのほうが～", usage: "A thì... hơn", example: "もみじのほうが やすいです" }
        ]
    },
    "7": {
        title: "BÀI 7: Vị trí, dụng cụ và hành động đang diễn ra",
        vocab: [
            { jp: "うち", vi: "nhà" },
            { jp: "バスてい", vi: "trạm xe buýt" },
            { jp: "コンビニ", vi: "cửa hàng tiện lợi" },
            { jp: "まえ", vi: "phía trước" },
            { jp: "した", vi: "phía dưới" },
            { jp: "ちかく", vi: "gần" },
            { jp: "とけい", vi: "đồng hồ" },
            { jp: "えき", vi: "nhà ga" },
            { jp: "スーパー", vi: "siêu thị" },
            { jp: "きっさてん", vi: "quán cà phê" },
            { jp: "ぎんこう", vi: "ngân hàng" },
            { jp: "やま", vi: "núi" },
            { jp: "かわ", vi: "sông" },
            { jp: "パン", vi: "bánh mì" },
            { jp: "やさい", vi: "rau" },
            { jp: "りんご", vi: "táo" },
            { jp: "ナイフ", vi: "dao" },
            { jp: "フォーク", vi: "nĩa" },
            { jp: "はし", vi: "đũa" },
            { jp: "て", vi: "tay" },
            { jp: "きります", vi: "cắt" },
            { jp: "たべます", vi: "ăn" },
            { jp: "います", vi: "có (người / động vật)" },
            { jp: "あります", vi: "có (vật / địa điểm)" },
            { jp: "でんわ", vi: "điện thoại" },
            { jp: "はなします", vi: "nói chuyện" },
            { jp: "おさら", vi: "đĩa / bát đĩa" },
            { jp: "あらいます", vi: "rửa" },
            { jp: "タバコ", vi: "thuốc lá" },
            { jp: "すいます", vi: "hút" },
            { jp: "ピアノ", vi: "đàn piano" },
            { jp: "ギター", vi: "đàn guitar" },
            { jp: "ひきます", vi: "chơi (nhạc cụ)" },
            { jp: "え", vi: "tranh" },
            { jp: "かきます", vi: "vẽ" },
            { jp: "うた", vi: "bài hát" },
            { jp: "うたいます", vi: "hát" }
        ],
        grammar: [
            { pattern: "Vật / địa điểm + にあります", usage: "Chỉ nơi có đồ vật / địa điểm", example: "まえに あります" },
            { pattern: "Người / động vật + にいます", usage: "Chỉ nơi có người / thú", example: "したに います" },
            { pattern: "Aのまえ／した／ちかく", usage: "Trước / dưới / gần A", example: "コンビニの まえ" },
            { pattern: "Công cụ + で", usage: "Dùng phương tiện / dụng cụ", example: "ナイフで きります" },
            { pattern: "Vています", usage: "Đang làm gì", example: "おさらを あらっています" },
            { pattern: "だれが + Vていますか", usage: "Hỏi ai đang làm", example: "だれが うたを うたっていますか" },
            { pattern: "Nはどこにいます／ありますか", usage: "Hỏi vị trí của người/vật", example: "たなかさんは どこに いますか" }
        ]
    }
};
