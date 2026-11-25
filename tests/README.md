# Tests

`BaDong.CoastalEscape.Tests` is the automated test project for repository data integrity and `ContentService` behavior. It targets `net10.0`, references the production project, and uses xUnit.net v3 with Microsoft Testing Platform.

Run it from the repository root:

```powershell
dotnet restore tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj
dotnet test --project tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj -c Release --no-restore
```

The copied test inputs come directly from `src/BaDong.CoastalEscape/wwwroot/data` and `wwwroot/images` at build time. The detailed automated coverage and the separate manual browser matrix are maintained in [`docs/TEST_PLAN.md`](../docs/TEST_PLAN.md).
