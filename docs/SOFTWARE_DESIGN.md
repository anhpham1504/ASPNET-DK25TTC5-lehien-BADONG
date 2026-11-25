# Hồ sơ thiết kế phần mềm

BA ĐỘNG — Coastal Escape là cẩm nang du lịch học thuật cho người muốn tìm hiểu biển Ba Động và lên lịch trình tham khảo. Phạm vi, ràng buộc và tiêu chí trải nghiệm được lấy từ [PRODUCT.md](../PRODUCT.md) và [SRS.md](SRS.md). Danh mục chức năng được đối chiếu với các trang Razor và bằng chứng tại [ma trận truy vết](TRACEABILITY_MATRIX.md).

## 1. Trường hợp sử dụng và điều hướng

Người truy cập mở trang chủ hoặc giới thiệu, xem và lọc địa điểm, tìm kiếm, mở chi tiết và sao chép liên kết, duyệt món ăn và thư viện, chọn lịch trình, đọc cẩm nang/FAQ và mở bản đồ. Phần mềm là ứng dụng tĩnh chạy trong trình duyệt. Nội dung được bảo trì bằng JSON trong Git. Các chức năng tài khoản, gửi biểu mẫu, đặt chỗ, thanh toán và lưu trữ phía máy chủ nằm ngoài phạm vi.

[App.razor](../src/BaDong.CoastalEscape/App.razor) dùng `Router`, `RouteView`, `FocusOnNavigate` và `Pages.NotFound`. [MainLayout](../src/BaDong.CoastalEscape/Layout/MainLayout.razor) cung cấp điều hướng desktop/mobile/footer và landmark `main`. Các route địa điểm và món ăn khớp mẫu URI rồi phân giải slug qua dữ liệu. Route không khớp dùng `NotFound`, cũng truy cập được tại `/khong-tim-thay`. Liên kết Maps mở dịch vụ ngoài.

## 2. Kiến trúc và thành phần

| Lớp | Trách nhiệm | Mã nguồn |
| --- | --- | --- |
| Khởi động | Gắn `App` và `HeadOutlet`; tạo scoped `HttpClient` theo base URI và scoped `ContentService`. | [Program.cs](../src/BaDong.CoastalEscape/Program.cs) |
| Trang | `Home`, `About`, `Explore`, `DestinationDetail`, `Cuisine`, `Gallery`, `Guide`, `Itineraries`, `Contact`, `NotFound`. `Cuisine` dùng chung component cho hai mẫu route. | [Pages](../src/BaDong.CoastalEscape/Pages) |
| Component dùng lại | `DestinationCard`, `FoodCard`, `Breadcrumbs`, `SourceNote`, `FaqAccordion`, `PhotoLightbox`. | [Components](../src/BaDong.CoastalEscape/Components) |
| Trình duyệt | Khôi phục route sau fallback, điều phối focus/scroll của hộp thoại và hỗ trợ sao chép URI. | [app.js](../src/BaDong.CoastalEscape/wwwroot/app.js), [404.html](../src/BaDong.CoastalEscape/wwwroot/404.html) |
| Nội dung | Sáu tập runtime, hai tập quản trị ảnh và ảnh tĩnh. | [data](../src/BaDong.CoastalEscape/wwwroot/data), [CONTENT_SOURCES.md](CONTENT_SOURCES.md) |

Trạng thái tải và lỗi trang chi tiết dùng `PageTitle`. Metadata description riêng của địa điểm hợp lệ và danh sách ẩm thực vẫn dùng `HeadContent`. Hai route chi tiết hiển thị thông báo hiện có khi slug không phân giải được.

## 3. Dịch vụ nội dung

[ContentService](../src/BaDong.CoastalEscape/Services/ContentService.cs) dùng `ConcurrentDictionary<string, object>` và `JsonSerializerDefaults.Web`. Cache được tra theo đường dẫn và kiểu. Khi miss, `GetFromJsonAsync` xử lý HTTP và deserialize. Giá trị hợp lệ được lưu trong bộ nhớ, kể cả giá trị rỗng/mặc định thay cho JSON `null`. Với `HttpRequestException`, `JsonException`, `NotSupportedException` hoặc `TaskCanceledException`, dịch vụ trả danh sách rỗng hoặc `SiteInfo` mặc định. Nhánh exception không ghi vào cache. UI nhận danh sách rỗng chung cho lỗi tải hoặc dữ liệu rỗng. Cache tồn tại cùng vòng đời instance của dịch vụ trong ứng dụng.

## 4. Mô hình và từ điển dữ liệu

