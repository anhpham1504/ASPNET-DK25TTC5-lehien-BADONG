# Mốc phát hành và đóng băng chức năng

Phát hành ngày 25/11/2026, lúc 11:24:19 theo giờ Việt Nam (04:24:19 UTC). Repository `anhpham1504/ASPNET-DK25TTC5-lehien-BADONG`, nhánh `main`.

| Mốc | Bằng chứng |
| --- | --- |
| SHA phát hành | [463da372613648411ef9d6002c4d895cb03cbb4d](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/463da372613648411ef9d6002c4d895cb03cbb4d) |
| Commit sửa title | [92c5fa62139e17ef8bc73bc5a288b3ea0c5c4391](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/92c5fa62139e17ef8bc73bc5a288b3ea0c5c4391) |
| CI | [45546387181, success](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45546387181), cùng SHA phát hành |
| Deploy to GitHub Pages | [45546387162, success](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45546387162), deployment `8048326076` ghi success cho cùng SHA |
| Production | [BA ĐỘNG — Coastal Escape](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/) |
| Local preflight và lượt xác minh lại | SDK `10.0.100`, restore app/test đạt, Release build 0 cảnh báo và 0 lỗi, 14 đạt, 0 lỗi, 0 bỏ qua |
| Remote CI | Release build 0 cảnh báo và 0 lỗi, 14 đạt, 0 lỗi, 0 bỏ qua |
| Kích thước artifact từ CI | Tổng các file Brotli trong thư mục framework 2.824.213 byte. Tệp runtime native WASM chưa nén 2.900.443 byte. Các số này là kích thước tệp từ workflow. |

## Smoke test production

Chrome Headless 158, viewport 1440 × 900, ngày 25/11/2026. Mỗi ca quan sát đúng URL và một thẻ `head title` sau khi Blazor render, cùng heading trong `main`.

| Route dưới base của dự án | HTTP tài liệu ban đầu | Document title |
| --- | ---: | --- |
| `/` | 200 | BA ĐỘNG — Coastal Escape · Nơi biển chạm vào nhịp sống miền Tây |
| `/kham-pha/bien-ba-dong` | 404 | Biển Ba Động · BA ĐỘNG — Coastal Escape |
| `/kham-pha/khong-ton-tai` | 404 | Không tìm thấy địa điểm · BA ĐỘNG — Coastal Escape |
| `/am-thuc` | 404 | Ẩm thực · BA ĐỘNG — Coastal Escape |
| `/am-thuc/cua-bien` | 404 | Cua biển · Ẩm thực Ba Động |
| `/am-thuc/khong-ton-tai` | 404 | Không tìm thấy món ăn · Ẩm thực Ba Động |
| `/khong-tim-thay` | 404 | Không tìm thấy · BA ĐỘNG — Coastal Escape |

Điều hướng từ lỗi địa điểm về Khám phá, mở Biển Ba Động, tải lại trang chi tiết và quay về danh sách ẩm thực đều đạt. Lượt hoàn tất ghi nhận CSS, JS, hình, WASM và JSON trả 200, không có lỗi request asset/JSON, page exception hay console error ngoài 404 tài liệu dự kiến. Lượt đầu có request framework bị Chromium hủy; lượt sau kiểm tra lại trên cùng bản phát hành và không tái hiện.

Lượt xác minh lại ngày 25/11/2026 ở 1440 × 900 kiểm tra đạt 7/7 title sau khi Blazor khởi động. Điều hướng từ slug địa điểm không tồn tại qua Khám phá đến Biển Ba Động hoạt động. Chromium ghi nhận một số yêu cầu bị hủy trong lượt điều hướng. Không ghi nhận phản hồi HTTP lỗi ở asset hoặc JSON, ngoại lệ JavaScript hoặc lỗi console ngoài HTTP 404 ban đầu của tài liệu deep link.

## Phạm vi đóng băng

Chức năng website được đóng băng tại SHA trên. Phase G–I cập nhật hồ sơ luận văn trong working tree. [Kết quả Phase D–F](evidence/academic-validation/2026-W48-phase-d-f.md) và [danh mục ảnh](evidence/screenshots/MANIFEST.md) giữ nguồn gốc local và lịch sử. Giới hạn HTTP 404 trước fallback, HTML loader chưa có title riêng, canonical theo route, ảnh PENDING và mức độ kiểm tra accessibility được ghi trong [Known limitations](KNOWN_LIMITATIONS.md).
