# 2230 · A

Statement: <https://codeforces.com/contest/2230/problem/A>

## Local samples

- Add `samples/001.in` (stdin)
- Optionally add matching `samples/001.out` for automated diff checks

Run (from repo root or this folder):

```bash
/Users/sanka/IdeaProjects/codeforces/bin/cf run 2230 A
# or cd here and run:
/Users/sanka/IdeaProjects/codeforces/bin/cf run
```

## IntelliJ (debug breakpoints)

Gradle only compiles **one** active folder at a time (so you do not get duplicate `Main` class errors):

```bash
/Users/sanka/IdeaProjects/codeforces/bin/cf use 2230 A
```

Then in IntelliJ: **Reload Gradle Project** → use run configuration **CF: Gradle run** from the toolbar → **Debug**, or Gradle tool window → **Tasks → application → run** → **Debug**.

The Gradle `run` task reads stdin from `samples/001.in` by default (override: `./gradlew run -Pcf.stdin=…`): `samples/OTHER.in` under the active problem folder (`gradle.properties cf.problem.dir`).


## Submit

Upload `Main.java`: public class Main, single file, no `package` line unless the site's Java rules change.
