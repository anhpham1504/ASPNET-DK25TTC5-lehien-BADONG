# CHƯƠNG 2. NGHIÊN CỨU LÝ THUYẾT

## 2.1. Nền tảng xây dựng ứng dụng web

### 2.1.1. .NET và ASP.NET Core

.NET cung cấp công cụ biên dịch, môi trường thực thi và thư viện cho chương trình C#. Trong đồ án, SDK thực hiện restore, build, test và publish. Khai báo phiên bản trong `global.json` và dự án `net10.0` giúp người dựng xác định môi trường tương thích. Restore chuẩn bị các gói cần thiết, build tạo đầu ra cho cấu hình đã chọn, còn publish chuẩn bị tập tài nguyên để phân phối. Các bước này cần được phân biệt vì một lần build thành công ở máy cá nhân chưa xác nhận nội dung đã được đóng gói và phân phối đúng base path.

ASP.NET Core cung cấp các thành phần của hệ sinh thái web mà Blazor sử dụng. Trong mô hình Blazor WebAssembly của đồ án, C# chạy trong trình duyệt [@wasm]. Máy chủ phát hành các tệp đầu ra qua HTTP. Có thể chạy trang tại máy để thử trong quá trình phát triển; điều đó không hàm ý bản công khai chạy một tiến trình ASP.NET Core xử lý nghiệp vụ. Sự phân biệt này quan trọng khi trình bày phụ thuộc, xác định nơi xảy ra lỗi và hướng dẫn cài đặt.

### 2.1.2. Blazor WebAssembly độc lập

Ứng dụng độc lập bắt đầu từ tài liệu HTML chứa điểm gắn giao diện và cấu hình URL cơ sở. Trình duyệt tải mã khởi động, tài nguyên WebAssembly và các phần môi trường thực thi cần thiết. Sau khi host sẵn sàng, Blazor tạo các thành phần và áp dụng phần hiển thị vào DOM, tức mô hình đối tượng tài liệu của trình duyệt. Trạng thái tương tác, như danh mục đang chọn hay ảnh đang xem, nằm trong phiên ứng dụng. Đổi bộ lọc có thể được xử lý ở thiết bị đọc mà không cần gọi máy chủ để tìm bản ghi.

Mô hình đó phù hợp với tập dữ liệu nhỏ được duy trì trong kho mã nguồn. Hệ thống có thể phát hành cùng dữ liệu trong một gói triển khai và xem lại chúng theo commit. Chi phí của cách làm là phần khởi động cần tải môi trường thực thi. Mở URL sâu còn phụ thuộc cấu hình của nơi phục vụ tài liệu. Bản kết xuất ban đầu của HTML không chứa nội dung chi tiết đã kết xuất, vì thế trang cần thông báo trong lúc khởi động và cần mô tả rõ giới hạn với tác nhân đọc HTML ban đầu. Đồ án kiểm tra bằng quan sát trình duyệt và phản hồi HTTP riêng biệt.

### 2.1.3. Thành phần Razor và trạng thái

Razor dùng cú pháp khai báo HTML cùng biểu thức và sự kiện C#. Một thành phần trang xác định các trạng thái để hiển thị, chẳng hạn đang tải, có bản ghi hoặc không phân giải được slug. Thành phần thẻ nhận model và biểu diễn phần tóm tắt. Khi dữ liệu thay đổi, cơ chế kết xuất cập nhật các vùng cần thiết. Tổ chức theo trạng thái giúp người đánh giá kiểm cả phần chuyển tiếp, thay vì chỉ mở một đường dẫn hợp lệ sau khi dữ liệu đã có.

Các sự kiện của trình duyệt như nhập từ khóa và nhấn nút có thể nối với phương thức C#. Trường hợp thao tác cần năng lực của trình duyệt, như ghi clipboard hoặc điều phối focus trong dialog, đi qua JavaScript interop. Đặt các thao tác đó ở một nhóm hàm nhỏ giúp phần Razor quản lý trạng thái hiển thị và phần JavaScript quản lý hiệu ứng cần DOM. Khi kiểm tra, có thể tách một lỗi xử lý dữ liệu khỏi lỗi focus sau khi thành phần hình ảnh xuất hiện.

!table|Vai trò của các thành phần nền tảng đang sử dụng|0.30,0.35,0.35
| Thành phần | Vai trò | Vị trí sử dụng |
| .NET SDK | Restore, biên dịch, test và publish | Trên máy phát triển và GitHub Actions |
| Blazor WebAssembly | Thực thi giao diện C# trên trình duyệt | Tài nguyên môi trường thực thi và assembly đã publish |
| Razor và CSS | Cấu trúc, sự kiện và bố cục | Các trang, thẻ, điều hướng, hộp thoại |
| HTTP và JSON | Tra cứu nội dung đã đóng gói | Dịch vụ nội dung và các tệp dưới data |
| JavaScript interop | Dùng khả năng DOM và trình duyệt | Focus, scroll, đường dẫn fallback và clipboard |

