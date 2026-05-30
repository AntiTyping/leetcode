Generate a comprehensive LeetCode study guide as a dated HTML file.

The guide's purpose: teach the user how to solve recommended next problems **without giving solutions**, reinforce previously learned concepts through spaced repetition, and build fluency in **Python, Go, TypeScript, Rust, and C++**. The user should read a section for a particular problem *before* attempting it, and that section should give them enough understanding to solve it on their own.

## Core Learning Principles

This guide is built on evidence-based learning science:

1. **Spaced Repetition (SM-2 / Ebbinghaus)**: Previously solved problems decay from memory. The guide includes a **Review Section** with problems due for re-solving based on the SM-2 algorithm. Each review resets retention to ~100% and flattens the forgetting curve.
2. **Retrieval Practice**: Re-solving a problem from scratch (closing all notes) is vastly more effective than re-reading a solution. The guide emphasizes "close the guide, solve from memory" for review problems.
3. **Blocked → Interleaved Practice**: New patterns are introduced in blocked groups (e.g., all stack problems together). Once a pattern has been seen 2-3 times, it is interleaved with other patterns in review sessions.
4. **Elaborative Interrogation**: Each problem's "Why This Works" section asks the reader to articulate *why* the algorithm is correct — not just *how* to implement it.
5. **Concrete-to-Abstract Progression**: Easy problems with small inputs first (concrete), then Medium/Hard problems that abstract the pattern.
6. **Multi-Language Fluency**: Code samples in Python, Go, TypeScript, Rust, and C++ teach idiomatic usage of each language's standard library, building transferable problem-solving skills across paradigms (dynamic, compiled/GC'd, typed/compiled, ownership-based, and manual memory management).

## File Naming and History

Guides are saved with dates so you can track what was recommended at each point in time:

1. **Get today's date** by running `date +%Y-%m-%d` in the shell.
2. **Save the guide** as `guides/guide-YYYY-MM-DD.html` (e.g., `guides/guide-2026-05-22.html`). Note: this is the top-level `guides/` directory, distinct from `guides/Dynamic Programming/` which holds study material.
3. **Create the `guides/` directory** if it does not exist (it likely already does).
4. **Update the symlink** so `guide.html` always points to the latest: `ln -sf guides/guide-YYYY-MM-DD.html guide.html`.
5. If a guide for today's date already exists, overwrite it (same day re-runs replace, not accumulate).

The guide header should display the generation date. In the footer, list **all previous guides** found by running `ls guides/guide-*.html | sort -r`. Link each entry using a relative path (e.g., `guide-2026-05-29.html` — no `guides/` prefix since the current file is already inside `guides/`). Mark the current guide's entry with "(current)". Example footer list:
```html
<li><a href="guide-2026-05-30.html">2026-05-30</a> (current)</li>
<li><a href="guide-2026-05-29.html">2026-05-29</a></li>
<li><a href="guide-2026-05-28.html">2026-05-28</a></li>
```
Also update the footers of all existing previous guides to include a link to the new guide being generated (so all guides cross-link to each other with correct relative paths).

## Step 0: Gather History and Review State

Before selecting problems, build a complete picture of what the user has already done:

1. **Inventory existing solutions**: Find all problem directories and solution files (`.py`, `.go`, `.ts`, `.js`, `.rs`, `.rb`) excluding `.venv/`. Extract problem numbers, topics, and languages used.
2. **Read git history**: Run `git log --pretty=format:"%ad|%s" --date=short` to determine *when* each problem was solved. This is critical for spaced repetition scheduling.
3. **Read past guides**: Check `guides/guide-*.html` files to see which problems were previously recommended. Problems that were recommended but never solved should be re-recommended with higher priority.
4. **Load review state**: Read `guides/review-state.json` if it exists. This JSON file tracks the SM-2 state for each solved problem:
   ```json
   {
     "problem_number": {
       "ef": 2.5,
       "interval": 6,
       "repetition": 2,
       "last_reviewed": "2026-05-22",
       "next_review": "2026-05-28"
     }
   }
   ```
   If the file does not exist, initialize it from git history — treat each problem's first commit date as its initial solve date and compute initial review schedules.
