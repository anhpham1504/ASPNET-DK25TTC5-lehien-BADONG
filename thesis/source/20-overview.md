# CHƯƠNG 1. TỔNG QUAN

## 1.1. Bối cảnh du lịch Biển Ba Động

### 1.1.1. Điểm đến và cách gọi địa danh

Biển Ba Động là một địa danh ven biển gắn với vùng Trường Long Hòa và Duyên Hải. Cổng thông tin điện tử tỉnh Vĩnh Long mô tả địa điểm giữa hai cửa biển Cung Hầu và Định An, thuộc khu vực từng được giới thiệu dưới tên Trà Vinh [@vinh-long]. Danh mục của Cục Du lịch Quốc gia Việt Nam sử dụng địa chỉ theo địa bàn trước đây trong bài giới thiệu [@national-tourism]. Hai nguồn hữu ích ở các thời điểm và nhiệm vụ khác nhau. Một nguồn giúp xác định cách gọi trong tài liệu du lịch đã phổ biến. Nguồn còn lại giúp ghi vị trí theo tên hành chính được cập nhật.

Trong sản phẩm, phần vị trí hiển thị phường Trường Long Hòa, tỉnh Vĩnh Long cùng ngữ cảnh Trà Vinh trước sáp nhập. Tên địa danh cũ vẫn có thể xuất hiện trong tiêu đề hồ sơ ảnh hoặc truy vấn bản đồ. Tách hai ngữ cảnh này giúp đối chiếu lại nguồn gốc. Việc đổi toàn bộ chuỗi địa danh trong tiêu đề ảnh theo địa chỉ mới sẽ làm khó quá trình tìm lại nguồn cấp phép. Ngược lại, chỉ để địa chỉ cũ trong mục vị trí sẽ khiến người đọc khó nhận ra mối liên hệ với cách gọi hiện hành.

Thông tin về cảnh quan và các điểm dừng được dùng với mức chi tiết vừa đủ cho việc tra cứu. Trang giới thiệu định vị câu chuyện chung, còn mục Khám phá đưa người đọc tới từng bản ghi địa điểm. Điện gió Duyên Hải được trình bày như một điểm liên quan đến vùng ven biển, có nguồn ảnh riêng. Các cảnh cần xác minh bổ sung vẫn có thể mang tên nội dung trong danh sách. Hình giữ chỗ ở những bản ghi này giúp người đọc nhận biết rõ phần tư liệu hình ảnh còn thiếu.

### 1.1.2. Thông tin có thể thay đổi

Nội dung như tên điểm đến, lưu ý giữ gìn môi trường và đường dẫn bản đồ phù hợp với một website editorial. Dữ liệu về giờ mở cửa, giá, điều kiện biển hoặc khả năng sử dụng dịch vụ thay đổi theo thời điểm và đòi hỏi cơ chế xác minh riêng. Đồ án giới hạn phần cẩm nang ở gợi ý chuẩn bị, duy trì câu nhắc đối chiếu trước khi đi và chuyển người đọc ra nguồn gốc khi cần thêm thông tin. Dữ liệu site có tuyên bố phạm vi học thuật. Bố cục không đặt nút mua hoặc gửi thông tin ở vị trí có thể làm người đọc hiểu đây là cổng giao dịch.

Một nguyên tắc tương tự áp dụng với ảnh. Hình chụp biển có thể dùng để giới thiệu cảnh tại điểm đến nếu hồ sơ đủ căn cứ. Hình ghi nhận tại cảng Định An hoặc ảnh món ăn ở địa phương khác cần ghi rõ phạm vi minh họa. Siêu dữ liệu dùng trong trang chi tiết cung cấp tác giả, giấy phép, địa điểm chụp và liên kết. Kết quả trình bày là một bản hướng dẫn có dấu vết kiểm chứng, phù hợp với việc đọc lại trong đồ án.

## 1.2. Nhu cầu người sử dụng

