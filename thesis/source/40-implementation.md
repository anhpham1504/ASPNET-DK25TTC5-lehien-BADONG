# CHƯƠNG 3. HIỆN THỰC HÓA NGHIÊN CỨU

## 3.1. Phân tích tác vụ và kiến trúc

### 3.1.1. Trường hợp sử dụng và ranh giới

Tác nhân trong hệ thống là người truy cập website. Trường hợp sử dụng bắt đầu bằng việc đọc giới thiệu hoặc đi thẳng tới một nhóm nội dung. Trong nhóm địa điểm, thao tác đọc danh sách dẫn tới tìm kiếm, lọc và mở chi tiết. Trong nhóm ẩm thực, người dùng có thể chọn danh mục, sau đó mở một món. Thư viện cung cấp xem ảnh lớn và cẩm nang cung cấp mục FAQ. Lịch trình và vị trí phục vụ giai đoạn chuẩn bị chuyến đi. Chức năng được gắn với thao tác hiện có của ứng dụng, gồm mở Google Maps hoặc sao chép liên kết ở chi tiết phù hợp.

!figure|docs/diagrams/rendered/use-case.png|Trường hợp sử dụng của người truy cập

Sơ đồ chức năng gom thao tác theo mục tiêu đọc. Mỗi nhóm có điểm vào khác nhau, nhưng dùng chung ngữ cảnh website và thành phần điều hướng. Người sửa nội dung hoạt động trong kho mã, chỉnh dữ liệu hoặc thẩm định ảnh trước khi phát hành. Người đó không phải là tác nhân quản trị bên trong sản phẩm đang chạy. Sự phân định này giúp loại khỏi kiến trúc các chức năng không tồn tại, như đăng nhập và duyệt đơn đặt dịch vụ.

### 3.1.2. Lớp dựng, triển khai và lưu lượng môi trường thực thi

Mã nguồn C#, Razor, dữ liệu JSON và ảnh là đầu vào của bước dựng. GitHub Actions chuẩn bị SDK và tạo gói triển khai. Gói cuối cùng chứa tài liệu HTML ban đầu, CSS, ảnh, mã JavaScript, môi trường thực thi và assembly có thể chạy trên trình duyệt. GitHub Pages phục vụ các tài nguyên đó dưới thư mục của dự án. Tải trang là quan hệ giữa trình duyệt và nơi phục vụ tệp. Khi hoạt động, Razor gọi dịch vụ đọc JSON thông qua HTTP để lấy nội dung.

!figure|docs/diagrams/rendered/system-architecture.png|Kiến trúc dựng bản phát hành và thực thi trong trình duyệt

Môi trường thực thi chạy tại thiết bị người dùng. Việc lọc danh sách, cập nhật tab và chuyển hình không gửi yêu cầu xử lý đến một API nghiệp vụ. Khối `HttpClient` đọc tệp tĩnh và trả dữ liệu để ứng dụng quản lý. Những yêu cầu đến bên ngoài như việc mở bản đồ đi theo liên kết rõ ràng. Cách bố trí này phù hợp với lượng dữ liệu và tốc độ thay đổi trong phạm vi đề tài. Nó cũng đưa lỗi startup, sai base path hoặc thiếu file ảnh thành các lỗi có thể tái hiện từ gói triển khai, thay vì lỗi ở lớp xử lý server.

### 3.1.3. Tổ chức kho mã

Thư mục `src/BaDong.CoastalEscape` chứa project Blazor và các phần tử xuất bản từ `wwwroot`. Các trang trong `Pages` theo nhóm chức năng. `Components` chứa thẻ và thành phần dùng chung. `Layout` chứa cấu trúc bao, còn `Services` và `Models` tạo hợp đồng đọc dữ liệu. Tests tham chiếu ứng dụng và sao dữ liệu cùng tài nguyên cần kiểm vào output của dự án test. Tệp `global.json` cung cấp cấu hình chọn SDK và runner test. Hai workflow trong `.github/workflows` phục vụ CI và GitHub Pages.

