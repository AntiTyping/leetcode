Generate a comprehensive LeetCode study guide as a dated HTML file.

The guide's purpose: teach the user how to solve their recommended next problems **without giving solutions**. The user should read a section for a particular problem *before* attempting it, and that section should give them enough understanding to solve it on their own. Python is the default language.

## File Naming and History

Guides are saved with dates so you can track what was recommended at each point in time:

1. **Get today's date** by running `date +%Y-%m-%d` in the shell.
2. **Save the guide** as `guides/guide-YYYY-MM-DD.html` (e.g., `guides/guide-2026-05-22.html`). Note: this is the top-level `guides/` directory, distinct from `guides/Dynamic Programming/` which holds study material.
3. **Create the `guides/` directory** if it does not exist (it likely already does).
4. **Update the symlink** so `guide.html` always points to the latest: `ln -sf guides/guide-YYYY-MM-DD.html guide.html`.
5. If a guide for today's date already exists, overwrite it (same day re-runs replace, not accumulate).

The guide header should display the generation date. If previous guides exist in `guides/`, include a "Previous Guides" link list in the footer showing all available dated guide HTML files (sorted newest first).

## Step 1: Identify Which Problems to Cover

Analyze the repository to determine which problems the user should tackle next:

1. **Inventory existing solutions**: Find all problem directories and solution files (`.py`, `.go`, `.ts`, `.js`, `.rs`, `.rb`) excluding `.venv/`. Extract problem numbers and topics already solved.
2. **Identify gaps**: Based on knowledge of LeetCode interview categories, determine which critical topics are underrepresented (e.g., Binary Search, Stack, Trees, Graph/DFS, Backtracking, Trie, Union-Find, Bit Manipulation).
3. **Select 15–25 problems** that fill the most important gaps, ordered by learning priority. Include a mix of Easy (to learn the pattern), Medium (to apply it), and Hard (to stretch existing strengths). For each selected problem, note which gap it fills and why it was chosen.

If `report.html` already exists and is recent, you can read it to extract the recommended "Next 20 Problems" and "Accelerated Learning Plan" instead of re-analyzing from scratch.

Group the selected problems by topic/pattern (e.g., Binary Search, Stack, Trees, Backtracking, Graph, Linked List, Trie, Hard Challenges).

## Step 2: Research Each Problem Deeply

For each problem, gather detailed teaching material. **Use parallel agents** to research problems concurrently for efficiency — e.g., one agent for Binary Search + Stack + Tree problems, another for Graph + Backtracking + Linked List + Trie + Hard problems.

For each problem, the research must produce:

1. **Problem statement** — brief but complete: what are the inputs, what to return, key constraints. Enough that the reader understands the problem without opening LeetCode.
2. **Difficulty** — Easy / Medium / Hard
3. **Key insight** — the single conceptual breakthrough that unlocks the solution. This is the most important part. It should be the "aha moment" — the one idea that, once understood, makes the solution fall into place. Examples: "at least one half is always sorted" for rotated array search, "store (value, current_min) tuples" for min stack.
4. **Step-by-step thinking process** — how to arrive at the approach, not the code. Walk through the reasoning: what data structure to use and why, how to set up the iteration, what decisions to make at each step, how to handle transitions. This should read like a mentor walking through the problem on a whiteboard.
5. **Common pitfalls and edge cases** — specific mistakes people make on this problem. Not generic advice like "watch for edge cases" but specific things like "using `<` instead of `<=` causes an infinite loop" or "forgetting to check the stack is empty before popping."
6. **Time and space complexity** of the optimal solution.
7. **Python-specific features that make the solution easier** — with short code snippets showing **only the language feature**, NOT the problem solution. These should teach the reader a Python tool they can apply. Examples:
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
   - String repetition: `"abc" * 3`
   - The `or` trick: `left or right` returns first truthy value
   - `any()` / `all()` for boolean aggregation
   
   Include 3–6 of the most relevant features per problem, with a 1–3 line code snippet and a comment explaining the feature.

