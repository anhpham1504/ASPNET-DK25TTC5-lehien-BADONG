# Mốc phát hành cuối và đóng băng chức năng

Thiết kế cuối được phát hành ngày **26/11/2026** từ repository `anhpham1504/ASPNET-DK25TTC5-lehien-BADONG`, nhánh `main`. Đây là mốc sản phẩm đóng băng dùng để đồng bộ luận văn; commit tích hợp tài liệu local không phải SHA production.

| Mốc | Bằng chứng |
| --- | --- |
| SHA sản phẩm cuối | [ec0d53f180570e59c084a9ce7f74aa89d5ee3abe](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/ec0d53f180570e59c084a9ce7f74aa89d5ee3abe) |
| Pull Request | [#4 — Final UI/UX redesign and release readiness](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/pull/4), merge commit |
| Candidate cuối | [92691a862e72ad0fedddef78a2e58a45b30e92cb](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/92691a862e72ad0fedddef78a2e58a45b30e92cb) |
| Commit thiết kế | [c79a5eb](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/c79a5eb), sau đó [92691a8](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/92691a8) sửa cascade responsive |
| Baseline trước redesign | [c992fda52dd0cb888b2bde5700e14f3628b38d3e](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/commit/c992fda52dd0cb888b2bde5700e14f3628b38d3e) |
| CI | [45775505092, success](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45775505092), đúng candidate `92691a8` |
| Deploy to GitHub Pages | [45775504992, success](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45775504992), đúng merge SHA sản phẩm cuối |
| Production | [BA ĐỘNG — Coastal Escape](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/) |
| Build và test | Release build 0 cảnh báo, 0 lỗi; 14 đạt, 0 lỗi, 0 bỏ qua |
| Native publish CI | PASS: cài `wasm-tools`, native relinking, compiling native assets và `wasm-opt` hoàn tất |
| Kích thước artifact CI | 43 framework resources; framework Brotli 2.826.634 byte; native runtime WASM 2.900.443 byte; native runtime WASM Brotli 931.222 byte |

## Xác minh production cuối

Chrome Headless 158 chạy **48/48 tổ hợp**, gồm 12 route × 4 viewport, trên bản đã triển khai `ec0d53f`. Mỗi lượt đợi ứng dụng tải xong rồi kiểm route, title, heading, tràn ngang, ảnh, asset, JSON và lỗi console/page. Không ghi nhận horizontal overflow, broken image, failed asset request hoặc console/page error trong phạm vi này. HTTP 404 của tài liệu ban đầu khi mở deep link được ghi riêng với lỗi chức năng; cơ chế SPA vẫn khôi phục đúng route sau khi ứng dụng tải.

Sitemap có **19/19 URL** kết xuất đúng sau khi ứng dụng tải hoàn tất. Kết quả này không có nghĩa 19 URL đều nhận HTTP 200 ở phản hồi đầu. Các nhóm search/filter, empty state, menu mobile, FAQ, itinerary tabs, lightbox, clipboard và focus restoration đều đạt. Năm địa điểm chưa có ảnh xác minh tiếp tục được trình bày bằng editorial card với trạng thái `PENDING`.

Bộ [28 ảnh production của `ec0d53f`](evidence/screenshots/release-ec0d53f/MANIFEST.md) gồm 10 ảnh desktop, 10 ảnh mobile và 8 ảnh tương tác. Ảnh được giữ nguyên nội dung và gắn route, viewport, ngày thu thập cùng release SHA.

## Số liệu hiệu năng lịch sử

Bảng sau là median của 5 lượt local Release, Chrome 1440 × 900, có warm-up và chạy xen kẽ Before/After. Đây không phải phép đo production cuối.

| Chỉ số | Before | After |
| --- | ---: | ---: |
| LCP | 988 ms | 1.028 ms |
| CLS | 0,00083 | 0,00106 |
| FCP | 236 ms | 276 ms |
| Load event | 625 ms | 654 ms |

Chênh lệch nhỏ theo hướng tăng trong phép đo này không được diễn giải thành cải thiện hiệu năng. Không có kết quả Lighthouse, TBT hoặc INP được công bố cho release cuối.

## Mốc lịch sử

- `463da372613648411ef9d6002c4d895cb03cbb4d` là mốc đóng băng trước đợt tinh chỉnh UI đầu tiên.
- `1c04cb15c700c5a78c4c89d3be63008af990fd5f` có ma trận production 52 lượt và 13 ảnh riêng.
- `c992fda52dd0cb888b2bde5700e14f3628b38d3e` là hotfix tương phản nút chia sẻ, có targeted regression riêng.
- `c79a5eb` là candidate redesign; `92691a8` sửa cascade ở breakpoint 820 px; `ec0d53f` là merge commit production chính thức.

Các kết quả lịch sử giữ nguyên SHA và phạm vi, không dùng để chứng minh release khác.

## Phạm vi đóng băng

Chức năng website được đóng băng tại SHA `ec0d53f180570e59c084a9ce7f74aa89d5ee3abe`. Sau mốc này không phát triển thêm tính năng, redesign, refactor hoặc migration. Chỉ sửa lỗi nghiêm trọng hoặc yêu cầu trực tiếp của giảng viên. Giới hạn HTTP 404 trước fallback, metadata HTML ban đầu, ảnh `PENDING` và phạm vi accessibility còn mở được ghi trong [Known limitations](KNOWN_LIMITATIONS.md).
