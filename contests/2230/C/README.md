# 2230 · C

Statement: <https://codeforces.com/contest/2230/problem/C>

## Local samples

- Add `samples/001.in` (stdin)
- Optionally add matching `samples/001.out` for automated diff checks

Run (from repo root or this folder):

```bash
/Users/sanka/IdeaProjects/codeforces/bin/cf run 2230 C
# or cd here and run:
/Users/sanka/IdeaProjects/codeforces/bin/cf run
```

## IntelliJ (debug breakpoints)

Gradle only compiles **one** active folder at a time (so you do not get duplicate `Main` class errors):

```bash
/Users/sanka/IdeaProjects/codeforces/bin/cf use 2230 C
```

Then in IntelliJ: **Reload Gradle Project** → Gradle tool window → **Tasks → application → run** → **Debug** (bug icon).

The Gradle `run` task redirects `stdin` from `samples/001.in` when that file exists (add paste from the statement).


## Submit

Upload `Main.java`: public class Main, single file, no `package` line unless the site's Java rules change.
