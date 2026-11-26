# LỜI CẢM ƠN

Em xin trân trọng cảm ơn quý thầy cô đã giảng dạy môn Chuyên đề ASP.NET. Đồ án là dịp để em vận dụng kiến thức về lập trình web, tổ chức dữ liệu và kiểm thử vào một sản phẩm có thể mở trên trình duyệt. Quá trình đối chiếu nguồn nội dung, mô tả quyết định thiết kế và kiểm tra lại sau triển khai giúp em hiểu rõ hơn trách nhiệm của người xây dựng phần mềm trước người đọc.

Em trân trọng các tài liệu kỹ thuật và nguồn tư liệu công khai đã được trích dẫn trong báo cáo, trong đó có các tác giả cung cấp ảnh kèm thông tin sử dụng. Các nguồn đó giúp em phân biệt điều có thể trình bày có căn cứ với những thông tin về địa điểm và hình ảnh cần tiếp tục xác minh.

# MỤC LỤC

!toc

# DANH MỤC HÌNH

!lof

# DANH MỤC BẢNG

!lot

# DANH MỤC CHỮ VIẾT TẮT

> API    Giao diện lập trình ứng dụng
> CI     Tích hợp liên tục
> CSS    Tập kiểu trình bày phân tầng
> DOM    Mô hình đối tượng tài liệu
> FAQ    Các câu hỏi thường gặp
> GVHD   Giảng viên hướng dẫn
> HTTP   Giao thức truyền siêu văn bản
> JSON   Dạng ký hiệu đối tượng JavaScript dùng trao đổi dữ liệu
> SDK    Bộ công cụ phát triển phần mềm
> SEO    Tối ưu hóa cho công cụ tìm kiếm
> SPA    Ứng dụng một trang
> TVHĐ   Thành viên hội đồng
> URL    Địa chỉ tài nguyên
> WASM   WebAssembly
> WCAG   Hướng dẫn khả năng tiếp cận nội dung web

# TÓM TẮT

Đồ án xây dựng BA ĐỘNG — Coastal Escape, một website giới thiệu điểm đến, ẩm thực và lịch trình tham khảo quanh Biển Ba Động. Đề tài tập trung vào việc tổ chức thông tin có nguồn, hỗ trợ tìm kiếm trên thiết bị cầm tay và tạo đường dẫn đi từ danh sách đến chi tiết. Giải pháp dùng Blazor WebAssembly độc lập trên .NET 10. Các thành phần Razor lấy dữ liệu JSON tĩnh qua dịch vụ nội dung có bộ nhớ đệm. Website được phát hành dưới dạng tài nguyên tĩnh trên GitHub Pages.

Kết quả gồm website, mô hình dữ liệu, hồ sơ thiết kế và bằng chứng kiểm thử gắn với phiên bản mã nguồn. Bản phát hành có Release build 0 cảnh báo, 0 lỗi và 14 kiểm thử tự động đạt. Trên bản triển khai cuối, 13 route được kiểm tra ở bốn viewport, tổng cộng 52 ca production; mỗi ca xác nhận title, heading chính, bố cục và tài nguyên sau khi Blazor khởi động. Đường dẫn sâu trên Pages vẫn có thể trả HTTP 404 trước khi ứng dụng khôi phục đúng trang, và một số địa điểm vẫn chờ ảnh đủ căn cứ. Các kết quả kiểm tra khả năng tiếp cận chỉ phản ánh phạm vi đã thực hiện.

Từ khóa: Ba Động, Blazor WebAssembly, GitHub Pages, dữ liệu JSON, truy vết kiểm thử.
