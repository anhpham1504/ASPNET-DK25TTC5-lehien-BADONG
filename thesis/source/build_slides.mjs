import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const output = process.argv[2] || path.join(root, "thesis", "abs", "BA-DONG-Coastal-Escape.pptx");
const evidence = "docs/evidence/screenshots";
const production = "https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/";
const release = "463da372613648411ef9d6002c4d895cb03cbb4d";
const repo = "https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG";
const ci = repo + "/actions/runs/45546387181";
const pages = repo + "/actions/runs/45546387162";
const serviceFile = "src/BaDong.CoastalEscape/Services/ContentService.cs";
const color = { dark:"#103C46", ink:"#172B31", white:"#FFFFFF", sand:"#F9F5EB",
  muted:"#4B6266", pale:"#E3EEEB", line:"#C3D4D0", accent:"#A45B2D", warm:"#F0BB84" };
const deck = Presentation.create({ slideSize:{ width:1280, height:720 } });
const margin = 76;

function box(s, left, top, width, height, fill, geometry = "rect") {
  return s.shapes.add({ geometry, position:{ left, top, width, height }, fill, line:{fill:"none",width:0} });
}
function txt(s, value, x, y, w, h, size, fill = color.ink, bold = false, typeface = "Arial") {
  const shape = box(s,x,y,w,h,"none","textbox");
  shape.text = value;
  shape.text.style = {typeface,fontSize:size+"pt",color:fill,bold,verticalAlignment:"top",wrap:"square",insets:0};
  return shape;
}
function rule(s,x,y,w,fill=color.line) { box(s,x,y,w,2,fill); }
function page(title, subtitle) {
  const s=deck.slides.add();
  s.background.fill=color.sand;
  box(s,margin,52,56,5,color.accent);
  txt(s,title,margin,79,1128,62,34,color.dark,true);
  if (subtitle) txt(s,subtitle,margin,148,1128,50,19,color.muted);
  return s;
}
function note(s, seconds, narration, sources) {
  s.speakerNotes.text="Thời lượng gợi ý "+seconds+" giây.\n\n"+narration
    +"\n\nNguồn đối chiếu\n"+sources.join("\n");
}
async function photo(s,file,alt,left,top,width,height,fit="contain") {
  const blob=await fs.readFile(path.join(root,file));
  s.images.add({blob,contentType:file.endsWith(".jpg")?"image/jpeg":"image/png",alt,fit,position:{left,top,width,height}});
}
async function shot(s,file,caption,x,y,w,h) {
  box(s,x,y,w,h,color.pale);
  await photo(s,evidence+"/"+file,caption,x+2,y+2,w-4,h-4);
  txt(s,caption,x,y+h+12,w,40,17,color.dark,true);
}
function row(s,label,detail,y,x=margin,w=1128,labelW=305) {
  rule(s,x,y,w);
  txt(s,label,x,y+16,labelW-20,70,23,color.dark,true);
  txt(s,detail,x+labelW,y+18,w-labelW,74,19,color.muted);
}
function rows(title,subtitle,content,seconds,narration,sources) {
  const s=page(title,subtitle);
  const start=subtitle?213:197;
  content.forEach(([label,detail],i)=>row(s,label,detail,start+i*(content.length===3?124:106)));
  note(s,seconds,narration,sources);
}
function block(s,heading,detail,x,y,w,h=132,fill=color.pale) {
  box(s,x,y,w,h,fill);
  txt(s,heading,x+18,y+18,w-36,40,22,color.dark,true);
  txt(s,detail,x+18,y+68,w-36,h-68,17);
}

