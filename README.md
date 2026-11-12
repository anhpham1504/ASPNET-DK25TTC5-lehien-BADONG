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

GitHub Pages publishes only `publish/wwwroot`. The deploy workflow requires the repository name `ba-dong-coastal-escape`, rewrites the base path to `/ba-dong-coastal-escape/`, configures the `404.html` SPA deep-link redirect, resolves the absolute sitemap/robots URL from the repository owner, and adds `.nojekyll`.

Before the first deployment, create or connect a GitHub repository named exactly `ba-dong-coastal-escape`, push `main`, then select **Settings → Pages → Source → GitHub Actions**. Do not deploy from a branch folder. The expected project-site URL is `https://<owner>.github.io/ba-dong-coastal-escape/`.

## Routes

`/`, `/gioi-thieu`, `/kham-pha`, `/kham-pha/{slug}`, `/am-thuc`, `/am-thuc/{slug}`, `/thu-vien`, `/cam-nang`, `/lich-trinh`, `/lien-he`, `/khong-tim-thay`.

## Architecture

`wwwroot/data/*.json` → `ContentService` (cached `HttpClient` deserialization with empty fallbacks) → Razor pages/components → static browser assets. Local responsive image variants live in `wwwroot/images`; `image-manifest.json` records provenance and `image-requirements.json` tracks missing photographs. There is no server runtime, database, authentication, tracking, or fake submission form.

## Documentation

- [Design system](docs/DESIGN_SYSTEM.md)
- [Test plan](docs/TEST_PLAN.md)
- [Content sources](docs/CONTENT_SOURCES.md)
- [Product context](PRODUCT.md)
- [Visual direction](DESIGN.md)

## Image integrity

The published gallery contains only locally stored photographs with a verifiable Wikimedia Commons file page and reuse license. The Ba Động hero and Duyên Hải wind-power image are verified to the named locations. Food images are labeled with their actual capture location; subject-reference photos are never presented as Ba Động photographs. Missing local scenes use an explicit `PENDING` graphic instead of unrelated stock imagery.

SEO is client-rendered and therefore less robust than pre-rendered HTML. A production Lighthouse run requires an authorized GitHub Pages deployment.
