# Mốc phát hành cuối và đóng băng chức năng

Phát hành cuối ngày **26/11/2026**. Repository `anhpham1504/ASPNET-DK25TTC5-lehien-BADONG`, nhánh `main`. Merge hoàn tất lúc 08:47 và deployment GitHub Pages hoàn tất lúc 08:48 theo giờ Việt Nam.

| Mốc | Bằng chứng |
| --- | --- |
| SHA sản phẩm cuối | [1c04cb15c700c5a78c4c89d3be63008af990fd5f](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/1c04cb15c700c5a78c4c89d3be63008af990fd5f) |
| Pull Request | [#2 — Improve responsive layouts and accessibility](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/pull/2), merge commit |
| Commit UI | [806002829a3e1d68981b4457644e3b39f714c144](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/806002829a3e1d68981b4457644e3b39f714c144) |
| Commit accessibility tab | [399393e69b71411bb41700e6b41a3cb983e53a54](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/399393e69b71411bb41700e6b41a3cb983e53a54) |
| CI | [45738100708, success](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45738100708), đúng SHA sản phẩm cuối |
| Deploy to GitHub Pages | [45738100919, success](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45738100919), deployment `8074236451`, đúng SHA sản phẩm cuối |
| Production | [BA ĐỘNG — Coastal Escape](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/) |
| Build và test | Release build 0 cảnh báo, 0 lỗi; 14 đạt, 0 lỗi, 0 bỏ qua |
| Native publish CI | PASS: cài `wasm-tools`, native relinking, compiling native assets và `wasm-opt` hoàn tất |
| Kích thước artifact CI | 43 framework resources; framework Brotli 2.826.661 byte; native runtime WASM 2.900.443 byte; native runtime WASM Brotli 931.222 byte |

## Xác minh production

Chrome Headless 158, ngày 26/11/2026. Ma trận mới kiểm tra 13 route ở bốn viewport 320 × 568, 390 × 844, 768 × 1024 và 1440 × 900, tổng cộng **52 lượt**. Tất cả lượt kết xuất đúng route, một title, heading chính, không tràn ngang, không ảnh hỏng và không có lỗi asset, JSON, JavaScript hoặc page exception.

Trong 48 lượt mở trực tiếp route sâu, GitHub Pages trả HTTP 404 cho tài liệu ban đầu rồi cơ chế SPA khôi phục đúng route. Bốn lượt trang chủ trả HTTP 200. Đây là giới hạn hosting đã biết, không phải lỗi điều hướng sau khi Blazor khởi động.

Các nhóm tương tác bổ sung xác nhận:

- tìm `hoàng hôn` và `hoang hon`, bộ lọc `aria-pressed`, empty state và reset;
- menu di động, focus, Escape, khóa cuộn và bố cục landscape;
- lightbox, caption trên thiết bị cảm ứng, đổi ảnh, Escape và khôi phục focus;
- FAQ, liên kết Google Maps, header ở loading, valid và error state;
- tab lịch trình có `aria-controls`, `aria-labelledby`, `aria-selected`, panel ẩn, roving `tabindex` và điều hướng ArrowLeft, ArrowRight, Home, End, Tab, Shift+Tab mà không làm đổi vị trí cuộn trang.

Mười ba ảnh production mới nằm trong [bộ bằng chứng gắn SHA](evidence/screenshots/release-1c04cb1/MANIFEST.md). Bộ 18 ảnh lịch sử ngày 25/11/2026 được giữ nguyên để bảo toàn nguồn gốc kiểm thử trước phát hành cuối.

## Mốc lịch sử

Mốc `463da372613648411ef9d6002c4d895cb03cbb4d` ngày 25/11/2026 là bản đóng băng trước đợt tinh chỉnh UI cuối. CI `45546387181`, Pages `45546387162` và deployment `8048326076` thuộc mốc lịch sử này. Không dùng các kết quả đó để chứng minh commit UI cuối.

## Phạm vi đóng băng

Chức năng website được đóng băng tại SHA `1c04cb15c700c5a78c4c89d3be63008af990fd5f`. Sau mốc này không phát triển thêm tính năng, redesign hoặc migration. Chỉ sửa lỗi nghiêm trọng hoặc yêu cầu trực tiếp của giảng viên. Commit học thuật sau phát hành chỉ cập nhật hồ sơ và phải phân biệt với SHA sản phẩm đã triển khai. Giới hạn HTTP 404 trước fallback, metadata HTML ban đầu, ảnh PENDING và phạm vi accessibility còn mở được ghi trong [Known limitations](KNOWN_LIMITATIONS.md).
