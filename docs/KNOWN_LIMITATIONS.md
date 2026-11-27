# Giới hạn đã biết

## GitHub Pages và đường dẫn sâu

GitHub Pages phục vụ artifact tĩnh của Blazor WebAssembly Standalone. Trong ma trận production cuối ngày 26/11/2026, 48/48 tổ hợp route/viewport đạt sau khi ứng dụng tải hoàn tất; các deep link vẫn có thể nhận HTTP 404 cho tài liệu ban đầu. Trang [404.html](../src/BaDong.CoastalEscape/wwwroot/404.html) lưu đường dẫn đích và [app.js](../src/BaDong.CoastalEscape/wwwroot/app.js) khôi phục route sau khi ứng dụng khởi động. Nội dung cuối, title, heading, asset và JSON đều đúng trong phạm vi đã kiểm, nhưng HTTP ban đầu vẫn ảnh hưởng crawler, bản xem trước liên kết và SEO.

Mã nguồn chưa cung cấp prerendering, SSR hoặc canonical riêng cho từng route. HTML loader trước khi tải xong WebAssembly vẫn dùng metadata tĩnh. Bản phát hành cuối không tuyên bố giải quyết giới hạn SEO này.

## Accessibility và trình duyệt

Bản phát hành cuối đã kiểm heading, landmark `main`, `lang=vi`, focus nhìn thấy, menu và lightbox bằng bàn phím, FAQ, filter `aria-pressed`, clipboard, focus restoration và quan hệ tab/panel lịch trình. Panel không chọn vẫn tồn tại trong DOM nhưng có `hidden`, chỉ panel đang hoạt động xuất hiện trong accessibility tree. ArrowLeft, ArrowRight, Home và End giữ nguyên vị trí cuộn; Tab và Shift+Tab không bị chặn.

Hotfix lịch sử `c992fda` bổ sung phép kiểm có mục tiêu cho nút Chia sẻ liên kết. Màu kết xuất đạt 11,91:1 ở normal/copied và 8,31:1 ở hover; focus ring, Enter, Space, touch và clipboard đều đạt trên Chrome Headless 158. Bản `ec0d53f` giữ hành vi này trong ma trận tương tác cuối. Kết quả vẫn không thay cho kiểm toán tương phản toàn site hoặc audit WCAG đầy đủ.

Các kiểm tra landscape, caption cảm ứng và font fallback khi stylesheet Google Fonts trả 503 cũng đạt. Các mục sau chưa chạy vì môi trường không có công cụ tương ứng hoặc không thể tạo phép đo đáng tin cậy mà không cài thêm dependency:

- Firefox: **NOT RUN**;
- WebKit: **NOT RUN**;
- axe-core: **NOT RUN**;
- browser zoom 200% thực tế: **NOT RUN**;
- screen reader, kiểm toán tương phản toàn site và audit WCAG 2.2 AA đầy đủ: **NOT RUN**.

Ma trận production cuối dùng Chrome Headless 158 và giả lập viewport/touch; nó không thay thế kiểm thử trên phần cứng di động thật hoặc công nghệ hỗ trợ.

## Nội dung và ảnh

| Nguồn | Kiểm kê theo JSON |
| --- | --- |
| Destinations | 7 mục: 2 `VERIFIED`, 5 `PENDING` |
| Foods | 4 mục: 1 `VERIFIED`, 3 `VERIFIED_SUBJECT` |
| Gallery | 7 mục: 3 `VERIFIED`, 1 `VERIFIED_REGION`, 3 `VERIFIED_SUBJECT` |
| Image manifest | 8 bản ghi: 3 `VERIFIED`, 1 `VERIFIED_REGION`, 3 `VERIFIED_SUBJECT`, 1 `INTERNAL_PLACEHOLDER` |
| Image requirements | 5 yêu cầu `PENDING` |
| Itineraries, FAQ, SiteInfo | 2 lịch trình, 5 câu hỏi, 1 object thông tin |

Địa điểm PENDING dùng SVG placeholder. Ảnh VERIFIED_REGION và VERIFIED_SUBJECT có phạm vi xác minh hẹp hơn ảnh chính xác tại địa điểm. Kiểm thử tự động đối chiếu metadata và sự hiện diện của file; chưa có đợt xác minh thực địa hoặc kiểm tra lại từng nguồn và giấy phép. Tham khảo [nguồn nội dung và giấy phép](CONTENT_SOURCES.md).

## Dữ liệu runtime

`ContentService` trả danh sách rỗng hoặc object mặc định khi HTTP/JSON lỗi. Trang chi tiết dùng thông báo trung tính cho dữ liệu rỗng hoặc chưa tải được, không khẳng định sai nguyên nhân. Phép lọc tiếng Việt bỏ dấu kết hợp và vẫn phân biệt `đ/d`. Nội dung lịch trình, thời tiết và bản đồ chỉ mang tính tham khảo.