## 2.2. Điều hướng và cung cấp phụ thuộc

### 2.2.1. Mẫu URL và tham số tuyến

Định tuyến ghép URL với mẫu đã khai báo bằng Razor. Mẫu có tham số như `/kham-pha/{Slug}` chỉ xác định cấu trúc URL và truyền chuỗi vào trang. Sau bước ghép tuyến, trang mới tra dữ liệu để xem slug có tồn tại hay không. Vì vậy có hai trường hợp lỗi khác nhau: Router không tìm được trang nào phù hợp, hoặc Router đã tìm được trang nhưng nguồn dữ liệu không có bản ghi. Hai trường hợp có thể dùng nội dung và lối quay về khác nhau [@routing].

Một liên kết trong phạm vi ứng dụng có thể chuyển route bằng Router khi môi trường thực thi đã chạy. Mở URL từ thanh địa chỉ hoặc tải lại gửi một yêu cầu tài liệu mới tới máy chủ. Trong lần truy cập đó, máy chủ tĩnh xử lý đường dẫn trước khi Router nhận được URL. Phân biệt hai cơ chế giải thích tại sao cùng route có nội dung và title đúng qua điều hướng nội bộ, nhưng trạng thái HTTP của lần mở trực tiếp khác với trang chủ.

Layout chia sẻ header, điều hướng và vùng nội dung chính để các trang duy trì cách đọc nhất quán. Việc cập nhật title là một phần của ngữ nghĩa trang. Blazor cung cấp `PageTitle`, `HeadContent` và `HeadOutlet` để đưa title và siêu dữ liệu vào phần head [@head]. Trang chi tiết có dữ liệu bất đồng bộ cần cung cấp title khi dữ liệu đang chờ. Title thông báo chưa có dữ liệu cũng hữu ích khi trang hoàn tất nhưng thiếu bản ghi cần hiển thị.

### 2.2.2. Cung cấp phụ thuộc và vòng đời

Kỹ thuật cung cấp phụ thuộc cho phép thành phần nhận dịch vụ thông qua khai báo thay vì tự khởi tạo mọi đối tượng. Host Blazor cung cấp các đăng ký dịch vụ ngay khi dựng ứng dụng [@di]. Đồ án đăng ký `HttpClient` có địa chỉ cơ sở theo môi trường và đăng ký `ContentService` cùng ở phạm vi dịch vụ của ứng dụng. Thành phần Razor yêu cầu `ContentService` để lấy danh sách hoặc thông tin chung.

Tách cấu hình kết nối khỏi component có hai hệ quả. Trước hết, cùng cách đọc đường dẫn tương đối áp dụng khi chạy tại máy và khi mở trang dự án. Tiếp theo, kiểm thử có thể tạo `HttpClient` dùng trình xử lý HTTP giả, đặt ra phản hồi thành công hoặc lỗi để kiểm tra phương thức dịch vụ. Ca kiểm này không phụ thuộc tốc độ Internet hoặc việc Pages đang chạy. Tính tái lập ở đây thuộc tầng dịch vụ. Kiểm chứng giao diện và lỗi cấu hình base path vẫn cần một lớp kiểm tra chạy trên trình duyệt.

## 2.3. Dữ liệu và giao tiếp

### 2.3.1. JSON làm định dạng trao đổi

JSON mô tả dữ liệu có cấu trúc theo object, array và các giá trị cơ bản [@json]. Trong website, một tệp chứa một tập bản ghi của cùng mục đích. Một tập địa điểm là mảng object, mỗi object có ID, slug và nội dung. Tệp thông tin chung là một object vì có một cấu hình cho website. JSON được lưu ở UTF-8 để giữ tên và nội dung tiếng Việt. Mô hình C# giúp mã giao diện dùng tên trường rõ ràng và kiểm tra được mối quan hệ với dữ liệu quan sát.

Một tài liệu JSON có thể đúng cú pháp nhưng chưa đáp ứng hợp đồng nội dung. Dữ liệu thiếu ảnh, có hai slug trùng nhau hoặc trỏ sai chi tiết vẫn có thể được phân tích cú pháp. Vì vậy bản thiết kế phân biệt yêu cầu đọc được với yêu cầu dùng được. Công cụ test trong repo kiểm tra cả khả năng deserialize và các bất biến của dữ liệu. Riêng các mối liên kết bằng slug và đường dẫn ảnh được xem như tham chiếu logic. Việc ghi một slug vào tệp không tự sinh khóa ngoại hoặc ràng buộc của hệ quản trị cơ sở dữ liệu.

