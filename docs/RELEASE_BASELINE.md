# Mốc phát hành cuối và đóng băng chức năng

Hotfix cuối phát hành ngày **26/11/2026**. Repository `anhpham1504/ASPNET-DK25TTC5-lehien-BADONG`, nhánh `main`. PR được merge lúc 09:55 và deployment GitHub Pages hoàn tất lúc 09:57 theo giờ Việt Nam.

| Mốc | Bằng chứng |
| --- | --- |
| SHA sản phẩm cuối | [c992fda52dd0cb888b2bde5700e14f3628b38d3e](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/c992fda52dd0cb888b2bde5700e14f3628b38d3e) |
| Pull Request hotfix | [#3 — Correct ghost button background contrast](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/pull/3), merge commit |
| Commit hotfix | [534f0d2ae31e23af76f3f88660bfac176edbbd46](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/534f0d2ae31e23af76f3f88660bfac176edbbd46) |
| Bản UI trước hotfix | [1c04cb15c700c5a78c4c89d3be63008af990fd5f](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/1c04cb15c700c5a78c4c89d3be63008af990fd5f), PR [#2](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/pull/2) |
| CI | [45745648779, success](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45745648779), đúng SHA sản phẩm cuối |
| Deploy to GitHub Pages | [45745648732, success](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45745648732), deployment `8075210041`, đúng SHA sản phẩm cuối |
| Production | [BA ĐỘNG — Coastal Escape](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/) |
| Build và test | Release build 0 cảnh báo, 0 lỗi; 14 đạt, 0 lỗi, 0 bỏ qua |
| Native publish CI | PASS: cài `wasm-tools`, native relinking, compiling native assets và `wasm-opt` hoàn tất |
| Kích thước artifact CI | 43 framework resources; framework Brotli 2.826.655 byte; native runtime WASM 2.900.443 byte; native runtime WASM Brotli 931.222 byte |

## Xác minh production

Ma trận 13 route × 4 viewport, tổng cộng **52 lượt**, được thực hiện trên bản `1c04cb1` ngay trước hotfix. Tất cả lượt kết xuất đúng route, một title, heading chính, không tràn ngang, không ảnh hỏng và không có lỗi asset, JSON, JavaScript hoặc page exception. Trong 48 lượt mở trực tiếp route sâu, GitHub Pages trả HTTP 404 cho tài liệu ban đầu rồi cơ chế SPA khôi phục đúng route; bốn lượt trang chủ trả HTTP 200. Không dùng ma trận này để tuyên bố 52 lượt đã chạy lại trên `c992fda`.

Hotfix `c992fda` được kiểm tra có mục tiêu tại `/kham-pha/bien-ba-dong` bằng Chrome Headless 158 ở 1440 × 900 và giả lập iPhone 15 ở 390 × 844. CSS production trả đúng `background: transparent`; trạng thái normal, hover, focus, copied, touch, Enter và Space đều đạt. Clipboard chứa đúng URL hiện tại, focus ring còn rõ và vị trí cuộn không đổi. Tương phản đo từ màu kết xuất đạt 11,91:1 ở normal/copied và 8,31:1 ở hover. PageTitle đúng, console không có error hoặc warning.

Các nhóm tương tác của bản `1c04cb1` được giữ làm bằng chứng hồi quy cho tìm kiếm, filter, empty state, menu, lightbox, FAQ, header state và tab lịch trình. Hotfix chỉ thay một khai báo CSS nên không chạy lại toàn bộ ma trận.

Mười ba ảnh production của bản `1c04cb1` nằm trong [bộ bằng chứng phát hành UI](evidence/screenshots/release-1c04cb1/MANIFEST.md). Ảnh chi tiết địa điểm sau hotfix nằm trong [bộ bằng chứng `c992fda`](evidence/screenshots/hotfix-c992fda/MANIFEST.md). Bộ 18 ảnh lịch sử ngày 25/11/2026 và tất cả ảnh `1c04cb1` được giữ nguyên.

## Mốc lịch sử

Mốc `463da372613648411ef9d6002c4d895cb03cbb4d` ngày 25/11/2026 là bản đóng băng trước đợt tinh chỉnh UI. Bản `1c04cb1` ngày 26/11/2026 là phát hành UI đã vượt qua ma trận production 52 lượt trước khi phát hiện nền mặc định của nút chia sẻ. Các kết quả lịch sử vẫn giữ nguyên SHA và phạm vi, không dùng để chứng minh hotfix.

## Phạm vi đóng băng

Chức năng website được đóng băng tại SHA `c992fda52dd0cb888b2bde5700e14f3628b38d3e`. Sau mốc này không phát triển thêm tính năng, redesign, refactor hoặc migration. Chỉ sửa lỗi nghiêm trọng hoặc yêu cầu trực tiếp của giảng viên. Commit học thuật sau phát hành chỉ cập nhật hồ sơ và phải phân biệt với SHA sản phẩm đã triển khai. Giới hạn HTTP 404 trước fallback, metadata HTML ban đầu, ảnh PENDING và phạm vi accessibility còn mở được ghi trong [Known limitations](KNOWN_LIMITATIONS.md).
