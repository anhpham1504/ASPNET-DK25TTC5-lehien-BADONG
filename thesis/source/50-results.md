# CHƯƠNG 4. KẾT QUẢ NGHIÊN CỨU

## 4.1. Môi trường và nguyên tắc đánh giá

### 4.1.1. Phạm vi theo mốc phiên bản

Phiên bản cơ sở trước khi sửa tiêu đề là `955956b`. Mốc `463da37` ngày 25/11/2026 giữ kết quả của đợt title và hồ sơ học thuật ban đầu. Đợt tinh chỉnh UI sau đó đi qua PR #2, gồm commit giao diện `8060028`, commit hoàn thiện quan hệ tab/panel `399393e` và merge commit sản phẩm cuối `1c04cb1`. Các kết quả CI và production cuối trong chương này chỉ dùng run gắn với merge commit đó.

Bộ 18 ảnh ngày 25/11/2026 tiếp tục là bằng chứng lịch sử của bản Release trên máy phát triển. Sau deployment cuối, em tạo thêm 13 ảnh production gắn hậu tố `1c04cb1`. Hai bộ không thay thế lẫn nhau. Các kết luận production dựa trên phản hồi HTTP, trạng thái DOM, yêu cầu tài nguyên và ảnh chụp mới; ảnh lịch sử chỉ được giữ ở những phần mô tả đúng đợt kiểm tra trước đó.

### 4.1.2. Kiểm tra dữ liệu và dịch vụ

Hai project restore thành công với SDK 10.0.100 trong kiểm tra trước phát hành. Bản app Release có 0 cảnh báo và 0 lỗi. Kết quả 14 test được xác minh trong máy phát triển và CI `45738100708` đúng SHA `1c04cb1`. CI còn cài workload `wasm-tools`, relink môi trường thực thi, biên dịch native assets và chạy `wasm-opt`. Kiểm tra JSON đọc tám tệp hợp lệ. Các test bao gồm model, file ảnh, siêu dữ liệu trạng thái, tham chiếu điểm dừng và hành vi tải HTTP.

!table|Kết quả xác minh kỹ thuật theo môi trường|0.38,0.31,0.31
| Phép kiểm | Kết quả trên máy phát triển | Kết quả CI đúng SHA |
| Restore | App và project test đạt | Bước restore đạt |
| Release build | 0 cảnh báo, 0 lỗi | 0 cảnh báo, 0 lỗi |
| Kiểm thử tự động | 14 đạt, 0 lỗi, 0 bỏ qua | 14 đạt, 0 lỗi, 0 bỏ qua |
| JSON và nguồn ảnh | 8 tệp đọc được; kiểm tra siêu dữ liệu bằng suite | Suite dữ liệu đạt |

Tài liệu kiểm thử giúp nhận diện ranh giới mà test bao phủ. Ví dụ test duy nhất của slug hữu ích vì Router tra phần tử bằng chuỗi; dữ liệu trùng có thể khiến lựa chọn bản ghi phụ thuộc thứ tự. Test đối chiếu ảnh trên máy phát triển hữu ích vì một tên không khớp chữ hoa/thường có thể chỉ phát hiện khi ra môi trường khác. Ca HTTP có chủ định với trình xử lý giả xác nhận dịch vụ trả giá trị rỗng. Mỗi ca kiểm có một đối tượng quan sát, thay cho kết luận chung rằng tất cả lỗi nội dung đã được loại bỏ.

## 4.2. Kết quả giao diện và chức năng

### 4.2.1. Trang chủ ở các kích thước

Ở desktop, vùng chính của trang chủ đặt ảnh và thông điệp nhận diện cùng các lối đi nổi bật. Người đọc có thể chuyển mục bằng điều hướng phía trên. Trong các ảnh tablet và mobile, kích thước cột và cách đưa menu thay đổi để sử dụng được chiều rộng hẹp. Hai chế độ vẫn giữ mục tiêu nhận diện trang và đi tiếp sang nội dung chính. Ảnh chủ đạo dùng tài nguyên đã xác minh của Biển Ba Động [@ba-dong-photo]. Hình minh họa bố cục trên thiết bị giả lập, không đại diện cho số liệu khả dụng của tập người dùng.