5. **Update review state**: After determining which problems are due for review, write the updated `guides/review-state.json`.

### SM-2 Algorithm Implementation

For each solved problem, track and update these variables:

- **EF** (Easiness Factor): starts at 2.5, minimum 1.3
- **n** (repetition count): starts at 0
- **I** (interval in days): I(1)=1, I(2)=6, I(n)=round(I(n-1) × EF) for n>2

Since the guide cannot observe the user's actual recall quality (grade q), use a **simplified schedule** based on time-since-solve:
- Problems solved in the last 1 day → not yet due
- Problems solved 1–2 days ago → due for first review (interval 1)
- Problems solved 3–7 days ago → due for second review (interval 6)
- Problems solved 1–3 weeks ago → due for third review (interval ~15)
- Problems solved 3–8 weeks ago → due for fourth review (interval ~37)
- Problems solved 2–6 months ago → due for fifth review (interval ~90)
- Problems solved 6+ months ago → due for refresh review

When generating the guide, select **5–8 review problems** that are currently due, prioritized by:
1. Problems most overdue (furthest past their next_review date)
2. Problems with lower EF (harder problems need more reinforcement)
3. Problems covering patterns that appear in the new problems section (interleaving)

## Step 1: Identify Which Problems to Cover

Analyze the repository to determine which **new** problems the user should tackle next:

1. **Identify gaps**: Based on knowledge of LeetCode interview categories, determine which critical topics are underrepresented (e.g., Binary Search, Stack, Trees, Graph/DFS, Backtracking, Trie, Union-Find, Bit Manipulation).
2. **Select 15–20 NEW problems** that fill the most important gaps, ordered by learning priority. Include a mix of Easy (to learn the pattern), Medium (to apply it), and Hard (to stretch existing strengths).
3. **Apply blocked → interleaved ordering**: For patterns the user is seeing for the first time, group 2-3 problems together (blocked). For patterns with 3+ solved problems, interleave them with other topics.

If `report.html` already exists and is recent, you can read it to extract the recommended "Next 20 Problems" and "Accelerated Learning Plan" instead of re-analyzing from scratch.

Group the selected problems by topic/pattern (e.g., Binary Search, Stack, Trees, Backtracking, Graph, Linked List, Trie, Hard Challenges).

## Step 2: Research Each Problem Deeply

For each problem (both new and review), gather detailed teaching material. **Use parallel agents** to research problems concurrently for efficiency — e.g., one agent for Binary Search + Stack + Tree problems, another for Graph + Backtracking + Linked List + Trie + Hard problems.

For each problem, the research must produce:

1. **Problem statement** — brief but complete: what are the inputs, what to return, key constraints. Enough that the reader understands the problem without opening LeetCode.
2. **Difficulty** — Easy / Medium / Hard
3. **Brute force approach** — the naive/obvious solution that most people think of first. Include:
   - A 2–4 sentence description of the approach (e.g., "Check every pair of elements" or "Generate all subsets and filter")
   - Time and space complexity of the brute force
   - **Why it's insufficient** — what makes it too slow? Which constraint makes it fail? (e.g., "With n up to 10⁵, O(n²) means 10¹⁰ operations — far too slow for a 1-second time limit")
   - A short **Python implementation** (5–15 lines) showing the brute force code. This should be a complete, working solution — not pseudocode. Keep it concise but correct.
   - A short **Go implementation** (5–15 lines) of the same brute force.
   - A short **TypeScript implementation** (5–15 lines) of the same brute force.
   - A short **Rust implementation** (5–15 lines) of the same brute force.
   - A short **C++ implementation** (5–15 lines) of the same brute force.
   
   The brute force serves two purposes: (1) it validates understanding of the problem before optimizing, and (2) it makes the efficiency gain of the optimal solution visceral — seeing O(n²) next to O(n) with concrete code makes the "why" of the optimization click.

