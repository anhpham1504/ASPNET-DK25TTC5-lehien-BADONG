# Repository rename record and release plan

This document records the approved in-place rename and the remaining controlled release checks. Observations were verified on 25 November 2026.

## Current verified state

| Item | Current value |
| --- | --- |
| GitHub owner | `anhpham1504` |
| Repository | `ASPNET-DK25TTC5-lehien-BADONG` |
| Remote | `https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG.git` |
| Visibility and permission | Public; authenticated viewer has `ADMIN` permission |
| Default branch | `main` |
| Preserved baseline | `46ba776893ba29445855080a5a6004c9e6ae0626` |
| Academic commit | `30bd3cb812784be12c161a9300673c6f713e67e0` |
| Pages method | GitHub Actions workflow |
| Configured Pages URL | `https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/` |
| Collaborators | Only `anhpham1504`; no pending invitations |
| Branch protection | `main` is not protected |
| Actions | Enabled; allowed-actions policy is `all` |

The former repository name was `ba-dong-coastal-escape`. GitHub resolves its old API path to the renamed repository, but the local remote was explicitly updated instead of relying on that redirect.

## Approved identity and deployment values

| Item | Planned value |
| --- | --- |
| Repository | `ASPNET-DK25TTC5-lehien-BADONG` |
| Remote | `https://github.com/anhpham1504/ASPNET-DK25TTC5-lehien-BADONG.git` |
| Pages base path | `/ASPNET-DK25TTC5-lehien-BADONG/` |
| Planned Pages URL | `https://anhpham1504.github.io/ASPNET-DK25TTC5-lehien-BADONG/` |

The repository and remote values were verified after the rename. The Pages URL is not claimed as production-PASS until the post-push workflow and browser checks complete.

## Impact analysis

### Runtime and deployment references that must change

- `.github/workflows/deploy-pages.yml`: expected repository-name validation.
- `.github/workflows/deploy-pages.yml`: `SITE_BASE` and `SITE_URL` values.
- `README.md`: current repository, base-path, and demo references after the new deployment is verified.

The source `index.html` intentionally keeps `<base href="/" />`; the workflow rewrites it at publish time. `404.html`, `robots.txt`, and `sitemap.xml` intentionally keep `__SITE_BASE__` or `__SITE_URL__` tokens and do not need the repository name hard-coded in source.

### SEO and social impact

The sitemap and robots URL are deployment tokens and will follow the new `SITE_URL`. The current source has no canonical link or `og:url`; adding tokenized values and workflow validation is a separate, optional engineering enhancement, not a prerequisite for preserving existing behavior. Any such enhancement must be verified against the published output.

### References that must remain unchanged

- .NET namespace, assembly, project names, routes, and the `src` directory.
- JSON schemas, content IDs/slugs, image paths, and automated-test paths.
- Git history, commit timestamps, and commit hashes.
- Historical evidence that accurately names the repository or URL at the time it was collected.

Repository-wide search found no literal old repository reference in `PRODUCT.md`, application source, JSON, test code, JavaScript, sitemap source, robots source, or SPA fallback source. Blind replacement is therefore not appropriate.

## Controlled execution sequence

1. Recheck working tree, secrets, target-name availability, GitHub authentication/permission, collaborators, Pages, Actions, branch, and HEAD.
2. Run restore, Release build, tests, JSON validation, documentation-link validation, workflow review, and `git diff --check`.
3. Review and stage only Academic Phase 0–3 files for commit `chore(academic): establish compliance structure and automated testing`.
4. Create that local commit with the real current timestamp; do not rewrite history.
5. Rename the existing GitHub repository to `ASPNET-DK25TTC5-lehien-BADONG`; do not create a replacement repository.
6. Update the deployment workflow and current README references to the new exact-case name, base path, remote, and planned URL.
7. Re-run local verification and create `chore(repository): update academic identity and deployment paths` only if its staged content matches that purpose.
8. Set `origin` to the verified new remote instead of relying on GitHub's redirect, then push `main`.
9. Monitor CI and Pages to completion and record actual run URLs and commit SHA.
10. Verify HTTPS, homepage assets, WebAssembly/JSON requests, navigation, direct deep links, refresh behavior, invalid slugs, `404.html`, `robots.txt`, and `sitemap.xml` at the new URL.
11. Invite the instructor account associated with `antonio86doan@gmail.com` only as a separately approved remote permission change and verify the resulting invitation/collaborator state.

At the time of this document update, steps 1–6 were completed: preflight passed, the academic commit was created, the existing repository was renamed, `origin` was updated, and deployment references were changed locally. Push, CI/Pages monitoring, production checks, and collaborator verification remain subject to observed results after the containing release commit.

## Commit boundaries

- `chore(academic): establish compliance structure and automated testing` — structure, academic documentation, setup guidance, tests, and CI test gate.
- `chore(repository): update academic identity and deployment paths` — verified academic identity plus the actual repository/deployment-path changes.

Before committing, use `git diff --cached --name-only` and `git diff --cached` to prevent accidental inclusion of temporary renders, build outputs, credentials, or unrelated user work.

## Risks and expected interruption

- The current Pages workflow deliberately rejects any repository name other than the current one. A rename before updating and pushing the workflow will temporarily make deployment fail.
- The project-site URL and base path change with the repository name. Existing bookmarks and search results may depend on GitHub redirects and should not be treated as guaranteed.
- GitHub Pages may be unavailable or serve the previous artifact while the post-rename deployment runs.
- Exact casing matters in the planned project URL and Linux deployment checks.
- An unprotected `main` branch allows direct updates; enabling protection is recommended but is a separate repository-setting change.
- Repository-name availability and authenticated permissions can change between audit and execution.

## Rollback

Prefer a focused corrective commit or `git revert` of the faulty change. Do not use `reset --hard`, force-push, or history rewriting. If deployment variables are wrong, restore the last verified repository name, `SITE_BASE`, and `SITE_URL` in a normal commit and redeploy. Rename the repository back only when necessary and explicitly approved, then update `origin` and verify Pages/settings again.

## Acceptance criteria

- The existing repository is visible under the exact new name; history and `main` HEAD are preserved.
- `origin` equals the verified new URL and no replacement repository was created.
- Both intended commits contain only reviewed files and real timestamps.
- CI restore, build, and 14-or-more current tests pass for the pushed SHA.
- Pages deployment succeeds for the same SHA and the new project URL loads without missing CSS, JavaScript, WebAssembly, JSON, or images.
- Homepage navigation, direct detail links, refresh/fallback behavior, invalid slugs, robots, and sitemap are verified.
- No unresolved `__SITE_URL__` or `__SITE_BASE__` token remains in published files.
- Old repository names remain only where they are accurate historical evidence.
- Instructor collaborator status is reported from GitHub after any separately approved invitation.

## Approval record

The user explicitly confirmed the combined Phase C operation on 25 November 2026: create the reviewed commits, rename the existing repository, update `origin`, push `main`, monitor CI/Pages, verify production, and invite the instructor using the supplied email when GitHub can resolve it without guessing an account. That approval does not authorize unrelated repository settings, history rewrites, force-pushes, or architecture changes.
