Generate a comprehensive LeetCode study guide as a dated HTML file.

The guide's purpose: teach the user how to solve recommended next problems **without giving solutions**, reinforce previously learned concepts through spaced repetition, and build fluency in both **Python and Go**. The user should read a section for a particular problem *before* attempting it, and that section should give them enough understanding to solve it on their own.

## Core Learning Principles

This guide is built on evidence-based learning science:

1. **Spaced Repetition (SM-2 / Ebbinghaus)**: Previously solved problems decay from memory. The guide includes a **Review Section** with problems due for re-solving based on the SM-2 algorithm. Each review resets retention to ~100% and flattens the forgetting curve.
2. **Retrieval Practice**: Re-solving a problem from scratch (closing all notes) is vastly more effective than re-reading a solution. The guide emphasizes "close the guide, solve from memory" for review problems.
3. **Blocked → Interleaved Practice**: New patterns are introduced in blocked groups (e.g., all stack problems together). Once a pattern has been seen 2-3 times, it is interleaved with other patterns in review sessions.
4. **Elaborative Interrogation**: Each problem's "Why This Works" section asks the reader to articulate *why* the algorithm is correct — not just *how* to implement it.
5. **Concrete-to-Abstract Progression**: Easy problems with small inputs first (concrete), then Medium/Hard problems that abstract the pattern.
6. **Dual Language Fluency**: Code samples in both Python and Go teach idiomatic usage of each language's standard library, building transferable problem-solving skills.

## File Naming and History

Guides are saved with dates so you can track what was recommended at each point in time:

1. **Get today's date** by running `date +%Y-%m-%d` in the shell.
2. **Save the guide** as `guides/guide-YYYY-MM-DD.html` (e.g., `guides/guide-2026-05-22.html`). Note: this is the top-level `guides/` directory, distinct from `guides/Dynamic Programming/` which holds study material.
3. **Create the `guides/` directory** if it does not exist (it likely already does).
4. **Update the symlink** so `guide.html` always points to the latest: `ln -sf guides/guide-YYYY-MM-DD.html guide.html`.
5. If a guide for today's date already exists, overwrite it (same day re-runs replace, not accumulate).

The guide header should display the generation date. If previous guides exist in `guides/`, include a "Previous Guides" link list in the footer showing all available dated guide HTML files (sorted newest first).

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
3. **Key insight** — the single conceptual breakthrough that unlocks the solution. This is the most important part. It should be the "aha moment" — the one idea that, once understood, makes the solution fall into place. Examples: "at least one half is always sorted" for rotated array search, "store (value, current_min) tuples" for min stack.
4. **Step-by-step thinking process** — how to arrive at the approach, not the code. Walk through the reasoning: what data structure to use and why, how to set up the iteration, what decisions to make at each step, how to handle transitions. This should read like a mentor walking through the problem on a whiteboard.
5. **Why this works** — a one-paragraph explanation of *why* the algorithm is correct, not just how. This supports elaborative interrogation. Example: "Binary search works on a rotated array because the rotation preserves the sorted property in at least one half — by identifying which half is sorted, you can determine which half to discard, maintaining the O(log n) elimination guarantee."
6. **Common pitfalls and edge cases** — specific mistakes people make on this problem. Not generic advice like "watch for edge cases" but specific things like "using `<` instead of `<=` causes an infinite loop" or "forgetting to check the stack is empty before popping."
7. **Time and space complexity** of the optimal solution.
8. **Python features that help** — with short code snippets showing **only the language feature**, NOT the problem solution. Include both basic Python idioms AND standard library features. Examples:
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

9. **Go features that help** — equivalent Go idioms and standard library features for the same problem. Show how Go approaches the same task differently. Examples:
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

10. **Connections to other problems** — when problems within a section build on each other, explicitly note the progression (e.g., "this uses the same monotonic stack pattern from #739" or "this extends the binary search template from #704 with one additional check").

## Step 3: Generate the HTML Guide

Write `guide.html` with the following structure and design.

### Layout
- **Fixed left sidebar** (300px) with navigation links grouped by topic section. Each link shows: problem number, short title, and a small difficulty badge (E/M/H with color).
- The sidebar should have a **"Review" section** at the top with the spaced repetition review problems, visually distinct (e.g., with a 🔄 icon or different background color).
- **Main content area** (max-width 860px) with all the teaching content.
- Sidebar collapses on screens narrower than 900px.

### Content Structure

1. **Header**: Title ("LeetCode Study Guide"), one-line description, generation date.

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
   - "Quick Reminder" — 1-2 sentence hint about the pattern (less detail than new problems since the user has solved this before)
   - "Key Insight" callout (same as new problems)
   - "Try to recall": A challenge prompt like "Can you implement this in under 10 minutes? What's the time complexity?"
   - A **language challenge**: "Last time you solved this in Python. Try it in Go this time." (or vice versa, based on what language was used in the repo)
   - Complexity box

