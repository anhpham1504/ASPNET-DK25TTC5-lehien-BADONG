# Câu hỏi chuẩn bị bảo vệ

Trả lời theo bản phát hành [463da37](../../docs/RELEASE_BASELINE.md). Đối chiếu thêm [hồ sơ thiết kế](../../docs/SOFTWARE_DESIGN.md), [ma trận truy vết](../../docs/TRACEABILITY_MATRIX.md) và [bằng chứng kiểm thử](../../docs/evidence/academic-validation/2026-W48-phase-d-f.md).

## Bài toán và thiết kế

1. **Vì sao chọn đề tài?** Người chuẩn bị chuyến đi cần tra cứu điểm đến, món ăn và lịch trình từ một chỗ. Ba Động là phạm vi đủ cụ thể để em kiểm tra nguồn thông tin và thử một cấu trúc cẩm nang.
2. **Đối tượng sử dụng là ai?** Người đọc muốn tìm hiểu vùng biển Ba Động, nhất là người tra cứu bằng điện thoại. Lịch trình và thông tin địa điểm dùng để tham khảo.
3. **Vì sao chọn Blazor WebAssembly?** Đề tài cần tương tác nhưng chỉ triển khai tệp tĩnh. Blazor WebAssembly cho phép dùng C# và Razor để xử lý giao diện ngay trong trình duyệt.
4. **ASP.NET Core có vai trò gì?** Blazor thuộc hệ sinh thái ASP.NET Core. Ứng dụng dùng mô hình WebAssembly độc lập, các thành phần Razor, định tuyến và cung cấp phụ thuộc. Bản công khai tải tệp qua GitHub Pages.
5. **Website có backend nghiệp vụ không?** Website phục vụ JSON và tài nguyên tĩnh. Các thao tác tìm, lọc và đổi tab chạy trong trình duyệt. Liên kết bản đồ hoặc nguồn mở trang của bên cung cấp.
6. **Vì sao không dùng SQL Server?** Tập nội dung nhỏ, đọc nhiều và cập nhật theo commit. JSON phù hợp với phạm vi và giúp triển khai tĩnh. Một cơ sở dữ liệu sẽ hữu ích khi nhu cầu ghi hoặc quản trị đồng thời xuất hiện.
7. **Razor Components hoạt động ra sao?** Mỗi thành phần kết hợp phần hiển thị, tham số và sự kiện. Khi trạng thái thay đổi, Blazor kết xuất phần giao diện liên quan.
8. **Router dùng dữ liệu như thế nào?** Router khớp mẫu đường dẫn với thành phần trang. Trang chi tiết nhận slug, tải tập dữ liệu tương ứng rồi tìm bản ghi.
9. **Slug là gì?** Là chuỗi nhận diện trong URL, ví dụ bien-ba-dong. Slug cần duy nhất trong tập tương ứng. Tiền tố kham-pha và am-thuc phân biệt các nhóm.
10. **Vì sao dùng JSON?** Tệp văn bản có cấu trúc giúp đọc bằng HTTP và đối chiếu thay đổi qua Git. Các kiểm thử kiểm trường, liên kết, ảnh và quan hệ trong dữ liệu.

## Dữ liệu và hiện thực

11. **ContentService làm gì?** Đọc sáu nhóm dữ liệu bằng HttpClient, chuyển JSON thành đối tượng .NET, lưu kết quả thành công và trả giá trị mặc định khi gặp lỗi đã xử lý.
12. **Bộ nhớ đệm hoạt động ra sao?** Dịch vụ dùng ConcurrentDictionary theo đường dẫn và kiểm kiểu trước khi lấy lại. Kết quả sống cùng dịch vụ trong phiên. Hai lần gọi đồng thời vẫn có thể tải trùng khi cùng chưa có dữ liệu.
13. **Lỗi HTTP được xử lý ở đâu?** Dịch vụ bắt HttpRequestException và các nhóm ngoại lệ đọc JSON, kiểu hoặc tác vụ bị hủy. Nó trả dữ liệu rỗng hoặc SiteInfo mặc định. Nhánh ngoại lệ không ghi kết quả vào bộ nhớ đệm.
14. **Nếu tệp JSON trả null thì sao?** Đối tượng null được đổi thành danh sách rỗng hoặc SiteInfo mặc định sau lần đọc thành công. Giá trị thay thế có thể được lưu vào bộ nhớ đệm.
15. **Tìm kiếm tiếng Việt được xử lý thế nào?** Chuẩn hóa FormD, loại ký tự NonSpacingMark, gom về FormC, chuyển chữ thường rồi so chuỗi con theo OrdinalIgnoreCase.
16. **Dấu tiếng Việt có trường hợp nào chưa hỗ trợ?** “Hoàng hôn” và “hoang hon” cùng tìm được Góc ngắm hoàng hôn. Đ và d là ký tự riêng nên vẫn phân biệt.
17. **Bộ lọc và từ khóa kết hợp ra sao?** Explore.razor xét danh mục trước. Khi có từ khóa, nó tìm trong tên, mô tả ngắn, đoạn mô tả đầu và tags. Thứ tự tệp JSON được giữ.
18. **Lịch trình tham chiếu địa điểm ra sao?** Điểm dừng có thể chứa slug của một địa điểm. Giá trị có nội dung phải phân giải được. Một điểm dừng có slug rỗng có thể hiện mô tả mà không tạo liên kết.
19. **Vì sao một số ảnh dùng ảnh giữ chỗ?** Năm địa điểm chưa có ảnh đủ căn cứ nguồn hoặc vị trí. Trạng thái PENDING làm rõ rằng ảnh cần được xác minh thêm.
20. **Mọi ảnh có phải chụp tại Ba Động?** Ảnh VERIFIED_REGION thuộc vùng liên quan. VERIFIED_SUBJECT xác minh chủ thể ở phạm vi phù hợp. Vị trí, tác giả và giấy phép thể hiện trong từng hồ sơ.
21. **Nguồn du lịch được quản lý thế nào?** Dữ liệu có liên kết và mốc cập nhật tùy loại. Sổ nguồn của kho mã nguồn lưu thông tin đối chiếu. Người đọc cần truy cập nguồn khi điều kiện tham quan thay đổi.

