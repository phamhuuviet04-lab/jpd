# jpd - Ứng dụng Ôn tập Từ vựng & Hán tự Tiếng Nhật (Hỗ trợ Đa môn học)

Ứng dụng web ôn tập và luyện tập từ vựng, chữ Hán (Kanji), trắc nghiệm hỗ trợ đa môn học (mặc định gồm **Tiếng Nhật Từ vựng できる日本語** và **Tiếng Nhật Ôn tập Từ Hán Kanji**, dễ dàng mở rộng thêm các môn khác như Tiếng Anh, Tiếng Hàn, Lịch sử, v.v.).

## Tính năng nổi bật
- **Phân loại Tiếng Nhật chuyên sâu (Mới)**:
  - **📖 Từ vựng (できる日本語)**: 249 câu từ vựng theo giáo trình Bài 4 - 7 (chia nhỏ theo 3 phần).
  - **🈸 Ôn tập Từ Hán (Kanji)**: Ôn tập 9 chữ Hán và các từ ghép tiêu biểu:
    - **東 (ĐÔNG)**: 東 (ひがし: phía đông), 東京 (とうきょう: Tokyo)
    - **京 (KINH)**: 東京 (とうきょう: Tokyo), 京都 (きょうと: Kyoto)
    - **名 (DANH)**: 名前 (なまえ: tên), 名人 (めいじん: danh nhân)
    - **前 (TIỀN)**: 前 (まえ: phía trước), 前日 (ぜんじつ: ngày trước)
    - **国 (QUỐC)**: 国 (くに: đất nước), 国語 (こくご: quốc ngữ)
    - **男 (NAM)**: 男の人 (おとこのひと: người đàn ông), 男女 (だんじょ: nam nữ)
    - **女 (NỮ)**: 女の人 (おannaのひと: người phụ nữ), 女の子 (おんなのこ: bé gái), 男女 (だんじょ: nam nữ)
    - **区 (KHU)**: 区 (く: khu, quận), なごや区 (なごやく: quận Nagoya)
    - **市 (THỊ)**: 市 (し: thành phố), ホーチミン市 (ホーチミンし: TP. Hồ Chí Minh), ハノイ市 (ハノイし: thành phố Hà Nội)
  - **Hỗ trợ 2 chiều hỏi đáp linh hoạt cho Hán tự**:
    - **Thuận**: Câu hỏi: `前` ➔ Đáp án: `まえ: phía trước`
    - **Nghịch**: Câu hỏi: `まえ: phía trước` ➔ Đáp án: `前`
    - **Trộn cả hai chiều** ngẫu nhiên.
  - Bộ lọc bài theo từng chữ Hán để luyện tập trọng tâm từng từ.
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
├── index.html          # Khung giao diện HTML với Menu chọn môn học & Sub-tabs
├── css/
│   └── style.css       # Tùy chỉnh giao diện, thanh cuộn, hiệu ứng
├── js/
│   ├── database.js     # Kho dữ liệu câu hỏi (Từ vựng, Hán tự) & cấu hình APP_SUBJECTS
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
