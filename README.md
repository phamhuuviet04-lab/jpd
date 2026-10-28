# jpd - Ứng dụng Ôn tập Từ vựng, Hán tự, Ngữ pháp & Luyện nói Tiếng Nhật (Hỗ trợ Đa môn học)

Ứng dụng web ôn tập và luyện tập từ vựng, chữ Hán (Kanji), ngữ pháp (Grammar), luyện nói phản xạ giao tiếp (Speaking/Kaiwa), trắc nghiệm hỗ trợ đa môn học (mặc định gồm **📖 Tiếng Nhật Từ vựng できる日本語**, **🈸 Tiếng Nhật Ôn tập Từ Hán Kanji**, **📐 Tiếng Nhật Ngữ pháp 文法** và **🗣️ Tiếng Nhật Luyện nói Hội thoại 会話**, dễ dàng mở rộng thêm các môn khác như Tiếng Anh, Tiếng Hàn, Lịch sử, v.v.).

## Tính năng nổi bật
- **Phân loại Tiếng Nhật chuyên sâu 4 trong 1 (Toàn diện)**:
  - **📖 Từ vựng (できる日本語)**: 249 câu từ vựng theo giáo trình Bài 4 - 7 (chia nhỏ theo 3 phần).
  - **🈸 Ôn tập Từ Hán (Kanji)**: Đầy đủ 75 từ vựng và chữ Hán ghép từ giáo trình FPT University (Bài 4 - 6).
  - **📐 Ngữ pháp (文法 - Tách 2 dạng câu hỏi song hành)**: Trọn bộ **166 câu hỏi ngữ pháp** bám sát 100% giáo trình và bài tập Bài 4 - 6 (83 câu hỏi lý thuyết/cấu trúc và 83 câu dịch Việt ➔ Nhật).
  - **🗣️ Luyện nói (会話 - Hội thoại thực tế Bài 4 - 7)**: Trọn bộ **34 câu hỏi luyện nói phản xạ** bao quát toàn bộ 34 cấu trúc câu hỏi giao tiếp thi vấn đáp Bài 4 - 7:
    - **Cơ chế phản xạ thông minh**: Hiển thị câu hỏi tiếng Nhật thực tế, người học chọn câu đáp phù hợp.
    - **Tức thì hiện dịch nghĩa**: Ngay sau khi bấm chọn đáp án, hệ thống lập tức hiển thị dịch nghĩa tiếng Việt của cả câu hỏi và câu trả lời.
    - **Mẫu trả lời mở rộng (🌟)**: Cung cấp thêm 2 - 3 cách trả lời thực tế khác trong đời sống để học viên phong phú hóa vốn câu khi đi thi hoặc giao tiếp.
    - **Mẹo giao tiếp & Phân tích cấu trúc (💡)**: Phân tích sắc thái, trợ từ, quy tắc trả lời chuẩn theo từng tình huống.
    - **Tích hợp phát âm tiếng Nhật chuẩn (🔊)**: Hỗ trợ nút nghe phát âm trực tiếp câu hỏi và câu đáp qua Web Speech API giọng Nhật tự nhiên.
    - **Phân loại đầy đủ Bài 4 - 7**:
      - **Bài 4 (9 câu)**: Khoảng cách thời gian (`〜から〜まで`), Phương tiện di chuyển (`〜で`), Đặc điểm nơi chốn (`どんなところ`), Cảm nhận (`どうですか`), Tính từ (`にぎやか`, `大きい`), Tồn tại (`あります`), Thời tiết (`月・季節`).
      - **Bài 5 (8 câu)**: Hành động quá khứ (`何をしましたか`), Đi đâu (`どこかへ`), Làm cùng ai (`だれと`), Hỏi lý do (`どうして〜から`), Mong muốn đồ vật (`ほしい`), Sở thích (`すき`), Mong muốn hành động (`〜たい`), Mục đích di chuyển (`〜に行きます`).
      - **Bài 6 (8 câu)**: Lời mời & Rủ rê (`〜ませんか`), Sự kiện diễn ra (`であります`), So sánh nhất (`何・だれ・どこ・何月がいちばん`), So sánh lựa chọn (`どちらが`), Đã làm gì chưa (`もう〜ましたか / まだです`).
      - **Bài 7 (9 câu)**: Vị trí công trình / ĐH FPT (`どこにありますか`), Vị trí người / thú cưng (`どこにいますか`), Tiện ích quanh đây (`近くに何がありますか`), Quanh nhà có gì (`うちの近くに何がありますか`), Dụng cụ (`何で切りますか`), Văn hóa ăn uống (`ベトナム人はフォークとナイフで...`), Dụng cụ ăn cơm của các nước (`何でご飯を食べますか`), Đang làm gì (`何をしていますか`), Ai đang làm gì (`だれが〜ていますか`).
    - **Bài 4 (19 từ)**:
      - **東 (ĐÔNG)**: 東 (ひがし: phía đông)
      - **京 (KINH)**: 東京 (とうきょう: Tokyo)
      - **名 (DANH)**: 名 (な: tên), 名人 (めいじん: danh nhân)
      - **前 (TIỀN)**: 前 (まえ: phía trước), 前日 (ぜんじつ: ngày trước), 名前 (なまえ: tên)
      - **国 (QUỐC)**: 国 (くに: đất nước), 国語 (こくご: quốc ngữ)
      - **男 (NAM)**: 男 (おとこ: đàn ông, con trai), 男の人 (おとこのひと: người đàn ông)
      - **女 (NỮ)**: 女 (おんな: con gái, nữ giới), 女の人 (おんなのひと: người phụ nữ), 男女 (だんじょ: nam nữ)
      - **区 (KHU)**: 区 (く: khu, quận), なごや区 (なごやく: quận Nagoya)
      - **市 (THỊ)**: 市 (し: thành phố), ホーチミン市 (ホーチミンし: TP. HCM), ハノイ市 (ハノイし: TP. Hà Nội)
    - **Bài 5 (29 từ)**:
      - **先 (TIÊN)**: 先生 (せんせい: giáo viên), 先日 (せんじつ: ngày trước), 先週 (せんしゅう: tuần trước)
      - **週 (CHU)**: 週間 (しゅうかん: ~ tuần)
      - **毎 (MỖI)**: 毎日 (まいにち: mỗi ngày), 毎週 (まいしゅう: mỗi tuần), 毎月 (まいつき: mỗi tháng), 毎年 (まいとし: mỗi năm)
      - **午 (NGỌ)**: 午前 (ごぜん: sáng, am)
      - **後 (HẬU)**: 午後 (ごご: buổi chiều, pm), 後 (あと: sau), 後ろ (うしろ: phía sau)
      - **見 (KIẾN)**: 見ます (みます: nhìn, xem), 見学 (けんがく: kiến tập), 見物 (けんぶつ: ngắm cảnh)
      - **食 (THỰC)**: 食べます (たべます: ăn), 食べ物 (たべもの: đồ ăn), 食事 (しょくじ: dùng bữa)
      - **飲 (ẨM)**: 飲みます (のみます: uống), 飲み物 (のみもの: đồ uống), 飲食 (いんしょく: ăn uống, ẩm thực)
      - **買 (MÃI)**: 買います (かいます: mua), 買い物 (かいもの: mua sắm)
      - **物 (VẬT)**: 人物 (じんぶつ: nhân vật)
      - **行 (HÀNH/HÀNG)**: 行きます (いきます: đi), 行 (ぎょう: dòng kẻ)
      - **休 (HƯU)**: 休みます (やすみます: nghỉ), 休み (やすみ: nghỉ, ngày nghỉ), 休日 (きゅうじつ: ngày nghỉ)
    - **Bài 6 (27 từ)**:
      - **今 (KIM)**: 今 (いま: bây giờ), 今日 (きょう: hôm nay), 今年 (ことし: năm nay), 今月 (こんげつ: tháng này), 今週 (こんしゅう: tuần này)
      - **来 (LAI)**: 来ます (きます: đến), 来週 (らいしゅう: tuần tới), 来月 (らいげつ: tháng tới), 来年 (らいねん: năm tới), 来日 (らいにち: đến Nhật Bản)
      - **帰 (QUY)**: 帰ります (かえります: về), 帰国 (きこく: về nước)
      - **会 (HỘI)**: 会います (あいます: gặp), 会見 (かいけん: hội họp), 国会 (こっかい: quốc hội)
      - **社 (XÃ)**: 会社 (かいしゃ: công ty), 社会 (しゃかい: xã hội)
      - **聞 (VĂN)**: 聞きます (ききます: nghe, hỏi), 新聞 (しんぶん: báo)
      - **読 (ĐỘC)**: 読みます (よみます: đọc), 読み物 (よみもの: sách, tạp chí...), 読書 (どくしょ: đọc sách)
      - **書 (THƯ)**: 書きます (かきます: viết), 書き物 (かきもの: bút, phấn... / đồ viết)
      - **話 (THOẠI)**: 話 (はなし: câu chuyện), 話します (はなします: nói chuyện), 会話 (かいわ: hội thoại)
  - **Hỗ trợ 2 chiều hỏi đáp linh hoạt cho Hán tự**:
    - **Thuận**: Câu hỏi: `前` ➔ Đáp án: `まえ: phía trước`
    - **Nghịch**: Câu hỏi: `まえ: phía trước` ➔ Đáp án: `前`
    - **Trộn cả hai chiều** ngẫu nhiên.
  - Hỗ trợ lọc theo từng **Bài 4**, **Bài 5**, **Bài 6** hoặc chọn **Tất cả bài** để ôn luyện tổng hợp.
