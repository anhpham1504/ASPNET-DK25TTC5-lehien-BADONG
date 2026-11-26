# Ảnh production của bản phát hành 1c04cb1

Các ảnh được chụp trực tiếp từ [production](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/) ngày **26/11/2026** bằng Chrome Headless 158 qua Playwright CLI. SHA đã triển khai: `1c04cb15c700c5a78c4c89d3be63008af990fd5f`. Ảnh là screenshot nguyên bản, không chỉnh sửa nội dung. Bộ này bổ sung cho 18 ảnh lịch sử và không thay thế nguồn gốc của chúng.

| Tệp | Route | Viewport | Trạng thái UI | Chức năng và liên kết truy vết | Caption |
| --- | --- | --- | --- | --- | --- |
| [01-home-desktop-1c04cb1.png](01-home-desktop-1c04cb1.png) | `/` | 1440 × 900 | Mặc định | Trang chủ desktop; F-01, N-03; §4.2.1 | Trang chủ production trên màn hình desktop |
| [02-home-mobile-1c04cb1.png](02-home-mobile-1c04cb1.png) | `/` | 390 × 844 | Mặc định | Trang chủ mobile; F-01, N-03; §4.2.1 | Trang chủ production trên thiết bị di động |
| [03-mobile-menu-1c04cb1.png](03-mobile-menu-1c04cb1.png) | `/` | 390 × 844 | Menu mở | Menu, focus và khóa cuộn; N-03; §4.3.2 | Điều hướng di động đang mở trên production |
| [04-explore-1c04cb1.png](04-explore-1c04cb1.png) | `/kham-pha` | 1440 × 900 | Danh sách mặc định | Tìm kiếm và filter; F-02; §4.2.2 | Danh mục địa điểm và công cụ tìm kiếm trên production |
| [05-destination-detail-1c04cb1.png](05-destination-detail-1c04cb1.png) | `/kham-pha/bien-ba-dong` | 1440 × 900 | Chi tiết hợp lệ | Địa điểm, nguồn ảnh và PageTitle; F-03; §4.2.2 | Chi tiết Biển Ba Động trên production |
| [06-cuisine-1c04cb1.png](06-cuisine-1c04cb1.png) | `/am-thuc` | 1440 × 900 | Danh sách mặc định | Danh sách và filter ẩm thực; F-05; §4.2.3 | Danh mục ẩm thực và bộ lọc trên production |
| [07-gallery-1c04cb1.png](07-gallery-1c04cb1.png) | `/thu-vien` | 390 × 844 | Caption cảm ứng hiển thị | Gallery với giả lập iPhone 15, `hover:none`, `pointer:coarse`; F-06, N-03; §4.2.3 | Caption ảnh hiển thị trên thiết bị cảm ứng |
| [08-lightbox-1c04cb1.png](08-lightbox-1c04cb1.png) | `/thu-vien` | 390 × 568 | Lightbox mở | Dialog màn hình thấp, focus và điều hướng ảnh; F-06, N-03; §4.2.3 | Lightbox production trên màn hình thấp |
| [09-itinerary-tabs-1c04cb1.png](09-itinerary-tabs-1c04cb1.png) | `/lich-trinh` | 1440 × 900 | Tab thứ hai được chọn | Tab/panel, roving tabindex và bàn phím; F-08, N-03; §4.2.4, §4.3.2 | Lịch trình hai ngày với tab thứ hai đang hoạt động |
| [10-location-1c04cb1.png](10-location-1c04cb1.png) | `/lien-he` | 1440 × 900 | Mặc định | Vị trí và liên kết Google Maps; F-09; §4.2.4 | Thông tin vị trí và lối mở Google Maps |
| [11-invalid-destination-1c04cb1.png](11-invalid-destination-1c04cb1.png) | `/kham-pha/khong-ton-tai` | 390 × 844 | Slug sai | Error state, header và PageTitle; F-10; §4.3.1 | Trạng thái không tìm thấy địa điểm trên production |
| [12-not-found-1c04cb1.png](12-not-found-1c04cb1.png) | `/khong-tim-thay` | 390 × 844 | Route 404 trong ứng dụng | Trang lỗi và lối phục hồi; F-10; §4.3.1 | Trang không tìm thấy thân thiện trên production |
| [13-landscape-menu-1c04cb1.png](13-landscape-menu-1c04cb1.png) | `/` | 740 × 390 | Menu mở landscape | Cuộn nội bộ và focus tới mục cuối; N-03; §4.3.2 | Menu di động ở chế độ xoay ngang |

## Điều kiện chụp

- Browser: Chrome Headless 158 trên Windows 10.
- Ảnh 07–08: Chromium với giả lập cảm ứng iPhone 15; các ảnh còn lại dùng viewport desktop/mobile được ghi trong bảng.
- URL production: `https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/`.
- CI: run `45738100708`; Pages: run `45738100919`; deployment: `8074236451`.
- Title và thuộc tính ARIA được xác minh qua DOM; ảnh chỉ minh họa trạng thái hiển thị.
