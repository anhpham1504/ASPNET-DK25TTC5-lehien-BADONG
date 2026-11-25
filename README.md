# BA ĐỘNG — Coastal Escape

An editorial-style, static travel guide to Ba Động built with .NET 10 Blazor WebAssembly Standalone, C#, Razor, CSS, and public JSON.

## Run locally

```powershell
dotnet restore src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj
dotnet run --project src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj
```

Open the HTTPS URL printed by the dev server. Development uses `<base href="/" />`.

## Build and publish

```powershell
dotnet build src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj -c Release
dotnet publish src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj -c Release -o ./publish
```

GitHub Pages publishes only `publish/wwwroot` from the repository `ASPNET-DK25TTC5-lehien-BADONG`. The deploy workflow rewrites the base path to `/ASPNET-DK25TTC5-lehien-BADONG/`, configures the `404.html` SPA deep-link redirect, resolves the absolute sitemap/robots URL from the repository owner, and adds `.nojekyll`.

The existing repository was renamed in place after explicit release approval; Git history, the `main` branch, project names, and namespaces were preserved. See the [repository rename record](docs/REPOSITORY_RENAME_PLAN.md) for impact, rollback, and acceptance criteria.

## Routes

`/`, `/gioi-thieu`, `/kham-pha`, `/kham-pha/{slug}`, `/am-thuc`, `/am-thuc/{slug}`, `/thu-vien`, `/cam-nang`, `/lich-trinh`, `/lien-he`, `/khong-tim-thay`.

## Architecture

`wwwroot/data/*.json` → `ContentService` (cached `HttpClient` deserialization with empty fallbacks) → Razor pages/components → static browser assets. Local responsive image variants live in `wwwroot/images`; `image-manifest.json` records provenance and `image-requirements.json` tracks missing photographs. There is no server runtime, database, authentication, tracking, or fake submission form.

## Documentation

- [Academic compliance matrix](docs/ACADEMIC_COMPLIANCE.md)
- [Repository rename plan](docs/REPOSITORY_RENAME_PLAN.md)
- [Setup and local verification](setup/README.md)
- [Weekly progress reports](progress-report/README.md)
- [Thesis workspace](thesis/README.md)
- [Design system](docs/DESIGN_SYSTEM.md)
- [Test plan](docs/TEST_PLAN.md)
- [Software design and data dictionary](docs/SOFTWARE_DESIGN.md)
- [Traceability matrix](docs/TRACEABILITY_MATRIX.md)
- [Rendered diagrams](docs/diagrams/README.md)
- [Technical evidence and screenshots](docs/evidence/README.md)
- [Known limitations](docs/KNOWN_LIMITATIONS.md)
- [Thesis plan](thesis/THESIS_PLAN.md)
- [Verified release and feature freeze](docs/RELEASE_BASELINE.md)
- [Thesis review files](thesis/README.md) in [DOCX](thesis/doc/BA-DONG-Coastal-Escape.docx), [PDF](thesis/pdf/BA-DONG-Coastal-Escape.pdf), and [offline HTML](thesis/html/index.html)
- [Defense presentation and demo](thesis/abs/README.md) and [submission checklist](thesis/SUBMISSION_CHECKLIST.md)
- [Content sources](docs/CONTENT_SOURCES.md)
- [Product context](PRODUCT.md)
- [Visual direction](DESIGN.md)

## Demo

- [GitHub Pages project site](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/)

Availability depends on the latest authorized GitHub Pages deployment. Local setup remains the reproducible verification path.

## Thông tin đồ án

| Thông tin | Nội dung |
| --- | --- |
| Tên đề tài | BA ĐỘNG — Coastal Escape |
| Môn học | Chuyên đề ASP.NET |
| Sinh viên thực hiện | Lê Hiền |
| Mã sinh viên | 170125405 |
| Mã lớp | DK25TTC5 |
| Repository | ASPNET-DK25TTC5-lehien-BADONG |
| Email | Chưa cung cấp |
| Điện thoại | Chưa cung cấp |
| Giảng viên hướng dẫn | Chưa xác nhận |

## Image integrity

The published gallery contains only locally stored photographs with a verifiable Wikimedia Commons file page and reuse license. The Ba Động hero and Duyên Hải wind-power image are verified to the named locations. Food images are labeled with their actual capture location; subject-reference photos are never presented as Ba Động photographs. Missing local scenes use an explicit `PENDING` graphic instead of unrelated stock imagery.

SEO is client-rendered. The GitHub Pages deep-link fallback restores the route in the browser after an initial HTTP 404. The verified release records the deployed title fix and the remaining limitations.
