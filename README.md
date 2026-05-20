# Codeforces — local Java workflow

Practice rounds here with **submission-shaped** Java: one file `Main.java`, `public class Main`, **no `package` line** — what Codeforces accepts for Java uploads.

## Quick start

From this repo root:

```bash
./bin/cf init 2072 A
```

That creates `contests/2072/A/Main.java`, `samples/`, and `README.md` with a plausible statement link pattern, updates **`gradle.properties`** for IntelliJ, and selects that folder as Gradle’s sole source root (`cf use`).

Paste tests from the problem into:

- `contests/<round>/<problem>/samples/NNN.in` — stdin replay
- `contests/<round>/<problem>/samples/NNN.out` — optional; if present, `cf run` diffs stdout

Compile + run locally:

```bash
./bin/cf run 2072 A          # default: first stdin sample only
./bin/cf run 2072 A --all    # run every *.in / *.txt in samples/

# convenience: cd into the problem folder
cd contests/2072/A && ../../../bin/cf run --all
```

Locate the submission file for copy–paste:

```bash
./bin/cf path 2072 A
```

## Contest folder names

**Numeric round** (`2072`) — README links to `https://codeforces.com/contest/2072/problem/A`.

**Gym** (`gym_102956` / `gym-102956` / similar) — links to `…/gym/<id>/problem/<letter>`.

Anything else (`edu-round-xyz`) — README uses a placeholder link; swap in the real URL when you browse the site.

## What you ship to Codeforces

Only `Main.java` from the problem folder, unless rules change:

- Filename / class **`Main`** — standard CF Java submissions.
- Do **not** add `package`; keep a single top-level `public class Main`.

Fast I/O: if you hit TLE with `BufferedReader` / `PrintWriter`, add your usual tokenizer or custom reader **inline** in `Main.java` (still one file).

## Helper commands

```text
cf init <contest> <problem>
cf use <contest> <problem>        # IntelliJ/Gradle active source folder
cf run [--all] [<contest> <problem>]
cf path <contest> <problem>
cf list
```

Optional: `alias cf="$PWD/bin/cf"` in your shell if you prefer `cf` everywhere.

## IntelliJ IDEA (debug with breakpoints)

This repo is a **Gradle** Java app so IntelliJ compiles exactly **one** `Main.java` at a time (each problem uses the same class name, which breaks true multi-root “compile everything” layouts).

### First open

- **File → Open…** → select the **`codeforces`** checkout folder (must contain `build.gradle.kts`).
- Import/trust the Gradle project. JDK **17** matches the Gradle toolchain.

### Switch problems (`cf use`)

```bash
./bin/cf use 2072 A
```

This writes **`gradle.properties`** → **`cf.problem.dir=contests/2072/A`**. In IntelliJ, **Sync / Reload Gradle Project** so indexes and the active sources update.

Then open that folder’s **`Main.java`** for breakpoints.

### Debug `Main`

Gradle tool window → **`Tasks` → `application` → `run`** → right-click → **Debug**.

The Gradle **`run`** task reads **`stdin`** from **`samples/001.in`** when present (paste a statement sample there for realistic debugging).

Tip: `./bin/cf init …` runs **`cf use`** automatically for the new folder.

## Cursor / VS Code

Open **this repo** (`codeforces`) as the workspace root.

With `Main.java` focused under some `contests/…/<problem>/`, run **Terminal → Run Task… → Codeforces: run samples** to execute `./bin/cf run --all` with the working directory set to that Java file’s folder.
