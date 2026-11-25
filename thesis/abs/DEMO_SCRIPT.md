# Kịch bản trình diễn BA ĐỘNG Coastal Escape

Trình bày 15 slide trong khoảng 12 phút 50 giây, gồm phần trình diễn 4 phút 40 giây ở slide 14. Có thể điều chỉnh theo thời lượng giảng viên yêu cầu. Mở sẵn [website](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/), kho mã nguồn, hai lần chạy Actions và terminal. Chọn đúng bản phát hành [463da37](../../docs/RELEASE_BASELINE.md).

| Mốc | Thao tác | Kết quả mong đợi và câu dẫn |
| --- | --- | --- |
| 00:00–00:15 | Mở URL production tại thư mục dự án. | Trang chủ hiện sau khi Blazor khởi động. “Đây là bản tĩnh đã công bố trên GitHub Pages.” |
| 00:15–00:30 | Giới thiệu ảnh đầu trang và nút Khám phá. | “Người dùng đi từ câu chuyện về bờ biển đến danh sách các điểm đến.” |
| 00:30–00:45 | Chọn Khám phá Ba Động. | Danh sách hiện 7 địa điểm ở trạng thái mặc định. “Mỗi thẻ dẫn tới một mục nội dung có đường dẫn riêng.” |
| 00:45–01:10 | Nhập “hoàng hôn”. Đổi thành “hoang hon”. | Cả hai lần cho Góc ngắm hoàng hôn. “Cách bỏ dấu kết hợp hỗ trợ cặp này. Chữ đ và d vẫn được phân biệt.” |
| 01:10–01:25 | Xóa từ khóa, chọn Thiên nhiên rồi trở lại Tất cả. | Danh sách được thu hẹp và khôi phục. “Danh mục và từ khóa là hai điều kiện của cùng phép lọc.” |
| 01:25–01:44 | Mở thẻ Biển Ba Động. | URL kết thúc bằng bien-ba-dong và tiêu đề đúng. “Slug được tra trong tập địa điểm.” |
| 01:44–02:00 | Trỏ vào ghi công và liên kết nguồn trên trang chi tiết. | “Ảnh Biển Ba Động có tác giả và giấy phép. Các mục chờ xác minh dùng ảnh giữ chỗ.” |
| 02:00–02:20 | Mở Ẩm thực, chọn Cua biển. | Trang món có mô tả và thông tin ảnh. “Thông tin dùng để tham khảo.” |
| 02:20–02:38 | Mở Thư viện, chọn một ảnh, dùng mũi tên và Escape. | Hộp thoại đổi ảnh, đóng và trả focus. “Ảnh có thông tin ghi công và có thể thao tác bằng bàn phím.” |
| 02:38–02:56 | Mở Lên lịch trình, chọn “2 ngày 1 đêm”. | Nội dung đổi theo tab. “Lịch trình là đề xuất và một số điểm dừng có liên kết đến địa điểm.” |
| 02:56–03:17 | Đổi vùng hiển thị xuống 390 px, mở menu rồi nhấn Escape. | Menu đóng và focus trở về nút mở. “Đây là kích thước giả lập trong trình duyệt.” |
| 03:17–03:44 | Mở Program.cs, ContentService.cs, Explore.razor và một tệp JSON đã đặt sẵn tab. | “Chương trình đăng ký dịch vụ một lần. Mỗi lần chọn bộ lọc chỉ xử lý dữ liệu trong trình duyệt.” |
| 03:44–04:13 | Chạy lệnh test đã chuẩn bị dưới đây. | “Đọc tổng số ca và kết quả mà terminal in.” Nếu lệnh chưa xong, dùng số liệu CI cùng SHA và nêu rõ đó là bằng chứng đã lưu. |
| 04:13–04:40 | Mở kết quả CI và Pages, trỏ vào SHA và trạng thái. | “Hai workflow có trách nhiệm riêng và đã thành công trên cùng commit. URL sâu trực tiếp có thể trả 404 trước khi ứng dụng chuyển đúng trang.” |

Các bước trình diễn dựa trên [bằng chứng kỹ thuật](../../docs/evidence/academic-validation/2026-W48-phase-d-f.md). Khả năng sao chép clipboard còn ngoài phạm vi kiểm tra đã ghi nhận.

## Phương án dự phòng tại máy

Chuẩn bị trước khi mất mạng. Khôi phục gói khi còn Internet. Giữ terminal ở thư mục gốc kho mã nguồn và kiểm tra SDK tương thích với [global.json](../../global.json).

~~~powershell
dotnet --version
$app = 'src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj'
$tests = 'tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj'
dotnet restore $app
dotnet restore $tests
dotnet build $app -c Release --no-restore
dotnet test --project $tests -c Release --no-restore
dotnet run --project $app -c Release --no-build --no-launch-profile --urls http://127.0.0.1:5198
~~~

Mở [bản local ở cổng 5198](http://127.0.0.1:5198/). Có thể chạy lệnh test trong terminal thứ hai sau khi đã khôi phục gói. Bản local minh họa giao diện và tương tác. Giới hạn HTTP 404 của GitHub Pages được giải thích bằng [bằng chứng của bản công khai](../../docs/RELEASE_BASELINE.md).

Khi local cũng không chạy được, mở PDF slide và [danh mục ảnh chụp đã xác minh](../../docs/evidence/screenshots/MANIFEST.md). Ảnh 01, 05–09, 11, 13, 15 và 04 lần lượt hỗ trợ trình bày trang chủ, tìm kiếm, chi tiết, món ăn, thư viện, lịch trình và menu. Dùng bảng kết quả trong luận văn để giải thích test và ghi rõ môi trường của số liệu.