Các hướng dẫn, dữ liệu kiểm thử, kết quả và sơ đồ được gắn với thư mục phù hợp để người chạy lại có thể phân biệt ba mục tiêu. Muốn chạy sản phẩm trên máy phát triển, bắt đầu từ `setup`. Muốn xem phạm vi release, theo mốc và commit trong `docs`. Muốn sửa báo cáo học thuật, dùng nguồn trong `thesis`. Đơn vị kiểm tra nội dung bằng phần mềm là commit, còn đơn vị tham chiếu ảnh là file có hồ sơ xuất xứ. Nhờ đó sửa một ảnh không làm mất dữ kiện về release trước.

## 3.2. Thành phần giao diện và điều hướng

### 3.2.1. Thành phần trang và phần tử dùng chung

`App` cấu hình Router, `RouteView` và điểm focus khi chuyển trang. `MainLayout` bao nội dung bằng điều hướng desktop, menu mobile và vùng `main`. `DestinationCard` và `FoodCard` nhận model làm tham số, dùng trong các trang có cùng kiểu dữ liệu. `Breadcrumbs` trình bày quan hệ danh sách và chi tiết. `SourceNote` hiển thị liên kết nguồn tại các vùng cần minh bạch. Các component được chia theo dữ liệu hoặc hành vi sử dụng lại, tránh sao chép nguyên cả trang.

!figure|docs/diagrams/rendered/component.png|Thành phần giao diện và phụ thuộc chính

`Gallery` quản lý danh sách ảnh sau lọc và mở `PhotoLightbox` với tập ảnh hiện tại. Component này hiển thị ảnh, caption, siêu dữ liệu và các nút chuyển ảnh. `FaqAccordion` nhận danh sách câu hỏi để dùng ở trang chủ và cẩm nang. Sự phân tách giúp kiểm thử tương tác trên một ngữ cảnh cụ thể và vẫn xác định điểm sở hữu trạng thái. Chẳng hạn danh mục thư viện thuộc trang, trong khi ảnh đang chọn và hành vi đóng thuộc hộp thoại.

### 3.2.2. Điều hướng, slug và trang không tìm thấy

Một slug được xem là định danh đường dẫn đọc được, chẳng hạn `bien-ba-dong`. Thẻ và điểm dừng lịch trình dùng slug để tạo URL chi tiết. Trong trang chi tiết, ứng dụng so sánh slug với model. Nếu có bản ghi, nó kết xuất nội dung tương ứng. Nếu tập có dữ liệu nhưng slug vắng mặt, trang cung cấp thông báo và liên kết trở về danh sách. Router dùng `NotFound` khi mẫu URL không khớp.

!figure|docs/diagrams/rendered/navigation.png|Điều hướng và xử lý URL không hợp lệ

Các liên kết liên quan được định tuyến tương đối tới base ứng dụng. Tên path trong sơ đồ là path bên trong ứng dụng, chưa gồm thư mục project site. Liên kết bản đồ thuộc dịch vụ bên ngoài và được xử lý bằng URL tuyệt đối. Điều này cũng giải thích vì sao kiểm thử `MapUrl` chỉ xác nhận định dạng hoặc đích liên kết, còn dịch vụ bên ngoài không nằm trong phạm vi bảo đảm của website.

### 3.2.3. Khởi tạo title theo trạng thái

Điểm lắp `HeadOutlet` được khai báo một lần. Title của hai trang chi tiết đi qua `PageTitle`. Trong `DestinationDetail`, điều kiện đang tải được xét trước. Khi đã tải, tên địa điểm hợp lệ được ưu tiên. Nếu không có đối tượng, title phân biệt danh sách rỗng với slug không khớp trên danh sách có dữ liệu. Trang món ăn giữ title tên món và title danh sách, đồng thời thêm chuỗi cụ thể cho trường hợp không tìm thấy món.

> <PageTitle>@(TitleLabel) · BA ĐỘNG — Coastal Escape</PageTitle>

