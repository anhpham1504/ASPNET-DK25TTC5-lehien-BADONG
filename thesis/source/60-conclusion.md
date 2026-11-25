# CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

## 5.1. Kết luận và đóng góp

### 5.1.1. Sản phẩm và hồ sơ

Đồ án hoàn thành cẩm nang BA ĐỘNG — Coastal Escape với các luồng tra cứu địa điểm, ẩm thực, ảnh và lịch trình tham khảo. Việc giữ nội dung trong JSON và triển khai bằng Blazor WebAssembly cho phép dựng lại sản phẩm từ một phiên bản của kho mã nguồn. Chương 4 trình bày kết quả kiểm thử của phiên bản đó.

Kết quả của đề tài gồm một cách tổ chức cẩm nang tĩnh có thể tái kiểm tra. Tên, slug, ảnh và nguồn được mô hình hóa để tìm lại từ dữ liệu. Ma trận truy vết nối yêu cầu với nơi hiện thực và bằng chứng, gồm các dòng chưa có kiểm tra. Nhờ ma trận, người đánh giá có thể tra lại điều kiện kiểm tra cho từng chức năng và nhận ra những tiêu chí còn mở.

### 5.1.2. Hạn chế của bản phát hành

Một số ảnh vẫn cần hồ sơ phù hợp với địa điểm. Website hiển thị ảnh giữ chỗ và trạng thái trong thời gian chưa có tư liệu. Router có thể khôi phục đường dẫn sâu sau khi máy chủ trả 404. Bản động của title cập nhật khi Razor hoạt động, còn HTML ban đầu chưa có title riêng. Các yếu tố này làm giảm khả năng diễn giải nội dung nếu trình duyệt hoặc tác nhân không chạy đủ ứng dụng.

Kiểm tra trình duyệt được chọn theo thay đổi và các tác vụ chính. Kết quả về focus, bố cục và tương tác có giá trị đối với môi trường đã đo. Cần thêm các bài kiểm tương phản, zoom và công nghệ hỗ trợ. Dữ liệu hiện tại phù hợp với mục đích tham khảo, còn việc đánh giá độ đầy đủ thông tin của người đi thực tế đòi hỏi khảo sát riêng và kiểm soát cách thu thập dữ liệu.

## 5.2. Hướng phát triển

### 5.2.1. Kết xuất và đường dẫn có thể kiểm chứng

Hướng ưu tiên là giảm vai trò của fallback HTTP 404 trên các route hợp lệ. Có thể thử kết xuất trước cho tập route hữu hạn và so sánh với cách phục vụ tĩnh hiện tại. Tiêu chí nghiệm thu gồm HTTP 200 trực tiếp cho slug hợp lệ, 404 thực đối với URL không tồn tại và title đúng từ tài liệu đầu tiên. Cần kiểm tra thêm sitemap, canonical, đường dẫn tài nguyên và điều hướng sau khi Blazor khởi động. Khi có phương án chạy ở cùng quy mô, có thể đo chênh lệch payload và thời gian hiển thị với điều kiện mạng đã ghi lại.

Công việc này nên bắt đầu với một nhánh thử nghiệm nhỏ và một số route thường dùng. Nếu xây tài liệu riêng cho mỗi slug, cần tránh sinh ra route rỗng hoặc để nội dung tồn tại ở hai URL khác nhau mà không có quy tắc canonical. Nếu đổi sang môi trường có máy chủ, cần đánh giá lại phương pháp triển khai, chi phí vận hành và khả năng tái hiện khi chấm đồ án. Các lựa chọn này là đề xuất, đặt ngoài mốc đóng băng hiện nay.

### 5.2.2. Dữ liệu và nguồn gốc hình ảnh

Năm yêu cầu ảnh PENDING nên được xử lý riêng theo hồ sơ đã ghi. Mỗi ảnh bổ sung cần xác minh nơi chụp, chủ thể, tác giả, giấy phép và quyền công bố phù hợp nếu người có thể nhận diện xuất hiện. Sau đó mới tạo biến thể, đổi đường dẫn, cập nhật caption và chạy lại bộ kiểm thử file cùng siêu dữ liệu. Quá trình có thể được thực hiện từng ảnh để người rà soát đối chiếu nguồn và xem vùng giao diện chịu ảnh hưởng.

Cuối cùng, nếu số lần thay đổi nội dung tăng, có thể khảo sát công cụ quản lý nội dung để hỗ trợ quy trình rà soát. Cần duy trì siêu dữ liệu nguồn, version và trạng thái chờ ở bất kỳ cách lưu nào. Một API chỉ có ích khi có nhu cầu thật về cập nhật và quản trị nội dung. Bản đồ tương tác hoặc giao diện đa ngôn ngữ cũng cần nhu cầu rõ ràng cùng kế hoạch kiểm tra, ví dụ cách ghi đúng nguồn và tên địa danh theo ngôn ngữ hiển thị.

### 5.2.3. Kiểm thử và đánh giá bổ sung

Có thể đưa một số ca trình duyệt hiện tại vào quy trình hồi quy có mã kiểm thử. Những ca ưu tiên gồm title ở route sai, lỗi đọc JSON, focus phục hồi sau đóng dialog và các cặp từ tiếng Việt có ranh giới chuẩn hóa. Khi bổ sung kiểm tra đ/d cần nêu trước quy tắc tương đương mong muốn và xác định từ khóa nào nên giữ khác biệt. Đồng thời, các route nội dung cần được kiểm tra với zoom, độ tương phản và trình đọc màn hình ở phạm vi có thể tái hiện.
