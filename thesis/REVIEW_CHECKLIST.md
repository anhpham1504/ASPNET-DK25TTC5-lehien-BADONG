# Checklist duyệt hồ sơ đồ án

## Mốc đối chiếu

Bản phát hành `1c04cb15c700c5a78c4c89d3be63008af990fd5f` trên GitHub Pages. Kết quả kỹ thuật dùng [mốc phát hành](../docs/RELEASE_BASELINE.md), [bằng chứng lịch sử](../docs/evidence/academic-validation/2026-W48-phase-d-f.md), [ảnh production](../docs/evidence/screenshots/release-1c04cb1/MANIFEST.md) và [ma trận 20 yêu cầu](../docs/TRACEABILITY_MATRIX.md).

| Mục | Trạng thái duyệt |
| --- | --- |
| Nội dung và định dạng | Bản đồng bộ có 40 trang chính, 65 trang tổng. Word cập nhật mục lục, danh mục hình, danh mục bảng và PAGEREF trước khi xuất PDF. |
| Hình, bảng và nguồn | 22 hình, 26 ảnh nhúng, 10 bảng, 17 nguồn. Bảng 7 rộng hơn ở cột tên trường. Hình 8 có nguồn Mermaid điều chỉnh cho A4. |
| HTML | Mở ngoại tuyến, 26 ảnh tải được. Thử mục lục, bàn phím, CSS in và bốn kích thước vùng hiển thị. |
| Hồ sơ bảo vệ | 15 slide có ghi chú, PDF 15 trang, kịch bản 14 thao tác và 38 câu hỏi. Có bước chuẩn bị và phương án tại máy. |
| Kết quả kỹ thuật | CI đúng SHA ghi nhận 14 ca tự động đạt và native publish hoàn tất. Chương 4 phân biệt các đợt lịch sử với 52 lượt production cuối và targeted keyboard/touch regression. |
| Siêu dữ liệu | Bản bàn giao ghi tác giả Lê Hiền và để trống người lưu cuối trong Word và PowerPoint. Thông tin công khai được rà soát riêng trong [checklist Phase L](SUBMISSION_CHECKLIST.md). |
| Lịch sử tuần | W48 có báo cáo và commit thực. Khoảng trống trước W48 vẫn được ghi nhận trong ma trận. |

## Thông tin và quyết định cần bổ sung

- Tên trường, khoa, họ tên giảng viên hướng dẫn và địa danh ghi trên bìa.
- Email và số điện thoại sinh viên. Cần đồng ý phạm vi công khai trước khi điền vào tệp chia sẻ.
- Mẫu bìa chính, bìa phụ, trang nhận xét của giảng viên hướng dẫn và thành viên hội đồng.
- Xác nhận tên đề tài chính thức. Tên đề xuất là **XÂY DỰNG WEBSITE GIỚI THIỆU DU LỊCH BIỂN BA ĐỘNG SỬ DỤNG BLAZOR WEBASSEMBLY**. Bản luận văn vẫn dùng tên sản phẩm BA ĐỘNG — Coastal Escape.
- Xác nhận định dạng .DOC/.DOCX, quy ước scr/src và cách kết hợp IEEE với thứ tự từ điển.
- Xác nhận tài khoản cộng tác của giảng viên. GitHub hiện có một chủ sở hữu và không có lời mời đang chờ.
- Xác nhận thời lượng, định dạng slide và yêu cầu nộp bản trình diễn ghi hình nếu có.

## Duyệt bản bàn giao

Mở [DOCX](doc/BA-DONG-Coastal-Escape.docx), [PDF](pdf/BA-DONG-Coastal-Escape.pdf), [HTML](html/index.html) và [PowerPoint](abs/BA-DONG-Coastal-Escape.pptx). Kiểm tra các thông tin hành chính trước khi dùng bản nộp chính thức. Nội dung và liên kết dựa vào [ma trận tuân thủ](../docs/ACADEMIC_COMPLIANCE.md).

Commit đề xuất sau khi hồ sơ được duyệt

~~~text
docs(academic): synchronize thesis and evidence with final UI release
~~~