Dòng trích trên đặt trước các nhánh giao diện trong `DestinationDetail.razor`. Cấu trúc này đủ để mỗi nhánh có title và không cần JavaScript ghi `document.title`. Thẻ mô tả vẫn ở nhánh có nội dung. Tài liệu `index.html` ban đầu là màn hình khởi động, chưa có title riêng. Phần kiểm chứng dùng mốc đã kết xuất của Razor để đánh giá thay đổi.

## 3.3. Mô hình và quy tắc dữ liệu

### 3.3.1. Các lớp nội dung

`Destination` và `Food` cùng có ID, slug, nhóm nội dung và trường ảnh. Chúng khác về nhiệm vụ trình bày. Địa điểm cần vị trí, mô tả, chủ đề và đường dẫn bản đồ. Món ăn cần mô tả món, gợi ý sử dụng và thông tin liên quan đến ảnh. `GalleryPhoto` tập trung vào nguồn và kích thước tệp, đáp ứng cả ảnh thu nhỏ và ảnh mở trong hộp thoại. `FaqItem` gồm câu hỏi, câu trả lời và nguồn.

!figure|docs/diagrams/rendered/class-model.png|Các lớp nội dung và dịch vụ đọc

`Itinerary` chứa danh sách `ItineraryStop`. Điểm dừng có thể mang slug địa điểm; khi slug rỗng, giao diện có thể hiển thị gợi ý như nghỉ trưa mà không tạo link. `SiteInfo` chứa một số thông tin chung và tập liên kết nguồn. Mối quan hệ về tham chiếu chỉ có hiệu lực khi kiểm thử hoặc mã môi trường thực thi tìm thấy dữ liệu tương ứng. Model không thêm một chính sách lưu trữ hoặc truy vấn riêng.

### 3.3.2. Tập JSON và dữ liệu kiểm tra

Sáu tệp được dịch vụ nội dung đọc khi phục vụ website. Hai tệp còn lại theo dõi tài nguyên ảnh và yêu cầu ảnh thiếu. Khi xem một đối tượng model, dữ liệu bắt buộc cho hiển thị được kiểm khác với trường tùy chọn. Slug địa điểm và món phải duy nhất trong từng tập, nhưng không cần duy nhất xuyên hai nhóm vì tiền tố route khác nhau. Ảnh và biến thể phải có đường dẫn đúng chữ hoa/thường trong gói triển khai. Kiểm tra này hữu ích khi quy trình phát hành chạy trên Ubuntu và dùng hệ thống tệp với quy tắc tên khác máy phát triển.

!figure|docs/diagrams/rendered/json-data-model.png|Quan hệ logic giữa các tệp nội dung và ảnh

!table|Kiểm kê dữ liệu trong phiên bản cơ sở phát hành|0.32,0.18,0.50
| Nhóm | Số mục | Vai trò và phép kiểm |
| Địa điểm | 7 | ID, slug, category, nguồn và đường dẫn ảnh. Năm mục đang chờ ảnh xác minh. |
| Món ăn | 4 | Slug, phân nhóm, biến thể và nhãn vị trí chụp. |
| Thư viện | 7 | Caption, mô tả thay thế, tác giả, giấy phép và ảnh. |
| Lịch trình | 2 | Danh sách điểm dừng. Slug có giá trị phải trỏ tới địa điểm hợp lệ. |
| FAQ và thông tin chung | 5 và 1 | Câu hỏi, câu trả lời, thuộc tính website và nguồn. |
| Hồ sơ ảnh và yêu cầu ảnh | 8 và 5 | Danh sách tài nguyên, biến thể, trạng thái xác minh và vị trí cần ảnh. |

### 3.3.3. Hồ sơ ảnh và ảnh đáp ứng