Các kiểu runtime nằm trong [SiteModels.cs](../src/BaDong.CoastalEscape/Models/SiteModels.cs). Bảng nhóm các trường có cùng mục đích. **B** là bất biến nội dung được kiểm trong suite hoặc cốt lõi cho chức năng được nêu. **T** là tùy trường hợp hoặc có giá trị mặc định model. Đây là hợp đồng nội dung, không phải schema bắt buộc do serializer thực thi. Ví dụ lấy từ các tệp JSON hiện tại. Phân biệt kiểu lúc deserialize với quy tắc kiểm thử và kiểm tra thủ công.

| Entity / tệp | Field | Kiểu | B/T | Mô tả và quy tắc | Ví dụ |
| --- | --- | --- | --- | --- | --- |
| Destination / [destinations.json](../src/BaDong.CoastalEscape/wwwroot/data/destinations.json) | `id`, `slug`, `name`, `category` | string | B | ID và slug không trùng trong tập; name/category phục vụ hiển thị và lọc. | `ba-dong-beach`, `bien-ba-dong`, Biển Ba Động, `thien-nhien` |
| Destination | `shortDescription`, `description`, `tags`, `subtitle` | string, string[], string[], string | B cho mô tả, T cho tags/subtitle | Mô tả ngắn và danh sách mô tả cần có; đoạn đầu và tags tham gia tìm kiếm. | `["bien","phong-canh","di-bo","dien-gio"]`; Đường chân trời mở ra từ đồng bằng |
| Destination | `thumbnail`, `heroImage`, `thumbnailWidth`, `heroWidth`, `imageAlt` | string, string, int, int, string | B cho đường dẫn và alt, T cho kích cỡ theo ảnh | Ảnh local; kích cỡ dùng trong srcset; PENDING dùng placeholder. | `images/locations/ba-dong-beach-800.jpg`, `960`, `1920` |
| Destination, Food | `imageLocation`, `imageAttribution`, `imageLicense`, `imageSourceUrl`, `imageVerificationStatus` | string | B theo trạng thái | Khi VERIFIED cần thông tin nguồn và URL; địa điểm PENDING dùng giá trị đánh dấu và URL rỗng. | `CC BY 4.0`, `VERIFIED`, `PENDING` |
| Destination | `mapUrl`, `sourceUrls`, `updatedAt` | string, string[], string | B cho mapUrl, T cho nguồn/ngày theo model | Tham chiếu Maps, nguồn và mốc cập nhật nội dung. | `https://travinh.gov.vn/` trong sourceUrls, `10/11/2026` |
| Food / [foods.json](../src/BaDong.CoastalEscape/wwwroot/data/foods.json) | `id`, `slug`, `name`, `category`, `description` | string | B | ID/slug duy nhất trong tập; nhóm dùng cho lọc; mô tả dùng trong thẻ và chi tiết. | `cua-bien`, Cua biển, `hai-san` |
| Food | `image`, `thumbnail`, `imageWidth`, `thumbnailWidth`, `alt` | string, string, int, int, string | B cho ảnh/alt, T cho kích cỡ theo ảnh | Đường dẫn ảnh local; biến thể có điều kiện theo kích cỡ. | `images/food/vietnamese-crab-dish-1600.jpg`, `1920`, `960` |
| Food | `bestEnjoyed`, `note`, `sourceUrls` | string, string, string[] | T | Ngữ cảnh, lưu ý và nguồn ở trang chi tiết. | Một bữa cơm ven biển |
| GalleryPhoto / [gallery.json](../src/BaDong.CoastalEscape/wwwroot/data/gallery.json) | `id`, `category`, `caption`, `alt`, `image`, `thumbnail` | string | B cho ID, caption, alt, đường dẫn; T theo model cho category | ID duy nhất; category dùng để lọc; đường dẫn tới JPG local. | `ba-dong-coast`, `bien`, Biển Ba Động nhìn từ đường ven biển. |
| GalleryPhoto | `imageWidth`, `imageHeight`, `thumbnailWidth`, `thumbnailHeight` | int | T theo model | Kích thước ảnh và thumbnail trong HTML. | `1920`, `1080`, `960`, `540` |
| GalleryPhoto | `author`, `license`, `sourceUrl`, `actualLocation`, `verificationStatus` | string | B cho ảnh đã xác minh | Ghi công, giấy phép, URL nguồn và vị trí thật. | `Baoothersks`, `CC BY 4.0`, `VERIFIED` |
| Itinerary / [itineraries.json](../src/BaDong.CoastalEscape/wwwroot/data/itineraries.json) | `id`, `title`, `durationLabel`, `summary`, `stops` | string × 4, object[] | B | ID duy nhất, mô tả có nội dung và ít nhất một stop. | `one-day`, Đi trong ngày |
| ItineraryStop | `timeLabel`, `title`, `description`, `image`, `imageAlt`, `slug` | string | B trừ slug T | Slug có giá trị phải phân giải được; slug rỗng không tạo link. Ảnh local. | Sáng, Đón gió ở Biển Ba Động, `bien-ba-dong`; stop Trưa dùng `""` |
| FaqItem / [faq.json](../src/BaDong.CoastalEscape/wwwroot/data/faq.json) | `id`, `question`, `answer`, `sourceUrls` | string × 3, string[] | B | ID duy nhất, câu hỏi/trả lời có nội dung và có nguồn. | `best-time`, Nên đi Ba Động vào thời điểm nào? |
| SiteInfo / [site-info.json](../src/BaDong.CoastalEscape/wwwroot/data/site-info.json) | `name`, `tagline`, `region`, `administrativeLocation`, `academicDisclaimer`, `updatedAt`, `mapUrl`, `sourceLinks` | string × 7, object[] | B cho tập xuất bản | Một object cấu hình nội dung; sourceLinks chứa label và URL tuyệt đối. | BA ĐỘNG — Coastal Escape, `06/11/2026` |
| SourceLink | `label`, `url` | string | B | Nhãn hiển thị và URL nguồn. | Cục Du lịch Quốc gia Việt Nam, `https://vietnamtourism.gov.vn/` |
| ImageManifestEntry / [image-manifest.json](../src/BaDong.CoastalEscape/wwwroot/data/image-manifest.json) | `filename`, `responsiveVariants`, `title`, `actualLocation`, `photographer`, `sourceUrl`, `license`, `attribution`, `verificationStatus` | string, string[], string × 7 | B cho file và provenance ảnh VERIFIED; danh sách biến thể có thể rỗng | Đối chiếu exact-case giữa manifest và các file xuất bản. | `images/locations/ba-dong-beach-1600.jpg`, `["images/locations/ba-dong-beach-800.jpg"]`, `Baoothersks` |
| Yêu cầu ảnh / [image-requirements.json](../src/BaDong.CoastalEscape/wwwroot/data/image-requirements.json) | `filename`, `title`, `actualLocation`, `photographer`, `sourceUrl`, `license`, `attribution`, `verificationStatus`, `targetPlacements` | string × 8, string[] | ID yêu cầu và route đích cần có để quản trị; URL T khi PENDING | `filename` là mã ảnh cần tìm, `targetPlacements` ghi route đưa ảnh vào sau khi có nguồn. | `ba-dong-casuarina-row`, `PENDING`, `/kham-pha/hang-duong-ven-bien` |

