# Academic compliance matrix

This matrix compares the repository with `QUY_DINH_CHUNG_ASP.net.pdf`. It records evidence observed on 25 November 2026 and separates mandatory PDF requirements from engineering improvements.

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

## Current result after independent audit and approved repository rename

| Requirement | Status after Phase 1 | Phase 1 evidence |
| --- | --- | --- |
| Maintained root README | PARTIAL | Academic documentation, setup, progress, thesis, test, demo, and rename-plan links are present. Verified student name, ID, and class are recorded; email, phone, and supervisor remain explicitly unavailable. |
| Weekly `progress-report` directory | PASS | Index, reusable template, and an evidence-based report for ISO week 48 are present. |
| Commit at least weekly | PARTIAL | Week 48 work is documented and committed with real timestamps, but the earlier gap cannot be repaired retroactively. |
| Thesis repository structure | PASS | Required subdirectories are represented by tracked README files. |
| Thesis body and formatting | DEFERRED | Explicitly reserved for a later authorized phase. |
| Root author email and phone | DEFERRED | Placeholders only, as required by the task. |
| `setup` guidance | PASS | Reproducible SDK, restore, build, run, test, and publish guidance is present. |
| Automated tests | PASS | Test project and CI gate are present; the verified Release run passed 14 tests with no failures or skips, including exact-case image-manifest coverage and rendered image metadata. |
| Repository naming convention | PASS | The existing repository was renamed in place to `ASPNET-DK25TTC5-lehien-BADONG` after explicit approval; history and `main` were preserved. |
| Supervisor invited as collaborator | MISSING | Only the owner is a collaborator and no invitation is pending. The PDF email is recorded as an invitation target only; sending it is a remote permission change requiring approval. |
| Source directory spelling | DEFERRED | `src` is intentionally retained. The PDF says `scr`, but changing a conventional source directory without instructor confirmation would add risk and is explicitly out of scope. |
| Student identity | PARTIAL | Name `Lê Hiền`, student ID `170125405`, and class `DK25TTC5` are verified from the task. Email and phone were not supplied; supervisor identity is unconfirmed. |

## Verified repository and GitHub state

| Item | Observed state on 25 November 2026 |
| --- | --- |
| Branch and baseline | `main`; pre-compliance HEAD `46ba776893ba29445855080a5a6004c9e6ae0626` remains in history |
| Academic commit | `30bd3cb812784be12c161a9300673c6f713e67e0` |
| Remote | `https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG.git` |
| Visibility and access | Public repository; authenticated viewer has `ADMIN` permission |
| GitHub Pages | Workflow deployment configured for `https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/`; remote run verification follows the containing release commit |
| Branch protection | `main` is not protected; this is an engineering risk, not a PDF requirement |
| Actions | Enabled; allowed-actions policy is `all` |
| Release state | Repository rename and deployment-path update were explicitly approved; CI/Pages results must still be verified from the pushed release commit |

## Classification boundary

- **Mandatory PDF requirements:** repository naming, collaborator access for the instructor, maintained README with author contact data, weekly commits and reports, thesis directory structure, thesis content/length/sections, prescribed document formatting, and IEEE references.
- **PDF-suggested repository organization:** setup guidance and other supporting directories where applicable.
- **Self-proposed engineering improvements:** automated tests, CI test gate, case-sensitive asset checks, branch protection, canonical/Open Graph URL enhancement, and browser/performance verification.

## Scope boundary

The following are not completion claims: thesis content, thesis page count, Word/PDF formatting, slides, `src` rename, accepted instructor collaborator access, email, phone, or supervisor identity. Optional `soft` and `docker` directories are not created because the current project does not need them. Weekly cadence cannot be repaired retroactively and must be maintained honestly going forward. A renamed Pages URL is not considered deployed until its workflow and production checks complete successfully.