### 1.2.1. Hành trình tìm hiểu trên trình duyệt

Người đọc mới thường cần nhận diện điểm đến trước khi sàng lọc nội dung. Trang chủ hỗ trợ việc này bằng tên địa danh, ảnh chủ đạo và các lối đi tới Khám phá hoặc Cẩm nang. Một người đã có chủ định, chẳng hạn muốn tìm góc ngắm hoàng hôn, có thể vào ngay Khám phá. Từ khóa đưa người đó tới tập thẻ nhỏ hơn, sau đó thẻ mở trang chi tiết bằng slug ổn định. Người lập lịch trình có thể bắt đầu từ một trình tự theo thời gian và đi ngược lại tới địa điểm liên quan qua điểm dừng đã liên kết.

Các luồng trên tạo ra yêu cầu về tính liên tục. Người dùng phải biết danh mục hoặc tab nào đang chọn, thấy được thông báo khi bộ lọc cho kết quả rỗng và tìm được cách quay lại từ một URL sai. Người dùng di động cần truy cập các nhóm trang qua menu mà không phải cuộn xuống chân trang. Những yêu cầu này được kiểm bằng việc quan sát trạng thái giao diện chứ không chỉ bằng sự tồn tại của đường dẫn trong mã nguồn.

Đối tượng xem đồ án có nhiệm vụ khác. Họ cần biết khi nào ảnh được chụp, cách kết quả build được tạo ra, bằng chứng nào thuộc bản công khai và đoạn mã nào hiện thực chức năng. Vì vậy website có hồ sơ dữ liệu và hồ sơ thiết kế kèm theo. Có thể lần từ một yêu cầu trong ma trận tới route, thành phần Razor, test hoặc ảnh. Khi một yêu cầu chưa có kiểm tra đầy đủ, ma trận để trạng thái riêng để tránh suy diễn từ nội dung đã có.

### 1.2.2. Yêu cầu biên tập và đọc trên màn hình nhỏ

Tính dễ đọc ở màn hình nhỏ đòi hỏi xử lý cả bố cục và từng thao tác. Danh sách phải nhìn được ở chiều rộng hẹp. Khi mở menu hoặc xem ảnh, focus cần nằm trong vùng tương tác và có lối đóng rõ. Tiêu đề trang và heading chính cho biết người đọc đang ở danh sách, chi tiết hay trang lỗi. Cụm tác vụ này liên quan đến khả năng tiếp cận. Tiêu chí WCAG được dùng để chỉ ra phép kiểm cụ thể, ví dụ thao tác bàn phím và nhận biết focus [@wcag]. Đồ án chưa thực hiện đánh giá theo toàn bộ tiêu chí của tiêu chuẩn.

Nội dung biên tập cần ngắn và nhất quán giữa thẻ và trang chi tiết. Một thẻ dùng tên, ảnh đại diện và mô tả ngắn để hỗ trợ quyết định mở. Chi tiết cung cấp thêm nội dung, nguồn và hành động có liên quan, chẳng hạn mở bản đồ hoặc sao chép đường dẫn. Dữ liệu tên và slug tách nhau để có thể sửa cách viết tên mà không làm hỏng đường dẫn đang tồn tại.

## 1.3. Khảo sát cách tổ chức thông tin

### 1.3.1. Phạm vi khảo sát

Khảo sát xem nội dung công khai của ba trang. Hai trang trực tiếp đề cập Biển Ba Động [@vinh-long] [@national-tourism]. Trang Phu Quoc của Vietnam Tourism cung cấp một ví dụ về cấu trúc giới thiệu điểm đến có phần hoạt động và việc chuẩn bị chuyến đi [@phu-quoc]. Các trang được chọn để đối chiếu cách đưa thông tin lên màn hình, không nhằm so sánh số lượt truy cập hay xếp hạng chất lượng. Dữ liệu của Phú Quốc không chuyển sang bộ dữ liệu Ba Động.

