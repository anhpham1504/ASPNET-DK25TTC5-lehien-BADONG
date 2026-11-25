# Giới hạn đã biết

## GitHub Pages và đường dẫn sâu

GitHub Pages phục vụ artifact tĩnh của Blazor WebAssembly Standalone. Mở trực tiếp một route như `/kham-pha/bien-ba-dong` có thể nhận HTTP 404. Trang [404.html](../src/BaDong.CoastalEscape/wwwroot/404.html) lưu đường dẫn đích trong session storage và chuyển về base của dự án. [app.js](../src/BaDong.CoastalEscape/wwwroot/app.js) khôi phục path cho Router, vì vậy trình duyệt hỗ trợ JavaScript có thể mở nội dung sau khi khởi động ứng dụng. HTTP ban đầu vẫn có ảnh hưởng với crawler, bản xem trước liên kết và SEO.

Prerendering, static-first hoặc SSR là hướng khảo sát sau nghiệm thu. Mã nguồn hiện tại chưa cung cấp canonical riêng theo route. Bản sửa title tại [mốc phát hành](RELEASE_BASELINE.md) áp dụng từ lúc trang Razor bắt đầu render. HTML loader trước khi tải xong WASM vẫn có các metadata tĩnh hiện có và chưa có title riêng.

## Accessibility

Đã kiểm tra heading, landmark `main`, `lang=vi`, focus nhìn thấy khi quay lại từ trang lỗi, vòng focus menu di động, lightbox bằng bàn phím, kích hoạt FAQ và tab lịch trình, reduced motion và các route responsive ở 320/390/768/1440 px. Bằng chứng này thuộc các route và tương tác liệt kê trong [báo cáo kiểm thử](evidence/academic-validation/2026-W48-phase-d-f.md). Kiểm thử với trình đọc màn hình, kiểm toán độ tương phản, 200% zoom, hỗ trợ công nghệ trợ năng và audit đầy đủ WCAG 2.2 AA còn mở.

## Bố cục trang chủ

Kiểm tra trên Chromium ở GitHub Pages ngày 25/11/2026 cho thấy chỉ dẫn “Cuộn để đi tiếp” bị cắt chữ ở chiều rộng 1.024, 1.280 và 1.289 px. Hai nút khám phá và xem hành trình nằm dưới vùng nhìn ban đầu ở 320 × 568 và 844 × 390 px. Ở 1.366 × 768 px, tiêu đề tự nhận focus, hiện viền cam và lần bấm `Tab` đầu tiên đến nút Khám phá Ba Động sau thanh điều hướng. Đây là các phát hiện trên [bản phát hành đã đóng băng](RELEASE_BASELINE.md).

## Nội dung và ảnh

| Nguồn | Kiểm kê theo JSON |
| --- | --- |
| Destinations | 7 mục: 2 `VERIFIED`, 5 `PENDING` |
| Foods | 4 mục: 1 `VERIFIED`, 3 `VERIFIED_SUBJECT` |
| Gallery | 7 mục: 3 `VERIFIED`, 1 `VERIFIED_REGION`, 3 `VERIFIED_SUBJECT` |
| Image manifest | 8 bản ghi: 3 `VERIFIED`, 1 `VERIFIED_REGION`, 3 `VERIFIED_SUBJECT`, 1 `INTERNAL_PLACEHOLDER` |
| Image requirements | 5 yêu cầu `PENDING` |
| Itineraries, FAQ, SiteInfo | 2 lịch trình, 5 câu hỏi, 1 object thông tin |

Địa điểm PENDING dùng SVG placeholder. Ảnh VERIFIED_REGION và VERIFIED_SUBJECT có phạm vi xác minh hẹp hơn ảnh chính xác tại địa điểm. Các con số phản ánh metadata trong repo tại baseline cùng thay đổi local. Kiểm thử tự động đối chiếu nội dung metadata và sự hiện diện của file. Việc xác minh mới từng ảnh ngoài đời hoặc kiểm tra lại từng nguồn và giấy phép không thuộc đợt này. Tham khảo [nguồn nội dung và giấy phép](CONTENT_SOURCES.md).

## Dữ liệu runtime

`ContentService` trả danh sách rỗng hoặc object mặc định khi HTTP/JSON lỗi. Trang chi tiết dùng title báo chưa có dữ liệu với danh sách rỗng, kể cả khi API tĩnh gửi danh sách rỗng hợp lệ. Phép lọc tiếng Việt bỏ dấu kết hợp và phân biệt cặp `đ/d`. Nội dung lịch trình, thời tiết và bản đồ là thông tin tham khảo.
