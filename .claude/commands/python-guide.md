Generate a daily Python programming study guide as a dated HTML file.

The guide's purpose: teach the user Python programming concepts through progressive daily lessons with spaced repetition reinforcement. Each day introduces **new concepts** and **reviews previously learned concepts** based on the forgetting curve. The user should read a concept section, study the examples, then attempt the exercises without looking at hints.

## Core Learning Principles

1. **Spaced Repetition (SM-2)**: Previously learned concepts decay from memory. The guide includes a **Review Section** with concepts due for re-study. Each review resets retention.
2. **Retrieval Practice**: Exercises ask the user to write code from memory — not copy examples.
3. **Blocked → Interleaved Practice**: New topics are introduced in groups (e.g., all string topics together). Once a topic has been seen 2+ times, it's interleaved with other topics in reviews.
4. **Concrete-to-Abstract**: Start with simple examples, build to real-world patterns.
5. **Progressive Curriculum**: Concepts build on each other day-over-day, from intermediate to advanced Python.

## File Naming and History

1. **Get today's date** by running `date +%Y-%m-%d`.
2. **Save** as `python-guides/python-guide-YYYY-MM-DD.html`.
3. **Create directory** if needed: `mkdir -p python-guides`.
4. **Update symlink**: `ln -sf python-guides/python-guide-YYYY-MM-DD.html python-guide.html`.
5. Same-day re-runs overwrite.

Include generation date in header. In the footer, list **all previous guides** found by running `ls python-guides/python-guide-*.html | sort -r`. For each file, extract the date from the filename and compute the day number (Day 1, Day 2, ...) based on chronological order. Link each entry using `python-guides/` prefix (e.g., `python-guides/python-guide-2026-05-28.html`) so links work when the file is opened via the root symlink `python-guide.html`. Mark the current day's entry with "(current)". Example footer list:
```html
<li><a href="python-guides/python-guide-2026-05-30.html">2026-05-30</a> (current &mdash; Day 3)</li>
<li><a href="python-guides/python-guide-2026-05-29.html">2026-05-29</a> (Day 2)</li>
<li><a href="python-guides/python-guide-2026-05-28.html">2026-05-28</a> (Day 1)</li>
```

## Step 0: Gather State

1. **Load review state**: Read `python-guides/review-state.json` if it exists. Tracks SM-2 state for each learned concept:
   ```json
   {
     "concept_id": {
       "ef": 2.5,
       "interval": 6,
       "repetition": 2,
       "last_reviewed": "2026-05-28",
       "next_review": "2026-06-03",
       "topic": "strings",
       "title": "F-String Debugging"
     }
   }
   ```
   If the file doesn't exist, this is the first guide — initialize it after generating.

2. **Read past guides**: Check `python-guides/python-guide-*.html` to see what was covered previously. Avoid repeating new concepts that were already introduced.

3. **Determine review queue**: Select 4–6 concepts due for review (next_review <= today), prioritized by most overdue and lowest EF.

### SM-2 Implementation

Same as the LeetCode guide:
- **EF**: starts 2.5, minimum 1.3
- **Intervals**: I(1)=1, I(2)=6, I(n)=round(I(n-1) × EF) for n>2
- Assume q=4 (correct with hesitation) for automatic advancement

## Step 1: Select Today's Concepts

### Python Curriculum (progressive order across days)

**Week 1 — Pythonic Foundations:**
- F-strings: debugging `=`, format specs, expressions, multiline
- String methods deep dive: partition, removeprefix/removesuffix, translate, maketrans
- Comprehensions: list, dict, set — nested, conditional, walrus operator
- Generator expressions vs list comprehensions: memory, laziness, chaining
- Unpacking: tuple unpacking, `*rest`, `**kwargs`, extended unpacking, swap idiom
- `collections` module: Counter, defaultdict, deque, namedtuple, ChainMap
- Decorators: function decorators, `@wraps`, stacking, parameterized decorators

