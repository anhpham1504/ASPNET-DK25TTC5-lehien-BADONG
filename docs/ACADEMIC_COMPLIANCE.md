# Academic compliance matrix

This matrix compares the repository with `QUY_DINH_CHUNG_ASP.net.pdf`. It records evidence through 26 November 2026 and separates mandatory PDF requirements from engineering improvements.

Status values: `PASS`, `PARTIAL`, `MISSING`, `DEFERRED`, and `BLOCKED`.

## Phase 0 baseline

| Requirement | Source | Status before Phase 1 | Direct evidence |
| --- | --- | --- | --- |
| Git repository used to manage the project | PDF, mandatory | PASS | Git repository on branch `main`, remote `origin`, HEAD `46ba776893ba29445855080a5a6004c9e6ae0626`. |
| Repository naming convention | PDF, mandatory | MISSING | Verified GitHub repository name is `ba-dong-coastal-escape`, not the required academic form. |
| Supervisor invited as collaborator | PDF, mandatory | MISSING | GitHub reports only owner `anhpham1504` as collaborator and no pending invitations. No invitation was sent. |
| Maintained root README | PDF, mandatory | PARTIAL | Run, build, routes, architecture, and source notes existed; academic links and author contact fields were absent. |
| Commit at least weekly | PDF, mandatory | MISSING | Verified history contains commits on 12 and 14 November 2026 only; history was not rewritten. |
| Weekly `progress-report` directory | PDF, mandatory | MISSING | Directory did not exist at Phase 0. |
| Source and test data directory | PDF, mandatory intent | PARTIAL | Source and static data existed under `src`; `src` is retained by task constraint. |
| `thesis` directory with `doc`, `pdf`, `html`, `abs`, `refs` | PDF, mandatory | MISSING | Directory did not exist at Phase 0. |
| Thesis body and prescribed formatting | PDF, mandatory for submission | MISSING | No thesis artifact existed. Writing the thesis is outside this phase. |
| Root author email and phone | PDF, mandatory | MISSING | No author contact information existed. Real author data is intentionally deferred. |
| `setup` guidance | PDF, suggested structure | MISSING | No `setup` directory existed. |
| Automated tests | Engineering improvement | MISSING | `tests/README.md` stated that no automated test project existed. |

## Final academic acceptance and submission status