{
  const s=deck.slides.add();
  s.background.fill=color.dark;
  await photo(s,"src/BaDong.CoastalEscape/wwwroot/images/locations/ba-dong-beach-1600.jpg",
    "Biển Ba Động nhìn từ bờ kè. Ảnh Baoothersks, CC BY 4.0.",688,0,592,720,"cover");
  box(s,76,84,72,5,color.warm);
  txt(s,"Chuyên đề ASP.NET",76,108,560,45,20,color.warm,true);
  txt(s,"BA ĐỘNG",76,166,600,93,55,color.white,true);
  txt(s,"Coastal Escape",76,263,585,55,33,color.white,true);
  txt(s,"Tên đề tài đề xuất · chờ xác nhận",76,370,580,32,16,color.warm,true);
  txt(s,"Xây dựng website giới thiệu du lịch\nBiển Ba Động sử dụng\nBlazor WebAssembly",76,412,575,110,22,color.white);
  txt(s,"Lê Hiền\nMSSV 170125405   Lớp DK25TTC5",76,563,588,90,21,color.white);
  note(s,20,"Giới thiệu sản phẩm BA ĐỘNG — Coastal Escape và phạm vi đồ án Chuyên đề ASP.NET. Tên học thuật là đề xuất chờ giảng viên xác nhận.",[
    "thesis/THESIS_PLAN.md","Ảnh Baoothersks, CC BY 4.0. Ảnh được cắt theo khung trình bày.",
    "https://commons.wikimedia.org/wiki/File:Bi%E1%BB%83n_Ba_%C4%90%E1%BB%99ng,_Tr%C3%A0_Vinh.jpg"]);
}
{
  const s=page("Lý do chọn đề tài","Người chuẩn bị chuyến đi cần tra cứu nhanh thông tin đã có nguồn.");
  txt(s,"Đi đâu?\nĂn gì?\nĐi trong bao lâu?",76,250,510,308,40,color.dark,true);
  row(s,"Thông tin phân tán","Địa điểm, ảnh và gợi ý hành trình nằm ở nhiều nguồn.",242,623,581,242);
  row(s,"Tra cứu trên điện thoại","Cần danh sách rõ, lọc nhanh và đường dẫn dễ mở.",363,623,581,242);
  row(s,"Nguồn ảnh","Người đọc cần biết ảnh minh họa cho địa điểm hay chủ thể nào.",484,623,581,242);
  note(s,35,"Nêu tình huống chuẩn bị chuyến đi. Người đọc muốn xem tổng quan, chọn vài địa điểm và biết mức độ xác minh của ảnh. Chương 1 đối chiếu ba nguồn du lịch công khai.",["thesis/source/20-overview.md","PRODUCT.md"]);
}
rows("Mục tiêu và phạm vi","",[
  ["Cẩm nang du lịch","Tra cứu địa điểm, ẩm thực, ảnh, cẩm nang và lịch trình tham khảo."],
  ["Nội dung có nguồn","Lưu dữ liệu và hồ sơ ảnh trong kho mã nguồn để đối chiếu khi cập nhật."],
  ["Triển khai tĩnh","Blazor WebAssembly chạy trong trình duyệt. GitHub Pages cung cấp tệp."],
  ["Giới hạn nghiệp vụ","Đề tài tập trung vào tra cứu. Đặt chỗ, thanh toán và tài khoản nằm ngoài phạm vi."],
],30,"Giải thích ba mục tiêu gắn với lựa chọn kiến trúc. Lịch trình là gợi ý. Thông tin có thể thay đổi nên người đọc cần đối chiếu nguồn trước chuyến đi.",["PRODUCT.md","docs/TRACEABILITY_MATRIX.md"]);
rows("Yêu cầu chức năng","Các luồng người dùng được hiện thực trong bản đã phát hành.",[
  ["Khám phá địa điểm","Danh sách, tìm kiếm tiếng Việt, lọc danh mục và trang chi tiết."],
  ["Ẩm thực và hình ảnh","Danh sách món, trang món, thư viện và hộp thoại xem ảnh."],
  ["Chuẩn bị chuyến đi","Các câu hỏi thường gặp, hai lịch trình và liên kết bản đồ."],
  ["Phục hồi điều hướng","Thông báo khi thiếu dữ liệu hoặc không tìm thấy trang."],
],30,"Đi từ nhu cầu tra cứu sang nhóm chức năng. Ma trận có 20 yêu cầu thuộc các nhóm chức năng, chất lượng và hồ sơ. Số 20 phản ánh quy mô truy vết.",["docs/TRACEABILITY_MATRIX.md","docs/SOFTWARE_DESIGN.md"]);
rows("Công nghệ sử dụng","",[
  ["Ứng dụng",".NET 10, C#, Blazor WebAssembly và Razor Components."],
  ["Dữ liệu","Tệp JSON tĩnh, HttpClient và System.Text.Json."],
  ["Phát hành","GitHub Actions dựng và kiểm thử. GitHub Pages công bố tài nguyên tĩnh."],
],35,"SDK .NET biên dịch và chuẩn bị gói ứng dụng. Razor định nghĩa cấu trúc, trạng thái và tương tác. Trình duyệt tải bản đã dựng rồi lấy JSON qua HTTP.",["global.json","src/BaDong.CoastalEscape/Program.cs",".github/workflows/ci.yml"]);
{
  const s=page("Kiến trúc hệ thống","Blazor WebAssembly xử lý giao diện ngay trên thiết bị người dùng.");
  box(s,76,215,700,311,color.pale);
  box(s,886,215,318,311,color.pale);
  txt(s,"Trình duyệt",96,237,650,45,24,color.dark,true);
  txt(s,"GitHub Pages",906,237,278,45,24,color.dark,true);
  block(s,"Trang Razor","Router và thành phần giao diện",96,321,263,148,color.white);
  block(s,"ContentService","Bộ nhớ đệm và HttpClient",478,321,277,148,color.white);
  box(s,383,383,72,22,color.accent,"rightArrow");
  txt(s,"HTTP",794,345,86,31,17,color.dark,true);
  box(s,795,383,72,22,color.accent,"rightArrow");
  txt(s,"Máy chủ tệp tĩnh\nHTML, WASM, JSON và ảnh",906,321,268,139,20);
  txt(s,"Khi thiếu dữ liệu trong bộ nhớ đệm, ContentService gửi yêu cầu đọc tệp JSON.",76,561,1114,68,21,color.muted);
  note(s,45,"Sơ đồ rút gọn luồng tải nội dung. Program.cs đăng ký HttpClient với địa chỉ cơ sở và đăng ký ContentService. Router chọn trang trong trình duyệt. GitHub Pages cung cấp tệp JSON và các tệp khởi động ứng dụng.",["docs/diagrams/system-architecture.mmd","src/BaDong.CoastalEscape/Program.cs","src/BaDong.CoastalEscape/Services/ContentService.cs"]);
}
{
  const s=page("Quan hệ dữ liệu JSON","Sáu tệp cung cấp nội dung. Hai tệp theo dõi nguồn ảnh và yêu cầu ảnh.");
  block(s,"itineraries.json","2 lịch trình, mỗi lịch trình có danh sách điểm dừng",76,238,383);
  block(s,"destinations.json","7 địa điểm, mỗi địa điểm có slug và đường dẫn ảnh",814,238,390);
  txt(s,"ItineraryStop.Slug\nkhớp Destination.Slug",498,238,313,75,17,color.dark,true);
  box(s,490,324,291,22,color.accent,"rightArrow");
  rule(s,76,401,1128);
  txt(s,"Đối chiếu ảnh",76,429,256,43,22,color.dark,true);
  txt(s,"Đường dẫn ảnh trong nội dung được đối chiếu với tệp ảnh và danh mục image-manifest.json.",357,429,847,79,20);
  txt(s,"Các tập nội dung khác",76,546,257,81,22,color.dark,true);
  txt(s,"4 món ăn, 7 ảnh thư viện, 5 câu hỏi và 1 đối tượng thông tin chung.",357,546,847,72,20,color.muted);
  note(s,35,"Slug của điểm dừng có thể rỗng. Nếu có giá trị, nó phải khớp slug của một địa điểm. Giải thích danh mục ảnh lưu đường dẫn, biến thể, tác giả, giấy phép và trạng thái. Kiểm thử đối chiếu tên tệp theo đúng chữ hoa thường. Năm địa điểm đang dùng ảnh giữ chỗ.",["src/BaDong.CoastalEscape/Models/SiteModels.cs","src/BaDong.CoastalEscape/wwwroot/data","docs/SOFTWARE_DESIGN.md"]);
}
{
  const s=page("Hiện thực dịch vụ và tìm kiếm");
  const service=await fs.readFile(path.join(root,serviceFile),"utf8");
  const cache=service.match(/^        if \(_cache\.TryGetValue\(path, out var cached\) && cached is IReadOnlyList<T> items\)\r?\n        \{\r?\n            return items;\r?\n        \}/m);
  if(!cache) throw new Error("Đoạn bộ nhớ đệm trong ContentService đã thay đổi");
  const lines=cache[0].split(/\r?\n/).map(line=>line.slice(8));
  lines[0]=lines[0].replace(" && ","\n    && ");
  box(s,76,206,714,326,color.dark);
  txt(s,"ContentService.cs",104,231,650,45,19,color.warm,true);
  txt(s,lines.join("\n"),104,296,657,202,20,color.white,false,"Consolas");
  txt(s,"Tìm kiếm tiếng Việt",834,224,363,51,24,color.dark,true);
  txt(s,"Chuẩn hóa Unicode, bỏ dấu kết hợp và so khớp chuỗi con.",834,294,363,109,20);
  txt(s,"“hoàng hôn” và “hoang hon” cho cùng kết quả. Chữ đ và d vẫn được phân biệt.",834,432,363,154,20,color.muted);
  txt(s,"Đoạn trích từ LoadAsync<T> tại bản phát hành 463da37",76,573,724,52,16,color.muted);
  note(s,45,"Đoạn mã trích trực tiếp từ LoadAsync<T>, xuống dòng điều kiện để dễ chiếu. Nếu chưa có mục đệm, phương thức gọi GetFromJsonAsync. Lỗi đã xử lý trả dữ liệu rỗng và không lưu nhánh lỗi. Tìm kiếm dùng FormD, bỏ NonSpacingMark, FormC và chữ thường.",[serviceFile,"src/BaDong.CoastalEscape/Pages/Explore.razor"]);
}
{
  const s=page("Giao diện chính","Từ trang chủ đến danh sách và chi tiết một điểm đến.");
  await shot(s,"01-home-desktop.png","Trang chủ",76,218,617,386);
  await shot(s,"05-explore.png","Khám phá",764,206,398,194);
  await shot(s,"09-destination.png","Chi tiết Biển Ba Động",764,447,398,194);
  txt(s,"Ảnh kiểm thử của bản Release tại máy phát triển",76,662,640,34,16,color.muted);
  note(s,35,"Dẫn người nghe theo luồng tra cứu. Một số ảnh có viền focus ghi lại trạng thái lúc kiểm thử. Trình diễn trực tiếp dùng bản công khai tương ứng với mốc phát hành.",["docs/evidence/screenshots/MANIFEST.md, ảnh 01, 05 và 09"]);
}
{
  const s=page("Ẩm thực, thư viện và lịch trình","Hai màn hình minh họa cách lọc món và xem thông tin nguồn ảnh.");
  await shot(s,"10-cuisine.png","Ẩm thực và bộ lọc",76,212,549,343);
  await shot(s,"13-gallery-lightbox.png","Thư viện và ghi công ảnh",655,212,549,343);
  txt(s,"Cẩm nang có câu hỏi thường gặp. Mục lịch trình có gợi ý một ngày và hai ngày.",76,620,1128,57,18,color.muted);
  note(s,30,"Nêu các chức năng theo thứ tự từ tìm món, xem ảnh kèm ghi công, mở câu hỏi thường gặp đến chọn lịch trình tham khảo.",["docs/evidence/screenshots/MANIFEST.md, ảnh 10, 13, 14 và 15"]);
}
{
  const s=page("Màn hình hẹp và khả năng tiếp cận");
  await shot(s,"02-home-tablet.png","768 × 900",76,175,318,416);
  await shot(s,"03-home-mobile.png","390 × 844",417,175,220,416);
  txt(s,"Các thao tác đã kiểm tra",688,205,515,53,25,color.dark,true);
  txt(s,"Tab và Shift+Tab trong menu\nEscape đóng và trả focus\nPhím mũi tên chuyển ảnh",688,281,512,156,22);
  rule(s,688,450,510);
  txt(s,"Phạm vi đánh giá WCAG 2.2 AA còn mở.",688,475,510,85,19,color.muted);
  note(s,35,"Hai ảnh tương ứng hai vùng hiển thị trong trình duyệt. Đã kiểm các thao tác bàn phím chọn lọc với menu, hộp thoại ảnh, FAQ và lịch trình. Kiểm toán đầy đủ, trình đọc màn hình, tương phản và phóng to 200% vẫn còn mở.",["docs/evidence/screenshots/MANIFEST.md, ảnh 02, 03 và 04","docs/KNOWN_LIMITATIONS.md"]);
}
{
  const s=page("Kết quả kiểm thử","Số ca, số lượt và số đường dẫn được báo cáo theo từng đợt.");
  const tests=[
    ["14/14","Kiểm thử tự động","Dữ liệu và dịch vụ"],
    ["48","Lượt phiên bản cơ sở","12 URL × 4 chiều rộng"],
    ["28","Lượt sửa tiêu đề","7 URL × 4 chiều rộng"],
    ["2","Ca HTTP 503","Mô phỏng khi tải JSON"],
    ["7/7","Tiêu đề bản công khai","Sau khi Blazor khởi động"],
  ];
  tests.forEach(([count,label,details],i)=>{
    const x=76+i*228;
    rule(s,x,253,210,color.accent);
    txt(s,count,x,282,212,94,47,color.dark,true);
    txt(s,label,x,392,214,88,20,color.ink,true);
    txt(s,details,x,489,210,92,17,color.muted);
  });
  note(s,45,"14 ca tự động kiểm tra dữ liệu và dịch vụ. 48 và 28 là lượt trình duyệt theo hai ma trận. Hai phản hồi 503 do bộ kiểm thử tạo trên bản local. Bảy tiêu đề thuộc lần kiểm tra sau triển khai. Mỗi kết quả có phạm vi riêng.",["docs/evidence/academic-validation/2026-W48-phase-d-f.md","docs/RELEASE_BASELINE.md",ci]);
}
{
  const s=page("CI/CD và triển khai","Hai workflow nhận cùng commit và chạy độc lập.");
  block(s,"main · 463da37","Commit phát hành",76,314,301,136);
  box(s,395,365,86,22,color.accent,"rightArrow");
  box(s,484,279,3,198,color.accent);
  box(s,487,279,49,18,color.accent,"rightArrow");
  box(s,487,459,49,18,color.accent,"rightArrow");
  block(s,"CI · 45546387181","Restore, build Release và kiểm thử tự động.",551,216,653,136);
  block(s,"Pages · 45546387162","Publish, thiết lập đường dẫn cơ sở và triển khai gói tĩnh.",551,396,653,136);
  txt(s,"Cả hai lần chạy thành công. CI ghi nhận 14/14 ca kiểm thử đạt.",76,581,1128,63,20,color.muted);
  note(s,40,"Mở trang kết quả CI và Pages để đối chiếu SHA. Hai workflow chạy độc lập. Job deploy của Pages sử dụng gói do job build của chính workflow đó tạo.",["Release SHA "+release,ci,pages,"docs/RELEASE_BASELINE.md"]);
}
{
  const s=page("Trình diễn và giới hạn");
  txt(s,"Luồng trình diễn",76,207,505,56,27,color.dark,true);
  txt(s,"Tìm và lọc địa điểm\nMở chi tiết và xem nguồn ảnh\nXem món, ảnh và lịch trình",76,284,515,173,23);
  txt(s,"Giới hạn của bản phát hành",655,207,545,56,27,color.dark,true);
  txt(s,"URL sâu nhận 404 ở phản hồi đầu\nDữ liệu đọc từ các tệp tĩnh\n5 địa điểm còn chờ xác minh ảnh",655,284,535,173,22);
  rule(s,76,497,1128,color.accent);
  const url=txt(s,production,76,532,1128,52,19,color.dark,true);
  url.text.get(production).hyperlink={uri:production,isExternal:true};
  note(s,280,"Thực hiện các thao tác trong DEMO_SCRIPT.md. Mở trước website, kho mã nguồn và terminal. Nếu mất mạng, dùng bản Release đã dựng tại máy hoặc dùng ảnh có ghi nguồn. Chỉ gọi ca test là chạy trực tiếp khi lệnh đã in kết quả.",[production,"thesis/abs/DEMO_SCRIPT.md","docs/KNOWN_LIMITATIONS.md"]);
}
{
  const s=deck.slides.add();
  s.background.fill=color.dark;
  box(s,76,72,70,5,color.warm);
  txt(s,"Kết luận và hướng phát triển",76,106,1128,79,37,color.white,true);
  txt(s,"Cẩm nang Ba Động có kiến trúc tĩnh,\nluồng tra cứu và bằng chứng kiểm thử truy vết được.",76,215,1120,125,29,color.white);
  rule(s,76,385,1128,"#517078");
  txt(s,"Khảo sát kết xuất trước cho URL sâu\nBổ sung ảnh có nguồn phù hợp\nMở rộng kiểm tra khả năng tiếp cận",76,420,1128,150,22,color.white);
  txt(s,"Trao đổi và câu hỏi",76,622,1128,66,25,color.warm,true);
  note(s,30,"Kết lại bằng kết quả đã làm được và ba hướng khảo sát sau nghiệm thu. Khi trao đổi, nhớ nêu phạm vi HTTP 404, tìm kiếm đ/d và đánh giá tiếp cận.",["thesis/source/60-conclusion.md","thesis/abs/QA_PREPARATION.md"]);
}
await fs.mkdir(path.dirname(output),{recursive:true});
await (await PresentationFile.exportPptx(deck)).save(output);
console.log(deck.slides.items.length+" slides with speaker notes");