**Week 2 — Functions & Iteration:**
- Closures and `nonlocal`, factory functions
- `itertools`: chain, islice, groupby, product, combinations, accumulate
- `functools`: partial, reduce, lru_cache/cache, total_ordering, singledispatch
- Lambda functions and when NOT to use them
- Type hints: basic annotations, Optional, Union, generics, Protocol
- Enum and dataclasses
- `operator` module: itemgetter, attrgetter, methodcaller

**Week 3 — OOP Mastery:**
- Classes: `__init__`, `__repr__`, `__str__`, `__eq__`, `__hash__`
- Properties, slots, class methods, static methods
- Inheritance, MRO (Method Resolution Order), `super()`
- Abstract base classes (ABC), interfaces via Protocol
- Dunder methods: `__getitem__`, `__len__`, `__contains__`, `__iter__`, `__call__`
- Descriptors: `__get__`, `__set__`, `__delete__`
- Metaclasses (overview, when to use, when NOT to)

**Week 4 — Error Handling & I/O:**
- Exception hierarchy, custom exceptions, exception groups
- Context managers: `__enter__`/`__exit__`, `@contextmanager`
- `pathlib` for file system operations
- `json`, `csv`, `configparser` for data formats
- `re` module: patterns, groups, lookahead, named groups
- `logging` module: levels, formatters, handlers
- `argparse` for CLI tools

**Week 5 — Concurrency & Performance:**
- `threading` vs `multiprocessing` vs `asyncio`
- `async`/`await` basics, event loop, `asyncio.gather`
- `concurrent.futures`: ThreadPoolExecutor, ProcessPoolExecutor
- Profiling: `timeit`, `cProfile`, line_profiler
- Memory: `__slots__`, `sys.getsizeof`, generators for large data
- `struct` and `memoryview` for binary data

**Week 6 — Testing & Packaging:**
- `pytest` basics: fixtures, parametrize, markers, conftest
- Mocking: `unittest.mock`, `patch`, `MagicMock`
- `typing` advanced: TypeVar, Generic, ParamSpec, overload
- Virtual environments, `pyproject.toml`, dependency management
- Design patterns in Python: singleton, factory, strategy, observer

**Week 7+ — Advanced Topics:**
- Metaprogramming: `__init_subclass__`, `__class_getitem__`
- Import system: `__import__`, importlib, sys.path
- CPython internals: GIL, reference counting, interning
- C extensions overview, ctypes, cffi
- Walrus operator patterns, structural pattern matching (3.10+)
- Performance: `__slots__`, `array` module, numpy interop

Select **5–7 new concepts** for today based on where the user is in the curriculum. Group them into 2–3 topic sections.

## Step 2: Research Each Concept

For each concept (both new and review), produce:

### New Concept Card:
1. **Title and topic tag** (e.g., "F-String Debugging" / Strings)
2. **Why it matters** — 1-2 sentences on when/why you'd use this in real code
3. **The concept explained** — clear explanation with progressive examples:
   - Start with the simplest possible example
   - Build to an intermediate example
   - Show a real-world usage pattern
4. **Code examples** — 3-5 runnable Python snippets, each with comments explaining what happens. Show both the code AND its output.
5. **Common mistakes** — specific anti-patterns with corrections:
   - Show the WRONG way (with ❌ marker)
   - Show the RIGHT way (with ✅ marker)
6. **Key rules** — 2-3 bullet points summarizing when to use (and when NOT to use) this feature
7. **Practice exercises** — 2-3 small coding challenges the user should attempt WITHOUT looking at examples:
   - State the problem clearly
   - Include expected input/output
   - Do NOT include solutions
   - Order from easy to harder
8. **Connections** — how this concept relates to previously learned or upcoming concepts

### Review Concept Card (condensed):
1. **Title, topic, days since last review**
2. **Quick reminder** — 1-2 sentence refresher
3. **Key pattern** — the most important code snippet for this concept
4. **Challenge exercise** — a single harder exercise that tests recall
5. **Common mistake recap** — the #1 pitfall for this concept

## Step 3: Generate the HTML Guide

