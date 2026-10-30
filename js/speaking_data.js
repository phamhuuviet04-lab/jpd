/**
 * KHO DỮ LIỆU CÂU HỎI LUYỆN NÓI NGỮ PHÁP TIẾNG NHẬT JPD123 (BÀI 4 - 7)
 * SỔ TAY ÔN THI SPEAKING JPD123 - TỔNG HỢP BÀI 4 → BÀI 7 (32 DẠNG CÂU HỎI)
 * Bám sát tài liệu “Đề cương FE SPEAKING_JPD123 – Ms Thuỷ” (9 trang).
 * Hỗ trợ tự do gõ câu trả lời và kiểm tra theo đúng cấu trúc ngữ pháp.
 */

window.SPEAKING_LESSON_PARTS = {
    "4": {
        "1": "Dạng 1: Mất bao lâu giữa hai địa điểm (どのくらい)",
        "2": "Dạng 2: Thời gian theo phương tiện (でどのくらい)",
        "3": "Dạng 3: Địa điểm / Thành phố thế nào (どんな～)",
        "4": "Dạng 4: Thành phố của bạn (どんなところ)",
        "5": "Dạng 5: Nhận xét đặc điểm (どうですか)",
        "6": "Dạng 6: Thành phố có nhộn nhịp không (にぎやかですか)",
        "7": "Dạng 7: Thành phố có lớn không (おおきいですか)",
        "8": "Dạng 8: Có địa điểm / Chùa / Núi không (～がありますか)"
    },
    "5": {
        "1": "Dạng 1: Đã làm gì (Hôm qua / Tuần trước)",
        "2": "Dạng 2: Hôm qua có đi đâu không (どこかへいきましたか)",
        "3": "Dạng 3: Làm việc gì với ai (だれと～ましたか)",
        "4": "Dạng 4: Vì sao hôm qua không đến trường (どうして～から)",
        "5": "Dạng 5: Hiện tại muốn thứ gì nhất (ほしいですか)",
        "6": "Dạng 6: Trái cây thích nhất (なにがいちばんすき)",
        "7": "Dạng 7: Nếu có nhiều tiền thì muốn làm gì (～たいですか)",
        "8": "Dạng 8: Ngày mai đi để làm gì (～にいきますか)"
    },
    "6": {
        "1": "Dạng 1: Rủ rê cùng làm gì (～ませんか・～ましょう)",
        "2": "Dạng 2: Ở đâu có sự kiện gì (でなにがありますか)",
        "3": "Dạng 3: Thứ gì nhất trong nhóm (なにがいちばん)",
        "4": "Dạng 4: Người nào nhất trong nhóm (だれがいちばん)",
        "5": "Dạng 5: Nơi nào nhất trong nhóm (どこがいちばん)",
        "6": "Dạng 6: Tháng nào nhất theo đặc điểm (なんがつがいちばん)",
        "7": "Dạng 7: So sánh hai đối tượng (どちらが～のほうが)"
    },
    "7": {
        "1": "Dạng 1: Nhà / Trường / Đồ vật ở đâu (どこにありますか)",
        "2": "Dạng 2: Người / Mèo / Chó ở đâu (どこにいますか)",
        "3": "Dạng 3: Gần địa điểm có gì (ちかくになにがありますか)",
        "4": "Dạng 4: Gần nhà bạn có gì (うちのちかくになにがありますか)",
        "5": "Dạng 5: Cắt đồ ăn bằng gì (なにできりますか)",
        "6": "Dạng 6: Người Việt có ăn bằng dao nĩa không (フォークとナイフで)",
        "7": "Dạng 7: Người các nước ăn bằng gì (なにでごはんをたべますか)",
        "8": "Dạng 8: Một người đang làm gì (なにをしていますか)",
        "9": "Dạng 9: Ai đang thực hiện hành động (だれが～ていますか)"
    }
};

