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

## Current result after independent audit and local preparation

| Requirement | Status after Phase 1 | Phase 1 evidence |
| --- | --- | --- |
| Maintained root README | PARTIAL | Academic documentation, setup, progress, thesis, test, demo, and rename-plan links are present. Verified student name, ID, and class are recorded; email, phone, and supervisor remain explicitly unavailable. |
| Weekly `progress-report` directory | PASS | Index, reusable template, and an evidence-based report for ISO week 48 are present. |
| Commit at least weekly | PARTIAL | Week 48 work is documented, but no commit is created and no history is rewritten by this task. |
| Thesis repository structure | PASS | Required subdirectories are represented by tracked README files. |
| Thesis body and formatting | DEFERRED | Explicitly reserved for a later authorized phase. |
| Root author email and phone | DEFERRED | Placeholders only, as required by the task. |
| `setup` guidance | PASS | Reproducible SDK, restore, build, run, test, and publish guidance is present. |
| Automated tests | PASS | Test project and CI gate are present; the verified Release run passed 14 tests with no failures or skips, including exact-case image-manifest coverage and rendered image metadata. |
| Repository naming convention | DEFERRED | Target `ASPNET-DK25TTC5-lehien-BADONG` was not found under verified owner `anhpham1504`; rename impact and rollback are documented. Execution requires explicit approval. |
| Supervisor invited as collaborator | MISSING | Only the owner is a collaborator and no invitation is pending. The PDF email is recorded as an invitation target only; sending it is a remote permission change requiring approval. |
| Source directory spelling | DEFERRED | `src` is intentionally retained. The PDF says `scr`, but changing a conventional source directory without instructor confirmation would add risk and is explicitly out of scope. |
| Student identity | PARTIAL | Name `Lê Hiền`, student ID `170125405`, and class `DK25TTC5` are verified from the task. Email and phone were not supplied; supervisor identity is unconfirmed. |

## Verified repository and GitHub state

| Item | Observed state on 25 November 2026 |
| --- | --- |
| Branch and HEAD | `main` at `46ba776893ba29445855080a5a6004c9e6ae0626` |
| Remote | `https://github.com/anhpham1504/ba-dong-coastal-escape.git` |
| Visibility and access | Public repository; authenticated viewer has `ADMIN` permission |
| GitHub Pages | Workflow deployment configured; current URL `https://anhpham1504.github.io/ba-dong-coastal-escape/` |
| Branch protection | `main` is not protected; this is an engineering risk, not a PDF requirement |
| Actions | Enabled; allowed-actions policy is `all` |
| Working tree | Previous academic structure and tests remain uncommitted; this preparation adds no commit, push, rename, invitation, or deployment |

## Classification boundary

- **Mandatory PDF requirements:** repository naming, collaborator access for the instructor, maintained README with author contact data, weekly commits and reports, thesis directory structure, thesis content/length/sections, prescribed document formatting, and IEEE references.
- **PDF-suggested repository organization:** setup guidance and other supporting directories where applicable.
- **Self-proposed engineering improvements:** automated tests, CI test gate, case-sensitive asset checks, branch protection, canonical/Open Graph URL enhancement, and browser/performance verification.

## Scope boundary

The following are not completion claims: thesis content, thesis page count, Word/PDF formatting, slides, repository rename, `src` rename, instructor invitation, deployment, email, phone, or supervisor identity. Optional `soft` and `docker` directories are not created because the current project does not need them. Weekly cadence cannot be repaired retroactively and must be maintained honestly going forward.