- **Menu chọn môn học linh hoạt**:
  - Chuyển đổi nhanh giữa các môn học chỉ với 1 cú click ngay ở thanh đầu trang.
  - Tự động lưu môn học đang chọn vào trình duyệt (`LocalStorage`).
  - Hỗ trợ nút **➕ Thêm môn**: Cho phép thêm môn học trực tiếp trên giao diện web hoặc xem mẫu code để cấu hình vĩnh viễn trong file mã nguồn.
  - Dữ liệu câu đã học và chế độ học được lưu độc lập cho từng môn học (không bị lẫn lộn).
- **Chế độ Học (Quiz)**:
  - 3 Chế độ hỏi đáp: Thuận, Nghịch, Trộn cả hai.
  - Tùy chọn ẩn Furigana: Tự động hiển thị đối với Từ vựng Tiếng Nhật và tự động ẩn khi học Hán tự hoặc các môn không dùng furigana.
  - Phản hồi chi tiết sau mỗi câu.
  - Tự động lặp lại các câu sai cho đến khi thuộc.
  - Phím tắt (1-9, Mũi tên, Enter) và hỗ trợ phím phụ chuột (mouse side buttons).
- **Màn hình Tất cả câu hỏi (List view)**:
  - Lọc theo từng Bài / Chữ Hán / Từng Phần.
  - Đánh dấu câu đã học, lưu tiến độ qua LocalStorage.
  - Nút định vị nhanh đến câu đã học gần nhất.

