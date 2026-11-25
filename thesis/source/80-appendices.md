# PHỤ LỤC

## A. Cài đặt và chạy trên máy phát triển

Từ thư mục gốc, thực hiện lệnh bằng SDK tương thích với `global.json`. Project ứng dụng và project test ở hai đường dẫn riêng. Cấu hình test của dự án dùng Microsoft Testing Platform và tham số `--project`.

> dotnet --version
> $app = 'src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj'
> $tests = 'tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj'
> dotnet restore $app
> dotnet restore $tests
> dotnet build $app -c Release --no-restore
> dotnet test --project $tests -c Release --no-restore
> dotnet run --project $app -c Release --no-build

Mở địa chỉ mà tiến trình chạy in ra. `setup/README.md` mô tả chuẩn bị, chạy thử và publish. Khi chạy tại máy, ứng dụng dùng base phát triển. Khi so sánh với Pages cần giữ base path và quy tắc fallback trong workflow triển khai. Dữ liệu nằm trong `wwwroot/data`; thay đổi ở đó có thể được xem cùng diff source.

## B. Cấu trúc JSON và ví dụ

Ví dụ sau chọn một số trường từ bản ghi địa điểm Biển Ba Động trong `destinations.json`. Dữ liệu thực có thêm nội dung, ảnh và thông tin nguồn. ID nêu khóa nội dung, slug nêu phần đường dẫn. Category dùng khi lọc.

> {
>   "id": "ba-dong-beach",
>   "slug": "bien-ba-dong",
>   "name": "Biển Ba Động",
>   "category": "thien-nhien",
>   "imageVerificationStatus": "VERIFIED"
> }

!table|Hợp đồng trường dùng khi đối chiếu dữ liệu|0.405,0.205,0.39
| Trường | Kiểu | Ràng buộc nghiệp vụ |
| Destination.id, Food.id | Chuỗi | Duy nhất trong từng tập. |
| Destination.slug, Food.slug | Chuỗi | Có giá trị, duy nhất trong tập và dùng để tạo đường dẫn. |
| Itinerary.stops | Mảng | Mỗi điểm dừng có nội dung; slug tùy chọn phải giải được nếu có. |
| GalleryPhoto.sourceUrl | Chuỗi | URL nguồn ảnh đã xác minh. |
| ImageManifestEntry.filename | Chuỗi | Khớp tên ảnh trên máy phát triển theo đúng chữ hoa/thường. |
| SiteInfo.sourceLinks | Mảng đối tượng | Mỗi nguồn có nhãn và URL. |

Từ điển đầy đủ trong `docs/SOFTWARE_DESIGN.md` nêu các trường hiển thị, trường tùy chọn, kích thước ảnh và ví dụ. Thay đổi tên file cần cập nhật đúng chỗ ở manifest, data và tham chiếu giao diện. Các trường chưa có minh chứng cần giữ trạng thái riêng để tránh được đọc như dữ liệu đã xác minh.

## C. Ca kiểm thử và truy vết

### C.1. Ca kiểm tra sau triển khai

!table|Route và title quan sát được trên bản công khai|0.34,0.14,0.52
| Route trong ứng dụng | HTTP đầu | Title sau kết xuất |
| / | 200 | BA ĐỘNG — Coastal Escape · Nơi biển chạm vào nhịp sống miền Tây |
| /kham-pha/bien-ba-dong | 404 | Biển Ba Động · BA ĐỘNG — Coastal Escape |
| /kham-pha/khong-ton-tai | 404 | Không tìm thấy địa điểm · BA ĐỘNG — Coastal Escape |
| /am-thuc | 404 | Ẩm thực · BA ĐỘNG — Coastal Escape |
| /am-thuc/cua-bien | 404 | Cua biển · Ẩm thực Ba Động |
| /am-thuc/khong-ton-tai | 404 | Không tìm thấy món ăn · Ẩm thực Ba Động |
| /khong-tim-thay | 404 | Không tìm thấy · BA ĐỘNG — Coastal Escape |

Chọn lối quay lại từ trang lỗi địa điểm, mở thẻ Biển Ba Động và tải lại trang chi tiết. Sau đó chọn lối quay lại từ lỗi món. So sánh URL cuối, một thẻ title, heading và tài nguyên tải được. Ghi 404 tài liệu của URL mở trực tiếp riêng với lỗi ở yêu cầu JSON, ảnh, CSS và môi trường thực thi.

### C.2. Hai trường hợp lỗi tải có kiểm soát

Từ bản Release trên máy phát triển, dùng trình duyệt kiểm thử để giữ request `destinations.json` khi mở chi tiết địa điểm. Xác nhận title đang tải. Trả HTTP 503 rồi xác nhận title chưa có dữ liệu, heading lỗi và một main. Thực hiện tương tự với `foods.json` ở trang món. Các request 503 do test tạo để tái hiện trạng thái, và được ghi tách khỏi kiểm tra deployment.

### C.3. Bảng chỉ mục 20 yêu cầu

