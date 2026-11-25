# Kế hoạch luận văn BA ĐỘNG — Coastal Escape

Sinh viên Lê Hiền · MSSV 170125405 · lớp DK25TTC5 · Chuyên đề ASP.NET. Đề cương dùng các mục 1–4 của PDF quy định môn học và [hồ sơ kỹ thuật](../docs/SOFTWARE_DESIGN.md).

## Cấu trúc, định dạng và số trang

Thứ tự dự kiến gồm bìa chính, bìa phụ, nhận xét GVHD, nhận xét TVHĐ, lời cảm ơn, mục lục, danh mục hình/bảng/ký hiệu/chữ viết tắt nếu có, tóm tắt, phần nội dung, tài liệu tham khảo và phụ lục. Tóm tắt nêu vấn đề, cách tiếp cận, giải pháp và kết quả đã xác minh. Kiểm đếm phần nội dung A4 tách khỏi bìa, cảm ơn, mục lục, tài liệu tham khảo và các phần ngoài thân bài theo quy định. PDF yêu cầu ít nhất 30 trang nội dung và khuyến nghị tối đa 50.

| Phần | Số trang kế hoạch | Nguồn chính |
| --- | ---: | --- |
| Mở đầu | 3 | [PRODUCT.md](../PRODUCT.md), [SRS.md](../docs/SRS.md) |
| Chương 1. Tổng quan | 5 | [PRODUCT.md](../PRODUCT.md), [SRS.md](../docs/SRS.md), [traceability](../docs/TRACEABILITY_MATRIX.md) |
| Chương 2. Nghiên cứu lý thuyết | 7 | [Program.cs](../src/BaDong.CoastalEscape/Program.cs), [global.json](../global.json), các tài liệu chính thức cần thu thập |
| Chương 3. Hiện thực hóa nghiên cứu | 12 | [Thiết kế](../docs/SOFTWARE_DESIGN.md), [sơ đồ](../docs/diagrams/README.md), [source](../src/BaDong.CoastalEscape), [setup](../setup/README.md) |
| Chương 4. Kết quả nghiên cứu | 8 | [Bằng chứng](../docs/evidence/README.md), [test plan](../docs/TEST_PLAN.md), kết quả CI/Pages |
| Chương 5. Kết luận và hướng phát triển | 3 | [Giới hạn](../docs/KNOWN_LIMITATIONS.md), [compliance](../docs/ACADEMIC_COMPLIANCE.md) |
| Tổng | **38** | Mục tiêu dàn trang, sẽ đo lại bản DOC/PDF |

A4, Times New Roman Unicode 13 pt, giãn dòng 1,5, trước/sau đoạn 6 pt. Lề trên/dưới/phải 2 cm và trái 3 cm; số trang góc phải dưới. Dùng số Ả Rập cho chương và mục, ví dụ 3.2.1. Đánh số bảng và hình, đặt caption và kiểm tra danh mục tự động. Điều kiện nộp còn phải đối chiếu mẫu bìa/nhận xét và định dạng được giảng viên chấp nhận.

## Mục lục dự kiến đến Heading 3

| Heading 1 | Heading 2 | Heading 3 |
| --- | --- | --- |
| Mở đầu | Lý do, mục đích | Bối cảnh tra cứu; mục tiêu đề tài |
| Mở đầu | Đối tượng, phạm vi và phương pháp | Người truy cập; dữ liệu và phương pháp kiểm chứng |
| Chương 1. Tổng quan | 1.1 Bài toán và người dùng | 1.1.1 Nhu cầu; 1.1.2 Giới hạn dịch vụ |
|  | 1.2 Yêu cầu hệ thống | 1.2.1 Chức năng; 1.2.2 Phi chức năng |
| Chương 2. Nghiên cứu lý thuyết | 2.1 Nền tảng frontend | 2.1.1 Blazor WebAssembly; 2.1.2 Razor và routing |
|  | 2.2 Dữ liệu và triển khai | 2.2.1 JSON, HTTP và cache; 2.2.2 GitHub Actions và Pages |
|  | 2.3 Kỹ thuật kiểm thử | 2.3.1 xUnit/MTP; 2.3.2 Browser và accessibility |
| Chương 3. Hiện thực hóa nghiên cứu | 3.1 Phân tích và kiến trúc | 3.1.1 Use case; 3.1.2 Kiến trúc và thành phần |
|  | 3.2 Dữ liệu và nghiệp vụ | 3.2.1 Mô hình lớp và từ điển; 3.2.2 Tải/cache; 3.2.3 Search/filter |
|  | 3.3 Hiện thực và triển khai | 3.3.1 Điều hướng/trạng thái lỗi; 3.3.2 Workflows và hướng dẫn cài đặt |
| Chương 4. Kết quả nghiên cứu | 4.1 Xác minh kỹ thuật | 4.1.1 Môi trường/Release build; 4.1.2 Test tự động, JSON và NuGet |
|  | 4.2 Giao diện chức năng | 4.2.1 Trang chủ/menu; 4.2.2 Địa điểm/tìm kiếm; 4.2.3 Ẩm thực/thư viện; 4.2.4 FAQ/lịch trình/vị trí |
|  | 4.3 Kiểm tra trình duyệt | 4.3.1 Title, loading và lỗi; 4.3.2 Responsive và accessibility |
|  | 4.4 Bằng chứng triển khai và giới hạn | 4.4.1 CI, Pages và HTTP; 4.4.2 Giới hạn hiệu năng và kiểm thử |
| Chương 5. Kết luận và hướng phát triển | 5.1 Kết quả và đóng góp | 5.1.1 Giải pháp và phạm vi đã xác minh |
|  | 5.2 Hướng phát triển | 5.2.1 Deep link và khả năng tiếp cận; 5.2.2 Dữ liệu và ảnh |