### Layout
- **Fixed left sidebar** (300px) with navigation grouped by: Review, then topic sections
- **Main content area** (max-width 860px)
- Sidebar collapses below 900px

### Content Structure

1. **Header**: "Python Daily Guide", date, concept count
2. **"How to Use"** box with numbered instructions
3. **Review Section** (if concepts are due): condensed review cards
4. **New Concepts** — topic sections with full concept cards

### Concept Card HTML Structure (new concepts):
```
<div class="concept-card">
  <div class="concept-header">
    <span class="concept-title">TITLE</span>
    <span class="ttag">TOPIC</span>
  </div>
  <p class="why-matters">WHY_IT_MATTERS</p>
  <div class="explanation">EXPLANATION_WITH_PROGRESSIVE_EXAMPLES</div>
  <div class="code-example">
    <div class="lang-badge">Python</div>
    <pre><code>CODE_WITH_COMMENTS</code></pre>
    <div class="output">OUTPUT</div>
  </div>
  (repeat for each example)
  <div class="callout-warning">
    <strong>Common Mistakes:</strong>
    <div class="mistake">❌ WRONG_WAY</div>
    <div class="correct">✅ RIGHT_WAY</div>
  </div>
  <div class="key-rules">
    <strong>Key Rules:</strong>
    <ul><li>RULE</li>...</ul>
  </div>
  <div class="exercises">
    <strong>Practice Exercises:</strong>
    <div class="exercise">EXERCISE_DESCRIPTION</div>
    ...
  </div>
  <div class="connections">CONNECTIONS_TO_OTHER_CONCEPTS</div>
</div>
```

### Review Card HTML Structure:
```
<div class="concept-card review-card">
  <div class="concept-header">
    <span class="concept-title">TITLE</span>
    <span class="ttag">TOPIC</span>
    <span class="days-since">N days since review</span>
  </div>
  <div class="reminder">QUICK_REMINDER</div>
  <div class="key-pattern">
    <div class="lang-badge">Python</div>
    <pre><code>KEY_PATTERN_CODE</code></pre>
  </div>
  <div class="exercises">
    <strong>Challenge:</strong>
    <div class="exercise">HARDER_EXERCISE</div>
  </div>
  <div class="callout-warning">
    <strong>#1 Pitfall:</strong> COMMON_MISTAKE
  </div>
</div>
```

### Design Requirements

Same as the LeetCode guide:
- **Light/dark theme toggle** (default dark, GitHub-dark colors)
- **Self-contained**: single HTML file, inline CSS/JS, no CDN
- CSS custom properties in `:root` and `[data-theme="light"]`
- localStorage persistence for theme (key: `lc-pyguide-theme`)
- Topic badges: blue-tinted inline badges
- Code blocks: monospace, surface2 background, with output sections
- Output sections: slightly different background to distinguish from code
- **Exercises**: distinct visual style — dashed border, slight indent, exercise number badges
- Step indicators for multi-step explanations
- Typography: `-apple-system` stack, 16px body, 1.7 line-height
- Responsive: sidebar hidden below 900px
- Review section with distinct background (purple tint, like the LeetCode guide)

### Critical Rules

- **NEVER include exercise solutions** — only the problem statement and expected I/O
- Code examples must be **runnable** — show actual output, not pseudocode
- Each concept must give enough understanding to use it in real code immediately
- Show both **what to do** and **what NOT to do** (anti-patterns are powerful teachers)
- Concepts within each section build on each other — order matters
- Review section comes first, before new material
- **Track and update `python-guides/review-state.json`** after generating

### State Management

After generating, update `python-guides/review-state.json`:
- For new concepts introduced today: initialize with EF=2.5, n=0, I=1, last_reviewed=today, next_review=today+1
- For reviewed concepts: advance repetition, update interval per SM-2, assume q=4
- Each concept gets a stable `concept_id` (e.g., `fstring_debugging`, `list_comprehension`, `counter_basics`)

After generating, open with `open python-guide.html`.