### 2.3.2. HTTP, ánh xạ dữ liệu và lỗi

HTTP mang trạng thái phản hồi độc lập với nội dung hiển thị [@http]. Trong ứng dụng, một phản hồi JSON thành công có thể được deserialize thành model. Trạng thái như 503 làm thao tác đọc thất bại, còn nội dung sai cấu trúc hoặc cú pháp có thể sinh lỗi deserialize. Một yêu cầu tài liệu của route sâu có thể gặp 404 tại Pages và sau đó tải thành công `index.html` ở yêu cầu mới. Hai trường hợp có mã lỗi nhưng xảy ra ở hai ranh giới khác nhau. Kiểm thử ghi rõ request nào được mô phỏng lỗi.

Dịch vụ lấy dữ liệu theo địa chỉ tương đối. Khi tệp được đọc thành công, ứng dụng dùng giá trị đã ánh xạ để kết xuất. Trong nhóm lỗi được xử lý, dịch vụ trả danh sách rỗng hoặc đối tượng mặc định để thành phần có thể hiện trạng thái phù hợp. Trong thiết kế hiện tại, trang nhận danh sách rỗng không biết bên dưới là tệp hợp lệ không có mục hay lỗi đọc. Bởi vậy thông điệp tổng quát về dữ liệu phản ánh điều ứng dụng biết tại thời điểm kết xuất.

### 2.3.3. Bộ nhớ đệm và chuẩn hóa từ khóa

Bộ nhớ đệm (cache) của ứng dụng lưu đối tượng đã đọc từ JSON. Khi đối tượng có sẵn, dịch vụ dùng lại kết quả mà không phát sinh yêu cầu HTTP từ lần gọi đó. Bộ nhớ đệm HTTP của trình duyệt lưu phản hồi theo chính sách của tài nguyên. Hai cơ chế làm việc ở những lớp khác nhau. Việc khởi động lại ứng dụng tạo một phiên mới.

Chuẩn Unicode chỉ ra nhiều cách biểu diễn cùng chữ, chẳng hạn chữ và dấu kết hợp tương ứng [@unicode]. Ứng dụng chuẩn hóa chuỗi về dạng phân rã để xử lý dấu kết hợp, sau đó hợp nhất lại và đưa về chữ thường để so khớp. Việc bỏ dấu ở đây phục vụ một quy tắc tìm kiếm của sản phẩm, nằm ngoài ý nghĩa cân bằng chuỗi chuẩn hóa của Unicode. Ký tự `đ` có hành vi riêng trong triển khai hiện tại. Trường hợp này cần được ghi nhận khi mô tả phạm vi tìm kiếm tiếng Việt.

## 2.4. Giao diện và khả năng tiếp cận

### 2.4.1. Thiết kế đáp ứng và tải ảnh

Thiết kế đáp ứng cho phép bố cục điều chỉnh theo bề rộng vùng hiển thị. CSS có thể chuyển cách bố trí lưới, thay kích thước không gian bao và chọn cách hiển thị điều hướng bằng media query [@responsive]. Chiều rộng không đồng nhất với một thiết bị vật lý cụ thể. Điều kiện 390 pixel CSS có thể đại diện cho một màn hình hẹp khi test, nhưng còn phụ thuộc mật độ hiển thị, font trình duyệt và thiết lập thu phóng. Vì vậy đợt kiểm tra nêu rõ số đo và môi trường.

Ảnh là thành phần quan trọng cả về giao diện và dung lượng tải. Một số cùng nguồn có nhiều tệp đã định kích thước để trình duyệt chọn theo vùng hiển thị. Thuộc tính `srcset` và `sizes` cung cấp thông tin để trình duyệt quyết định phù hợp với môi trường. Khi ảnh có kích thước khai báo, trình duyệt cũng có căn cứ bố trí không gian. Thuộc tính `alt` cần mô tả nội dung phù hợp. Địa điểm chưa có ảnh được thể hiện bằng hình giữ chỗ có ý nghĩa, thay vì cung cấp ảnh cảnh khác nhưng khiến người đọc tưởng là cùng nơi.

### 2.4.2. Ngữ nghĩa, bàn phím và chuyển động

Khả năng tiếp cận là tập yêu cầu về cách người dùng nhận biết, thao tác và hiểu nội dung. WCAG 2.2 có các tiêu chí có thể kiểm cho bàn phím, focus và tiêu đề trang [@wcag]. Trong một SPA, thay đổi route cần làm rõ tên trang mới. Vùng `main` nêu phần nội dung nổi bật, còn heading thể hiện trang hiện tại. Khi mở hộp thoại xem ảnh, thiết kế cần theo dõi focus từ nút mở đến hộp thoại và kiểm tra nó trở về sau khi đóng. Nếu focus ra vùng bị che, người dùng bàn phím có thể tiếp tục thao tác ở vị trí không nhận thấy.