4. **Key insight** — the single conceptual breakthrough that unlocks the optimal solution. This is the most important part. It should be the "aha moment" — the one idea that, once understood, makes the solution fall into place. Frame it as: "The brute force does X repeatedly/redundantly. The insight is that Y eliminates this redundancy." Examples: "The brute force checks every pair — the insight is that a hash map lets you check complements in O(1)" or "The brute force rescans the window — the insight is that a monotonic stack resolves all pending days in one pass."
5. **Step-by-step thinking process** — how to arrive at the optimal approach, not the code. Walk through the reasoning: what data structure to use and why, how to set up the iteration, what decisions to make at each step, how to handle transitions. This should read like a mentor walking through the problem on a whiteboard.
6. **Why this works** — a one-paragraph explanation of *why* the algorithm is correct, not just how. This supports elaborative interrogation. Example: "Binary search works on a rotated array because the rotation preserves the sorted property in at least one half — by identifying which half is sorted, you can determine which half to discard, maintaining the O(log n) elimination guarantee."
7. **Common pitfalls and edge cases** — specific mistakes people make on this problem. Not generic advice like "watch for edge cases" but specific things like "using `<` instead of `<=` causes an infinite loop" or "forgetting to check the stack is empty before popping."
8. **Time and space complexity** of the optimal solution, shown side-by-side with the brute force complexity so the improvement is clear.
9. **Python features that help** — with short code snippets showing **only the language feature**, NOT the problem solution. Include both basic Python idioms AND standard library features. Examples:
   - `bisect.bisect_left()` for binary search
   - `heapq.heappush/heappop` for priority queues
   - `collections.deque` with `popleft()` for BFS
   - `collections.Counter` for frequency counting
   - `collections.defaultdict(list)` for adjacency lists
   - `functools.cache` / `@lru_cache` for memoization
   - `itertools.accumulate(arr, max)` for running maximums
   - Tuple unpacking: `a, b = b, a` for swaps without temp variables
   - Chained comparisons: `low < val < high`
   - `float('inf')` / `float('-inf')` as sentinels
   - `enumerate()` for index + value iteration
   - List as stack: `append()` / `pop()` / `[-1]`
   - `str.isdigit()`, `str.isalpha()` for character classification
   - The `or` trick: `left or right` returns first truthy value
   - `any()` / `all()` for boolean aggregation
   
   Include 3–6 of the most relevant features per problem, with a 1–3 line code snippet and a comment explaining the feature.

10. **Go features that help** — equivalent Go idioms and standard library features for the same problem. Show how Go approaches the same task differently. Examples:
   - `sort.Search()` / `sort.SearchInts()` for binary search
   - `container/heap` interface for priority queues
   - Slices as stacks: `append()` / `s[:len(s)-1]`
   - `map[T]bool` for sets, `map[T]int` for counters
   - `make([]int, n)` for pre-allocated slices
   - `math.MaxInt`, `math.MinInt` as sentinels
   - `strings.Builder` for efficient string concatenation
   - Multiple return values for error handling
   - `range` for iteration with index + value
   - `sort.Slice()` with custom comparator
   - `sync.WaitGroup` for concurrent BFS (advanced)
   - Struct-based TreeNode/ListNode definitions
   - Go's lack of generics before 1.18 / type parameters after
   - `unicode.IsLetter()`, `unicode.IsDigit()` for char classification
   
   Include 3–6 of the most relevant features per problem, with a 1–3 line code snippet and a comment explaining the feature.