## Kiểm thử và khả năng tiếp cận

22. **14 kiểm thử tự động bao phủ gì?** Chúng kiểm tệp và cấu trúc JSON, ID và slug, đường dẫn ảnh, thông tin xác minh, tham chiếu lịch trình và hành vi ContentService trước phản hồi hợp lệ hoặc lỗi.
23. **14 ca đạt có chứng minh toàn bộ website hết lỗi không?** Kết quả cho biết những hành vi được định nghĩa trong bộ kiểm đã đạt ở môi trường đã chạy. Giao diện, mạng và thao tác người dùng có những lượt kiểm riêng.
24. **48 và 28 là số gì?** 48 là lượt của phiên bản cơ sở, gồm 12 URL × 4 chiều rộng. 28 là lượt hồi quy tiêu đề của bản sửa trên máy phát triển, gồm 7 URL × 4 chiều rộng.
25. **Hai lỗi HTTP 503 có thật trên production không?** Đây là hai phản hồi mô phỏng đối với destinations.json và foods.json để quan sát từ trạng thái đang tải sang chưa có dữ liệu.
26. **Accessibility đã kiểm đến mức nào?** Có các lượt kiểm heading, main, lang, focus, menu, hộp thoại ảnh, FAQ, tab và reduced motion. Kiểm toán đầy đủ WCAG 2.2 AA, tương phản, phóng to 200% và trình đọc màn hình còn mở.
27. **Ảnh chụp có viền focus là lỗi hình ảnh hay kết quả kiểm thử?** Ảnh lấy từ bản Release chạy tại máy phát triển và ghi lại DOM lúc kiểm thử. Trường hợp trang chủ tự focus tiêu đề ở bản công khai cũng được ghi trong giới hạn.
28. **Đã kiểm tra clipboard chưa?** Chức năng có trong mã nguồn. Hồ sơ này chưa có bằng chứng thao tác chép và dán clipboard.
29. **Số liệu dung lượng có thay cho đánh giá tốc độ không?** CI đo kích thước tệp Brotli và WASM trong gói. Thời gian khởi động và số byte tải thực tế phụ thuộc mạng, thiết bị, tài nguyên được chọn và bộ nhớ đệm.

## Triển khai, giới hạn và phát triển

30. **GitHub Actions thực hiện công việc gì?** CI khôi phục gói, dựng Release, chạy test và kiểm tra gói WebAssembly. Workflow Pages dựng bản tĩnh, áp dụng URL cơ sở, tải gói lên và triển khai.
31. **CI và CD khác gì trong dự án?** CI kiểm tra việc tích hợp mã nguồn. Luồng triển khai tạo và công bố gói. Hai workflow chạy độc lập, nên đối chiếu trạng thái và SHA của từng lần.
32. **Vì sao URL sâu trả HTTP 404?** GitHub Pages tìm một tệp theo URL tĩnh. Những URL của Router không có tệp HTML riêng. Trang 404 giữ đường dẫn để ứng dụng khôi phục sau khi tải, còn HTTP ban đầu vẫn là 404.
33. **PageTitle giải quyết vấn đề gì?** Thành phần đặt tiêu đề thẻ trình duyệt sau khi Blazor kết xuất. Các nhánh đang tải, có dữ liệu, không tìm thấy và chưa có dữ liệu có tiêu đề phù hợp.
34. **SEO đã đạt đến đâu?** Có tiêu đề sau khi ứng dụng chạy, sitemap và robots theo đường dẫn đã triển khai. URL sâu, HTML ban đầu và canonical riêng theo route vẫn là giới hạn.
35. **Cách triển khai lại website?** Dùng quy trình GitHub Pages đã cấu hình khi có quyền và phê duyệt. So SHA của CI và Pages, mở URL có base đúng rồi kiểm các đường dẫn quan trọng.
36. **Nếu khảo sát SSR thì phải đổi gì?** Cần môi trường chạy ASP.NET Core phía máy chủ, xử lý route ở đó, kiểm cấu hình cung cấp phụ thuộc, nguồn nội dung, metadata và mã phản hồi. Giữ SSR như hướng khảo sát sau mốc đóng băng.
37. **Hạn chế nào đáng ưu tiên?** URL sâu và bố cục đầu trang là vấn đề kỹ thuật. Năm ảnh chờ xác minh là vấn đề dữ liệu. Khả năng tiếp cận cần mở rộng kiểm tra trước khi kết luận về WCAG.
