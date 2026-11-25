# Test plan

## Verification policy

Only commands executed in the current review may be marked `PASS`. Historical notes retain their baseline SHA. The [Phase D–F evidence report](evidence/academic-validation/2026-W48-phase-d-f.md) records local browser checks independently of automated data and service checks.

## Automated gate

| Check | Command | Current result |
| --- | --- | --- |
| Restore application | `dotnet restore src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj` | PASS - 25 November 2026 |
| Restore tests | `dotnet restore tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj` | PASS - 25 November 2026 |
| Release build | `dotnet build src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj -c Release --no-restore` | PASS - 0 warnings, 0 errors |
| Automated tests | `dotnet test --project tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj -c Release --no-restore` | PASS - 14 passed, 0 failed, 0 skipped |

## Automated coverage

The test project covers:

1. syntax validation for every JSON document in `wwwroot/data`;
2. deserialization into the production content models;
3. unique IDs across each content collection;
4. unique route slugs for destinations and foods;
5. existence of every referenced local image;
6. required content fields used by the current UI;
7. itinerary destination references resolving to real destination slugs;
8. required provenance for `VERIFIED`, `VERIFIED_REGION`, and `VERIFIED_SUBJECT` images in the manifest;
9. required image metadata exposed by verified destination, food, and gallery content;
10. exact-case, bidirectional coverage between published image files and the image manifest for Linux CI;
11. the `PENDING` destination placeholder policy;
12. `ContentService` behavior for valid JSON, invalid JSON, and HTTP failure.

The first test invocation placed the project path positionally and failed before test discovery because .NET 10 Microsoft Testing Platform requires `--project`. The command shown above is the corrected invocation that completed successfully.

## Manual/browser matrix

1. Open `/`, `/kham-pha`, `/kham-pha/bien-ba-dong`, `/am-thuc`, `/thu-vien`, `/cam-nang`, `/lich-trinh`, and `/lien-he`.
2. Search Explore with both `bien` and `biển`; confirm case/diacritic-insensitive matches and empty state.
3. Use category chips and reset controls.
4. Open gallery lightbox; test Left, Right, Escape, visible close button, and focus restoration.
5. Open mobile menu; test keyboard Escape, close-on-link, focus containment, and body scroll lock.
6. Open FAQ and itinerary tabs with keyboard.
7. Refresh a deep link under the GitHub Pages base path.
8. Inspect console and network for runtime errors or failed JSON requests.
9. Check 320/360/390/768/1024/1440px and 200% zoom for horizontal overflow.
10. Enable reduced motion and confirm non-essential animation is suppressed.

## Historical browser notes

Phase C exercised 48 production route/viewport combinations against baseline `955956b`. Invalid destination rendered the error body with an empty document title. Phase D reproduced the defect in both environments, then ran 28 local route/viewport combinations for the changed title logic and error-state controls. Two controlled 503 cases exercised loading and empty-data titles. The [traceability matrix](TRACEABILITY_MATRIX.md) links individual cases to source and evidence.

## Remaining verification scope

- Re-run affected title cases against production when a release of the local fix is authorized.
- Extend accessibility coverage to contrast, 200% zoom and screen readers. See the [known limitations](KNOWN_LIMITATIONS.md).
- Record Lighthouse or other performance results only after running the named tool against a documented URL and configuration.