11. **TypeScript features that help** — TypeScript idioms and patterns for the same problem. Show how TS approaches the task with its type system. Examples:
   - `Map<K, V>` and `Set<T>` for hash-based collections
   - Array destructuring: `const [a, ...rest] = arr`
   - `Array.from({length: n}, (_, i) => i)` for range generation
   - `arr.sort((a, b) => a - b)` for numeric sort (default is lexicographic!)
   - `arr.reduce()` for accumulation, `arr.flatMap()` for flatten + map
   - `??` (nullish coalescing) and `?.` (optional chaining)
   - `Number.MAX_SAFE_INTEGER`, `Infinity`, `-Infinity` as sentinels
   - `string.charCodeAt()` for character arithmetic
   - Template literal types and `as const` for exhaustive checks
   - `Record<string, number>` for frequency maps
   - Stack/queue via array: `push()` / `pop()` / `shift()` (note: `shift()` is O(n))
   
   Include 3–6 of the most relevant features per problem, with a 1–3 line code snippet and a comment explaining the feature.

12. **Rust features that help** — Rust idioms and standard library features. Show how Rust's ownership model and iterator chains approach the problem. Examples:
   - `HashMap<K, V>` and `HashSet<T>` from `std::collections`
   - `BinaryHeap<T>` for max-heap, `BinaryHeap<Reverse<T>>` for min-heap
   - `entry().or_insert()` / `entry().or_default()` for map updates
   - Iterator chains: `.iter().enumerate()`, `.filter()`, `.map()`, `.collect()`
   - `vec![]` macro, `Vec::with_capacity(n)` for pre-allocation
   - Pattern matching with `match` and `if let`
   - `Option<T>` and `Result<T, E>` — `.unwrap_or()`, `.map()`, `?` operator
   - `i32::MAX`, `i32::MIN`, `usize::MAX` as sentinels
   - Slice patterns: `[first, rest @ ..]`
   - `.windows(n)` and `.chunks(n)` for sliding window on slices
   - `VecDeque<T>` for double-ended queue / BFS
   - Ownership/borrowing: `&[T]` slices vs `Vec<T>` owned vectors
   
   Include 3–6 of the most relevant features per problem, with a 1–3 line code snippet and a comment explaining the feature.

13. **C++ features that help** — C++ idioms and STL features. Show how C++ approaches the problem with its rich standard library. Examples:
   - `unordered_map<K, V>` and `unordered_set<T>` for hash-based collections
   - `priority_queue<int>` (max-heap), `priority_queue<int, vector<int>, greater<>>` (min-heap)
   - `sort(v.begin(), v.end())` with custom comparators via lambdas
   - `vector<int>` operations: `push_back()`, `pop_back()`, `back()`, `emplace_back()`
   - `stack<T>`, `queue<T>`, `deque<T>` from `<stack>`, `<queue>`, `<deque>`
   - Range-based for: `for (auto& x : vec)` and structured bindings: `auto [key, val] = pair`
   - `INT_MAX`, `INT_MIN` from `<climits>`, or `numeric_limits<int>::max()`
   - `string::substr()`, `string::find()`, `isalpha()`, `isdigit()` from `<cctype>`
   - `accumulate()` from `<numeric>`, `min_element()` / `max_element()` from `<algorithm>`
   - `pair<int,int>` and `tuple<>` for multi-value storage
   - `bitset<N>` for fixed-size bit manipulation
   - Lambda captures: `[&]`, `[=]`, `[&visited]` for closures
   
   Include 3–6 of the most relevant features per problem, with a 1–3 line code snippet and a comment explaining the feature.

14. **Connections to other problems** — when problems within a section build on each other, explicitly note the progression (e.g., "this uses the same monotonic stack pattern from #739" or "this extends the binary search template from #704 with one additional check").

## Step 3: Generate the HTML Guide

Write `guide.html` with the following structure and design.

### Layout
- **Fixed left sidebar** (300px) with navigation links grouped by topic section. Each link shows: problem number, short title, and a small difficulty badge (E/M/H with color).
- The sidebar should have a **"Review" section** at the top with the spaced repetition review problems, visually distinct (e.g., with a 🔄 icon or different background color).
- **Main content area** (max-width 860px) with all the teaching content.
- Sidebar collapses on screens narrower than 900px.

### Content Structure

1. **Header**: Title ("LeetCode Study Guide"), one-line description ("Master patterns through guided problem-solving — Python, Go, TypeScript, Rust & C++"), generation date.

