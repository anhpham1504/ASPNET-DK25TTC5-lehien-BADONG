# Checklist nghiệm thu và nộp đồ án

Ngày kiểm tra 26/11/2026. Bộ hồ sơ đối chiếu với bản phát hành `1c04cb15c700c5a78c4c89d3be63008af990fd5f`. [Mốc phát hành](../docs/RELEASE_BASELINE.md) · [Ma trận tuân thủ](../docs/ACADEMIC_COMPLIANCE.md)

## Kết quả kiểm tra

| Mục | Trạng thái | Bằng chứng hoặc điều kiện còn lại |
| --- | --- | --- |
| Nội dung và số trang | PASS | Word và PDF có 40 trang nội dung chính (yêu cầu 30–50) trên 66 trang. Mở đầu và Chương 1–5 lần lượt 3, 4, 7, 13, 11 và 2 trang. |
| Định dạng luận văn | PASS | A4, Times New Roman 13 pt ở thân bài, cách dòng 1,5, cách đoạn 6 pt, lề trái 3 cm, các lề còn lại 2 cm. Số trang góc phải dưới. Heading theo cấp, đánh số chương và mục bằng số Ả Rập, mục lục và hai danh mục được cập nhật bằng Word. |
| Hình, bảng và nguồn | PASS | 22 hình, 26 ảnh nhúng, 10 bảng, 17 nguồn được trích dẫn. Kiểm tra caption, thứ tự và liên kết URL giữa các bản. |
| HTML ngoại tuyến | PASS | 26 ảnh dùng đường dẫn tương đối. Dùng được mục lục, phím Tab và CSS in. Bốn chiều rộng 320, 390, 768 và 1.440 px không tràn ngang. |
| PowerPoint và PDF slide | PASS | 15 slide 16:9. Mỗi slide có ghi chú. PowerPoint desktop xuất được PDF 15 trang. |
| Nội dung demo và câu hỏi | PASS | Có kịch bản 14 bước và 38 câu hỏi. Đã thử các thao tác chính trên Pages. [Kịch bản](abs/DEMO_SCRIPT.md) ghi lệnh và phương án dự phòng tại máy. |
| Hướng dẫn cài đặt và hồ sơ thiết kế | PASS | Có [cài đặt](../setup/README.md), [thiết kế](../docs/SOFTWARE_DESIGN.md), [9 sơ đồ](../docs/diagrams/README.md), [20 yêu cầu truy vết](../docs/TRACEABILITY_MATRIX.md), 18 ảnh lịch sử và [13 ảnh production](../docs/evidence/screenshots/release-1c04cb1/MANIFEST.md). |
| Dựng lại tài liệu | PASS | Dựng lại Mermaid, DOCX, PDF, HTML, PPTX và PDF slide trong bản clone, cập nhật trường Word và chuẩn hóa metadata. [Hướng dẫn](source/README.md). |
| Bản phát hành và kiểm thử | PASS | CI 45738100708 và Pages 45738100919 thành công cùng SHA `1c04cb1`. CI ghi 14 ca đạt và native publish hoàn tất; production có 52 lượt route/viewport đạt. |
| Thư mục và báo cáo tuần | PARTIAL | Cấu trúc hồ sơ và báo cáo W48 có sẵn. Lịch sử vẫn có khoảng trống trước W48. |
| Siêu dữ liệu bản bàn giao | PASS | Author là Lê Hiền. Word và PowerPoint bỏ trường Last Modified By. PDF slide dùng tiêu đề BA ĐỘNG — Coastal Escape — Báo cáo bảo vệ và tác giả Lê Hiền. |
| Công khai tệp | DEFERRED | Kho mã nguồn ở chế độ public. README tại SHA hiện hành đã có tên và MSSV. Hồ sơ mới lặp lại các trường này trên bìa và slide, nên cần duyệt phạm vi công khai trước khi push. Email và điện thoại vẫn để trường chờ. |

## Kết luận nghiệm thu

| Phạm vi | Trạng thái |
| --- | --- |
| Hoàn thành kỹ thuật | PASS |
| Nội dung luận văn | PASS |
| Bộ tài liệu bảo vệ | PASS |
| Hồ sơ kỹ thuật và học thuật | PASS |
| Tuân thủ hành chính | PARTIAL |
| Sẵn sàng nộp chính thức | NOT READY |