8. **Connections to other problems** — when problems within a section build on each other, explicitly note the progression (e.g., "this uses the same monotonic stack pattern from #739" or "this extends the binary search template from #704 with one additional check").

## Step 3: Generate the HTML Guide

Write `guide.html` with the following structure and design.

### Layout
- **Fixed left sidebar** (300px) with navigation links grouped by topic section. Each link shows: problem number, short title, and a small difficulty badge (E/M/H with color).
- **Main content area** (max-width 860px) with all the teaching content.
- Sidebar collapses on screens narrower than 900px.

### Content Structure

1. **Header**: Title ("LeetCode Study Guide"), one-line description of the guide's purpose.

2. **"How to Use This Guide"** box: Numbered instructions:
   - Read the section for the next problem on your list
   - Close the guide and open LeetCode — attempt the problem for at least 20 minutes
   - If stuck, re-read the "Key Insight" box — it contains the conceptual breakthrough
   - After solving (or failing after 40 min), compare your approach to the thinking steps
   - Move to the next problem — problems within each section build on each other

3. **Topic sections**, each containing:

   **Section divider** with:
   - Topic name (e.g., "Binary Search", "Stack", "Trees")
   - 1–2 sentences of context: why this topic matters, how many problems the user has in this area currently, and what pattern they'll learn

   **Problem cards** (one per problem), each containing:
   - **Problem header**: Number, title, difficulty badge, topic badges
   - **"The Problem"**: What to solve. Brief, clear, no hints. The reader should understand *what* they need to build.
   - **"Key Insight"**: Highlighted callout box (blue left border) with the conceptual breakthrough. This is the section the reader re-reads when stuck. Write it as a standalone paragraph that makes the "aha" click.
   - **"How to Think About It"**: Numbered steps (with circular step indicators) walking through the reasoning process. Each step should be one concrete action or decision. 4–6 steps typical. This is *how to think*, not *what to code*.
   - **"Watch Out For"**: Bullet list of specific pitfalls. Use a red-bordered warning callout box for the single most dangerous mistake on this problem.
   - **Alternative approaches** (when relevant): Brief mention of other valid approaches — e.g., "You can also solve this with an in-order traversal" or "A BFS approach (Kahn's algorithm) avoids recursion."
   - **"Python Features That Help"**: A code block with 3–6 relevant Python features. Each feature gets a comment explaining what it does. The snippets show the *feature*, not the *solution*. For example, show how `heapq.heappush` works, not how to solve the specific problem with it.
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

- **Self-contained**: Single HTML file with all CSS and JS inline. No external CDN dependencies.
- **Difficulty badges**: Green for Easy, yellow/amber for Medium, red for Hard. Use `rgba()` backgrounds with the difficulty color at low opacity.
- **Topic badges**: Blue-tinted small inline badges.
- **Insight callout**: Blue left border, slightly tinted background.
- **Warning callout**: Red left border, slightly tinted background.
- **Code blocks**: Monospace font (`SF Mono`, `Fira Code`, `Consolas`), surface2 background, subtle border, horizontal scroll for overflow.
- **Step indicators**: Circular numbered badges (CSS counter) to the left of each step.
- **Complexity box**: Inline-flex with time and space displayed side by side.
- **Typography**: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif`. Body text ~16px, comfortable line-height (1.7).
- **Responsive**: Sidebar hidden below 900px, main content gets padding instead of margin.

### Critical Rules

- **NEVER include actual problem solutions** — only the thinking process and Python feature snippets that demonstrate language features in isolation.
- Each section must give the reader **enough understanding** to solve the problem on their own. The test: could someone read just this section, close the guide, and write a working solution?
- **Python is the default language** for all feature snippets and examples.
- Problems within each section should be ordered by **increasing difficulty** — Easy first, then Medium, then Hard.
- When two problems share a pattern, the second problem's section should reference the first (e.g., "Apply the same binary search template from #704, but add a check for which half is sorted").

After generating the file, open it with `open guide.html` (which follows the symlink to the dated file).