2. **"How to Use This Guide"** box: Numbered instructions:
   - Start with the **Review Section** — re-solve these problems from memory before looking at hints
   - Read the section for the next new problem on your list
   - Close the guide and open LeetCode — attempt the problem for at least 20 minutes
   - If stuck, re-read the "Key Insight" box — it contains the conceptual breakthrough
   - After solving (or failing after 40 min), compare your approach to the thinking steps
   - After solving, ask yourself: **"Why does this algorithm work?"** — articulate the correctness argument
   - Move to the next problem — problems within each section build on each other

3. **Review Section** (spaced repetition):
   
   **Section header** with:
   - Title: "Review — Spaced Repetition"
   - Explanation: "These are problems you've solved before that are due for review based on the forgetting curve. Re-solve them from scratch without looking at your previous solution. This retrieval practice is the most effective way to build long-term retention."
   - A small table showing the review schedule: "Day 1 → Day 6 → Day 15 → Day 37 → Day 90"
   
   **Review problem cards** (condensed format compared to new problems):
   - Problem header with number, title, difficulty, topic, and **days since last solved**
   - **"The Problem"** — a brief 1–3 sentence description of what the problem asks. This is critical for review cards because the user may not remember the problem from its title alone. Keep it concise but complete enough to jog memory (e.g., "Given an array of integers and a target, return indices of the two numbers that add up to the target. Each input has exactly one solution, and you may not use the same element twice.").
   - "Quick Reminder" — 1-2 sentence hint about the pattern (less detail than new problems since the user has solved this before)
   - "Key Insight" callout (same as new problems)
   - "Try to recall": A challenge prompt like "Can you implement this in under 10 minutes? What's the time complexity?"
   - A **language challenge**: "Last time you solved this in Python. Try it in Go this time." (or vice versa, based on what language was used in the repo)
   - Complexity box
   - **"Examples"** — 2–4 concrete input/output examples shown BEFORE any code blocks. These help the user re-anchor on the problem's exact shape (input format, edge cases, expected return type). Render as a `<div class="examples">` containing one `<div class="example">` per case. Each example shows `Input:` and `Output:` in monospace, with an optional `Explanation:` line for non-obvious cases. Include at least one normal case, one edge case (empty input, single element, all-same values, etc.), and one tricky case if the problem has a well-known gotcha. Format inputs/outputs exactly as LeetCode shows them (e.g. `nums = [2,7,11,15], target = 9` → `[0,1]`). Place this section right after the Complexity box and before the "Previous Solution" block. Style: subtle surface2 background, dotted divider, monospace font for input/output values.
   - **"Previous Solution"** — a collapsible `<details>` block (collapsed by default) containing the user's actual prior solution code from the repo. Read the solution file(s) from the corresponding problem directory (e.g. `NNNN Problem Title/leet.py`, `leet.go`, etc.) and embed the code inside a `<pre><code>` block with a language badge. If multiple language files exist, include each in its own code block. The summary line should read `Previous Solution (click to reveal — try without it first)`. This lets the user attempt from memory but check their prior approach when stuck or after solving. Use `<details class="prev-solution"><summary>...</summary>...</details>` so it can be styled with a purple border matching the review accent. The reasoning: re-solving from memory is the goal, but seeing the *exact code the user wrote before* (not a generic reference solution) is a powerful retrieval-failure recovery tool.
   - **"Optimal Solution (Reference)"** — a SECOND collapsible `<details>` block (collapsed by default), placed immediately AFTER the "Previous Solution" block. This contains the canonical optimal solution to the problem — not the user's code, but the best-known implementation that an experienced practitioner would write. Include **all five languages** (Python, Go, TypeScript, Rust, C++) inside the same `<details>`, each as a `<pre><code>` block with a language badge labeled "Python — Optimal" / "Go — Optimal" / "TypeScript — Optimal" / "Rust — Optimal" / "C++ — Optimal". The summary line should read `Optimal Solution (reference) — click to reveal`. Use `<details class="optimal-solution"><summary>...</summary>...</details>` so it can be styled with a GREEN left border (distinct from the purple "Previous Solution" border). This serves a different purpose than "Previous Solution": (a) lets the user compare their prior approach to the gold standard, (b) shows the cleanest idiomatic version even if their old code was clumsy or non-optimal, (c) for problems where the user's prior solution used a sub-optimal approach (e.g., brute force, or a different pattern), this block reveals the canonical technique. Keep each language version concise (5-20 lines) — focus on the cleanest expression of the optimal pattern, not the most verbose. This is the ONLY place in the guide where optimal solution code appears — it stays appropriate because review problems are ones the user has already attempted, so revealing the optimal is not a spoiler.

