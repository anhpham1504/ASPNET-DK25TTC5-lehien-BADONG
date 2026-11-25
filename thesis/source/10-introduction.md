# MỞ ĐẦU

## Lý do chọn đề tài

### Bối cảnh tra cứu điểm đến

Một người chuẩn bị đi Biển Ba Động cần trả lời các câu hỏi khác nhau trong một lần tra cứu. Họ muốn biết địa danh nằm ở đâu, có thể xem gì, món nào gắn với vùng ven biển và nên tổ chức các điểm dừng thế nào. Nguồn giới thiệu của ngành du lịch ghi theo địa danh Trà Vinh, trong khi bài về biển Ba Động trên cổng tỉnh Vĩnh Long cập nhật tên phường Trường Long Hòa [@national-tourism] [@vinh-long]. Một website hướng dẫn chuyến đi cần xử lý cách gọi này ngay trên giao diện. Tên trong tiêu đề ảnh và địa danh lịch sử có thể được giữ theo nguồn, còn vị trí hiện hành cần được giải thích khi người đọc mở mục vị trí.

Ảnh có sức thuyết phục cao hơn một câu mô tả, vì vậy nhầm lẫn giữa ảnh chụp tại điểm đến và ảnh minh họa có thể tạo kỳ vọng sai. Ví dụ, ảnh món cua ở Cà Mau có giá trị nhận diện món nhưng chưa mô tả một món cụ thể bán tại Ba Động. Đồ án chọn lưu nguồn và vị trí chụp cùng với bản ghi ảnh, hiển thị trạng thái chờ đối với cảnh chưa có ảnh xác minh. Cách tổ chức này làm rõ trách nhiệm của website là hỗ trợ tìm hiểu ban đầu và để người đọc lần lại căn cứ.

### Bài toán kỹ thuật

Đề tài bắt đầu từ một câu hỏi triển khai cụ thể. Câu hỏi đặt ra là cách xây dựng luồng tra cứu bằng Razor và C# trên một máy chủ chỉ cung cấp tệp tĩnh. Blazor WebAssembly đáp ứng mô hình thực thi trong trình duyệt [@wasm]. Khi triển khai, việc khởi động môi trường thực thi, phân giải liên kết tương đối và khôi phục route khi mở URL sâu đều trở thành điều kiện quan sát được. Vì vậy cần kiểm tra từ trang chủ đến chi tiết và kiểm tra lại sau khi xuất bản.

## Mục đích và phạm vi

### Mục tiêu

Mục tiêu thứ nhất là xây một cẩm nang trình bày địa điểm, món ăn và lịch trình theo các luồng đọc ngắn. Người dùng có thể bắt đầu từ danh sách, thu hẹp kết quả bằng từ khóa hoặc danh mục, rồi mở chi tiết. Mục tiêu thứ hai là tạo dữ liệu có thể kiểm tra độc lập với giao diện. Mỗi điểm dừng có liên kết cần chỉ tới một địa điểm tồn tại, từng ảnh cục bộ có đường dẫn đúng và siêu dữ liệu phù hợp với trạng thái xác minh. Mục tiêu thứ ba là công bố phiên bản có thể đối chiếu giữa mã nguồn, quy trình build, kết quả kiểm thử và hành vi trên trình duyệt.

### Đối tượng và ranh giới

Đối tượng nghiên cứu là cách tổ chức website hướng dẫn du lịch tĩnh và cách kiểm chứng các luồng thông tin của website đó. Hai nhóm sử dụng chính gồm người muốn tìm hiểu một chuyến đi ngắn và người đọc đánh giá đồ án. Nhóm đầu cần thông tin dễ tra cứu trên màn hình nhỏ. Nhóm sau cần cấu trúc kho mã, cách chạy lại và bằng chứng cho mỗi kết luận. Phạm vi nội dung tập trung vào Biển Ba Động và ngữ cảnh ven biển liên quan. Lịch trình mang tính tham khảo, bản đồ là liên kết ngoài và các điều kiện có thể thay đổi cần được kiểm tra tại thời điểm đi.

Website không thực hiện đặt dịch vụ, thanh toán hay thu thông tin đặt chỗ. Sản phẩm cũng không cung cấp dự báo thời tiết hoặc xác nhận dịch vụ địa phương theo thời gian thực. Các giới hạn này tác động trực tiếp đến kiến trúc: dữ liệu editorial có thể được đưa vào bản phát hành tĩnh và bộ kiểm thử có thể đối chiếu chúng trong kho mã. Khi cần dữ liệu thay đổi liên tục hoặc trách nhiệm giao dịch, phạm vi thiết kế sẽ khác.

## Phương pháp thực hiện và kết quả

### Phân tích nguồn và thiết kế

Đồ án phân tích nội dung cần thiết của từng đường dẫn, xem hai trang giới thiệu điểm đến và một trang hướng dẫn du lịch để đối chiếu cách tổ chức. Việc khảo sát thực hiện trên tài liệu công khai. Các nhu cầu được suy ra từ nhiệm vụ sử dụng, ví dụ từ danh sách chọn được một địa điểm và từ lịch trình đi được tới chi tiết. Các suy luận này dùng để đặt tiêu chí kiểm tra, không phải kết quả phỏng vấn hay thống kê hành vi.

Từ các tiêu chí đó, bản thiết kế xác định mô hình dữ liệu và trách nhiệm cho từng thành phần. Các tệp JSON được giữ bên cạnh mã nguồn để thay đổi nội dung có thể xem dưới dạng diff. Ứng dụng lấy tệp qua HTTP rồi ánh xạ sang kiểu C#. Các trang hiển thị khác nhau chia sẻ dịch vụ đọc. Trước khi phát hành, test ở tầng kho mã nguồn kiểm tra các quy tắc dữ liệu và test dịch vụ thực hiện với HTTP giả lập. Tiếp theo, trình duyệt kiểm tra trạng thái người dùng thấy được, bao gồm các trường hợp mà chỉ đọc JSON sẽ không phát hiện.

### Kiểm chứng theo phiên bản

Trường hợp title rỗng minh họa phương pháp này. Trên phiên bản cơ sở, slug sai dẫn đến nội dung lỗi đúng nhưng phần head rỗng vì title chỉ được khai báo ở nhánh chi tiết hợp lệ. Kết quả này được tái hiện trên trình duyệt trước khi sửa. Sau khi thay bằng thành phần title cấp trang, lượt trên máy phát triển kiểm tra riêng việc chờ dữ liệu, lỗi tải và nội dung hợp lệ. Phiên bản phát hành sau đó được kiểm tra lại trên bản công khai bằng đúng route đã tái hiện lỗi.

Sản phẩm đạt bản dựng Release và 14 kiểm thử tự động trên máy phát triển và trong CI của lần phát hành. Hồ sơ kỹ thuật có chín sơ đồ, bằng chứng giao diện và định danh phiên bản triển khai. Bảy ca trên bản công khai xác nhận tiêu đề sau khi Blazor khởi động. Báo cáo giữ riêng quan sát trên máy phát triển và trên bản công khai để người đọc có thể tái kiểm tra, đặc biệt khi mã HTTP ban đầu của URL sâu vẫn là 404.