!figure|docs/evidence/screenshots/release-1c04cb1/01-home-desktop-1c04cb1.png|Trang chủ production ở vùng hiển thị 1440 × 900

!figure|docs/evidence/screenshots/release-1c04cb1/02-home-mobile-1c04cb1.png|Trang chủ production ở vùng hiển thị 390 × 844|10.5

Menu mobile được kiểm bằng thao tác phím. Trong đợt trên máy phát triển, Enter mở menu, nhìn thấy focus vào nút đóng, và Tab cùng Shift+Tab chuyển vòng trong dialog. Escape đóng menu và trở về nút ban đầu. Body khóa cuộn khi hộp thoại mở. Khi giả lập giảm chuyển động, thời lượng animation hero quan sát còn 0,01 ms. Ảnh menu ở Phụ lục E giúp đối chiếu bố cục, còn kết quả focus dựa trên kiểm tra DOM và thao tác, vì một ảnh tĩnh không chứng minh thứ tự tác vụ.

### 4.2.2. Danh sách địa điểm và tìm kiếm

Người đọc mở Khám phá để thấy các thẻ địa điểm và các điều khiển. Khi nhập hoàng hôn và hoang hon, kiểm tra ghi nhận cùng một thẻ `goc-ngam-hoang-hon`. Khi lọc Thiên nhiên, tập kết quả thu hẹp và vẫn còn mục. Khi dùng một chuỗi không khớp, vùng kết quả rỗng đưa ra cách xóa bộ lọc. Sau khi xóa, bảy thẻ xuất hiện. Phép kiểm giữ ba giai đoạn tách nhau: xác nhận lọc đúng, nhận thấy trạng thái rỗng, rồi xác nhận có thể khôi phục danh sách.

!figure|docs/evidence/screenshots/release-1c04cb1/04-explore-1c04cb1.png|Danh mục Khám phá trên production sau đợt tinh chỉnh UI

Kiểm tra hỗ trợ bỏ dấu vẫn có giới hạn. Kết quả cho hai truy vấn đã nêu khớp, còn thuật toán không ánh xạ riêng đ/d. Một test dùng từ có đ và một test dùng dấu kết hợp sẽ đánh giá hai khía cạnh khác nhau. Mục truy vết của tìm kiếm vì vậy ở trạng thái một phần. Ảnh danh sách, kết quả tìm kiếm, danh mục đã chọn và chi tiết địa điểm nằm ở Phụ lục E.

Chi tiết địa điểm giữ lối mở bản đồ và nguồn ảnh. Khi đi từ thẻ trong danh sách, slug được giữ trong URL và title. Trong kiểm tra bản công khai, đường dẫn từ trang lỗi về danh sách cho phép mở lại Biển Ba Động và tải lại trang chi tiết. Giao diện có chức năng sao chép liên kết, nhưng việc đọc lại giá trị thật từ clipboard chưa có ca xác minh trong đợt này.

### 4.2.3. Ẩm thực và thư viện

Mục Ẩm thực có bốn món ở trạng thái ban đầu. Ở trên máy phát triển, bộ lọc Hải sản giảm từ bốn xuống một món, và nút Tất cả khôi phục bốn mục. Chi tiết Cua biển có tên món trong title và nhãn xuất xứ trong phần ảnh. Nội dung không dùng ảnh tham chiếu làm bằng chứng về món được bán tại Ba Động. Hai trạng thái danh sách và chi tiết được chụp riêng để có thể xem lại ngữ cảnh.

!figure|docs/evidence/screenshots/release-1c04cb1/06-cuisine-1c04cb1.png;docs/evidence/screenshots/11-food-detail.png|Danh sách ẩm thực trên production và chi tiết món trong bộ lịch sử