4. **New Problems — Topic sections**, each containing:

   **Section divider** with:
   - Topic name (e.g., "Binary Search", "Stack", "Trees")
   - 1–2 sentences of context: why this topic matters, how many problems the user has in this area currently, and what pattern they'll learn
   - **Learning mode indicator**: "Blocked Practice" (for new patterns, 2-3 problems grouped) or "Interleaved" (for patterns with 3+ prior solutions)

   **Problem cards** (one per problem), each containing:
   - **Problem header**: Number, title, difficulty badge, topic badges
   - **"The Problem"**: What to solve. Brief, clear, no hints. The reader should understand *what* they need to build.
   - **"Brute Force"**: A collapsible/expandable section (using `<details><summary>`) showing the naive approach. Contains:
     - A 2–4 sentence description of the brute force approach
     - **Complete Python implementation** (5–15 lines, working code, not pseudocode)
     - **Complete Go implementation** (5–15 lines, working code)
     - **Complete TypeScript implementation** (5–15 lines, working code)
     - **Complete Rust implementation** (5–15 lines, working code)
     - **Complete C++ implementation** (5–15 lines, working code)
     - **Complexity** (time and space) of the brute force
     - **"Why optimize?"** — one sentence explaining what constraint makes brute force too slow (e.g., "With n up to 10⁵, the O(n²) nested loops mean ~10¹⁰ operations — 100× over the time limit.")
     
     The brute force section uses a distinct visual style: amber/yellow left border callout to signal "this works but isn't good enough." The code blocks here ARE full solutions (unlike the feature snippets in the optimal section which show only language features). This contrast is intentional — seeing the complete brute force code next to the optimal thinking process teaches when and why to optimize.
   - **"Key Insight"**: Highlighted callout box (blue left border) with the conceptual breakthrough. Frame it as the bridge from brute force to optimal: what redundancy does the brute force have, and how does this insight eliminate it? This is the section the reader re-reads when stuck.
   - **"How to Think About It"**: Numbered steps (with circular step indicators) walking through the reasoning process for the optimal solution. Each step should be one concrete action or decision. 4–6 steps typical. This is *how to think*, not *what to code*.
   - **"Why This Works"**: A callout explaining the correctness argument — why the algorithm produces the right answer. This is distinct from "how to think about it" (which is the problem-solving process). This section answers "if I implemented this correctly, why would it give the right answer?"
   - **"Watch Out For"**: Bullet list of specific pitfalls. Use a red-bordered warning callout box for the single most dangerous mistake on this problem.
   - **Alternative approaches** (when relevant): Brief mention of other valid approaches — e.g., "You can also solve this with an in-order traversal" or "A BFS approach (Kahn's algorithm) avoids recursion."
   - **"Python Features That Help"**: A code block with 3–6 relevant Python features for the **optimal** solution. Each feature gets a comment explaining what it does. The snippets show the *feature*, not the *solution*. Include both basic idioms and standard library features (`collections`, `heapq`, `bisect`, `itertools`, `functools`).
   - **"Go Features That Help"**: A separate code block with 3–6 relevant Go features for the **optimal** solution. Show idiomatic Go — struct definitions, slice manipulation, `container/heap`, `sort`, `strings`, `unicode` packages. Each snippet should be syntactically valid Go with a comment explaining the feature.
   - **"TypeScript Features That Help"**: A code block with 3–6 relevant TypeScript features. Show idiomatic TS — `Map`/`Set`, array methods, destructuring, type annotations. Each snippet should be syntactically valid TypeScript.
   - **"Rust Features That Help"**: A code block with 3–6 relevant Rust features. Show idiomatic Rust — ownership patterns, iterator chains, `std::collections` types, pattern matching. Each snippet should compile.
   - **"C++ Features That Help"**: A code block with 3–6 relevant C++ features. Show modern C++ (C++17+) — STL containers, algorithms, lambdas, structured bindings, range-based for.
   - **Complexity box**: Inline display showing **both** brute force and optimal complexities side by side, making the improvement visually obvious (e.g., "Brute: O(n²) → Optimal: O(n)").

