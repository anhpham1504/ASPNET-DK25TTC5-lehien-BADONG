# BA ĐỘNG — Coastal Escape SRS

## 1. Mục tiêu và phạm vi

BA ĐỘNG — Coastal Escape là website giới thiệu du lịch chạy bằng .NET 10 Blazor WebAssembly Standalone. Người dùng có thể tra cứu địa điểm, ẩm thực, thư viện ảnh, cẩm nang, lịch trình tham khảo và vị trí. Dữ liệu được đọc từ JSON tĩnh; sản phẩm không có backend nghiệp vụ, database, tài khoản, đặt chỗ hoặc thanh toán.

## 2. Yêu cầu chức năng

- Trang chủ và Giới thiệu cung cấp nhận diện, bối cảnh và lối vào các nhóm nội dung.
- Khám phá hỗ trợ danh sách, tìm kiếm tiếng Việt có/không dấu kết hợp, lọc danh mục, reset và empty state.
- Trang chi tiết địa điểm hiển thị mô tả, nguồn ảnh, bản đồ và sao chép liên kết.
- Ẩm thực hỗ trợ danh sách, lọc và trang chi tiết món.
- Thư viện hỗ trợ lọc, mở lightbox, chuyển ảnh, đóng và khôi phục focus.
- Cẩm nang hiển thị FAQ; Lịch trình dùng tab một ngày/hai ngày; Vị trí mở Google Maps.
- Route hoặc slug không hợp lệ có title, thông báo trung tính và lối phục hồi.

## 3. Yêu cầu phi chức năng

- Responsive ở desktop, tablet và mobile; không tràn ngang trong ma trận release.
- Keyboard baseline gồm focus nhìn thấy, menu/lightbox, FAQ, filter và tab lịch trình.
- Ảnh đã xác minh phải có provenance; địa điểm thiếu ảnh giữ trạng thái `PENDING` và dùng editorial card không gây hiểu nhầm.
- GitHub Actions phải restore, Release build, chạy 14 automated tests và native publish với `wasm-tools`.
- GitHub Pages phân phối artifact tĩnh dưới base path của project; deep link có thể nhận HTTP 404 ban đầu rồi được SPA khôi phục.

## 4. Baseline nghiệm thu

Phiên bản đóng băng là `ec0d53f180570e59c084a9ce7f74aa89d5ee3abe`. Chi tiết triển khai, test và giới hạn nằm trong [Software Design](SOFTWARE_DESIGN.md), [Test Plan](TEST_PLAN.md), [Traceability Matrix](TRACEABILITY_MATRIX.md), [Release Baseline](RELEASE_BASELINE.md) và [Known Limitations](KNOWN_LIMITATIONS.md).