Focus nhìn thấy, thứ tự tab và việc có thể thoát hộp thoại là các kiểm tra khác nhau. Một nút có nhãn đúng vẫn cần nhìn thấy focus trong trạng thái sử dụng. Việc giảm chuyển động theo tùy chọn trình duyệt hỗ trợ người nhạy cảm với animation. Trong đồ án, kiểm tra tính năng được thực hiện ở một số luồng cụ thể. Kết quả của chúng chưa thay thế việc kiểm độ tương phản, zoom, trình đọc màn hình hoặc sự tương thích của mọi route với các công nghệ trợ năng.

## 2.5. Quản lý phiên bản, triển khai và kiểm thử

### 2.5.1. Git và GitHub Actions

Git ghi những thay đổi theo commit. Việc lưu một thay đổi về mã title và một thay đổi về hồ sơ ở hai commit giúp người xem lần lại nguyên nhân thay đổi và kết quả. GitHub cung cấp nơi lưu bản sao remote, theo dõi thay đổi và chạy công việc tự động. Trong GitHub Actions, workflow được kích hoạt bởi event, có job chạy trên runner và có các step cho từng thao tác [@actions]. Mỗi lần chạy có URL và SHA, để tránh dùng kết quả của phiên bản trước làm bằng chứng cho bản phát hành mới.

Ở dự án này, một workflow thực hiện kiểm thử và kiểm tra publish. Workflow Pages đóng gói lại output tĩnh và triển khai. Logic phụ thuộc giữa các job nằm bên trong workflow Pages. Bởi hai workflow độc lập, quy trình xác minh xem xét kết luận của cả hai. Một workflow thành công chưa khẳng định workflow còn lại đã chạy thành công cho SHA yêu cầu. Trạng thái deployment và kiểm tra truy cập trình duyệt sau deploy tạo thêm bằng chứng về môi trường công bố.

### 2.5.2. GitHub Pages và khả năng được lập chỉ mục

GitHub Pages phục vụ website tĩnh và project site thường được công bố dưới đường dẫn kho mã nguồn [@pages]. Một base path chính xác giúp các tài nguyên tương đối và điều hướng cùng trỏ vào thư mục dự án. Trong website SPA hiện tại, route chi tiết không tương ứng với một tài liệu HTML riêng ở máy chủ. Cơ chế fallback có thể đưa người dùng trở lại ứng dụng để Router xử lý, nhưng tài liệu ban đầu vẫn có trạng thái HTTP của đường dẫn đã yêu cầu.

Tiêu đề HTML, trạng thái HTTP và nội dung được kết xuất là ba tín hiệu liên quan đến công cụ tìm kiếm [@seo]. Bản sửa `PageTitle` làm title có ý nghĩa sau khi Razor chạy. Nó không sửa khâu đáp ứng tài liệu từ máy chủ. Cần đo hai kết quả độc lập: phản hồi lúc mở đường dẫn và title hiện trên DOM. Giải pháp kết xuất trước có thể tạo tài liệu phù hợp hơn cho một số route, nhưng thay đổi cấu trúc xuất bản sẽ đi cùng kiểm tra lại toàn bộ link, dữ liệu và workflow. Đó là hướng phát triển chứ chưa phải phần đã thực hiện.

### 2.5.3. Kiểm thử tự động và kiểm tra sau phát hành

Môi trường chạy test cung cấp phương thức thực thi và thống kê. Microsoft Testing Platform có thể chạy các dự án test trong nhiều ngữ cảnh, bao gồm dòng lệnh và CI [@mtp]. Trong đồ án, dự án xUnit xác minh model, tham chiếu, asset và xử lý HTTP ở điều kiện kiểm soát. Các ca test xác nhận tiền đề của ứng dụng, chẳng hạn dữ liệu có thể đọc và các đường dẫn ảnh phân biệt đúng chữ hoa thường. Chúng không mở UI, do đó cần bổ sung lượt kiểm tra trình duyệt cho title, focus và hướng điều hướng khi có lỗi.

Kiểm tra hồi quy cần giữ điều kiện đủ rõ để tái hiện. Với bản sửa title, kiểm tra trên máy phát triển thay đổi bề rộng và kiểm soát lỗi JSON. Kiểm tra bản công khai tập trung vào bảy URL sau khi công bố và kèm theo dấu vết commit. Trình duyệt kiểm tra title sau khi Blazor khởi động, thay vì đọc HTML phản hồi như thể đó là kết quả cuối. Bằng chứng này cho thấy lỗi đã được khắc phục trong phạm vi ca kiểm. Các phép đo thời gian tải hay tuyên bố mức tuân thủ WCAG đòi hỏi phương pháp kiểm thử riêng.
