# Danh mục ảnh chụp ứng dụng

## Bộ lịch sử ngày 25/11/2026

Tất cả ảnh được chụp ngày **25/11/2026**, bằng Chrome Headless 158, Playwright CLI 0.1.25, trên **local Release** tại `http://127.0.0.1:5198/`. Trạng thái mã nguồn cho từng ảnh là working tree Phase D–F trên commit `955956b2298be11fd84937ea390d66d5bd2119bc`, đã gồm bản sửa title. Ảnh 08 và 14 là ảnh chụp vùng component, cột viewport vẫn ghi kích thước cửa sổ thực. Bản không dấu được lưu cho ca tìm kiếm, hai truy vấn có dấu và không dấu có cùng kết quả tại E-U02.

| Tệp | Route | Viewport | Chức năng | Caption đề xuất |
| --- | --- | --- | --- | --- |
| [01-home-desktop.png](01-home-desktop.png) | `/` | 1440 × 900 | Trang chủ desktop | Trang chủ BA ĐỘNG trên desktop |
| [02-home-tablet.png](02-home-tablet.png) | `/` | 768 × 900 | Trang chủ tablet | Trang chủ trên màn hình tablet |
| [03-home-mobile.png](03-home-mobile.png) | `/` | 390 × 844 | Trang chủ mobile | Trang chủ trên thiết bị di động |
| [04-mobile-menu.png](04-mobile-menu.png) | `/` | 390 × 844 | Menu mobile mở | Điều hướng di động khi menu mở |
| [05-explore.png](05-explore.png) | `/kham-pha` | 1440 × 900 | Danh sách địa điểm | Danh mục địa điểm và công cụ tìm kiếm |
| [06-explore-search.png](06-explore-search.png) | `/kham-pha` | 1440 × 900 | Tìm từ khóa không dấu | Tìm “hoang hon” cho cùng kết quả với “hoàng hôn” |
| [07-explore-filter.png](07-explore-filter.png) | `/kham-pha` | 1440 × 900 | Lọc Thiên nhiên | Kết quả lọc địa điểm theo danh mục Thiên nhiên |
| [08-explore-empty.png](08-explore-empty.png) | `/kham-pha` | 1440 × 900 | Empty state, chụp vùng | Thông báo không có kết quả và thao tác xóa bộ lọc |
| [09-destination.png](09-destination.png) | `/kham-pha/bien-ba-dong` | 1440 × 900 | Chi tiết địa điểm | Trang chi tiết Biển Ba Động |
| [10-cuisine.png](10-cuisine.png) | `/am-thuc` | 1440 × 900 | Danh sách ẩm thực | Món ăn và bộ lọc danh mục |
| [11-food-detail.png](11-food-detail.png) | `/am-thuc/cua-bien` | 1440 × 900 | Chi tiết món ăn | Chi tiết Cua biển với ghi công ảnh |
| [12-gallery.png](12-gallery.png) | `/thu-vien` | 1440 × 900 | Thư viện lưới | Thư viện ảnh có hồ sơ nguồn |
| [13-gallery-lightbox.png](13-gallery-lightbox.png) | `/thu-vien` | 1440 × 900 | Lightbox | Hộp thoại xem ảnh Biển Ba Động |
| [14-guide-faq.png](14-guide-faq.png) | `/cam-nang` | 1440 × 900 | FAQ mở, chụp vùng | Câu hỏi về thời điểm đi Ba Động và nguồn tham khảo |
| [15-itinerary.png](15-itinerary.png) | `/lich-trinh` | 1440 × 900 | Tab lịch trình thứ hai | Lịch trình hai ngày được chọn |
| [16-location.png](16-location.png) | `/lien-he` | 1440 × 900 | Thông tin vị trí | Vị trí tham khảo và điểm mở Google Maps |
| [17-invalid-destination.png](17-invalid-destination.png) | `/kham-pha/khong-ton-tai` | 1440 × 900 | Slug địa điểm sai | Trạng thái không tìm thấy địa điểm và lối quay lại |
| [18-not-found.png](18-not-found.png) | `/khong-tim-thay` | 1440 × 900 | Trang không tìm thấy | Trang 404 thân thiện và điều hướng phục hồi |

Title trong browser được xác minh qua DOM trong [báo cáo kỹ thuật](../academic-validation/2026-W48-phase-d-f.md). Ảnh nội dung trang hỗ trợ minh họa trạng thái hiển thị trong thân trang.

## Bộ production của bản phát hành cuối

Bộ 18 ảnh trên được giữ nguyên như bằng chứng lịch sử. Bản phát hành cuối `1c04cb15c700c5a78c4c89d3be63008af990fd5f` có [13 ảnh production và manifest riêng](release-1c04cb1/MANIFEST.md), chụp ngày 26/11/2026. Khi trích dẫn kết quả UI cuối, dùng tên file có hậu tố `1c04cb1`; khi mô tả kiểm thử Phase D–F, tiếp tục dùng ảnh 01–18 lịch sử.