Mỗi ảnh đã xác minh có một đường dẫn cục bộ và thông tin lấy từ hồ sơ nguồn. Tập trường xác minh gồm chủ thể, vị trí chụp, tác giả, giấy phép và URL. Địa điểm Biển Ba Động sử dụng ảnh có hồ sơ Wikimedia Commons của Baoothersks và giấy phép CC BY 4.0 [@ba-dong-photo]. Dữ liệu lưu tên nguồn cùng vị trí như được đối chiếu. Khi ảnh chỉ được xác minh về chủ thể, mô tả vị trí không tự động coi ảnh là ảnh của Ba Động. Năm địa điểm đang chờ ảnh vẫn dùng dạng hình giữ chỗ nội bộ.

Các biến thể có kích thước khác nhau giúp trình duyệt chọn tệp phù hợp. Khi có hai bản ảnh địa điểm, trang mô tả chúng bằng `srcset`; ảnh PENDING dùng tài nguyên ảnh giữ chỗ tương ứng. Mục thư viện giữ thumbnail để xem lướt và dùng tệp ảnh chi tiết khi mở. Việc có siêu dữ liệu đầy đủ và file tồn tại mới xác nhận cấu trúc và quy trình xuất bản. Chất lượng ảnh tại địa điểm và độ mới của tư liệu là vấn đề biên tập cần nguồn xác minh tiếp theo.

## 3.4. Dịch vụ và xử lý nội dung

### 3.4.1. Tải qua HTTP và lưu kết quả

`ContentService` nhận `HttpClient` từ host. Mỗi phương thức công khai chỉ định một đường dẫn cố định. Khi yêu cầu tiếp tục từ trang khác, phương thức có thể trả dữ liệu bộ nhớ đệm bằng đường dẫn và kiểu phù hợp. Nếu chưa có, dịch vụ gọi `GetFromJsonAsync` với cấu hình web của `System.Text.Json`. Kết quả thành công được đưa vào bộ nhớ đệm. Trường hợp JSON chứa `null` dùng giá trị rỗng hoặc mặc định và bộ nhớ đệm giá trị đó.

!figure|docs/diagrams/rendered/content-loading-sequence.png|Trình tự tải nội dung khi có và chưa có bộ nhớ đệm

Bộ nhớ đệm dùng `ConcurrentDictionary<string, object>` để đọc và ghi an toàn trên cấu trúc từ điển. Hai yêu cầu cùng lúc vẫn có thể tải cùng một tệp khi cả hai chưa tìm thấy dữ liệu. Kết quả được dùng lại giữa các trang trong vòng đời của dịch vụ. Khi chỉnh sửa JSON, cần phát hành lại tệp để người đọc nhận dữ liệu mới.

### 3.4.2. Trạng thái lỗi có thể xử lý

Dịch vụ xử lý bốn nhóm ngoại lệ gồm lỗi HTTP, lỗi đọc JSON, kiểu không được hỗ trợ và tác vụ bị hủy. Khi có ngoại lệ, dịch vụ trả danh sách rỗng hoặc một `SiteInfo` mặc định và không ghi vào bộ nhớ đệm. Các trang dùng kết quả đó để quyết định có đủ dữ liệu cho nhánh chi tiết hay không. Title báo chưa có dữ liệu được sử dụng ở trạng thái rỗng, gồm lỗi tải và tập rỗng hợp lệ. Hướng xử lý này tránh thông báo sự cố kết nối khi nguyên nhân chưa phân biệt được.

Một quy tắc khác là không đẩy lỗi từ môi trường thử vào kết luận bản công khai. Ca 503 được định nghĩa bằng chặn request JSON trên máy phát triển có chủ đích. Người kiểm biết thời điểm request bị giữ, biết thời điểm HTTP 503 trả về và có thể đọc DOM ở hai trạng thái. Số liệu bản công khai ghi riêng theo môi trường. Cùng một mã 404 có thể xuất hiện ở log của bản công khai nhưng đó là 404 tài liệu ban đầu khi mở route sâu, khác với JSON 503 được dùng để kiểm nội dung rỗng.

### 3.4.3. Tìm kiếm có dấu và bộ lọc