| Requirement | Status | Evidence |
| --- | --- | --- |
| Maintained root README | PARTIAL | Academic documentation, setup, progress, thesis, test, demo, and rename-plan links are present. Verified student name, ID, and class are recorded; email, phone, and supervisor remain explicitly unavailable. |
| Weekly `progress-report` directory | PASS | Index, reusable template, and an evidence-based report for ISO week 48 are present. |
| Commit at least weekly | PARTIAL | Week 48 work is documented and committed with real timestamps, but the earlier gap cannot be repaired retroactively. |
| Thesis repository structure | PASS | Required subdirectories are represented by tracked README files. |
| Thesis body and formatting | PARTIAL | The [DOCX review](../thesis/doc/BA-DONG-Coastal-Escape.docx) includes the front matter, introduction, five chapters, references and appendices. The [PDF review](../thesis/pdf/BA-DONG-Coastal-Escape.pdf) was rendered for review. Official form and submission-format checks remain open. |
| Main-content extent and review layout | PASS | [Review QA](../thesis/pdf/README.md) measures 40 A4 main-content pages out of 65 total. Layout, pagination, all TOC/PAGEREF entries, figure/table lists and references were checked on the synchronized export. |
| Root author email and phone | DEFERRED | Placeholders only, as required by the task. |
| `setup` guidance | PASS | Reproducible SDK, restore, build, run, test, and publish guidance is present. |
| Automated tests | PASS | Test project and CI gate are present; the verified Release run passed 14 tests with no failures or skips, including exact-case image-manifest coverage and rendered image metadata. |
| Repository naming convention | PASS | The existing repository was renamed in place to `ASPNET-DK25TTC5-lehien-BADONG` after explicit approval; history and `main` were preserved. |
| Supervisor invited as collaborator | MISSING | Only the owner is a collaborator and no invitation is pending. The PDF email is recorded as an invitation target only; sending it is a remote permission change requiring approval. |
| Source directory spelling | DEFERRED | `src` is intentionally retained. The PDF says `scr`, but changing a conventional source directory without instructor confirmation would add risk and is explicitly out of scope. |
| Student identity | PARTIAL | Name `Lê Hiền`, student ID `170125405`, and class `DK25TTC5` are verified from the task. Email and phone were not supplied; supervisor identity is unconfirmed. |
| Software design documentation | PASS | [Design and data dictionary](SOFTWARE_DESIGN.md), [nine editable/rendered diagrams](diagrams/README.md) and [traceability](TRACEABILITY_MATRIX.md). |
| Technical evidence for thesis | PASS | Historical local evidence and the [production screenshot set for `1c04cb1`](evidence/screenshots/release-1c04cb1/MANIFEST.md) are recorded separately. |
| Thesis plan and source list | PASS | The [38-page target](../thesis/THESIS_PLAN.md) maps chapters to evidence. [Editable source](../thesis/source/README.md) and [bibliography](../thesis/refs/REFERENCES.md) accompany the review. |
| Official covers and review pages | MISSING | Main/secondary cover and GVHD/TVHĐ review templates still need confirmation. |
| Thesis exports and slides | PARTIAL | DOCX, PDF, offline HTML, editable 15-slide PowerPoint, PDF slides, demo script and defense questions are available for local review. The final submission template and formats remain open. See the [review checklist](../thesis/REVIEW_CHECKLIST.md). |
| Technical completion | PASS | The final frozen release `1c04cb1` passed CI, native publish and 14 automated tests; Pages deployed the same SHA. |
| Thesis content | PASS | The validated final outline has an introduction, five chapters, references and appendices. The main text uses 40 of 65 pages; the footer-only page between the figure and table lists has been removed. |
| Presentation package | PASS | The 15-slide PowerPoint and its PDF open, with an editable deck and speaker notes. The demo script and defense questions are available for review. |
| Documentation | PASS | The setup guide, software design, evidence, progress report, traceability, and document build instructions are present. |
| Administrative compliance | PARTIAL | The student identity is confirmed. Official templates, supervisor and institution details, contact information, collaborator status and submission-format decisions remain open. |
| Submission readiness | BLOCKED | The [submission checklist](../thesis/SUBMISSION_CHECKLIST.md) records NOT READY while mandatory administrative items are open. |
| Personal information in the public repository | DEFERRED | The reviewed files retain confirmed identity fields for academic review. Approve the publication scope before pushing the package. |
| Accepted editable format | DEFERRED | PDF says `.DOC`. Confirm whether the reviewer accepts `.DOCX`. |
| Reference numbering | PARTIAL | The review uses IEEE-style numbered references sorted alphabetically by author or organization, then title. Confirm the numbering convention for the final submission. |

## Verified repository and GitHub state

| Item | Observed state through 26 November 2026 |
| --- | --- |
| Branch and baseline | `main`; pre-compliance HEAD `46ba776893ba29445855080a5a6004c9e6ae0626` remains in history |
| Academic commit | `30bd3cb812784be12c161a9300673c6f713e67e0` |
| Remote | `https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG.git` |
| Visibility and access | Public repository; authenticated viewer has `ADMIN` permission |
| GitHub Pages | [Production](https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/) serves the verified release at `1c04cb1`. Initial direct deep links still return HTTP 404 in the observed cases. |
| Branch protection | `main` is not protected; this is an engineering risk, not a PDF requirement |
| Actions | Enabled; allowed-actions policy is `all` |
| Release state | [Feature-frozen release](RELEASE_BASELINE.md), SHA `1c04cb15c700c5a78c4c89d3be63008af990fd5f`. CI and Pages succeeded for the same SHA. Production verification covered 52 route/viewport cases and targeted keyboard, touch and landscape interactions. |

## Classification boundary

- **Mandatory PDF requirements:** repository naming, collaborator access for the instructor, maintained README with author contact data, weekly commits and reports, thesis directory structure, thesis content/length/sections, prescribed document formatting, and IEEE references.
- **PDF-suggested repository organization:** setup guidance and other supporting directories where applicable.
- **Self-proposed engineering improvements:** automated tests, CI test gate, case-sensitive asset checks, branch protection, canonical/Open Graph URL enhancement, and browser/performance verification.

## Scope boundary

The thesis and defense package is synchronized to release `1c04cb1` for internal review. Official templates, final file formats, the academic title, `src/scr`, instructor collaborator access, email, phone and supervisor identity remain open. Weekly commit cadence is evaluated from actual Git history. The [checklist](../thesis/REVIEW_CHECKLIST.md) records the approval checkpoint.