Thư viện cho phép mở ảnh lớn và đọc chú thích. Ở ca kiểm tra bàn phím trên máy phát triển, Enter từ thẻ mở hộp thoại. Mũi tên phải đổi ảnh và mũi tên trái khôi phục ảnh ban đầu. Escape đóng và trả focus về thẻ. Điều này xác nhận thao tác đã kiểm và lối trở về tương tác sau khi xem ảnh. Nguồn và giấy phép vẫn xuất hiện trong vùng caption của hộp thoại.

!figure|docs/evidence/screenshots/release-1c04cb1/08-lightbox-1c04cb1.png|Hộp thoại ảnh production trên màn hình thấp với mô tả và thông tin nguồn|10.5

### 4.2.4. Cẩm nang, lịch trình và vị trí

Cẩm nang để người đọc mở câu hỏi thường gặp và xem câu trả lời trong trang. Lượt trên máy phát triển kích hoạt FAQ bằng Enter và đọc đáp án hiển thị. Với lịch trình, lựa chọn tab thứ hai đưa bố cục sang gợi ý hai ngày và thuộc tính `aria-selected` trở thành true. Tham chiếu slug từ điểm dừng được luồng test dữ liệu kiểm tra. Kết hợp hai lớp kiểm tra giúp xác nhận cả thao tác chọn và tiền đề của đường dẫn.

!figure|docs/evidence/screenshots/14-guide-faq.png;docs/evidence/screenshots/release-1c04cb1/09-itinerary-tabs-1c04cb1.png|FAQ trong bộ lịch sử và tab lịch trình production đã hoàn thiện quan hệ ARIA

Mục Vị trí đặt thông tin hành chính và liên kết Google Maps cùng phần dẫn nguồn. URL bản đồ đi ra dịch vụ ngoài và được đối chiếu ở mốc kiểm tra đường dẫn. Lịch trình không ước lượng giờ di chuyển theo lưu lượng thực tế. Người dùng có thể dùng lối mở bản đồ như điểm bắt đầu và tự kiểm tra lại đường đi khi lên kế hoạch. Ảnh trang Vị trí ở Phụ lục E.

## 4.3. Hồi quy title, điều hướng và khả năng tiếp cận

### 4.3.1. Phát hiện và sửa lỗi

Mở slug địa điểm sai ở phiên bản trước cho thấy heading lỗi đúng nhưng không có `head title`. Tái hiện trên máy phát triển cho kết quả tương tự. Kiểm tra mã cho thấy title nằm trong nhánh chỉ chạy khi có địa điểm. Sau khi sửa, title đứng ở cấp component. Ca chi tiết hợp lệ dùng tên thật, ca slug sai có thông báo cụ thể, và trong lúc tải trang cho biết đang tải nội dung.

Kiểm tra trên máy phát triển gồm bảy đường dẫn ở bốn chiều rộng 320, 390, 768 và 1440 pixel CSS, tổng cộng 28 lượt. Các URL gồm chi tiết địa điểm hợp lệ, chi tiết địa điểm sai, danh sách món, chi tiết món hợp lệ, chi tiết món sai, trang lỗi có route rõ và URL không khớp mẫu. Mỗi lượt kiểm title, một thẻ title, một heading chính và một vùng main. Đợt trên máy phát triển còn có hai lần giữ request JSON rồi trả 503 để kiểm quá trình từ đang tải sang chưa có dữ liệu. Heading lỗi được quan sát sau phản hồi mô phỏng.

!figure|docs/evidence/screenshots/release-1c04cb1/11-invalid-destination-1c04cb1.png;docs/evidence/screenshots/release-1c04cb1/12-not-found-1c04cb1.png|Hai nhánh lỗi trên production ở vùng hiển thị 390 × 844