4. **New Problems — Topic sections**, each containing:

   **Section divider** with:
   - Topic name (e.g., "Binary Search", "Stack", "Trees")
   - 1–2 sentences of context: why this topic matters, how many problems the user has in this area currently, and what pattern they'll learn
   - **Learning mode indicator**: "Blocked Practice" (for new patterns, 2-3 problems grouped) or "Interleaved" (for patterns with 3+ prior solutions)

   **Problem cards** (one per problem), each containing:
   - **Problem header**: Number, title, difficulty badge, topic badges
   - **"The Problem"**: What to solve. Brief, clear, no hints. The reader should understand *what* they need to build.
   - **"Key Insight"**: Highlighted callout box (blue left border) with the conceptual breakthrough. This is the section the reader re-reads when stuck. Write it as a standalone paragraph that makes the "aha" click.
   - **"How to Think About It"**: Numbered steps (with circular step indicators) walking through the reasoning process. Each step should be one concrete action or decision. 4–6 steps typical. This is *how to think*, not *what to code*.
   - **"Why This Works"**: A callout explaining the correctness argument — why the algorithm produces the right answer. This is distinct from "how to think about it" (which is the problem-solving process). This section answers "if I implemented this correctly, why would it give the right answer?"
   - **"Watch Out For"**: Bullet list of specific pitfalls. Use a red-bordered warning callout box for the single most dangerous mistake on this problem.
   - **Alternative approaches** (when relevant): Brief mention of other valid approaches — e.g., "You can also solve this with an in-order traversal" or "A BFS approach (Kahn's algorithm) avoids recursion."
   - **"Python Features That Help"**: A code block with 3–6 relevant Python features. Each feature gets a comment explaining what it does. The snippets show the *feature*, not the *solution*. Include both basic idioms and standard library features (`collections`, `heapq`, `bisect`, `itertools`, `functools`).
   - **"Go Features That Help"**: A separate code block with 3–6 relevant Go features for the same problem. Show idiomatic Go — struct definitions, slice manipulation, `container/heap`, `sort`, `strings`, `unicode` packages. Each snippet should be syntactically valid Go with a comment explaining the feature.
   - **Complexity box**: Inline display showing target time and space complexity.

### Design Requirements

- **Light/dark theme toggle** — fixed button in the top-right corner:
  - Default: dark theme (GitHub-dark: `#0d1117` bg, `#161b22` surfaces, `#30363d` borders, `#e6edf3` text)
  - Light theme: (`#ffffff` bg, `#f6f8fa` surfaces, `#d0d7de` borders, `#1f2328` text)
  - All colors defined as CSS custom properties in `:root` (dark) and `[data-theme="light"]` (light override)
  - Toggle persists preference in `localStorage` (key: `lc-guide-theme`)
  - Button shows moon icon + "Light" label in dark mode, sun icon + "Dark" label in light mode
  - Light mode adjusts badge/tag backgrounds for proper contrast (increase rgba opacity)
  - Set `data-theme="dark"` on the `<html>` element by default

- **Language toggle for code blocks** — a small toggle (Python | Go) near each code block, or a global toggle in the header that switches all code blocks. Default: show both languages stacked. The toggle uses `localStorage` (key: `lc-guide-lang`) to persist preference.

- **Self-contained**: Single HTML file with all CSS and JS inline. No external CDN dependencies.
- **Difficulty badges**: Green for Easy, yellow/amber for Medium, red for Hard. Use `rgba()` backgrounds with the difficulty color at low opacity.
- **Topic badges**: Blue-tinted small inline badges.
- **Insight callout**: Blue left border, slightly tinted background.
- **Warning callout**: Red left border, slightly tinted background.
- **"Why This Works" callout**: Green left border, slightly tinted background.
- **Review section**: Distinct visual treatment — e.g., a subtle gradient or different surface color to separate review from new material.
- **Code blocks**: Monospace font (`SF Mono`, `Fira Code`, `Consolas`), surface2 background, subtle border, horizontal scroll for overflow. **Label each code block** with a small "Python" or "Go" badge in the top-right corner of the block.
- **Step indicators**: Circular numbered badges (CSS counter) to the left of each step.
- **Complexity box**: Inline-flex with time and space displayed side by side.
- **Typography**: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif`. Body text ~16px, comfortable line-height (1.7).
- **Responsive**: Sidebar hidden below 900px, main content gets padding instead of margin.

### Critical Rules

- **NEVER include actual problem solutions** — only the thinking process and language feature snippets that demonstrate language features in isolation.
- Each section must give the reader **enough understanding** to solve the problem on their own. The test: could someone read just this section, close the guide, and write a working solution?
- **Both Python and Go** code samples for every problem. Python samples should cover both basic idioms and the extended standard library. Go samples should show idiomatic Go with relevant standard library packages.
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
