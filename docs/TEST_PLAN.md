# Test plan

## Verification policy

Only commands executed in the current review may be marked `PASS`. Historical notes retain their baseline SHA. The [Phase D–F evidence report](evidence/academic-validation/2026-W48-phase-d-f.md) records local browser checks independently of automated data and service checks.

## Automated gate

| Check | Command | Current result |
| --- | --- | --- |
| Restore application | `dotnet restore src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj` | PASS - 26 November 2026 |
| Restore tests | `dotnet restore tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj` | PASS - 26 November 2026 |
| Release build | `dotnet build src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj -c Release --no-restore` | PASS - 0 warnings, 0 errors |
| Automated tests | `dotnet test --project tests/BaDong.CoastalEscape.Tests/BaDong.CoastalEscape.Tests.csproj -c Release --no-restore` | PASS - 14 passed, 0 failed, 0 skipped |

The final product SHA `c992fda52dd0cb888b2bde5700e14f3628b38d3e` passed the same Release build and 14-test gate in [CI run 45745648779](https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG/actions/runs/45745648779). The workflow also completed `wasm-tools` installation, native relinking, native asset compilation and `wasm-opt`.

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

The UI release-candidate review later compared 126 local and 126 production combinations before the final itinerary correction. Those historical runs are not reported as if they ran on the final SHA.

## Production regression — 26 November 2026

Chrome Headless 158 ran a fresh 13-route × 4-viewport matrix against deployed SHA `1c04cb1`, for 52 cases. All cases reached the intended UI route with one title, the expected main heading, no horizontal overflow, no broken images, and no failed CSS, script, image, JSON or WebAssembly request. Forty-eight direct deep-link documents initially returned GitHub Pages HTTP 404 and then recovered through the expected SPA fallback; the four homepage cases returned HTTP 200.

Targeted interaction groups also passed for search with and without Vietnamese accents, filter `aria-pressed`, empty-state reset, mobile menu focus and Escape, landscape menu scrolling, touch gallery captions, lightbox focus and restoration, FAQ, Google Maps href, header themes and itinerary tabs. Every itinerary `aria-controls` target existed; inactive panels were `hidden`; the active panel had `aria-labelledby`; `aria-selected` and roving `tabindex` moved with ArrowLeft, ArrowRight, Home and End. Tab and Shift+Tab remained available, and navigation keys did not change page scroll position.

The final hotfix SHA `c992fda` received targeted desktop and mobile checks for the share button rather than a repeat of the 52-case matrix. Normal, hover, focus, copied, touch, Enter and Space states passed; clipboard content matched the current URL and keyboard activation did not move the page. Rendered contrast was 11.91:1 for normal/copied and 8.31:1 for hover. The production CSS, PageTitle and console were also checked.

The 13-image release set remains indexed in the [release evidence manifest](evidence/screenshots/release-1c04cb1/MANIFEST.md). The affected destination screenshot after the hotfix is indexed in the [`c992fda` manifest](evidence/screenshots/hotfix-c992fda/MANIFEST.md).

## Remaining verification scope

- Run Firefox and WebKit when their Playwright binaries are available.
- Run axe-core, real browser zoom 200%, screen-reader and full-site contrast audits. See the [known limitations](KNOWN_LIMITATIONS.md).
- Record Lighthouse or other performance results only after running the named tool against a documented URL and configuration.