Ảnh thân trang giúp thấy lối đi khi gặp lỗi. Giá trị title đến từ kiểm tra DOM chứ không đọc từ ảnh. Sau khi sửa, ca chuyển từ trang lỗi về danh sách và mở lại trang hợp lệ giúp phát hiện title cũ còn sót lại khi đổi route. Phép kiểm tải lại là một trường hợp khác vì trình duyệt phải nhận phản hồi mới từ nơi phục vụ site. Các ca thực tế cùng title quan sát được ghi theo môi trường trong Phụ lục C.

### 4.3.2. Khả năng tiếp cận và đáp ứng

Các lượt production cuối ghi nhận heading, `main`, ngôn ngữ vi và không tràn ngang ở 52 ca route/viewport. Phạm vi bàn phím gồm mở và đóng menu mobile, cuộn nội bộ ở landscape, đổi ảnh và đóng lightbox, mở FAQ và điều khiển tab lịch trình. Mỗi `aria-controls` của tab trỏ tới một panel tồn tại. Panel không chọn có `hidden`; panel hoạt động có `aria-labelledby`; `aria-selected` và roving `tabindex` đổi đồng bộ. ArrowLeft, ArrowRight, Home và End không làm đổi vị trí cuộn trang. Tab đi vào panel hoạt động, còn Shift+Tab quay lại tab đang chọn.

!table|Phạm vi kiểm tra giao diện và khả năng tiếp cận|0.39,0.61
| Phần đã kiểm | Phạm vi và kết quả |
| Tiêu đề, heading và landmark | Đạt ở 52 lượt production cuối. |
| Vùng hiển thị | 320 × 568, 390 × 844, 768 × 1024 và 1440 × 900. Không quan sát tràn ngang. |
| Bàn phím và focus | Menu, ảnh, FAQ, lịch trình, dialog và quay lại từ lỗi đạt trong các nhóm tương tác đã chạy. |
| Giảm chuyển động | Quan sát media query và thời lượng animation hero khi giả lập. |
| Firefox, WebKit, axe-core, tương phản, trình đọc màn hình, zoom 200% thực tế | Chưa chạy; không được suy diễn từ kiểm tra Chromium. |

Mức đánh giá là một phần so với mục tiêu khả năng tiếp cận. Máy kiểm dùng trình duyệt desktop giả lập bề rộng, do đó không đại diện cho toàn bộ phần cứng và công nghệ hỗ trợ. Chương 5 đề xuất bổ sung tổ hợp test có thể tái lập, trong đó ghi công cụ, môi trường và tình huống đo cụ thể. Không quy đổi trực tiếp số ca đạt thành mức tuân thủ WCAG.

## 4.4. Phát hành và giới hạn quan sát

### 4.4.1. Kết quả CI và Pages đúng phiên bản

Mốc phát hành đầy đủ là `1c04cb15c700c5a78c4c89d3be63008af990fd5f`. [CI 45738100708](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45738100708) và [Pages 45738100919](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45738100919) đều thành công cho SHA này. Deployment `8074236451` hoàn tất ngày 26/11/2026. Việc xác nhận SHA của workflow độc lập với kiểm tra đường dẫn công khai. Runner xác nhận quy trình dựng và native publish; trình duyệt xác nhận artifact đã triển khai kết xuất đúng các ca đã chọn.

!table|Tóm tắt kiểm tra trình duyệt theo môi trường|0.30,0.36,0.34
| Môi trường | Đối tượng kiểm | Kết quả |
| Phiên bản cơ sở | 48 lượt trình duyệt, 12 URL × 4 chiều rộng | Đợt hồi quy trước thay đổi tiêu đề. Khi tái hiện lỗi, slug địa điểm sai có heading nhưng tiêu đề thẻ trình duyệt rỗng. |
| Bản sửa trên máy phát triển | 28 lượt, 7 URL × 4 chiều rộng. Hai ca HTTP 503 mô phỏng được kiểm riêng. | Tiêu đề và các phần tử DOM đạt trong 28 lượt. Hai ca 503 hiển thị trạng thái chưa có dữ liệu. |
| Candidate UI trước sửa tab cuối | 126 tổ hợp local và 126 tổ hợp production | Bằng chứng lịch sử của candidate; không dùng để chứng minh merge SHA cuối. |
| Bản công khai cuối | 52 lượt, 13 route × 4 viewport, cùng các nhóm tương tác | 52 lượt chức năng đạt. Bốn trang chủ HTTP 200; 48 direct deep link HTTP 404 rồi khôi phục đúng route. |

