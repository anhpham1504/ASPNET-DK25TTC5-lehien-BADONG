# Kết quả kiểm thử kỹ thuật tuần 2026-W48

Ngày 25/11/2026, múi giờ Asia/Bangkok. Baseline `955956b2298be11fd84937ea390d66d5bd2119bc` khớp HEAD của `main` local và remote trước khi sửa. Git status ban đầu sạch. Môi trường local là Windows, .NET SDK 10.0.100, Release, Chrome Headless 158, Playwright CLI 0.1.25, `http://127.0.0.1:5198/`. Bản sửa nằm trong working tree trên baseline này.

| Phạm vi | Kiểm tra | Kết quả và bằng chứng |
| --- | --- | --- |
| Lịch sử xác minh | GitHub Actions CI và Pages | SUCCESS cùng SHA baseline. [CI 45542500443](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45542500443), [Pages 45542500074](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45542500074). |
| Lịch sử xác minh | Browser matrix Phase C | 48 lượt, 12 URL × 320/390/768/1440 px. Quan sát trước đợt này gồm render các route, deep-link fallback, search/filter, menu, lightbox, FAQ, tab và liên kết Maps. |
| Production hiện tại | HTTP base và tài nguyên SEO | Homepage, robots, sitemap và `404.html` trả HTTP 200. Direct URL `/kham-pha/bien-ba-dong` trả 404. Các phản hồi chứa base mới và không còn deployment token. |
| Production hiện tại | D-T00 tái hiện lỗi | FAILED trên baseline: `/kham-pha/khong-ton-tai` có heading “Trang này đã trôi khỏi đường bờ.”, title rỗng và 0 thẻ `head title`. Tái hiện thêm trên Release local trước khi build bản sửa. |
| Local hiện tại | Restore + Release build | Restore app/test PASS. Build app PASS, 0 warning, 0 error. |
| Local hiện tại | D-J01 JSON và test | 8/8 content JSON hợp lệ. Microsoft Testing Platform, 14/14 PASS, 0 failed, 0 skipped. |
| Local hiện tại | NuGet audit | Hai project đã chạy `dotnet list … package --vulnerable --include-transitive`. Không ghi nhận package dễ tổn thương từ nguồn NuGet đã truy vấn. |
| Local hiện tại | D-T01 đến D-T07 title và layout | 28/28 lượt có đúng nội dung title và h1, một `head title`, một `h1`, một `main`, `lang=vi`, không overflow. Bốn chiều rộng 320/390/768/1440 px, cao 900 px. |
| Local hiện tại | D-T08 navigation/refresh | Enter trên link quay lại, từ Khám phá mở Biển Ba Động, reload chi tiết và Enter về Ẩm thực đều cập nhật URL/title đúng. Focus link có outline solid. |
| Local hiện tại | D-T09 loading / HTTP 503 | Hai ca độc lập giữ request JSON rồi trả HTTP 503: title từ “Đang tải địa điểm” sang “Địa điểm chưa có dữ liệu”, từ “Đang tải ẩm thực” sang “Ẩm thực chưa có dữ liệu”. Hai nhánh có một title và một main. Error heading xuất hiện sau 503. Đây là lỗi mô phỏng có kiểm soát trong Playwright. |
| Local hiện tại | Lỗi trình duyệt và metadata | Lượt cuối 0 page exception, 0 console error, 0 asset/JSON failure ngoài mô phỏng. Lượt đầu có hai font Google bị hủy khi đổi trang nhanh; lượt cuối đợi font và không tái hiện. Không có canonical trên các route kiểm tra; thay đổi chỉ chạm title và giữ nguyên hai description. |
| Local hiện tại | Accessibility | PARTIAL. Ngữ nghĩa, viewport, focus nhìn thấy và thao tác bàn phím chọn lọc đã kiểm tra. Kiểm toán WCAG, độ tương phản, trình đọc màn hình và zoom 200% thuộc NOT RUN. |
| Local hiện tại | Render sơ đồ | 9 nguồn Mermaid được parse và tạo 9 SVG cùng 9 PNG. [Danh mục](../../diagrams/README.md). |
| Production bản sửa | CI, Pages và trình duyệt trên bản sửa | NOT RUN. Các run đã xác minh ở trên thuộc baseline. |