!table|Truy vết rút gọn theo nhóm và bằng chứng|0.14,0.37,0.49
| Mã | Yêu cầu | Bằng chứng hoặc trạng thái |
| F-01 | Trang chủ và giới thiệu | Ảnh 01–03 và kiểm tra route lịch sử. |
| F-02 | Tìm kiếm và lọc | E-U02, ảnh 05–08. Phạm vi đ/d còn mở. |
| F-03 | Địa điểm và nguồn ảnh | D-T01, D-J01, ảnh 09. |
| F-04 | Sao chép URL | Mã nguồn có. Chưa kiểm clipboard. |
| F-05 | Ẩm thực và lọc | D-T03–05, E-U05, ảnh 10–11. |
| F-06 | Thư viện và lightbox | E-U03, D-J01, ảnh 12–13. |
| F-07 | Cẩm nang và FAQ | E-U04, D-J01, ảnh 14. |
| F-08 | Lịch trình và điểm dừng | E-U04, D-J01, ảnh 15. |
| F-09 | Vị trí và liên kết bản đồ | E-U05, href đã kiểm ở Phase C, ảnh 16. |
| F-10 | Slug sai và trang lỗi | D-T00–09, kiểm tra nhanh trên bản công khai, ảnh 17–18. |
| F-11 | Đặt chỗ và giao dịch | Ngoài phạm vi sản phẩm. |
| N-01 | JSON và hồ sơ ảnh | D-J01, chính sách VERIFIED và PENDING. |
| N-02 | Dịch vụ và bộ nhớ đệm | Test dịch vụ, hai ca 503 trên máy phát triển. |
| N-03 | Đáp ứng và trợ năng | Ma trận 28 lượt, ca bàn phím và ảnh; một phần. |
| N-04 | Triển khai tĩnh | CI, Pages và kiểm tra nhanh; còn HTTP 404 ban đầu. |
| N-05 | Đánh giá hiệu năng | Có kích thước gói triển khai. Chưa đo hiệu năng trải nghiệm. |
| A-01 | Kho mã nguồn, README, setup | Có cấu trúc và hướng dẫn. Thiếu liên hệ. |
| A-02 | Báo cáo và collaborator | Có W48. Collaborator giảng viên còn thiếu. |
| A-03 | Thiết kế và bằng chứng | Có chín sơ đồ và hồ sơ truy vết. |
| A-04 | Hồ sơ văn bản và bảo vệ | Có DOCX, PDF, HTML và slide nội bộ để duyệt. Hồ sơ nộp chính thức đang chờ xác nhận. |

Ma trận trong `docs/TRACEABILITY_MATRIX.md` có thêm route, mã nguồn và bằng chứng theo từng yêu cầu. Bảng chỉ mục giữ các mã D/E của báo cáo Phase D–F. Mục F-10 bổ sung kết quả kiểm tra nhanh trên bản công khai từ mốc phát hành.

## D. Quy trình GitHub Actions và triển khai

Commit sửa title là `92c5fa62139e17ef8bc73bc5a288b3ea0c5c4391`. Commit hồ sơ học thuật và SHA phát hành là `463da372613648411ef9d6002c4d895cb03cbb4d`. Các link [CI](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45546387181) và [Deploy to GitHub Pages](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45546387162) mở lần chạy cụ thể. Kết quả truy cập dùng [project site](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/).

Để xem lại pipeline, mở workflow `ci.yml` và tìm bước restore, build, test và báo kích thước. Workflow `deploy-pages.yml` có bước kiểm tên repo, thay base và token, tải gói triển khai và triển khai. So sánh SHA của hai run với SHA công bố trước khi ghi kết quả. `docs/RELEASE_BASELINE.md` ghi thời gian success của deployment và kiểm tra trình duyệt sau công bố.

## E. Giao diện chính bổ sung

Các ảnh trong mục này chụp trên máy phát triển cùng đợt với Chương 4. Mã và tên mỗi ảnh theo manifest trong kho mã nguồn.

!figure|docs/evidence/screenshots/04-mobile-menu.png|Menu di động ở vùng hiển thị 390 × 844|10.5

!figure|docs/evidence/screenshots/05-explore.png|Danh sách Khám phá và công cụ sàng lọc địa điểm

!figure|docs/evidence/screenshots/06-explore-search.png;docs/evidence/screenshots/07-explore-filter.png|Kết quả từ khóa không dấu và trạng thái lọc Thiên nhiên

!figure|docs/evidence/screenshots/09-destination.png|Chi tiết Biển Ba Động với lối mở bản đồ và ghi công ảnh

!figure|docs/evidence/screenshots/12-gallery.png|Danh sách ảnh trước khi mở lightbox

!figure|docs/evidence/screenshots/16-location.png|Thông tin vị trí và lối mở bản đồ|6.7

## F. Siêu dữ liệu và nguồn ảnh

Tệp `image-manifest.json` và sổ `docs/CONTENT_SOURCES.md` là nơi đối chiếu các đường dẫn và giấy phép. Ví dụ ảnh Biển Ba Động của Baoothersks có giấy phép CC BY 4.0 và các bản ảnh kích thước khác nhau [@ba-dong-photo]. Ghi công trong hình sử dụng nội dung hiện có của giao diện. Khi đưa ảnh giao diện sang tài liệu, cần duy trì chỉ dẫn tới nguồn và không đổi diễn giải vị trí.

!table|Cách đọc trạng thái xác minh ảnh|0.41,0.59
| Trạng thái | Diễn giải trong dự án |
| VERIFIED | Có căn cứ cho chủ thể và địa điểm khai báo. |
| VERIFIED_REGION | Ảnh thuộc vùng liên quan. Ghi địa điểm cụ thể. |
| VERIFIED_SUBJECT | Chủ thể phù hợp; vị trí khác hoặc không đủ để gọi là Ba Động. |
| INTERNAL_PLACEHOLDER | Hình giữ chỗ do dự án quản lý. |
| PENDING | Mục cần tìm hoặc xác minh ảnh phù hợp. |

Danh sách nguồn và biến thể giữ riêng với nhiệm vụ biên tập. Một ảnh vùng rộng hơn không dùng để thỏa yêu cầu ảnh chụp cảnh cụ thể nếu nguồn chưa chứng minh. Khi cập nhật hồ sơ, dùng nhãn trạng thái nhất quán giữa trang, siêu dữ liệu và tài liệu.