## Cấu trúc thư mục dự án

```text
quizlet/
├── index.html          # Khung giao diện HTML với Menu chọn môn học & Sub-tabs (Từ vựng, Hán tự, Ngữ pháp)
├── css/
│   └── style.css       # Tùy chỉnh giao diện, thanh cuộn, hiệu ứng
├── js/
│   ├── database.js     # Kho dữ liệu câu hỏi (Từ vựng, Hán tự) & cấu hình APP_SUBJECTS
│   ├── grammar_data.js # Kho 160 câu hỏi ngữ pháp (Bài 4 - 6) & phân loại GRAMMAR_LESSON_PARTS
│   ├── parser.js       # Bộ phân tích dữ liệu câu hỏi và ánh xạ bài học
│   └── app.js          # Logic điều khiển chính (Chuyển môn, Quiz, Danh sách, Phím tắt, LocalStorage)
└── README.md           # Tài liệu hướng dẫn
```

## Hướng dẫn thêm môn học mới

### Cách 1: Thêm trực tiếp trên giao diện Web (Nhanh nhất)
1. Mở file [index.html](file:///c:/Users/TUF%20FX506/Downloads/quizlet/index.html) trên trình duyệt.
2. Bấm nút **➕ Thêm môn** trên thanh menu chọn môn học.
3. Điền mã môn học (ID), tên môn học, biểu tượng icon và dán nội dung câu hỏi.
4. Bấm **Lưu & Chuyển sang môn này** để bắt đầu học ngay.

### Cách 2: Thêm cố định vào mã nguồn
Mở file [js/database.js](file:///c:/Users/TUF%20FX506/Downloads/quizlet/js/database.js) và thêm môn học mới vào `window.APP_SUBJECTS`:

```javascript
"korean": {
    id: "korean",
    name: "Tiếng Hàn",
    fullName: "Tiếng Hàn Sơ Cấp (Bài 1 - 5)",
    icon: "🇰🇷",
    badge: "Sơ cấp 1",
    hasFurigana: false,
    quizType: "vocab", // hoặc "standard" nếu là môn trắc nghiệm thông thường
    langFrom: "Tiếng Hàn",
    langTo: "Tiếng Việt",
    modeLabels: {
        "jp-vi": "🇰🇷 ➔ 🇻🇳 Hàn - Việt",
        "vi-jp": "🇻🇳 ➔ 🇰🇷 Việt - Hàn",
        "mix": "🔀 Trộn cả hai"
    },
    rawText: `
Câu 1 [BÀI 1: Nhập môn]
안녕하세요
  A. Tạm biệt
  B. Xin chào  ✓
  C. Cảm ơn
  D. Xin lỗi
→ Đáp án: B
────────────────────────────────────────────────────────────
`
}
```
Lưu lại và tải lại trang trên trình duyệt.
