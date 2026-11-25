# Setup and verification

## Prerequisites

- .NET SDK `10.0.100` or a compatible .NET 10 feature band allowed by `global.json`.
- Git.
- A modern browser for manual UI checks.
- The WebAssembly build tools workload only when publishing with native relinking.

Verify the selected SDK from the repository root:

```powershell
dotnet --version
```

The result must resolve to .NET 10 and satisfy `global.json`.

## Restore

```powershell
dotnet restore src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj
dotnet restore tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj
```

## Run locally

```powershell
dotnet run --project src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj
```

Open the HTTPS URL printed by the development server. Local development uses `<base href="/" />`.

## Build and test

```powershell
dotnet build src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj -c Release --no-restore
dotnet test --project tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj -c Release --no-restore
```

The automated tests validate static content, image paths, provenance policies, route references, and `ContentService` error handling. Browser interactions remain in the manual matrix in [`docs/TEST_PLAN.md`](../docs/TEST_PLAN.md).

## Publish locally

Install the workload used by CI for native relinking:

```powershell
dotnet workload install wasm-tools --skip-manifest-update
dotnet publish src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj -c Release -o publish -p:WasmBuildNative=true -p:RunAOTCompilation=false
```

The GitHub Pages workflow performs additional base-path, SPA fallback, sitemap, robots, and `.nojekyll` configuration. Do not treat a plain local `publish` directory as the final Pages artifact.

## Configuration and data

- Application content: `src/BaDong.CoastalEscape/wwwroot/data`.
- Local images: `src/BaDong.CoastalEscape/wwwroot/images`.
- No application secrets, database, authentication provider, or server environment variables are required.
- Do not add credentials or private data to the repository.