## Hình, bảng và bằng chứng dự kiến

Hình 3.1–3.9 lấy từ [danh mục sơ đồ](../docs/diagrams/README.md). Hình Chương 4 chọn từ [18 ảnh](../docs/evidence/screenshots/MANIFEST.md). Ghép ảnh responsive 01–03 thành một hình nếu giữ được chữ đọc rõ. Dùng ảnh 04 cho menu, 05–09 cho khám phá, 10–13 cho ẩm thực/thư viện, 14–16 cho FAQ/lịch trình/vị trí, 17–18 cho lỗi. Có thể đưa các hình tương tự vào phụ lục để giữ ngân sách 8 trang của Chương 4.

| Bảng dự kiến | Nguồn đối chiếu |
| --- | --- |
| Bảng 1.1. Yêu cầu và phạm vi | [Traceability](../docs/TRACEABILITY_MATRIX.md) |
| Bảng 2.1. Công nghệ và vai trò | [Thiết kế](../docs/SOFTWARE_DESIGN.md) |
| Bảng 3.1. Từ điển dữ liệu | [Thiết kế, mục 4](../docs/SOFTWARE_DESIGN.md#4-mô-hình-và-từ-điển-dữ-liệu) |
| Bảng 4.1. Build, tests và JSON | [Báo cáo kỹ thuật](../docs/evidence/academic-validation/2026-W48-phase-d-f.md), D-J01 |
| Bảng 4.2. Route, title và trạng thái lỗi | Cùng báo cáo, D-T00–09. Tách lỗi production baseline và kết quả local. |
| Bảng 4.3. UI, responsive, accessibility và phạm vi | D-T01–08, E-U01–05 và baseline 48 lượt. Nêu mục chưa kiểm. |
| Bảng 4.4. CI, Pages và HTTP | Run cùng baseline, homepage và tài nguyên HTTP 200, deep link ban đầu HTTP 404. |
| Bảng 5.1. Giới hạn và hướng phát triển | [Giới hạn](../docs/KNOWN_LIMITATIONS.md) |

Phụ lục A dự kiến chứa lệnh cài đặt, thông tin release và danh mục học thuật. Phụ lục B chứa ma trận kiểm thử đầy đủ, ảnh bổ sung và định danh phiên bản.

## Tài liệu tham khảo và thông tin chờ

- Thu thập các trang Microsoft Learn về Blazor WASM, routing, PageTitle, System.Text.Json và Microsoft Testing Platform; tài liệu xUnit; tài liệu GitHub Actions/Pages; hướng dẫn W3C về WCAG và tài liệu ảnh sử dụng thật trong [sổ nguồn](../docs/CONTENT_SOURCES.md). Lưu tác giả/tổ chức, tiêu đề, phiên bản và ngày truy cập thật trong [refs](refs/README.md).
- PDF yêu cầu hình thức IEEE đồng thời ghi đánh số theo thứ tự từ điển. Xác nhận với giảng viên cách áp dụng khi thứ tự trích dẫn trong bài khác thứ tự từ điển. Chỉ đưa nguồn thật đã trích dẫn hoặc dùng để bàn luận.
- Còn thiếu email và điện thoại sinh viên, họ tên GVHD và thông tin trường/khoa theo mẫu. Cần mẫu bìa chính, bìa phụ, nhận xét GVHD, nhận xét TVHĐ. Xác nhận `.DOC` so với `.DOCX`, `scr` so với `src`, cùng checklist xuất DOC, PDF, HTML và bản trình bày.