Trang Khám phá nhận giá trị khi người dùng nhập. Đối với mỗi đối tượng, thuật toán kiểm tra danh mục trước. Danh mục mặc định cho đi qua tất cả điểm. Nếu cần so khớp từ khóa, chuỗi tìm kiếm và các trường tên, mô tả ngắn, đoạn đầu mô tả và tags được chuẩn hóa. Kết quả so chuỗi con được áp dụng theo thứ tự dữ liệu ban đầu. Khi không có phần tử phù hợp, ứng dụng hiện thông báo và nút xóa bộ lọc.

!figure|thesis/source/diagrams/search-filter-activity.png|Hoạt động lọc và so khớp từ khóa địa điểm

Tách lọc nhóm và lọc từ khóa giúp người dùng giải thích được kết quả. Chọn lại Tất cả bỏ điều kiện danh mục. Nút xóa bộ lọc còn đặt từ khóa về rỗng. Dữ liệu hiện có ít phần tử nên mỗi thao tác lọc có thể đi qua danh sách đang ở bộ nhớ. Đồ án không dùng chỉ mục toàn văn, thứ hạng, sửa chính tả hay phân đoạn từ tiếng Việt. Việc bỏ dấu kết hợp giúp các ca như hoàng hôn và hoang hon. Cặp đ và d là trường hợp riêng vì ký tự đ không bị loại bởi thao tác xóa dấu kết hợp.

## 3.5. Hộp thoại, menu và triển khai

### 3.5.1. Focus và tương tác

Menu di động và lightbox có cơ chế lưu vị trí focus ban đầu, điều phối focus khi mở, giới hạn vòng tab khi hộp thoại hoạt động và trả focus khi đóng. Khóa cuộn được áp dụng cho body trong thời gian hộp thoại mở. Khi kích hoạt Escape, ứng dụng điều phối việc đóng từ trạng thái UI. Lightbox còn phản hồi phím mũi tên để đổi ảnh. Mã Razor quyết định ảnh đang xem và việc mở/đóng; mã JavaScript áp dụng thao tác cần trạng thái DOM.

Tương tác ở các nhóm nội dung khác dùng phần tử ngữ nghĩa và thuộc tính ARIA tương ứng. FAQ mở rộng nội dung khi người dùng kích hoạt nút. Mỗi tab lịch trình có `aria-controls` trỏ tới một panel tồn tại; panel không chọn mang thuộc tính `hidden`, còn panel hoạt động có `aria-labelledby` trỏ lại tab. Roving `tabindex` giữ một tab trong thứ tự Tab. ArrowLeft, ArrowRight, Home và End đổi lựa chọn mà không làm cuộn trang; Tab và Shift+Tab vẫn hoạt động bình thường. Trang còn cung cấp chỉ dẫn focus cho điều hướng và CSS điều chỉnh animation khi người dùng yêu cầu giảm chuyển động.

### 3.5.2. Build, publish và đường dẫn triển khai

Workflow CI chạy restore app và project test, dựng bản Release, test và publish để kiểm tra cấu hình relinking của WebAssembly. Workflow Pages dùng SDK .NET 10 và workload wasm-tools, dựng output, áp dụng base path và các token triển khai. Job deploy nhận gói triển khai từ job build của cùng workflow. Hai workflow có thể chạy song song khi push `main`, nên kết luận của từng lần chạy được lưu riêng khi phát hành.

!figure|docs/diagrams/rendered/deployment.png|Hai workflow từ commit đến kiểm thử và triển khai

Trong bản publish, thẻ base trỏ vào thư mục của repo. `robots.txt` và sitemap dùng URL public đã thay token. `404.html` đặt mục tiêu điều hướng trong session storage và chuyển về base. Khi ứng dụng khởi động, đoạn JavaScript xử lý mục tiêu và cập nhật lịch sử để Router nhận path mong muốn. Cơ chế này duy trì trải nghiệm khi trình duyệt thực thi được các bước trên. Nó không biến lần phản hồi đầu thành HTTP 200. Điều kiện thành công thực tế gồm hai kết quả đồng thời: trạng thái ban đầu được ghi đúng và nội dung sau khi khởi động ứng với route ban đầu.