## Kết quả chi tiết kiểm tra title

| Case | URL localhost | Title mong đợi và quan sát | Heading/nhánh |
| --- | --- | --- | --- |
| D-T01 | `/kham-pha/bien-ba-dong` | Biển Ba Động · BA ĐỘNG — Coastal Escape | Biển Ba Động |
| D-T02 | `/kham-pha/khong-ton-tai` | Không tìm thấy địa điểm · BA ĐỘNG — Coastal Escape | Trang này đã trôi khỏi đường bờ. |
| D-T03 | `/am-thuc` | Ẩm thực · BA ĐỘNG — Coastal Escape | Vị biển trên bàn ăn. |
| D-T04 | `/am-thuc/cua-bien` | Cua biển · Ẩm thực Ba Động | Cua biển |
| D-T05 | `/am-thuc/khong-ton-tai` | Không tìm thấy món ăn · Ẩm thực Ba Động | Món này chưa có trong thực đơn. |
| D-T06 | `/khong-tim-thay` | Không tìm thấy · BA ĐỘNG — Coastal Escape | Trang này không có trong bản đồ. |
| D-T07 | `/route-khong-ton-tai` | Không tìm thấy · BA ĐỘNG — Coastal Escape | Router dùng NotFound |

## Kiểm tra tương tác và accessibility

| Case | Bằng chứng local |
| --- | --- |
| E-U01 Trang chủ và menu | Chụp trang chủ desktop/tablet/mobile. Ở 390 px, Enter mở menu, focus vào nút đóng, Tab/Shift+Tab vòng trong dialog, Escape đóng và trả focus về nút menu. Scroll body bị khóa khi mở. Với reduced motion, animation hero còn 0,01 ms. |
| E-U02 Tìm kiếm, lọc và empty | `hoàng hôn` và `hoang hon` cùng trả đúng một thẻ `goc-ngam-hoang-hon`. Lọc Thiên nhiên có ít hơn 7 kết quả và còn kết quả; truy vấn không khớp hiện empty state; xóa bộ lọc trả lại 7 thẻ. |
| E-U03 Gallery | Enter mở lightbox. Mũi tên phải đổi ảnh, mũi tên trái quay lại ảnh cũ. Escape đóng và trả focus về thẻ ảnh. |
| E-U04 FAQ và lịch trình | Enter mở đáp án FAQ. Enter trên tab thứ hai cập nhật `aria-selected=true`. |
| E-U05 Nội dung các trang | Chụp listing/chi tiết món, địa điểm, vị trí và hai trang lỗi. Bộ lọc Hải sản giảm từ 4 món xuống 1; Tất cả khôi phục 4 món. |

Tệp kiểm thử tự động [RepositoryDataTests.cs](../../../tests/BaDong.CoastalEscape.Tests/RepositoryDataTests.cs) và [ContentServiceTests.cs](../../../tests/BaDong.CoastalEscape.Tests/ContentServiceTests.cs) kiểm tra dữ liệu và dịch vụ. Các kiểm tra DOM, bàn phím và network nêu trên thực hiện riêng trong trình duyệt. Khả năng dùng clipboard, tab order toàn site, tương phản màu, benchmark và Lighthouse là NOT RUN trong đợt local.

## Lệnh tái kiểm tra kỹ thuật

```powershell
dotnet --version
dotnet restore src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj
dotnet restore tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj
dotnet build src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj -c Release --no-restore
dotnet test --project tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj -c Release --no-restore
dotnet run --project src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj -c Release --no-build --no-launch-profile --urls http://127.0.0.1:5198
```

Đối chiếu [ảnh chụp](../screenshots/MANIFEST.md), [ma trận truy vết](../../TRACEABILITY_MATRIX.md) và [giới hạn](../../KNOWN_LIMITATIONS.md) trước khi đưa kết quả vào luận văn.