PASS là đã xác minh. PARTIAL là mới đạt một phần. MISSING là chưa có. DEFERRED là còn cần quyết định hoặc phê duyệt. BLOCKED là điều kiện đang chặn việc nộp hoặc công bố.

## Điều kiện hành chính còn mở

| Hạng mục | Trạng thái | Điều cần xác nhận |
| --- | --- | --- |
| Trường | MISSING | Tên dùng trên bìa. |
| Khoa | MISSING | Tên khoa hoặc đơn vị đào tạo. |
| GVHD | MISSING | Họ tên chính thức. |
| Địa danh | MISSING | Địa danh in trên bìa. |
| Email sinh viên | MISSING | Địa chỉ và phạm vi được phép sử dụng. |
| Điện thoại sinh viên | MISSING | Số liên hệ và phạm vi được phép sử dụng. |
| Mẫu bìa | MISSING | Mẫu chính thức cho bìa chính và bìa phụ. |
| Mẫu nhận xét | MISSING | Mẫu cho GVHD và thành viên hội đồng. |
| Collaborator | MISSING | Kho hiện có một chủ sở hữu và không có lời mời đang chờ. Xác nhận tài khoản và quyền trước khi mời. |
| Tên đề tài chính thức | DEFERRED | Tên trên slide có nhãn đề xuất. Bản luận văn mang tên sản phẩm BA ĐỘNG — Coastal Escape. |
| DOC/DOCX | DEFERRED | PDF quy định ghi .DOC. Xác nhận có chấp nhận .DOCX. |
| PPT/PPTX | DEFERRED | PDF quy định nêu .PPT. Xác nhận có chấp nhận .PPTX và có cần bản ghi trình diễn. |
| src/scr | DEFERRED | PDF ghi scr. Kho dùng src theo phạm vi đã chốt. |
| Quy tắc tài liệu tham khảo | PARTIAL | Bản duyệt dùng dạng IEEE với số theo thứ tự từ điển. Xin xác nhận cách áp dụng. |
| Bản nộp chính thức | BLOCKED | Chờ các mẫu, thông tin bắt buộc, quyền cộng tác và xác nhận định dạng. |

## Phạm vi commit học thuật

Người dùng đã phê duyệt nghiệm thu kỹ thuật Phase L và cho phép commit local. Việc push lên kho public còn chờ xác nhận đồng ý công khai hồ sơ. Trạng thái nộp chính thức vẫn là NOT READY.

Danh sách 45 tệp trong phạm vi commit học thuật gồm cả thay đổi đã có ở checkpoint K.

| Thư mục | Tệp |
| --- | --- |
| Gốc | README.md |
| docs | ACADEMIC_COMPLIANCE.md, KNOWN_LIMITATIONS.md, RELEASE_BASELINE.md |
| progress-report | 2026-W48.md |
| thesis | README.md, REVIEW_CHECKLIST.md, SUBMISSION_CHECKLIST.md |
| thesis/doc | README.md, BA-DONG-Coastal-Escape.docx |
| thesis/pdf | README.md, BA-DONG-Coastal-Escape.pdf |
| thesis/html | README.md, index.html, styles.css |
| thesis/abs | README.md, BA-DONG-Coastal-Escape.pptx, BA-DONG-Coastal-Escape-Slides.pdf, DEMO_SCRIPT.md, QA_PREPARATION.md |
| thesis/refs | README.md, REFERENCES.md, references.bib, sources/README.md |
| thesis/source | README.md, 00-front.md, 10-introduction.md, 20-overview.md, 30-theory.md, 40-implementation.md, 50-results.md, 60-conclusion.md, 70-references.md, 80-appendices.md, references.json, build_thesis.py, export_review.ps1, verify_review.py, export_html.py, build_slides.mjs, export_slides.ps1, normalize_metadata.py |
| thesis/source/diagrams | mermaid.json, search-filter-activity.mmd, search-filter-activity.png |

~~~text
docs(academic): synchronize thesis and evidence with final UI release
~~~