!table|Đối chiếu cấu trúc ba nguồn thông tin công khai|0.27,0.37,0.36
| Nguồn | Tổ chức quan sát được | Áp dụng vào đề tài |
| Vĩnh Long [@vinh-long] | Bài viết về biển Ba Động trong tập địa danh. Có ngữ cảnh địa lý và tên hành chính hiện hành. | Hiển thị vị trí hiện hành ở mục Vị trí và dẫn nguồn. |
| Cục Du lịch [@national-tourism] | Trang điểm đến riêng, chia thông tin vị trí và đặc điểm. | Tách nhận diện và đặc điểm khỏi các gợi ý nên kiểm tra trước chuyến đi. |
| Vietnam Tourism [@phu-quoc] | Trang Phu Quoc có nhóm điểm nên xem, cách đến và thông tin du lịch. | Tách các tác vụ xem điểm, lên lịch và đọc cẩm nang theo route. |

### 1.3.2. Quyết định cấu trúc thông tin

Một bài dài phù hợp với người muốn đọc bối cảnh liên tục. Khi mục tiêu là chọn một điểm dừng, danh sách có lọc sẽ rút ngắn quãng đọc và hỗ trợ xem thêm bằng một hành động. Đồ án dùng cả hai dạng. Phần giới thiệu kể câu chuyện chung, còn dữ liệu địa điểm được chia thành các thẻ. Cẩm nang và lịch trình tiếp tục nhiệm vụ sau khi người đọc đã hiểu vùng. Nguồn và nhãn ảnh xuất hiện gần nội dung tương ứng để người đọc không phải tìm một trang chú thích riêng.

Các trang tham khảo có độ bao quát khác nhau. Trang Phu Quoc có các khối thời tiết và di chuyển, nhưng việc đưa một dự báo vào Ba Động đòi hỏi nguồn và thời điểm cập nhật mà đồ án không vận hành. Thay vào đó, cẩm nang nêu điều cần kiểm tra và liên kết một số nguồn công khai. Một ảnh bãi biển cũng không được dùng để minh họa mặt nước luôn ở cùng trạng thái. Ngữ cảnh về vị trí chụp và lưu ý của trang giúp tránh diễn giải rộng hơn căn cứ hiện có.

## 1.4. Yêu cầu và giới hạn sản phẩm

### 1.4.1. Nhóm chức năng

Trang chủ và giới thiệu cung cấp bối cảnh. Khám phá gồm danh sách, lọc, tìm kiếm, chi tiết và quay lại khi đường dẫn không phân giải. Ẩm thực có bộ lọc và trang chi tiết món, trong đó chú thích ảnh nêu nơi chụp. Thư viện cho xem ảnh và mở hộp thoại. Cẩm nang có câu hỏi thường gặp, lịch trình cho chọn gợi ý và vị trí cung cấp liên kết bản đồ. Những nhóm này tương ứng với các trạng thái và thao tác cụ thể trong hồ sơ truy vết. Với chức năng sao chép liên kết, mã hiện thực tồn tại, còn kết quả dùng clipboard trong đợt đánh giá chưa được thu thập.

### 1.4.2. Nhóm yêu cầu chất lượng

Yêu cầu dữ liệu gồm ID và slug duy nhất theo tập, ảnh trên máy phát triển tồn tại, tham chiếu lịch trình hợp lệ và đầy đủ thành phần nguồn cho ảnh xác minh. Yêu cầu giao diện gồm đáp ứng bề rộng phổ biến, ngữ nghĩa heading và có lối thao tác bằng bàn phím. Yêu cầu triển khai gồm kết quả dựng có thể tái lập, URL chính xác theo thư mục dự án và khả năng đối chiếu phiên bản phát hành. Khi URL sâu gặp 404 từ máy chủ tĩnh, tiêu chí kiểm tra ghi cả trạng thái HTTP và kết quả người dùng nhìn thấy sau khi môi trường thực thi hoạt động.