### Design Requirements

- **Light/dark theme toggle** — fixed button in the top-right corner:
  - Default: dark theme (GitHub-dark: `#0d1117` bg, `#161b22` surfaces, `#30363d` borders, `#e6edf3` text)
  - Light theme: (`#ffffff` bg, `#f6f8fa` surfaces, `#d0d7de` borders, `#1f2328` text)
  - All colors defined as CSS custom properties in `:root` (dark) and `[data-theme="light"]` (light override)
  - Toggle persists preference in `localStorage` (key: `lc-guide-theme`)
  - Button shows moon icon + "Light" label in dark mode, sun icon + "Dark" label in light mode
  - Light mode adjusts badge/tag backgrounds for proper contrast (increase rgba opacity)
  - Set `data-theme="dark"` on the `<html>` element by default

- **Language toggle for code blocks** — a global toggle in the header that switches all code blocks. Options: All | Python | Go | TypeScript | Rust | C++. Default: show all languages stacked. The toggle uses `localStorage` (key: `lc-guide-lang`) to persist preference. Each language's code block must have `data-lang="python"`, `data-lang="go"`, `data-lang="typescript"`, `data-lang="rust"`, or `data-lang="cpp"` attribute so the toggle can show/hide them.

- **Self-contained**: Single HTML file with all CSS and JS inline. No external CDN dependencies.
- **Difficulty badges**: Green for Easy, yellow/amber for Medium, red for Hard. Use `rgba()` backgrounds with the difficulty color at low opacity.
- **Topic badges**: Blue-tinted small inline badges.
- **Insight callout**: Blue left border, slightly tinted background.
- **Warning callout**: Red left border, slightly tinted background.
- **"Why This Works" callout**: Green left border, slightly tinted background.
- **"Brute Force" section**: Amber/yellow left border callout, collapsible via `<details><summary>`. Summary line shows "Brute Force — O(n²) time" (with the actual complexity). When expanded, shows description, complete Python and Go code, and a "Why optimize?" note. The code blocks here use the same styling as other code blocks but with an amber "Brute Force" badge instead of language badge.
- **"Examples" block** (review cards only): A `<div class="examples">` placed right after the complexity box and before the "Previous Solution" block. Contains 2–4 `<div class="example">` rows, each showing `Input:`, `Output:`, and optional `Explanation:`. Subtle surface2 background with a soft 1px border, no left accent border. Labels (`Input:`, `Output:`, `Explanation:`) in `var(--text-muted)` with `font-weight:600`; values in monospace (`SF Mono`, `Consolas`). Each example separated by a 1px dotted divider. The block is NOT collapsible — examples are quick reference and should be visible at a glance.
- **"Previous Solution" block** (review cards only): Collapsed by default `<details class="prev-solution">` with a purple/violet left border (matching the review section accent). The summary line reads `Previous Solution — click to reveal (try without it first)`. When expanded, displays the actual code the user previously wrote (read from the problem's directory in the repo) inside `<pre><code>` blocks with language badges. If multiple language files exist (e.g. `leet.py` and `leet.go`), include one collapsible block per language inside the same `<details>`, OR a single block with both stacked. Style: subtle dotted divider above, low-contrast surface background so it doesn't compete visually with the "Key Insight" callout the user should read first.
- **"Optimal Solution (Reference)" block** (review cards only): Collapsed by default `<details class="optimal-solution">` with a GREEN left border (distinct from the purple "Previous Solution"). Placed immediately after the "Previous Solution" block. The summary line reads `Optimal Solution (reference) — click to reveal`. When expanded, displays a canonical/best-known implementation in all five languages (Python, Go, TypeScript, Rust, C++), each as a separate `<pre><code>` block with a language badge ("Python — Optimal", "Go — Optimal", "TypeScript — Optimal", "Rust — Optimal", "C++ — Optimal"). Background should match the "Why This Works" green-tinted callout family. The green border signals "this is the gold standard / target pattern".
- **Complexity box** (enhanced): Shows brute force and optimal side by side with an arrow between them, e.g., "Brute: O(n²) → Optimal: O(n)". Use a subtle color transition (red/amber for brute → green for optimal) to make the improvement visually obvious.
- **Review section**: Distinct visual treatment — e.g., a subtle gradient or different surface color to separate review from new material.
- **Code blocks**: Monospace font (`SF Mono`, `Fira Code`, `Consolas`), surface2 background, subtle border, horizontal scroll for overflow. **Label each code block** with a small language badge ("Python", "Go", "TypeScript", "Rust", or "C++") in the top-left corner of the block.
- **Step indicators**: Circular numbered badges (CSS counter) to the left of each step.
- **Complexity box**: Inline-flex with time and space displayed side by side.
- **Typography**: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif`. Body text ~16px, comfortable line-height (1.7).
- **Responsive**: Sidebar hidden below 900px, main content gets padding instead of margin.

### Critical Rules

- **Include brute force solutions** (complete working code in all five languages: Python, Go, TypeScript, Rust, and C++) inside the collapsible "Brute Force" section. This is the one exception to the no-solutions rule — the brute force is a teaching tool, not a spoiler. It validates problem understanding and makes the optimization contrast visceral.
- **NEVER include the optimal solution** for NEW problems — only the thinking process and language feature snippets that demonstrate language features in isolation. The reader must synthesize the optimal solution themselves from the key insight, thinking steps, and feature snippets. (Exceptions on REVIEW cards only: each review card includes TWO collapsed `<details>` blocks at the bottom — (1) "Previous Solution" with the user's actual prior code from the repo, and (2) "Optimal Solution (reference)" with a canonical best-known implementation in all five languages. Both are collapsed by default. This is safe because review problems are ones the user has already attempted, so revealing the optimal is a comparison tool, not a spoiler. Optimal solution code MUST NOT appear anywhere in the new-problem sections.)
- Each section must give the reader **enough understanding** to solve the problem on their own. The test: could someone read just this section, close the guide, and write a working solution?
- **All five languages** (Python, Go, TypeScript, Rust, C++) for code samples on every problem. Python samples should cover both basic idioms and the extended standard library. Go samples should show idiomatic Go. TypeScript samples should demonstrate modern TS with proper types. Rust samples should show idiomatic ownership patterns and iterator chains. C++ samples should use modern C++ (C++17+) with STL.
- Problems within each section should be ordered by **increasing difficulty** — Easy first, then Medium, then Hard.
- When two problems share a pattern, the second problem's section should reference the first (e.g., "Apply the same binary search template from #704, but add a check for which half is sorted").
- The **Review Section always comes first** in the guide, before new material.
- **Track and update `guides/review-state.json`** with the current SM-2 state after generating the guide.

### Spaced Repetition State Management

After generating the guide, update `guides/review-state.json`:
- For newly solved problems (found in repo but not in review-state.json), initialize with EF=2.5, n=0, I=1, last_reviewed=solve_date, next_review=solve_date+1
- For problems included in this guide's review section, advance their repetition count: n+=1, update interval using SM-2 formula (assume q=4 "correct with hesitation" as default grade), update next_review
- Write the updated JSON file

After generating the file, open it with `open guide.html` (which follows the symlink to the dated file).
