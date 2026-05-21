# Codeforces practice (Java)

You **already opened this project in IntelliJ**. Work through **Steps 1–7** once; after that, use the **checklist** at the bottom for each new problem.

**Example:** contest **2230**, problem **C** — replace with your round number and letter (A, B, C, …).

---

## Step 1 — Terminal and the `cf` command

1. In IntelliJ: **View → Tool Windows → Terminal** (tab at the bottom).
2. The terminal should already be inside this project. If not:
   ```bash
   cd path/to/codeforces
   ```
3. Run once per terminal session:
   ```bash
   source env.sh
   ```
4. Check it works:
   ```bash
   cf list
   ```

**If you see `command not found`:** run `source env.sh` again, or use `./bin/cf` instead of `cf` (example: `./bin/cf new 2230 C`).

**Optional — every new terminal window:** add this line to `~/.zshrc` (use your real folder path):

```bash
source /path/to/codeforces/env.sh
```

---

## Step 2 — Create a problem folder

On Codeforces you are solving **2230C** (contest **2230**, letter **C**).

In the terminal:

```bash
cf new 2230 C
```

In the Project panel (left): **contests → 2230 → C → Main.java** — double-click to open.

You should see:

```
contests/2230/C/
  Main.java      ← write code here
  samples/       ← test files here
```

---

## Step 3 — Copy sample tests from the problem page

On Codeforces, open the problem → find the **example** (input and output).

1. Copy the **input** text.
2. In IntelliJ: right-click **samples** → **New → File** → name **`001.in`** → paste → **Save**.
3. Copy the **output** text.
4. New file **`001.out`** → paste → **Save**.

| What you copied on Codeforces | File to create |
|------------------------------|----------------|
| Example input | `contests/2230/C/samples/001.in` |
| Example output | `contests/2230/C/samples/001.out` |

**Mac:** after copying input on the website:

```bash
pbpaste | cf sample 2230 C
```

Then still create **`001.out`** by hand in IntelliJ.

Add more tests later as `002.in` / `002.out`, etc.

---

## Step 4 — Run your program on the samples

```bash
cf run 2230 C --all
```

- **OK** — output matches `001.out` (and any other `.out` files).
- **FAIL** — wrong answer; fix `Main.java` and run again.

Run this command often while you code.

---

## Step 5 — Solve the problem in `Main.java`

Edit **`contests/2230/C/Main.java`**.

Rules for Codeforces:

- Class name must be **`Main`**.
- Do **not** put `package something;` at the top.
- One file is enough — paste that same file when you submit.

When you think you’re done:

```bash
cf run 2230 C --all
```

Keep editing until you see **OK**.

---

## Step 6 — Debug in IntelliJ (optional)

1. Open **`Main.java`** for 2230 C.
2. Click left of a line number → red **breakpoint**.
3. Top bar: select **`CF: Gradle run`**.
4. Click the **bug** icon (**Debug**).
5. Program runs with input from **`samples/001.in`** and stops at your breakpoint. Press **F8** to step line by line.

**Switching to another problem** (e.g. you worked on B and now want C):

```bash
cf use 2230 C
```

Then in IntelliJ: **Gradle** tool window → **Reload** (refresh icon). Debug again.

---

## Step 7 — Submit on Codeforces

1. Browser: problem **2230C** → **Submit** → language **Java**.
2. IntelliJ: open **`contests/2230/C/Main.java`** → select all (**Cmd+A**) → copy (**Cmd+C**).
3. Paste into the submit box → **Submit**.

To see the file location in the terminal:

```bash
cf path 2230 C
```

---

## Next problem (same contest)

| Goal | Command |
|------|---------|
| Start empty (new letter **D**) | `cf new 2230 D` |
| Copy your Java style from **C** | `cf copy 2230 C 2230 D` |

Then: new samples in `samples/`, edit `Main.java`, `cf run 2230 D --all`, submit `contests/2230/D/Main.java`.

---

## Checklist (every problem)

1. `cf new <contest> <letter>` or `cf copy …`
2. `samples/001.in` + `001.out` from the statement
3. `cf run <contest> <letter> --all` until **OK**
4. Debug with **CF: Gradle run** if needed
5. Submit **`Main.java`** on Codeforces

---

## All commands (swap 2230 / C for yours)

```bash
cf new 2230 C
cf copy 2230 C 2230 D
cf use 2230 C
cf run 2230 C --all
cf path 2230 C
cf list
pbpaste | cf sample 2230 C
```

If `cf` does not work, use `./bin/cf` (e.g. `./bin/cf run 2230 C --all`).
