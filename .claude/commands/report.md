Generate a comprehensive LeetCode performance report as a dated HTML file. The report assesses the user's performance and provides a structured learning plan.

## File Naming and History

Reports are saved with dates so you can track progress over time:

1. **Get today's date** by running `date +%Y-%m-%d` in the shell.
2. **Save the report** as `reports/report-YYYY-MM-DD.html` (e.g., `reports/report-2026-05-22.html`).
3. **Create the `reports/` directory** if it does not exist: `mkdir -p reports`.
4. **Update the symlink** so `report.html` always points to the latest: `ln -sf reports/report-YYYY-MM-DD.html report.html`.
5. If a report for today's date already exists, overwrite it (same day re-runs replace, not accumulate).

The report header should display the generation date prominently. If previous reports exist in `reports/`, include a "Previous Reports" link list in the footer showing all available dated reports (sorted newest first) so the user can compare progress over time.

## Data Collection

Gather all of the following in parallel:

1. **Solution inventory**: Find all solution files (`.py`, `.go`, `.ts`, `.js`, `.rs`, `.rb`, `.cpp`, `.c`) excluding `.venv/`. For each problem directory, identify:
   - Problem number and title (from directory name)
   - Languages used
   - Number of solution files (multiple approaches?)
   - Lines of code

2. **Git history**: Run `git log --pretty=format:"%h|%ad|%s" --date=short` to get commit dates and messages. Also get commit frequency by date with `git log --pretty=format:"%ad" --date=short | sort | uniq -c | sort -k2`.

3. **Solution analysis**: For each problem, read the solution code and determine:
   - Difficulty (Easy/Medium/Hard) based on LeetCode problem knowledge
   - Topics/categories (DP, Two Pointers, Sliding Window, Hash Map, Tree, Graph, BFS/DFS, Binary Search, Greedy, Stack, Backtracking, Heap, Trie, Union-Find, etc.)
   - Algorithm approach used
   - Whether multiple approaches were explored
   - Code quality observations

## Analysis

From the collected data, compute:

- **Totals**: Problems solved, breakdown by difficulty, breakdown by topic
- **Strengths**: Topics with deep coverage (5+ problems), patterns showing mastery, quality of implementations
- **Weaknesses/Gaps**: Important interview topics with 0-2 problems, missing classic problems, suboptimal solutions for Hard problems
- **Activity patterns**: Study frequency, gaps, bursts vs. consistency
- **Code quality**: Pythonic idioms, common anti-patterns (e.g. `list.pop(0)` instead of `deque`, variable shadowing builtins, leftover debug prints), naming consistency
- **Languages**: Primary vs. secondary language usage

## Report Structure

Generate `report.html` with a dark-themed, visually rich design containing:

1. **Header**: Title, user name, generation date
2. **Key Metrics**: Cards showing total solved, Easy/Medium/Hard counts, multi-approach count
3. **Difficulty Distribution**: Visual donut/pie chart with percentages and a target recommendation
4. **Activity Timeline**: Bar chart of commits per day, highlighting gaps and bursts
5. **Topic Coverage**: Horizontal bar chart of problems per topic, plus a coverage assessment grid (strong/moderate/weak/missing)
6. **Strengths & Weaknesses**: Two-column layout with detailed cards for each strength and gap
7. **Code Quality Assessment**: Itemized list of positives and areas for improvement with specific examples
8. **Accelerated Learning Plan**: Phased plan (3-4 phases over ~7 weeks) with specific problem numbers to solve, ordered by priority
9. **Next 20 Problems**: Prioritized table of the most impactful problems to solve next, with difficulty, topic, and rationale
10. **Full Problem Inventory**: Scrollable table of all solved problems with number, title, difficulty badge, topics, approach, languages, and multi-approach indicator

## Design Requirements

- Dark theme (GitHub-dark inspired: `#0d1117` background, `#161b22` surfaces, `#30363d` borders)
- Self-contained HTML with inline CSS (no external dependencies)
- Difficulty color coding: green for Easy, yellow/amber for Medium, red for Hard
- Responsive layout using CSS grid
- Topic tags and language badges as styled inline elements
- Clean typography with `-apple-system, BlinkMacSystemFont, 'Segoe UI'` font stack

## Theme Toggle

Include a light/dark theme toggle (fixed top-right button):
- Default: dark theme (GitHub-dark: `#0d1117` bg, `#161b22` surfaces, `#30363d` borders)
- Light theme: (`#ffffff` bg, `#f6f8fa` surfaces, `#d0d7de` borders)
- All colors via CSS custom properties in `:root` and `[data-theme="light"]`
- Persist preference in `localStorage` (key: `lc-report-theme`)
- Moon/sun icon toggle button
- Set `data-theme="dark"` on `<html>` by default

After generating the file, open it with `open report.html` (which follows the symlink to the dated file).