Lượt kiểm tra nhanh trên bản công khai dùng Chrome Headless 158. Tại mỗi URL, phép kiểm đợi title và heading đúng sau môi trường thực thi, xác nhận thẻ title duy nhất và theo dõi yêu cầu tài nguyên. CSS, JavaScript, WebAssembly, JSON và ảnh có phản hồi thành công ở lượt hoàn tất. Không ghi nhận lỗi JavaScript, lỗi yêu cầu asset/JSON hoặc lỗi console ngoài 404 của tài liệu được dự kiến. Chromium có hủy một số yêu cầu khi điều hướng. Các lượt ghi nhận được trình bày riêng trong hồ sơ phát hành. Phạm vi đánh giá giới hạn ở các đường dẫn và tài nguyên quan sát trong từng lượt.

Một URL ở lớp ứng dụng có thể hoạt động với người đọc dù lần đáp ứng trực tiếp từ nơi lưu trữ tĩnh là 404. Kết quả này là bằng chứng cho giới hạn fallback và SEO. Nó cũng giúp phân biệt route lỗi theo nghĩa nội dung với mã phản hồi máy chủ. Trang chi tiết địa điểm hợp lệ và route slug không tồn tại đều có thể bắt đầu bằng HTTP 404 trong môi trường Pages, rồi cho hai kết quả UI khác nhau khi ứng dụng đã đọc dữ liệu.

### 4.4.2. Số liệu gói triển khai và giới hạn hiệu năng

CI của mốc phát hành báo 43 framework resources. Tổng dung lượng Brotli của thư mục framework là 2.826.661 byte. Tệp native runtime WASM chưa nén có kích thước 2.900.443 byte và bản Brotli của tệp này là 931.222 byte. Các đại lượng mô tả artifact theo phương pháp của workflow, không phải số byte thực tải của một phiên truy cập và không dùng để cộng thành tổng.

Đợt phát hành chưa đo Lighthouse, Web Vitals hoặc thời gian khởi động chuẩn hóa. Không có kết quả để so sánh tốc độ theo device hoặc mức mạng. Các kiểm tra tải asset và JSON nhằm xác nhận đường dẫn đang phục vụ được. Phép đo hiệu năng, nếu bổ sung, cần chọn trình duyệt, vùng hiển thị, mức mô phỏng mạng, trạng thái bộ nhớ đệm và số lần lặp, sau đó lưu kết quả cùng SHA.

## 4.5. Đánh giá kết quả

Khi đánh giá mỗi URL, em ghi cả mã HTTP ban đầu, tiêu đề và trang cuối cùng. Nhờ vậy có thể kiểm tra bản sửa tiêu đề mà vẫn nhìn thấy giới hạn triển khai tĩnh. Ảnh giao diện minh họa trạng thái đã quan sát trong lần chạy tương ứng.

Giới hạn chính là HTTP ban đầu của URL sâu, năm địa điểm dùng ảnh giữ chỗ và phạm vi kiểm tra khả năng tiếp cận còn hẹp. Đợt tinh chỉnh cuối đã xử lý chỉ dẫn cuộn, khoảng cách trên màn hình thấp, menu landscape, caption cảm ứng và quan hệ tab/panel. Firefox, WebKit, axe-core, zoom 200% thực tế, trình đọc màn hình và kiểm toán tương phản vẫn chưa có kết quả.
