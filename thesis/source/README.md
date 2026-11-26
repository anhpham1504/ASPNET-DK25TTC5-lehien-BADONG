# Nguồn tái tạo luận văn

Các tệp Markdown đánh số chứa phần đầu, mở đầu, năm chương, tài liệu tham khảo và phụ lục. `references.json` lưu thư mục nguồn theo thứ tự từ điển. Kết quả kỹ thuật được đối chiếu tại [mốc đóng băng cuối](../../docs/RELEASE_BASELINE.md). Ảnh production dùng bộ gắn SHA `1c04cb1`; 18 ảnh cũ tiếp tục làm bằng chứng lịch sử. Sơ đồ dùng trực tiếp từ [hồ sơ thiết kế](../../docs/diagrams/README.md).

## Dựng lại ở Windows

Cần Python có python-docx, Pillow và Microsoft Word desktop. Chạy từ gốc repository:

```powershell
python thesis/source/build_thesis.py
python thesis/source/export_html.py
& ./thesis/source/export_review.ps1
python -X utf8 thesis/source/verify_review.py
```

Bước dựng thay thế DOCX và biểu ghi tham khảo do script tạo. Bước xuất dùng Word để cập nhật field, lưu và xuất PDF review. Giữ riêng bản đã sửa trực tiếp bằng Word trước khi dựng lại. Script xác minh dùng thêm pypdf và pdfplumber để kiểm khổ giấy, lề, kích thước chữ, số trang, mục lục, caption và tài liệu tham khảo. Tùy chọn `-X utf8` giữ nguyên tên chương tiếng Việt khi PowerShell ghi kết quả kiểm tra vào log. Sau mỗi lần xuất, mở PDF để kiểm trực quan bố cục và dấu tiếng Việt.

Chỉ thị `!figure|đường dẫn|caption` chèn ảnh từ repository, có thể dùng dấu chấm phẩy để ghép nhiều ảnh. Với một ảnh, trường thứ tư tùy chọn quy định chiều cao tối đa theo cm. `!table|caption|tỷ lệ cột` mở bảng có các dòng phân cách bằng dấu gạch đứng. `[@mã-nguồn]` tạo chỉ số theo danh mục. `!toc`, `!lof`, `!lot` và `!refs` tạo các danh mục và nội dung tham khảo. Bìa, chân trang, style và trường Word được cấu hình trong generator.

Bìa và trang nhận xét có trường chờ xác nhận. Danh mục dùng trình bày dạng IEEE với số theo thứ tự từ điển theo PDF môn học. Xác nhận cách đánh số trước khi chốt hồ sơ nộp.

## Dựng lại sơ đồ và slide

Hình 8 có [nguồn Mermaid](diagrams/search-filter-activity.mmd) và PNG trong cùng thư mục. Dùng Mermaid CLI 11.12.0 với thiết lập trong mermaid.json. Các sơ đồ và ảnh kiểm thử khác trỏ đến tệp bằng chứng đã có.

~~~powershell
npx --yes --package @mermaid-js/mermaid-cli@11.12.0 mmdc -i thesis/source/diagrams/search-filter-activity.mmd -o thesis/source/diagrams/search-filter-activity.png -c thesis/source/diagrams/mermaid.json -b white -w 1750 -s 3
node thesis/source/build_slides.mjs
& ./thesis/source/export_slides.ps1
~~~

Trình dựng slide cần Node.js có thể phân giải @oai/artifact-tool. Lượt duyệt dùng thư viện đã có trong runtime Codex và dựng trong bản sao tạm của kho. Bước xuất PDF cần PowerPoint desktop. Bản PowerPoint giữ các hộp chữ, sơ đồ rút gọn và ghi chú ở dạng chỉnh sửa được.

Sau khi xuất cả bốn tệp DOCX, PDF luận văn, PPTX và PDF slide, chạy bước chuẩn hóa bằng môi trường Python có pypdf hỗ trợ ghi XMP. Bước này giữ tác giả đã xác nhận và bỏ trường người lưu cuối của công cụ xuất trong hai tệp Office. Khi dựng lại ở thư mục mới, chạy từ gốc bản sao kho mã nguồn để đường dẫn tương đối tới các ảnh hoạt động.

~~~powershell
python -X utf8 thesis/source/normalize_metadata.py
~~~

Thư viện dựng PPTX có thể ghi tệp inspect.ndjson cạnh bản xuất. Chỉ đưa bản PPTX đã kiểm tra và PDF slide vào hồ sơ. Dùng bản sao kho mã nguồn để giữ riêng tệp đã chỉnh trực tiếp trong Office.
