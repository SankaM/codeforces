# Codeforces — local Java workflow

Practice rounds here with **submission-shaped** Java: one file `Main.java`, `public class Main`, **no `package` line** — what Codeforces accepts for Java uploads.

## Fastest loop (IntelliJ + one active problem)

1. Open this folder (**must contain `build.gradle.kts`**) → trust Gradle → JDK **17**.
2. Create + select a problem: `./bin/cf new 2230 C` (`new` ≡ `init`: scaffolds + runs `use` → updates `gradle.properties`).
3. Load tests: Competitive Companion paste (see below), or **`pbpaste | ./bin/cf sample 2230 C`** → `samples/001.in`.
4. **Toolbar → `CF: Gradle run` → Debug** (shared Gradle task). Stdin defaults to **`samples/001.in`** under the active `cf.problem.dir`. Override Gradle stdin: `./gradlew run -Pcf.stdin=samples/002.in`.
5. `./bin/cf path 2230 C` gives the submission file.

Reuse another letter: `./bin/cf use 2230 D` → **Gradle reload** → same Debug config.

Paste tests manually if you prefer: `samples/NNN.in` (+ optional `NNN.out` for `./bin/cf run … --all`).

## Compared to typical setups

| Approach | Strengths | Downsides vs here |
|---------|-----------|---------------------|
| **This repo (`bin/cf` + Gradle)** | No extra installs; **`Main.java`** always matches CF; one source root ⇒ **duplicate `Main` fixed**; **checked-in IntelliJ Gradle run entry** (`CF: Gradle run`); pipes for samples. | No auto-submit; no polygon from browser (paste or Companion text). |
| **[cf-tool](https://github.com/xalanq/cf-tool)** (Go CLI) | Pull samples, local test, **submit** from terminal. | Another binary; still need your own **Java project layout** + duplicate-`Main` story if you compile many problems in one module. |
| **AutoCp + [Competitive Companion](https://github.com/jmerle/competitive-companion)** (IntelliJ plugin) | One-click parse task + test UI from browser. | Plugin + extension; you still choose how to structure Java (often same “one class name” pain unless template matches). |
| **KHelper** (Java/Kotlin helper) | Tight IntelliJ integration for CP. | Plugin install; opinionated template. |

This repo **intentionally stays minimal**: shell + Gradle + optional Companion paste; you can add **cf-tool** or **AutoCp** later without conflict.

## Helper commands

```text
cf new|init <contest> <problem>
cf use <contest> <problem>
cf sample <contest> <problem> [name]   # stdin → samples/[name] default 001.in
cf run [--all] [<contest> <problem>]
cf path <contest> <problem>
cf list
```

Optional: `alias cf="$PWD/bin/cf"`.

## Contest folder names

**Numeric round** (`2072`) — README links to `https://codeforces.com/contest/2072/problem/A`.

**Gym** (`gym_102956` / `gym-102956`) — links to `…/gym/<id>/problem/<letter>`.

Other slugs — placeholder link in per-problem `README.md`.

## What you ship to Codeforces

Only that folder’s `Main.java` (no `package`). Fast I/O: keep helpers **inline** in the same file.

## Gradle / stdin details

- **`gradle.properties`**: **`cf.problem.dir=…`** — only directory compiled (avoids conflicting `Main` classes).
- **`-Pcf.stdin=relative/path`** — path is **relative inside** `cf.problem.dir`, default **`samples/001.in`**.

## Cursor / VS Code

Run Task **Codeforces: run samples** (`./bin/cf run --all` with cwd = active file directory) — best when Gradle is not involved.
