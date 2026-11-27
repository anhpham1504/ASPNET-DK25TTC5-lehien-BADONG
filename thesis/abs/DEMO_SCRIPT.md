# Kịch bản trình diễn BA ĐỘNG Coastal Escape

Trình bày 15 slide trong khoảng 12 phút 50 giây, gồm phần trình diễn 4 phút 40 giây ở slide 14. Có thể điều chỉnh theo thời lượng giảng viên yêu cầu. Mở sẵn [website](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/), kho mã nguồn, [CI 45775505092](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45775505092), [Pages 45775504992](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45775504992) và terminal. Chọn đúng bản phát hành [ec0d53f](../../docs/RELEASE_BASELINE.md).

| Mốc | Thao tác | Kết quả mong đợi và câu dẫn |
| --- | --- | --- |
| 00:00–00:15 | Mở URL production tại thư mục dự án. | Trang chủ hiện sau khi Blazor khởi động. “Đây là bản tĩnh đã công bố trên GitHub Pages.” |
| 00:15–00:30 | Giới thiệu ảnh đầu trang và nút Khám phá. | “Người dùng đi từ câu chuyện về bờ biển đến danh sách các điểm đến.” |
| 00:30–00:45 | Chọn Khám phá Ba Động. | Danh sách hiện 7 địa điểm ở trạng thái mặc định. “Mỗi thẻ dẫn tới một mục nội dung có đường dẫn riêng.” |
| 00:45–01:10 | Nhập “hoàng hôn”. Đổi thành “hoang hon”. | Cả hai lần cho Góc ngắm hoàng hôn. “Cách bỏ dấu kết hợp hỗ trợ cặp này. Chữ đ và d vẫn được phân biệt.” |
| 01:10–01:25 | Xóa từ khóa, chọn Thiên nhiên rồi trở lại Tất cả. | Danh sách được thu hẹp và khôi phục. “Danh mục và từ khóa là hai điều kiện của cùng phép lọc.” |
| 01:25–01:44 | Mở thẻ Biển Ba Động. | URL kết thúc bằng bien-ba-dong và tiêu đề đúng. “Slug được tra trong tập địa điểm.” |
| 01:44–02:00 | Chọn Chia sẻ liên kết rồi trỏ vào ghi công ảnh. | Nút đổi thành Đã sao chép và vẫn rõ trên nền tối. “Ảnh Biển Ba Động có tác giả và giấy phép; URL hiện tại đã được đưa vào clipboard.” |
| 02:00–02:20 | Mở Ẩm thực, chọn Cua biển. | Trang món có mô tả và thông tin ảnh. “Thông tin dùng để tham khảo.” |
| 02:20–02:38 | Mở Thư viện, chọn một ảnh, dùng mũi tên và Escape. | Hộp thoại đổi ảnh, đóng và trả focus. “Ảnh có thông tin ghi công và có thể thao tác bằng bàn phím.” |
| 02:38–02:56 | Mở Lên lịch trình, dùng ArrowRight rồi Home và End. | Tab, nội dung và focus đổi đồng bộ, trang không cuộn ngoài ý muốn. “Mỗi tab liên kết với một panel tồn tại; panel không chọn được ẩn.” |
| 02:56–03:17 | Đổi vùng hiển thị xuống 390 px, mở menu rồi nhấn Escape. | Menu đóng và focus trở về nút mở. “Đây là kích thước giả lập trong trình duyệt.” |
| 03:17–03:44 | Mở Program.cs, ContentService.cs, Explore.razor và một tệp JSON đã đặt sẵn tab. | “Chương trình đăng ký dịch vụ một lần. Mỗi lần chọn bộ lọc chỉ xử lý dữ liệu trong trình duyệt.” |
| 03:44–04:13 | Chạy lệnh test đã chuẩn bị dưới đây. | “Đọc tổng số ca và kết quả mà terminal in.” Nếu lệnh chưa xong, dùng số liệu CI cùng SHA và nêu rõ đó là bằng chứng đã lưu. |
| 04:13–04:40 | Mở kết quả CI và Pages, trỏ vào candidate `92691a8`, merge SHA `ec0d53f` và trạng thái. | “CI xác minh candidate; Pages triển khai merge commit. CI hoàn tất native relinking và wasm-opt. URL sâu trực tiếp có thể trả 404 trước khi ứng dụng chuyển đúng trang.” |

Các bước trình diễn dựa trên [mốc phát hành](../../docs/RELEASE_BASELINE.md) và [28 ảnh production cuối](../../docs/evidence/screenshots/release-ec0d53f/MANIFEST.md). Clipboard và focus restoration nằm trong nhóm tương tác đã kiểm của release cuối.

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

Khi local cũng không chạy được, mở PDF slide, [bộ 28 ảnh `ec0d53f`](../../docs/evidence/screenshots/release-ec0d53f/MANIFEST.md) và bản HTML luận văn offline. Dùng bảng kết quả trong luận văn để giải thích test và ghi rõ môi trường của số liệu. Các bộ ảnh cũ chỉ dùng khi trình bày lịch sử hồi quy.