Quan hệ là tham chiếu logic giữa các tệp tĩnh. `ItineraryStop.slug` liên kết `Destination.slug`; đường dẫn ảnh hội tụ về `wwwroot/images`. Các biến thể ảnh và thông tin cấp phép được kiểm kê trong manifest. Các tập quản trị ảnh phục vụ tài liệu và kiểm thử, ngoài sáu API đọc của `ContentService`.

## 5. Tìm kiếm và lọc

[Explore.razor](../src/BaDong.CoastalEscape/Pages/Explore.razor) cập nhật truy vấn qua `oninput`. Mỗi phần tử được kiểm tra danh mục trước. Hàm `Normalize` chuyển FormD, bỏ `NonSpacingMark`, gom lại FormC và chuyển chữ thường. Nếu truy vấn không rỗng, chương trình tìm chuỗi con trong name, shortDescription, đoạn description đầu và tags bằng `OrdinalIgnoreCase`. Thứ tự JSON được giữ. Nút xóa bộ lọc đặt lại từ khóa và danh mục; nút Tất cả chỉ đặt lại danh mục. Phép bỏ dấu kết hợp chưa ánh xạ riêng cặp `đ/d`.

## 6. Triển khai và khả năng kiểm chứng

[CI](../.github/workflows/ci.yml) và [Deploy Pages](../.github/workflows/deploy-pages.yml) chạy độc lập. CI chạy khi push `main` hoặc pull request, gồm restore app/test, Release build, automated test và publish để kiểm tra native relinking. Pages chạy khi push `main` hoặc kích hoạt tay, gồm build/publish, thay base path cùng các token 404/robots/sitemap, upload artifact và deploy qua job phụ thuộc build. Hai workflow dùng .NET 10 và workload `wasm-tools`. Test là bước của CI, giữa hai workflow hiện chưa có dependency.

[Danh mục sơ đồ](diagrams/README.md) có SVG/PNG dùng cho Word. [Bằng chứng kỹ thuật](evidence/README.md) và [giới hạn](KNOWN_LIMITATIONS.md) tách kết quả local, production và các mục còn mở.
