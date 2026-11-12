# Test plan

## Automated gate

| Check | Command | Result |
| --- | --- | --- |
| Restore | `dotnet restore src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj` | PASS |
| Release build | `dotnet build src/BaDong.CoastalEscape/BaDong.CoastalEscape.csproj -c Release --no-restore` | PASS |
| Tests | No test project exists yet; static UI is covered by the manual matrix below | SKIPPED |

## Manual/browser matrix

1. Open `/`, `/kham-pha`, `/kham-pha/bien-ba-dong`, `/am-thuc`, `/thu-vien`, `/cam-nang`, `/lich-trinh`, and `/lien-he`.
2. Search Explore with both `bien` and `biển`; confirm case/diacritic-insensitive matches and empty state.
3. Use category chips and reset controls.
4. Open gallery lightbox; test Left, Right, Escape, visible close button, and focusable trigger.
5. Open mobile menu; test keyboard Escape, close-on-link, and body scroll lock.
6. Open FAQ and itinerary tabs with keyboard.
7. Refresh a deep link under the GitHub Pages base path.
8. Inspect console and network for runtime errors or failed JSON requests.
9. Check 320/360/390/768/1024/1440px and 200% zoom for horizontal overflow.
10. Enable reduced motion and confirm non-essential animation is suppressed.

## Known verification limitation

This repository has no attached production GitHub Pages URL yet, so production-host and Lighthouse scores remain pending after the first authorized deployment. The workflow is prepared but not run against a remote repository in this session.

## Browser results

- PASS: home and every required content route rendered without console errors.
- PASS: Vietnamese diacritic-insensitive search and category filtering.
- PASS: friendly invalid-slug state.
- PASS: lightbox previous/next/Escape and mobile-menu Escape/body-scroll release.
- PASS: no horizontal overflow at 320, 360, 390, 768, 1024, or 1440 CSS pixels.
- PASS: reduced-motion media query is present and was emulated successfully.
- PENDING DEPLOYMENT: production deep-link refresh, Lighthouse scores, and remote workflow execution.