/**
 * QUY TẮC KIỂM TRA CẤU TRÚC CHO 32 DẠNG SPEAKING
 * Không ép buộc nội dung từ vựng phải giống mẫu, chỉ cần đúng cấu trúc ngữ pháp.
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
        errorMessage: "Cần nêu khoảng thời gian di chuyển kèm 'くらい/ぐらいです' hoặc 'です' (Ví dụ: 2じかんはん くらいです, 30ぷんくらいです, 1じかんです)."
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
        title: "Dạng 3: Hỏi địa điểm/thành phố/đại học/quốc gia như thế nào",
        pattern: "～はどんなところ／まち／だいがく／くにですか。",
        structure: "[Tính từ な] + な + [Danh từ] です HOẶC [Tính từ い] + [Danh từ] です HOẶC [Tính từ] です",
        examples: ["にぎやかなまちです。", "おおきいだいがくです。", "きれいなくにです。", "いいところです。"],
        validate: (norm) => {
            const hasNounMod = /.+な(まち|ところ|だいがく|くに)/.test(norm) || /.+い(まち|ところ|だいがく|くに)/.test(norm);
            const hasDesu = /です$/.test(norm);
            const hasAdjWords = /(にぎやか|きれい|おおきい|ちいさい|しずか|いい|たのしい|ふるい|あたらし|あつい|さむい|すずし|おおい|すくない|ゆうめい)/.test(norm);
            return (hasNounMod && hasDesu) || (hasAdjWords && hasDesu) || hasNounMod;
        },
        errorMessage: "Cần dùng tính từ miêu tả danh từ (Tính từ な + な + N / Tính từ い + N) kết thúc bằng 'です' (Ví dụ: にぎやかなまちです, おおきいだいがくです)."
    },
    "4_4": {
        title: "Dạng 4: Hỏi thành phố của bạn như thế nào",
        pattern: "～さんのまちはどんなところですか。",
        structure: "[Tính từ / Đặc điểm] + ところです HOẶC [Tính từ] です",
        examples: ["にぎやかなところです。", "ひとが おおいところです。", "しずかなところです。", "きれいです。"],
        validate: (norm) => {
            const hasTokoro = /ところ(です)?$/.test(norm) || /まち(です)?$/.test(norm);
            const hasAdj = /(にぎやか|きれい|おおきい|ちいさい|しずか|いい|たのしい|ふるい|あたらし|おおい|すくない|ゆうめい)/.test(norm);
            const hasDesu = /です$/.test(norm);
            return (hasTokoro && hasAdj) || (hasTokoro && norm.length >= 5) || (hasAdj && hasDesu);
        },
        errorMessage: "Cần kết thúc bằng '...ところです' (hoặc '...まちです') miêu tả đặc điểm nơi đó (Ví dụ: にぎやかなところです, ひとがおおいところです)."
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
        structure: "Khẳng định: はい、にぎやかです • Phủ định: いいえ、しずかです / にぎやかじゃありません",
        examples: ["はい、にぎやかです。", "いいえ、しずかです。", "いいえ、にぎやかじゃありません。"],
        validate: (norm) => {
            const isAffirm = /はい.*(にぎやか|そう)/.test(norm) || norm === 'にぎやかです';
            const isNeg = /いいえ.*(しずか|にぎやかじゃ|にぎやかでは|ちがい)/.test(norm) || /にぎやかじゃありま/.test(norm) || norm === 'しずかです';
            return isAffirm || isNeg;
        },
        errorMessage: "Cần trả lời: 'はい、にぎやかです' (Có, nhộn nhịp) hoặc 'いいえ、しずかです' / 'いいえ、にぎやかじゃありません' (Không, yên tĩnh / không nhộn nhịp)."
    },
    "4_7": {
        title: "Dạng 7: Hỏi thành phố có lớn không",
        pattern: "～さんのまちはおおきいですか。",
        structure: "Khẳng định: はい、おおきいです • Phủ định: いいえ、ちいさいです / おおきくないです",
        examples: ["はい、おおきいです。", "いいえ、ちいさいです。", "いいえ、おおきくないです。"],
        validate: (norm) => {
            const isAffirm = /はい.*おおきい/.test(norm) || norm === 'おおきいです';
            const isNeg = /いいえ.*(ちいさい|おおきくない)/.test(norm) || /おおきくない/.test(norm) || norm === 'ちいさいです';
            return isAffirm || isNeg;
        },
        errorMessage: "Cần trả lời: 'はい、おおきいです' (Có, lớn) hoặc 'いいえ、ちいさいです' / 'いいえ、おおきくないです' (Không, nhỏ / không lớn)."
    },
    "4_8": {
        title: "Dạng 8: Hỏi nơi bạn sống có địa điểm không",
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
        structure: "[Hành động] ました (thời quá khứ)",
        examples: ["ともだちのいえへ いきました。", "ゲームを しました。", "そうじを しました。", "にほんごを べんきょうしました。"],
        validate: (norm) => {
            return /ました/.test(norm);
        },
        errorMessage: "Cần chia động từ thì quá khứ kết thúc bằng '～ました' (Ví dụ: ゲームを しました, いえへ いきました, べんきょうしました)."
    },
    "5_2": {
        title: "Dạng 2: Hỏi hôm qua có đi đâu không",
        pattern: "きのうどこかへいきましたか。",
        structure: "Khẳng định: はい、[Địa điểm]へ いきました • Phủ định: いいえ、どこ(へ/に)?も いきませんでした",
        examples: ["はい、デパートへ いきました。", "いいえ、どこも いきませんでした。", "いいえ、どこへも いきませんでした。"],
        validate: (norm) => {
            const isAffirm = /はい.*(へ|に)?.*いきました/.test(norm) || /デパート.*いきました/.test(norm);
            const isNeg = /いいえ.*(どこ.*いきませんでした|どこへも|どこも)/.test(norm) || /どこ(へ|に)?も.*いきませんでした/.test(norm);
            return isAffirm || isNeg;
        },
        errorMessage: "Khẳng định: 'はい、[Địa điểm]へ いきました' • Phủ định: 'いいえ、どこも いきませんでした' (hoặc 'どこへも いきませんでした')."
    },
    "5_3": {
        title: "Dạng 3: Hỏi tuần trước làm việc gì với ai",
        pattern: "せんしゅう、～さんはだれと～ましたか。",
        structure: "[Người] と ... ました (hoặc ひとりで ... ました)",
        examples: ["ともだちと デパートで かいものしました。", "かぞくと レストランで しょくじしました。", "ともだちと たべました。", "ひとりで べんきょうしました。"],
        validate: (norm) => {
            return /(と|ひとりで).*ました/.test(norm);
        },
        errorMessage: "Cần dùng trợ từ 'と' sau người cùng làm hoặc 'ひとりで' kèm động từ đuôi '～ました' (Ví dụ: ともだちと かいものしました, かぞくと たべました)."
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
        errorMessage: "Mong muốn sở hữu một vật dùng cấu trúc: '[Đồ vật] が (いちばん) ほしいです' (Ví dụ: おかねが いちばん ほしいです, くるまが ほしいです)."
    },
    "5_6": {
        title: "Dạng 6: Hỏi loại trái cây thích nhất",
        pattern: "くだもので なにが いちばん すきですか。",
        structure: "[Tên vật/quả] が (いちばん) すきです",
        examples: ["りんごが いちばん すきです。", "バナナが いちばん すきです。", "すいかが すきです。"],
        validate: (norm) => {
            return /すき/.test(norm);
        },
        errorMessage: "Hỏi sở thích nhất dùng cấu trúc: '[Danh từ] が (いちばん) すきです' (Ví dụ: りんごが いちばん すきです, バナナが すきです)."
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
        errorMessage: "Diễn tả mục đích đi đâu dùng: '[Động từ bỏ ます / Danh từ] に いきます' (Ví dụ: えいがを みに いきます, かいものに いきます)."
    },

    // === BÀI 6 ===
    "6_1": {
        title: "Dạng 1: Rủ người khác cùng làm gì",
        pattern: "こんばん、いっしょに～ませんか。",
        structure: "Đồng ý: はい、いいですね。～ましょう • Từ chối: いいえ、ちょっと……",
        examples: ["はい、いいですね。たべましょう。", "いいえ、ちょっと……。", "たべましょう。", "いきましょう。"],
        validate: (norm) => {
            const isAgree = /ましょう/.test(norm) || /いいですね/.test(norm);
            const isDecline = /ちょっと/.test(norm) || /すみません/.test(norm);
            return isAgree || isDecline;
        },
        errorMessage: "Rủ rê '～ませんか': Đồng ý dùng '～ましょう' (vd: たべましょう) • Từ chối lịch sự dùng 'いいえ、ちょっと……'."
    },
    "6_2": {
        title: "Dạng 2: Hỏi ở đâu có sự kiện gì",
        pattern: "～でなにがありますか。",
        structure: "[Sự kiện] が あります",
        examples: ["サッカーの しあいが あります。", "おまつりが あります。", "セールが あります。", "パーティーが あります。"],
        validate: (norm) => {
            return /ありま/.test(norm);
        },
        errorMessage: "Sự kiện diễn ra ở đâu dùng: '[Sự kiện] が あります' (Ví dụ: おまつりが あります, サッカーのしあいが あります)."
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
        examples: ["ソン・トゥンM-TPが いちばん すきです。", "ナムさんが いちばん せが たかいです。", "たなかさんが すきです。"],
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
        errorMessage: "So sánh 2 đối tượng (～と～とどちらが...): Câu trả lời bắt buộc dùng cấu trúc '[Đối tượng] の ほうが [Tính từ] です' (Ví dụ: Bコースのほうが おおいです, もみじのほうが やすいです)."
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
        structure: "いいえ、はしで (ごはんを) たべます",
        examples: ["いいえ、はしで ごはんを たべます。", "いいえ、はしで たべます。"],
        validate: (norm) => {
            return /いいえ/.test(norm) && (/はし/.test(norm) || /たべま/.test(norm));
        },
        errorMessage: "Cần trả lời phủ định và nêu dụng cụ ăn: 'いいえ、はしで ごはんを たべます' (Không, ăn bằng đũa)."
    },
    "7_7": {
        title: "Dạng 7: Hỏi người các nước ăn cơm bằng gì",
        pattern: "～じんはなにでごはんをたべますか。",
        structure: "[Dụng cụ / Bộ phận] で (ごはんを) たべます",
        examples: ["はしで ごはんを たべます。", "フォークと ナイフで ごはんを たべます。", "てで ごはんを たべます。", "はしで たべます。"],
        validate: (norm) => {
            return /で.*たべま/.test(norm);
        },
        errorMessage: "Dụng cụ dùng bữa: '[Dụng cụ/Tay] で ごはんを たべます' (Ví dụ: はしで たべます, フォークとナイフで たべます, てで たべます)."
    },
    "7_8": {
        title: "Dạng 8: Hỏi một người đang làm gì",
        pattern: "～さんはなにをしていますか。",
        structure: "[Hành động] ています / でいます (thì hiện tại tiếp diễn)",
        examples: ["でんわを しています。", "おさらを あらっています。", "ピアノを ひいています。", "うたを うたっています。", "ほんを よんでいます。"],
        validate: (norm) => {
            return /(ています|でいます)/.test(norm);
        },
        errorMessage: "Hành động đang diễn ra tại thời điểm nói: động từ thể tiếp diễn đuôi '～ています' (Ví dụ: でんわを しています, おさらを あらっています, ピアノを ひいています)."
    },
    "7_9": {
        title: "Dạng 9: Hỏi ai đang thực hiện một hành động",
        pattern: "だれが～ていますか。",
        structure: "[Tên người] (さん)? が ... ています / でいます",
        examples: ["メアリーンさんが ギターを ひいています。", "にしかわさんが うたを うたっています。", "アンナさんが でんわを かけています。", "たなかさんが ひいています。"],
        validate: (norm) => {
            return /が.*(ています|でいます)/.test(norm);
        },
        errorMessage: "Hỏi ai đang làm việc gì (だれが...): trả lời '[Tên người]さんが ... ています' (Ví dụ: メアリーンさんが ギターを ひいています, にしかわさんが うたを うたっています)."
    }
};

window.RAW_DATABASE_SPEAKING = `
Câu 1 [BÀI 4 - PHẦN 1: Mất bao lâu giữa hai địa điểm] [LUYỆN NÓI]
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
Câu 2 [BÀI 4 - PHẦN 1: Mất bao lâu giữa hai địa điểm] [LUYỆN NÓI]
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
Câu 3 [BÀI 4 - PHẦN 2: Thời gian theo phương tiện] [LUYỆN NÓI]
とうきょうから ソウルまで ひこうきで どのくらいですか。
  A. 2じかんはん です。  ✓
  B. ひこうきが あります。
  C. 2じかんに いきます。
  D. でんしゃです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Đi máy bay từ Tokyo đến Seoul mất bao lâu?"
💬 Dịch câu trả lời: "2 tiếng rưỡi."
💡 Mẹo ngữ pháp: Trợ từ「で」chỉ phương tiện di chuyển (ひこうきで = bằng máy bay). Trả lời: [Thời gian] +「です」(hoặc「くらいです」).
────────────────────────────────────────────────────────────
Câu 4 [BÀI 4 - PHẦN 3: Địa điểm / Thành phố thế nào] [LUYỆN NÓI]
ハノイは どんなまちですか。
  A. にぎやかなまちです。  ✓
  B. まちへ いきます。
  C. ハノイです。
  D. ベトナムに あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hà Nội là thành phố thế nào?"
💬 Dịch câu trả lời: "Là thành phố nhộn nhịp."
💡 Mẹo ngữ pháp:「どんな＋Danh từ」hỏi đặc điểm. Tính từ đuôi な đứng trước N giữ な (にぎやかなまちです).
────────────────────────────────────────────────────────────
Câu 5 [BÀI 4 - PHẦN 3: Địa điểm / Thành phố thế nào] [LUYỆN NÓI]
FPTだいがくは どんなだいがくですか。
  A. おおきいだいがくです。  ✓
  B. がくせいです。
  C. だいがくへ いきます。
  D. べんきょうします。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Đại học FPT như thế nào?"
💬 Dịch câu trả lời: "Là trường đại học lớn."
💡 Mẹo ngữ pháp: Tính từ đuôi い bổ nghĩa trực tiếp cho danh từ:「おおきいだいがくです」.
────────────────────────────────────────────────────────────
Câu 6 [BÀI 4 - PHẦN 4: Thành phố của bạn] [LUYỆN NÓI]
あなたのまちは どんなところですか。
  A. にぎやかなところです。  ✓
  B. まちです。
  C. きたに あります。
  D. ともだちが います。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố bạn thế nào?"
💬 Dịch câu trả lời: "Là nơi nhộn nhịp."
💡 Mẹo ngữ pháp: Mẫu「～さんのまちは どんなところですか」. Trả lời: [Tính từ] +「ところです」.
────────────────────────────────────────────────────────────
Câu 7 [BÀI 4 - PHẦN 4: Thành phố của bạn] [LUYỆN NÓI]
あなたのまちは どんなところですか。
  A. ひとが おおいところです。  ✓
  B. ひとが いません。
  C. まちへ かえります。
  D. ちかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố bạn thế nào?"
💬 Dịch câu trả lời: "Là nơi đông người."
💡 Mẹo ngữ pháp: Có thể dùng cụm vị ngữ miêu tả:「ひとが おおいところです」(nơi đông người).
────────────────────────────────────────────────────────────
Câu 8 [BÀI 4 - PHẦN 5: Nhận xét đặc điểm] [LUYỆN NÓI]
ハノイは どうですか。
  A. きれいです。  ✓
  B. まちです。
  C. ハノイに いきます。
  D. ベトナムです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hà Nội thế nào?"
💬 Dịch câu trả lời: "Đẹp."
💡 Mẹo ngữ pháp:「～はどうですか」dùng hỏi cảm nhận, nhận xét. Trả lời trực tiếp bằng tính từ:「きれいです」.
────────────────────────────────────────────────────────────
Câu 9 [BÀI 4 - PHẦN 5: Nhận xét đặc điểm] [LUYỆN NÓI]
FPTだいがくは どうですか。
  A. おおきいです。  ✓
  B. だいがくです。
  C. いきました。
  D. あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Đại học FPT thế nào?"
💬 Dịch câu trả lời: "Lớn."
💡 Mẹo ngữ pháp: Trả lời trực tiếp nhận xét:「おおきいです」.
────────────────────────────────────────────────────────────
Câu 10 [BÀI 4 - PHẦN 6: Thành phố có nhộn nhịp không] [LUYỆN NÓI]
あなたのまちは にぎやかですか。
  A. はい、にぎやかです。  ✓
  B. いいえ、にぎやかです。
  C. まちです。
  D. いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của bạn có nhộn nhịp không?"
💬 Dịch câu trả lời: "Có, nhộn nhịp."
💡 Mẹo ngữ pháp: Khẳng định tính từ:「はい、にぎやかです」.
────────────────────────────────────────────────────────────
Câu 11 [BÀI 4 - PHẦN 6: Thành phố có nhộn nhịp không] [LUYỆN NÓI]
あなたのまちは にぎやかですか。
  A. いいえ、しずかです。  ✓
  B. はい、しずかです。
  C. にぎやかでした。
  D. まちに あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của bạn có nhộn nhịp không?"
💬 Dịch câu trả lời: "Không, yên tĩnh."
💡 Mẹo ngữ pháp: Phủ định có thể dùng tính từ trái nghĩa:「いいえ、しずかです」(hoặc「いいえ、にぎやかじゃありません」).
────────────────────────────────────────────────────────────
Câu 12 [BÀI 4 - PHẦN 7: Thành phố có lớn không] [LUYỆN NÓI]
あなたのまちは おおきいですか。
  A. はい、おおきいです。  ✓
  B. いいえ、おおきいです。
  C. まちが あります。
  D. おおきくありませんでした。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của bạn có lớn không?"
💬 Dịch câu trả lời: "Có, lớn."
💡 Mẹo ngữ pháp: Khẳng định tính từ đuôi い:「はい、おおきいです」.
────────────────────────────────────────────────────────────
Câu 13 [BÀI 4 - PHẦN 7: Thành phố có lớn không] [LUYỆN NÓI]
あなたのまちは おおきいですか。
  A. いいえ、ちいさいです。  ✓
  B. はい、ちいさいです。
  C. おおきいでした。
  D. まちです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Thành phố của bạn có lớn không?"
💬 Dịch câu trả lời: "Không, nhỏ."
💡 Mẹo ngữ pháp: Phủ định dùng từ trái nghĩa:「いいえ、ちいさいです」(hoặc「いいえ、おおきくないです」).
────────────────────────────────────────────────────────────
Câu 14 [BÀI 4 - PHẦN 8: Có địa điểm / Chùa / Núi không] [LUYỆN NÓI]
あなたのまちに おてらが ありますか。
  A. はい、あります。  ✓
  B. おてらへ いきます。
  C. いいえ、います。
  D. きのうです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở thành phố bạn có chùa không?"
💬 Dịch câu trả lời: "Có."
💡 Mẹo ngữ pháp: Hỏi sự tồn tại của vật thể, công trình:「～がありますか」. Khẳng định:「はい、あります」.
────────────────────────────────────────────────────────────
Câu 15 [BÀI 4 - PHẦN 8: Có địa điểm / Chùa / Núi không] [LUYỆN NÓI]
あなたのまちに やまが ありますか。
  A. いいえ、ありません。  ✓
  B. はい、ありません。
  C. やまへ いきます。
  D. たかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở thành phố bạn có núi không?"
💬 Dịch câu trả lời: "Không có."
💡 Mẹo ngữ pháp: Phủ định của「あります」là「ありません」(Không có).
────────────────────────────────────────────────────────────
Câu 16 [BÀI 5 - PHẦN 1: Đã làm gì (Hôm qua / Tuần trước)] [LUYỆN NÓI]
きのう、なにをしましたか。
  A. ともだちのいえへ いきました。  ✓
  B. ともだちのいえへ いきます。
  C. あした いきます。
  D. ともだちです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua bạn đã làm gì?"
💬 Dịch câu trả lời: "Tôi đến nhà bạn."
💡 Mẹo ngữ pháp: Quá khứ khẳng định động từ chia đuôi「～ました」(いきました).
────────────────────────────────────────────────────────────
Câu 17 [BÀI 5 - PHẦN 1: Đã làm gì (Hôm qua / Tuần trước)] [LUYỆN NÓI]
きのう、なにをしましたか。
  A. ゲームを しました。  ✓
  B. ゲームを します。
  C. ゲームが ほしいです。
  D. おもしろいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua bạn đã làm gì?"
💬 Dịch câu trả lời: "Tôi chơi game."
💡 Mẹo ngữ pháp: Quá khứ:「ゲームを しました」.
────────────────────────────────────────────────────────────
Câu 18 [BÀI 5 - PHẦN 1: Đã làm gì (Hôm qua / Tuần trước)] [LUYỆN NÓI]
せんしゅう、なにをしましたか。
  A. そうじを しました。  ✓
  B. そうじを します。
  C. へやです。
  D. きれいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tuần trước bạn đã làm gì?"
💬 Dịch câu trả lời: "Tôi dọn dẹp."
💡 Mẹo ngữ pháp: せんしゅう (tuần trước) chia quá khứ:「そうじを しました」.
────────────────────────────────────────────────────────────
Câu 19 [BÀI 5 - PHẦN 2: Hôm qua có đi đâu không] [LUYỆN NÓI]
きのう どこかへ いきましたか。
  A. はい、デパートへ いきました。  ✓
  B. はい、いきませんでした。
  C. デパートが あります。
  D. かいものします。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua bạn có đi đâu không?"
💬 Dịch câu trả lời: "Có, tôi đã đến trung tâm thương mại."
💡 Mẹo ngữ pháp: どこかへ = nơi nào đó. Khẳng định:「はい、[Địa điểm]へ いきました」.
────────────────────────────────────────────────────────────
Câu 20 [BÀI 5 - PHẦN 2: Hôm qua có đi đâu không] [LUYỆN NÓI]
きのう どこかへ いきましたか。
  A. いいえ、どこも いきませんでした。  ✓
  B. はい、どこも いきませんでした。
  C. どこかへ いきました。
  D. うちです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hôm qua bạn có đi đâu không?"
💬 Dịch câu trả lời: "Không, tôi không đi đâu cả."
💡 Mẹo ngữ pháp: Phủ định hoàn toàn:「いいえ、どこも いきませんでした」(hoặc「どこへも いきませんでした」).
────────────────────────────────────────────────────────────
Câu 21 [BÀI 5 - PHẦN 3: Làm việc gì với ai] [LUYỆN NÓI]
せんしゅう、だれと かいものしましたか。
  A. ともだちと デパートで かいものしました。  ✓
  B. ともだちが かいものしました。
  C. デパートへ いきました。
  D. にちようびでした。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tuần trước mua sắm với ai?"
💬 Dịch câu trả lời: "Với bạn bè tại cửa hàng bách hóa."
💡 Mẹo ngữ pháp: だれと = với ai. Trả lời: [Người] +「と」... ました. Trợ từ「で」chỉ nơi diễn ra hành động.
────────────────────────────────────────────────────────────
Câu 22 [BÀI 5 - PHẦN 3: Làm việc gì với ai] [LUYỆN NÓI]
せんしゅう、だれと しょくじしましたか。
  A. かぞくと レストランで しょくじしました。  ✓
  B. かぞくが しょくじしました。
  C. レストランです。
  D. おいしかったです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tuần trước ăn cùng ai?"
💬 Dịch câu trả lời: "Với gia đình tại nhà hàng."
💡 Mẹo ngữ pháp:「[Người]と [Địa điểm]で しょくじしました」.
────────────────────────────────────────────────────────────
Câu 23 [BÀI 5 - PHẦN 4: Vì sao hôm qua không đến trường] [LUYỆN NÓI]
きのう どうして がっこうへ いきませんでしたか。
  A. かぜでしたから。  ✓
  B. かぜでした。
  C. がっこうへ いきますから。
  D. バスで いきました。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Vì sao hôm qua bạn không đến trường?"
💬 Dịch câu trả lời: "Vì bị cảm."
💡 Mẹo ngữ pháp: Hỏi「どうして」(tại sao), câu trả lời kết thúc bằng「～から」(vì...).
────────────────────────────────────────────────────────────
Câu 24 [BÀI 5 - PHẦN 4: Vì sao hôm qua không đến trường] [LUYỆN NÓI]
きのう どうして がっこうへ いきませんでしたか。
  A. あめでしたから。  ✓
  B. あめです。
  C. いきませんでしたから。
  D. あした いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Vì sao hôm qua bạn không đến trường?"
💬 Dịch câu trả lời: "Vì trời mưa."
💡 Mẹo ngữ pháp: Nêu lý do trong quá khứ:「あめでしたから」(bởi vì trời đã mưa).
────────────────────────────────────────────────────────────
Câu 25 [BÀI 5 - PHẦN 5: Hiện tại muốn thứ gì nhất] [LUYỆN NÓI]
いま、なにが いちばん ほしいですか。
  A. おかねが いちばん ほしいです。  ✓
  B. おかねを かいます。
  C. おかねが あります。
  D. ほしくないです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hiện tại bạn muốn có thứ gì nhất?"
💬 Dịch câu trả lời: "Tôi muốn tiền nhất."
💡 Mẹo ngữ pháp: Mong muốn sở hữu đồ vật:「[Đồ vật]が (いちばん) ほしいです」.
────────────────────────────────────────────────────────────
Câu 26 [BÀI 5 - PHẦN 5: Hiện tại muốn thứ gì nhất] [LUYỆN NÓI]
いま、なにが いちばん ほしいですか。
  A. じてんしゃが いちばん ほしいです。  ✓
  B. じてんしゃで いきます。
  C. じてんしゃを のります。
  D. あたらしかったです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Hiện tại bạn muốn có thứ gì nhất?"
💬 Dịch câu trả lời: "Tôi muốn xe đạp nhất."
💡 Mẹo ngữ pháp:「[Đồ vật]が いちばん ほしいです」.
────────────────────────────────────────────────────────────
Câu 27 [BÀI 5 - PHẦN 6: Trái cây thích nhất] [LUYỆN NÓI]
くだもので なにが いちばん すきですか。
  A. りんごが いちばん すきです。  ✓
  B. りんごを たべました。
  C. くだものを かいました。
  D. あかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong các loại trái cây, bạn thích gì nhất?"
💬 Dịch câu trả lời: "Tôi thích táo nhất."
💡 Mẹo ngữ pháp: Nhóm「で なにが いちばん すきですか」. Trả lời:「[Danh từ]が いちばん すきです」.
────────────────────────────────────────────────────────────
Câu 28 [BÀI 5 - PHẦN 6: Trái cây thích nhất] [LUYỆN NÓI]
くだもので なにが いちばん すきですか。
  A. バナナが いちばん すきです。  ✓
  B. バナナを かいます。
  C. きいろいです。
  D. すきじゃありません。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong các loại trái cây, bạn thích gì nhất?"
💬 Dịch câu trả lời: "Tôi thích chuối nhất."
💡 Mẹo ngữ pháp:「[Quả]が いちばん すきです」.
────────────────────────────────────────────────────────────
Câu 29 [BÀI 5 - PHẦN 7: Nếu có nhiều tiền thì muốn làm gì] [LUYỆN NÓI]
おかねが たくさん あります。なにを したいですか。
  A. りょこうしたいです。  ✓
  B. りょこうしました。
  C. おかねが ほしいです。
  D. ぎんこうへ いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Bây giờ bạn có nhiều tiền. Bạn muốn làm gì?"
💬 Dịch câu trả lời: "Tôi muốn đi du lịch."
💡 Mẹo ngữ pháp: Muốn làm hành động gì dùng động từ thể「～たいです」(V-たいです).
────────────────────────────────────────────────────────────
Câu 30 [BÀI 5 - PHẦN 7: Nếu có nhiều tiền thì muốn làm gì] [LUYỆN NÓI]
おかねが たくさん あります。なにを したいですか。
  A. くるまを かいたいです。  ✓
  B. くるまを かいました。
  C. くるまが あります。
  D. たかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Bây giờ bạn có nhiều tiền. Bạn muốn làm gì?"
💬 Dịch câu trả lời: "Tôi muốn mua ô tô."
💡 Mẹo ngữ pháp: かいます ➔ かいたいです (muốn mua).
────────────────────────────────────────────────────────────
Câu 31 [BÀI 5 - PHẦN 8: Ngày mai đi để làm gì] [LUYỆN NÓI]
あした なにを しに いきますか。
  A. えいがを みに いきます。  ✓
  B. えいがを みました。
  C. えいがかんへ いきます。
  D. おもしろいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ngày mai bạn đi để làm gì?"
💬 Dịch câu trả lời: "Tôi đi xem phim."
💡 Mẹo ngữ pháp: Diễn tả mục đích đi:「[Động từ bỏ ます] + にいきます」(みます ➔ みに いきます).
────────────────────────────────────────────────────────────
Câu 32 [BÀI 5 - PHẦN 8: Ngày mai đi để làm gì] [LUYỆN NÓI]
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
Câu 33 [BÀI 6 - PHẦN 1: Rủ rê cùng làm gì] [LUYỆN NÓI]
こんばん、いっしょに ごはんを たべませんか。
  A. はい、いいですね。たべましょう。  ✓
  B. はい、たべました。
  C. ごはんを たべます。
  D. おいしいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tối nay cùng ăn cơm nhé?"
💬 Dịch câu trả lời: "Được, hay đấy. Cùng ăn nhé."
💡 Mẹo ngữ pháp: Mẫu rủ rê「～ませんか」. Đồng ý vui vẻ dùng「はい、いいですね。～ましょう」.
────────────────────────────────────────────────────────────
Câu 34 [BÀI 6 - PHẦN 1: Rủ rê cùng làm gì] [LUYỆN NÓI]
こんばん、いっしょに ごはんを たべませんか。
  A. いいえ、ちょっと……。  ✓
  B. いいえ、たべません。
  C. たべましょう。
  D. こんばんは。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Tối nay cùng ăn cơm nhé?"
💬 Dịch câu trả lời: "Xin lỗi, tôi hơi khó sắp xếp."
💡 Mẹo ngữ pháp: Từ chối lịch sự trong tiếng Nhật dùng:「いいえ、ちょっと……」(tránh từ chối thẳng thừng).
────────────────────────────────────────────────────────────
Câu 35 [BÀI 6 - PHẦN 2: Ở đâu có sự kiện gì] [LUYỆN NÓI]
FPTだいがくで なにが ありますか。
  A. サッカーの しあいが あります。  ✓
  B. がくせいが います。
  C. としょかんが あります。
  D. べんきょうします。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở đại học FPT có sự kiện gì?"
💬 Dịch câu trả lời: "Có trận bóng đá."
💡 Mẹo ngữ pháp:「[Địa điểm]で [Sự kiện]が あります」. Trợ từ「で」chỉ nơi diễn ra sự kiện.
────────────────────────────────────────────────────────────
Câu 36 [BÀI 6 - PHẦN 2: Ở đâu có sự kiện gì] [LUYỆN NÓI]
ハノイで なにが ありますか。
  A. おまつりが あります。  ✓
  B. ハノイへ いきます。
  C. きれいです。
  D. ひとが います。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ở Hà Nội có gì?"
💬 Dịch câu trả lời: "Có lễ hội."
💡 Mẹo ngữ pháp:「おまつりが あります」(Có lễ hội).
────────────────────────────────────────────────────────────
Câu 37 [BÀI 6 - PHẦN 2: Ở đâu có sự kiện gì] [LUYỆN NÓI]
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
Câu 38 [BÀI 6 - PHẦN 3: Thứ gì nhất trong nhóm] [LUYỆN NÓI]
くだもので なにが いちばん すきですか。
  A. りんごが いちばん すきです。  ✓
  B. りんごを かいました。
  C. くだものです。
  D. あかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong trái cây, thích loại nào nhất?"
💬 Dịch câu trả lời: "Táo là thích nhất."
💡 Mẹo ngữ pháp:「～で なにが いちばん [Tính từ]ですか」. Trả lời:「[Vật]が いちばん [Tính từ]です」.
────────────────────────────────────────────────────────────
Câu 39 [BÀI 6 - PHẦN 4: Người nào nhất trong nhóm] [LUYỆN NÓI]
かしゅで だれが いちばん すきですか。
  A. ソン・トゥンM-TPが いちばん すきです。  ✓
  B. うたを うたいます。
  C. かしゅです。
  D. おんがくを ききます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong các ca sĩ, bạn thích ai nhất?"
💬 Dịch câu trả lời: "Sơn Tùng M-TP là thích nhất."
💡 Mẹo ngữ pháp: Hỏi người nổi bật nhất:「だれが いちばん [Tính từ]ですか」. Trả lời:「[Tên người]が いちばん [Tính từ]です」.
────────────────────────────────────────────────────────────
Câu 40 [BÀI 6 - PHẦN 5: Nơi nào nhất trong nhóm] [LUYỆN NÓI]
せかいで どこが いちばん ひろいですか。
  A. ロシアが いちばん ひろいです。  ✓
  B. ロシアへ いきます。
  C. ひろくないです。
  D. くにです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trên thế giới, nơi nào rộng nhất?"
💬 Dịch câu trả lời: "Nga rộng nhất."
💡 Mẹo ngữ pháp: Hỏi nơi chốn nhất:「どこが いちばん [Tính từ]ですか」. Trả lời:「[Địa điểm]が いちばん [Tính từ]です」.
────────────────────────────────────────────────────────────
Câu 41 [BÀI 6 - PHẦN 6: Tháng nào nhất theo đặc điểm] [LUYỆN NÓI]
1ねんで なんがつが いちばん さむいですか。
  A. 12がつが いちばん さむいです。  ✓
  B. ふゆが すきです。
  C. さむくないです。
  D. ゆきです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trong một năm, tháng nào lạnh nhất?"
💬 Dịch câu trả lời: "Tháng 12 là lạnh nhất."
💡 Mẹo ngữ pháp: Hỏi mốc tháng nhất:「なんがつが いちばん [Tính từ]ですか」. Trả lời:「[Tháng]が いちばん [Tính từ]です」.
────────────────────────────────────────────────────────────
Câu 42 [BÀI 6 - PHẦN 7: So sánh hai đối tượng] [LUYỆN NÓI]
Aコースと Bコースと どちらが りょうりが おおいですか。
  A. Bコースのほうが りょうりが おおいです。  ✓
  B. Aコースが すきです。
  C. りょうりを たべます。
  D. おいしいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Giữa suất A và B, suất nào nhiều món hơn?"
💬 Dịch câu trả lời: "Suất B nhiều món hơn."
💡 Mẹo ngữ pháp: So sánh 2 đối tượng「Aと Bと どちらが～」. Trả lời:「[A/B]の ほうが [Tính từ]です」.
────────────────────────────────────────────────────────────
Câu 43 [BÀI 6 - PHẦN 7: So sánh hai đối tượng] [LUYỆN NÓI]
さくらと もみじと どちらが やすいですか。
  A. もみじのほうが やすいです。  ✓
  B. さくらが やすいです。
  C. たかいです。
  D. きれいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Giữa Sakura và Momiji, cái nào rẻ hơn?"
💬 Dịch câu trả lời: "Momiji rẻ hơn."
💡 Mẹo ngữ pháp: Cấu trúc「～の ほうが やすいです」(phía... rẻ hơn).
────────────────────────────────────────────────────────────
Câu 44 [BÀI 7 - PHẦN 1: Nhà / Trường / Đồ vật ở đâu] [LUYỆN NÓI]
バスていは どこに ありますか。
  A. コンビニの まえに あります。  ✓
  B. バスが います。
  C. バスに のります。
  D. あした いきます。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Trạm xe buýt ở đâu?"
💬 Dịch câu trả lời: "Ở phía trước cửa hàng tiện lợi."
💡 Mẹo ngữ pháp: Đồ vật, công trình dùng động từ「あります」:「[Vị trí]に あります」.
────────────────────────────────────────────────────────────
Câu 45 [BÀI 7 - PHẦN 2: Người / Mèo / Chó ở đâu] [LUYỆN NÓI]
たなかさんは どこに いますか。
  A. とけいの したに います。  ✓
  B. とけいの したに あります。
  C. たなかさんです。
  D. きのう あいました。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Anh/chị Tanaka ở đâu?"
💬 Dịch câu trả lời: "Ở dưới đồng hồ."
💡 Mẹo ngữ pháp: Con người và động vật dùng động từ「います」:「[Vị trí]に います」.
────────────────────────────────────────────────────────────
Câu 46 [BÀI 7 - PHẦN 3: Gần địa điểm có gì] [LUYỆN NÓI]
さくらえきの ちかくに なにが ありますか。
  A. スーパーが あります。  ✓
  B. えきへ いきます。
  C. おおきいです。
  D. でんしゃです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Gần ga Sakura có gì?"
💬 Dịch câu trả lời: "Có siêu thị."
💡 Mẹo ngữ pháp:「[Địa điểm]の ちかくに [Vật/Công trình]が あります」.
────────────────────────────────────────────────────────────
Câu 47 [BÀI 7 - PHẦN 3: Gần địa điểm có gì] [LUYỆN NÓI]
きっさてんの ちかくに なにが ありますか。
  A. ぎんこうが あります。  ✓
  B. コーヒーを のみます。
  C. きっさてんです。
  D. ちかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Gần quán cà phê có gì?"
💬 Dịch câu trả lời: "Có ngân hàng."
💡 Mẹo ngữ pháp:「ぎんこうが あります」(Có ngân hàng).
────────────────────────────────────────────────────────────
Câu 48 [BÀI 7 - PHẦN 4: Gần nhà bạn có gì] [LUYỆN NÓI]
あなたの うちの ちかくに なにが ありますか。
  A. やまが あります。  ✓
  B. うちへ かえります。
  C. やまへ いきます。
  D. たかいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Gần nhà bạn có gì?"
💬 Dịch câu trả lời: "Có núi."
💡 Mẹo ngữ pháp: Giới thiệu cảnh quan xung quanh nơi ở:「[Danh từ]が あります」.
────────────────────────────────────────────────────────────
Câu 49 [BÀI 7 - PHẦN 4: Gần nhà bạn có gì] [LUYỆN NÓI]
あなたの うちの ちかくに なにが ありますか。
  A. かわが あります。  ✓
  B. かわへ いきます。
  C. みずです。
  D. さかなが います。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Gần nhà bạn có gì?"
💬 Dịch câu trả lời: "Có sông."
💡 Mẹo ngữ pháp:「かわが あります」(Có sông).
────────────────────────────────────────────────────────────
Câu 50 [BÀI 7 - PHẦN 5: Cắt đồ ăn bằng gì] [LUYỆN NÓI]
なにで パンを きりますか。
  A. ナイフで きります。  ✓
  B. パンを たべました。
  C. パンやさんで かいました。
  D. おいしいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Cắt bánh mì bằng gì?"
💬 Dịch câu trả lời: "Bằng dao."
💡 Mẹo ngữ pháp: Trợ từ「で」chỉ dụng cụ:「[Dụng cụ]で きります」.
────────────────────────────────────────────────────────────
Câu 51 [BÀI 7 - PHẦN 6: Người Việt có ăn bằng dao nĩa không] [LUYỆN NÓI]
ベトナムじんは フォークと ナイフで ごはんを たべますか。
  A. いいえ、はしで ごはんを たべます。  ✓
  B. はい、ナイフで たべます。
  C. たべません。
  D. レストランです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Việt có ăn cơm bằng dao nĩa không?"
💬 Dịch câu trả lời: "Không, ăn bằng đũa."
💡 Mẹo ngữ pháp: Trợ từ「で」chỉ dụng cụ dùng bữa:「はしで ごはんを たべます」.
────────────────────────────────────────────────────────────
Câu 52 [BÀI 7 - PHẦN 7: Người các nước ăn bằng gì] [LUYỆN NÓI]
にほんじんと ベトナムじんは なにで ごはんを たべますか。
  A. はしで ごはんを たべます。  ✓
  B. スプーンです。
  C. ごはんを たべました。
  D. おいしいです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Nhật và người Việt ăn cơm bằng dụng cụ gì?"
💬 Dịch câu trả lời: "Ăn bằng đũa."
💡 Mẹo ngữ pháp:「はしで ごはんを たべます」(Ăn bằng đũa).
────────────────────────────────────────────────────────────
Câu 53 [BÀI 7 - PHẦN 7: Người các nước ăn bằng gì] [LUYỆN NÓI]
アメリカじんは なにで ごはんを たべますか。
  A. フォークと ナイフで ごはんを たべます。  ✓
  B. はしで たべます。
  C. パンを たべます。
  D. アメリカです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Mỹ ăn cơm bằng dụng cụ gì?"
💬 Dịch câu trả lời: "Dùng nĩa và dao."
💡 Mẹo ngữ pháp:「フォークと ナイフで ごはんを たべます」.
────────────────────────────────────────────────────────────
Câu 54 [BÀI 7 - PHẦN 7: Người các nước ăn bằng gì] [LUYỆN NÓI]
インドじんは なにで ごはんを たべますか。
  A. てで ごはんを たべます。  ✓
  B. はしで たべます。
  C. カレーです。
  D. てが あります。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Người Ấn ăn cơm bằng dụng cụ gì?"
💬 Dịch câu trả lời: "Ăn bằng tay."
💡 Mẹo ngữ pháp: Điểm văn hóa Bài 7:「てで ごはんを たべます」(Ăn bằng tay).
────────────────────────────────────────────────────────────
Câu 55 [BÀI 7 - PHẦN 8: Một người đang làm gì] [LUYỆN NÓI]
アンナさんは なにを していますか。
  A. でんわを しています。  ✓
  B. でんわを しました。
  C. でんわです。
  D. ともだちです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Anna đang làm gì?"
💬 Dịch câu trả lời: "Anna đang nói chuyện điện thoại."
💡 Mẹo ngữ pháp: Hỏi hành động đang diễn ra:「なにを していますか」. Trả lời:「V-ています」.
────────────────────────────────────────────────────────────
Câu 56 [BÀI 7 - PHẦN 8: Một người đang làm gì] [LUYỆN NÓI]
パクさんは なにを していますか。
  A. おさらを あらっています。  ✓
  B. おさらを あらいました。
  C. おさらです。
  D. だいどころです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Park đang làm gì?"
💬 Dịch câu trả lời: "Park đang rửa bát."
💡 Mẹo ngữ pháp: あらいます ➔ あらっています (đang rửa).
────────────────────────────────────────────────────────────
Câu 57 [BÀI 7 - PHẦN 8: Một người đang làm gì] [LUYỆN NÓI]
マリアさんは なにを していますか。
  A. ピアノを ひいています。  ✓
  B. ピアノを ひきました。
  C. ピアノが あります。
  D. おんがくです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Maria đang làm gì?"
💬 Dịch câu trả lời: "Maria đang chơi đàn piano."
💡 Mẹo ngữ pháp: ひきます ➔ ひいています (đang chơi nhạc cụ).
────────────────────────────────────────────────────────────
Câu 58 [BÀI 7 - PHẦN 8: Một người đang làm gì] [LUYỆN NÓI]
にしかわさんは なにを していますか。
  A. うたを うたっています。  ✓
  B. うたを うたいました。
  C. うたです。
  D. かしゅです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Nishikawa đang làm gì?"
💬 Dịch câu trả lời: "Nishikawa đang hát."
💡 Mẹo ngữ pháp: うたいます ➔ うたっています (đang hát).
────────────────────────────────────────────────────────────
Câu 59 [BÀI 7 - PHẦN 9: Ai đang thực hiện hành động] [LUYỆN NÓI]
だれが ギターを ひいていますか。
  A. メアリーンさんが ギターを ひいています。  ✓
  B. ギターを ひきます。
  C. メアリーンさんです。
  D. おんがくしつです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ai đang chơi guitar?"
💬 Dịch câu trả lời: "Maryn đang chơi guitar."
💡 Mẹo ngữ pháp: Hỏi chủ ngữ hành động「だれが」. Trả lời:「[Tên người]さんが V-ています」.
────────────────────────────────────────────────────────────
Câu 60 [BÀI 7 - PHẦN 9: Ai đang thực hiện hành động] [LUYỆN NÓI]
だれが うたを うたっていますか。
  A. にしかわさんが うたを うたっています。  ✓
  B. うたを うたいました。
  C. にしかわさんです。
  D. かしゅです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ai đang hát?"
💬 Dịch câu trả lời: "Nishikawa đang hát."
💡 Mẹo ngữ pháp:「[Tên người]さんが うたを うたっています」.
────────────────────────────────────────────────────────────
Câu 61 [BÀI 7 - PHẦN 9: Ai đang thực hiện hành động] [LUYỆN NÓI]
だれが でんわを かけていますか。
  A. アンナさんが でんわを かけています。  ✓
  B. でんわを かけました。
  C. アンナさんです。
  D. いまです。
→ Đáp án: A
Giải thích: 🗣️ Dịch câu hỏi: "Ai đang gọi điện?"
💬 Dịch câu trả lời: "Anna đang gọi điện."
💡 Mẹo ngữ pháp:「[Tên người]さんが でんわを かけています」.
────────────────────────────────────────────────────────────
`;
