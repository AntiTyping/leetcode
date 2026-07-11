Regenerate the LeetCode Recall Cheat Sheet as `cheatsheet.html`.

The cheatsheet lists every solved problem with a short recall hint — the key insight needed to solve it in 1-2 sentences.

## Data Collection

1. **Find all problem directories**: Scan for directories matching `[0-9]*` in the repo root. Exclude `.venv/`, `node_modules/`, `guides/`, `reports/`, `.claude/`, `.git/`.
2. **For each directory**: Extract problem number and title from the directory name. List all solution files (`.py`, `.go`, `.ts`, `.js`, `.rs`, `.rb`, `.cpp`, `.c`) to determine languages used.
3. **Read existing cheatsheet**: If `cheatsheet.html` already exists, read it to preserve the existing problem data structure and hints. Only add newly found problems.

## Problem Data

For each problem, determine:
- **Number** and **title** (from directory name)
- **Difficulty**: Easy / Medium / Hard (from LeetCode knowledge)
- **Topics**: 1-3 topic tags (e.g., `arrays`, `hash-map`, `DP`, `two-pointers`, `sliding-window`, `tree`, `graph`, `backtracking`, `greedy`, `stack`, `binary-search`, `linked-list`, `heap`, `trie`, `bit-manipulation`, `prefix-sum`, `intervals`, `math`, `string`, `design`)
- **Languages**: Short badges based on file extensions (Py, Go, TS, JS, Rs, Rb, C++)
- **Problem description**: One sentence describing what the problem asks. Example: `Given an array and a target, return indices of two numbers that add up to the target.`
- **Recall hint**: 1-2 short sentences with the **key insight** for solving the problem. The first sentence should be bold and name the technique. Example: `**Hash map of complement.** Store {val: index}, check if target - num exists in one pass.`

## HTML Structure

Generate `cheatsheet.html` as a self-contained HTML file (inline CSS/JS, no CDN).

### Layout
- Single-column responsive layout, max-width 860px, centered
- Compact cards, one per problem, **randomly shuffled by default** (Fisher-Yates on page load)

### Header
- Title: "LeetCode Recall Cheat Sheet"
- Subtitle: "N problems — quick hints to jog your memory" with generation date
- Stats bar: total count, Easy/Medium/Hard breakdown
- **Controls**: Search input (filter by number, title, or topic), sort dropdown (by number, difficulty, topic)
- **Global toggle buttons**: "Labels" (on by default — shows topic tags), "Show Hints" (off by default — hints hidden for recall practice)
- **Topic filter buttons**: Clickable pills for each topic, with "All" button

### Card Design
Each card shows:
- Problem number + title as header
- Difficulty badge (green Easy, amber Medium, red Hard)
- Problem description (one sentence, always visible)
- Topic tags as small pills, languages as accent-colored badges
- **Per-card buttons**: "show labels" (visible when global labels off), "show hint" (visible when global hints off)
- Hint text (hidden by default)
- Subtle left border color matching difficulty

### Design Theme
- Dark/light theme toggle (default dark, GitHub-dark colors)
- localStorage key: `lc-cheatsheet-theme`
- CSS custom properties in `:root` / `[data-theme="dark"]` / `[data-theme="light"]`
- Typography: `-apple-system` stack, 16px body

### Interactive Behavior
- **Global "Labels" toggle**: Shows/hides all topic tags. When off, per-card "show labels" buttons appear.
- **Global "Show Hints" toggle**: Shows/hides all hints. When off, per-card "show hint" buttons appear.
- **Per-card toggles**: Independently show/hide labels or hint for a single card.
- **Search**: Filters cards by number, title, or topic in real-time.
- **Topic filter pills**: Click to show only problems with that topic.
- **Sort**: By number, difficulty, topic, or **random** (default). Random shuffle uses Fisher-Yates and re-shuffles each time the "Random" option is selected or the page loads.

### Critical Rules
- Every solved problem in the repo must appear
- Hints must be concise — 1-2 sentences max, focused on the key insight
- No full solutions — just the technique/pattern name and core idea
- Hints should use `<strong>` for the technique name and `<code>` for code snippets

After generating, open with `open cheatsheet.html`.
