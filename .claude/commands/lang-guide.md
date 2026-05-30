Generate a daily multi-language programming study guide as a dated HTML file.

The guide's purpose: teach the user programming concepts across **Python, Go, TypeScript, Rust, and C++** through progressive daily lessons with spaced repetition reinforcement. Each day introduces **new concepts** and **reviews previously learned concepts** based on the forgetting curve. For each concept, the guide shows idiomatic implementations in all five languages side-by-side, highlighting how different paradigms approach the same problem.

## Core Learning Principles

1. **Spaced Repetition (SM-2)**: Previously learned concepts decay from memory. The guide includes a **Review Section** with concepts due for re-study. Each review resets retention.
2. **Retrieval Practice**: Exercises ask the user to write code from memory — not copy examples.
3. **Blocked → Interleaved Practice**: New topics are introduced in groups (e.g., all collection topics together). Once a topic has been seen 2+ times, it's interleaved with other topics in reviews.
4. **Concrete-to-Abstract**: Start with simple examples, build to real-world patterns.
5. **Progressive Curriculum**: Concepts build on each other day-over-day, from intermediate to advanced.
6. **Cross-Paradigm Fluency**: Seeing the same concept in dynamic (Python), GC-compiled (Go), typed-compiled (TypeScript), ownership-based (Rust), and manual-memory (C++) languages builds deep understanding of *why* languages differ, not just *how*.

## File Naming and History

1. **Get today's date** by running `date +%Y-%m-%d`.
2. **Save** as `lang-guides/lang-guide-YYYY-MM-DD.html`.
3. **Create directory** if needed: `mkdir -p lang-guides`.
4. **Update symlink**: `ln -sf lang-guides/lang-guide-YYYY-MM-DD.html lang-guide.html`.
5. Same-day re-runs overwrite.

Include generation date in header. In the footer, list **all previous guides** found by running `ls lang-guides/lang-guide-*.html | sort -r`. For each file, extract the date from the filename and compute the day number (Day 1, Day 2, ...) based on chronological order. Link each entry using a relative path (e.g., `lang-guide-2026-05-29.html` — no `lang-guides/` prefix since the current file is already inside `lang-guides/`). Mark the current day's entry with "(current)". Example footer list:
```html
<li><a href="lang-guide-2026-05-30.html">2026-05-30</a> (current &mdash; Day 2)</li>
<li><a href="lang-guide-2026-05-29.html">2026-05-29</a> (Day 1)</li>
```
Also update the footers of all existing previous guides to include links to the new guide being generated (so all guides cross-link to each other with correct relative paths).

## Step 0: Gather State

1. **Load review state**: Read `lang-guides/review-state.json` if it exists. Tracks SM-2 state for each learned concept:
   ```json
   {
     "concept_id": {
       "ef": 2.5,
       "interval": 6,
       "repetition": 2,
       "last_reviewed": "2026-05-28",
       "next_review": "2026-06-03",
       "topic": "Collections",
       "title": "Hash Maps & Sets"
     }
   }
   ```
   If the file doesn't exist, this is the first guide — initialize it after generating.

2. **Read past guides**: Check `lang-guides/lang-guide-*.html` to see what was covered previously. Avoid repeating new concepts that were already introduced.

3. **Determine review queue**: Select 4–6 concepts due for review (next_review <= today), prioritized by most overdue and lowest EF.

### SM-2 Implementation

Same as the LeetCode guide:
- **EF**: starts 2.5, minimum 1.3
- **Intervals**: I(1)=1, I(2)=6, I(n)=round(I(n-1) × EF) for n>2
- Assume q=4 (correct with hesitation) for automatic advancement

## Step 1: Select Today's Concepts

### Multi-Language Curriculum (progressive order across days)

**Week 1 — Data Structures & Collections:**
- Arrays/slices/vectors: creation, indexing, slicing, iteration
- Hash maps & hash sets: insertion, lookup, iteration, frequency counting
- Strings: immutability vs mutability, Unicode, common operations, formatting
- Stacks & queues: push/pop idioms, deques, LIFO/FIFO patterns
- Tuples, structs, and records: named data, destructuring, pattern matching
- Sorting: built-in sort, custom comparators, stable vs unstable
- Linked lists & trees: node definitions, ownership patterns, recursive structures

**Week 2 — Control Flow & Iteration:**
- Iterators & generators: lazy evaluation, chaining, map/filter/reduce
- Pattern matching: switch/match/when, exhaustiveness, destructuring
- Error handling: exceptions vs Result vs error returns vs try/catch
- Closures & lambdas: capture semantics, lifetimes, function types
- Enums & algebraic data types: Option/Maybe, Result, tagged unions
- Range-based iteration: for-in, range(), iterators, enumerate
- Concurrency primitives: goroutines, async/await, threads, tokio, std::thread

**Week 3 — Functions & Abstractions:**
- Higher-order functions: map, filter, reduce, fold across languages
- Generic programming: templates (C++), generics (Go/Rust/TS), duck typing (Python)
- Interfaces & traits: Go interfaces, Rust traits, TS interfaces, Python Protocol, C++ concepts
- Decorators/middleware: Python decorators, Go middleware, TS decorators, Rust macros, C++ CRTP
- Module systems: Python packages, Go modules, TS/ES modules, Rust crates, C++ headers/modules
- Builder pattern & method chaining across languages
- Smart pointers & memory: Python refs, Go GC, TS GC, Rust Box/Rc/Arc, C++ unique_ptr/shared_ptr

**Week 4 — I/O & Data Processing:**
- File I/O: reading/writing files idiomatically in each language
- JSON handling: parsing, serializing, type safety across languages
- String formatting & interpolation: f-strings, fmt, template literals, format!, std::format
- Regular expressions: syntax differences, named groups, common patterns
- Command-line argument parsing: argparse, flag, commander, clap, getopt
- HTTP clients: requests, net/http, fetch, reqwest, libcurl
- CSV/data processing: pandas vs standard library approaches

**Week 5 — Testing & Error Handling:**
- Unit testing: pytest, go test, jest/vitest, cargo test, gtest/catch2
- Mocking & test doubles across languages
- Assertion patterns and custom matchers
- Benchmarking: timeit, go bench, vitest bench, criterion, google benchmark
- Logging: logging, log/slog, winston/pino, tracing, spdlog
- Type systems deep dive: gradual typing, structural typing, nominal typing, type inference

**Week 6 — Advanced Patterns:**
- Async/await deep dive: asyncio, goroutines+channels, Promise, tokio, std::async/coroutines
- Serialization/deserialization: pickle, encoding/gob, class-transformer, serde, cereal/boost
- Design patterns: iterator, observer, strategy, factory across paradigms
- Metaprogramming: Python metaclasses, Go generate, TS decorators, Rust proc macros, C++ templates
- Memory management: GC tuning, ownership patterns, RAII, move semantics
- FFI & interop: ctypes/cffi, cgo, node-ffi/wasm, Rust FFI, extern "C"

**Week 7+ — Language-Specific Deep Dives:**
- Python: comprehensions, dataclasses, asyncio internals, GIL
- Go: goroutine scheduling, channels patterns, context, reflect
- TypeScript: type gymnastics, conditional types, template literal types, satisfies
- Rust: lifetimes, trait objects, unsafe, async runtimes, macros
- C++: SFINAE, concepts (C++20), ranges (C++20), coroutines, move semantics

Select **4–6 new concepts** for today based on where the user is in the curriculum. Group them into 2–3 topic sections.

## Step 2: Research Each Concept

For each concept (both new and review), produce:

### New Concept Card:
1. **Title and topic tag** (e.g., "Hash Maps & Sets" / Collections)
2. **Why it matters** — 1-2 sentences on when/why you'd use this in real code
3. **The concept explained** — clear explanation with progressive examples:
   - Start with the simplest possible example
   - Build to an intermediate example
   - Show a real-world usage pattern
4. **Code examples in ALL 5 LANGUAGES** — for each example, show idiomatic implementations side-by-side:
   - Python: Pythonic idioms, standard library
   - Go: idiomatic Go, standard library
   - TypeScript: modern TS with proper types
   - Rust: idiomatic Rust with ownership patterns
   - C++: modern C++17/20 with STL
   
   Show both the code AND its output. Use `data-lang` attributes on each block for the language toggle. Each code block should be RUNNABLE — not pseudocode. Show 3-5 progressive examples per concept.

5. **Language comparison callout** — a brief box highlighting the key difference in how each language approaches this concept. E.g., "Python uses `dict()` with dynamic typing, Go uses `map[K]V` with static types, Rust uses `HashMap<K,V>` with ownership, C++ uses `unordered_map<K,V>` with RAII, TypeScript uses `Map<K,V>` with structural typing."

6. **Common mistakes per language** — specific anti-patterns with corrections:
   - Show the WRONG way (with ❌ marker) and RIGHT way (with ✅ marker)
   - Include at least one mistake that's language-specific (e.g., forgetting `&` in Rust iterations, Go map iteration order, C++ iterator invalidation, TS array sort being lexicographic)

7. **Key rules** — 2-3 bullet points summarizing when to use (and when NOT to use) this feature

8. **Practice exercises** — 2-3 small coding challenges the user should attempt in ALL 5 LANGUAGES without looking at examples:
   - State the problem clearly
   - Include expected input/output
   - Do NOT include solutions
   - Order from easy to harder
   - Specify: "Implement in all 5 languages"

9. **Connections** — how this concept relates to previously learned or upcoming concepts

### Review Concept Card (condensed):
1. **Title, topic, days since last review**
2. **Quick reminder** — 1-2 sentence refresher
3. **Key pattern per language** — the most important code snippet in each of the 5 languages
4. **Challenge exercise** — a single harder exercise to attempt in all 5 languages
5. **Common mistake recap** — the #1 pitfall per language for this concept

## Step 3: Generate the HTML Guide

### Layout
- **Fixed left sidebar** (300px) with navigation grouped by: Review, then topic sections
- **Main content area** (max-width 920px)
- Sidebar collapses below 900px

### Content Structure

1. **Header**: "Multi-Language Daily Guide", date, concept count, "Python · Go · TypeScript · Rust · C++"
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
  
  <!-- For each example, show all 5 languages -->
  <div class="code-example">
    <div data-lang="python"><div class="lang-badge">Python</div><pre><code>CODE</code></pre><div class="output">OUTPUT</div></div>
    <div data-lang="go"><div class="lang-badge">Go</div><pre><code>CODE</code></pre><div class="output">OUTPUT</div></div>
    <div data-lang="typescript"><div class="lang-badge">TypeScript</div><pre><code>CODE</code></pre><div class="output">OUTPUT</div></div>
    <div data-lang="rust"><div class="lang-badge">Rust</div><pre><code>CODE</code></pre><div class="output">OUTPUT</div></div>
    <div data-lang="cpp"><div class="lang-badge">C++</div><pre><code>CODE</code></pre><div class="output">OUTPUT</div></div>
  </div>
  (repeat for each example)
  
  <div class="callout-insight">
    <strong>Language Comparison:</strong> COMPARISON_TEXT
  </div>
  
  <div class="callout-warning">
    <strong>Common Mistakes:</strong>
    <div class="mistake">❌ [Python] WRONG_WAY</div>
    <div class="correct">✅ [Python] RIGHT_WAY</div>
    <div class="mistake">❌ [Go] WRONG_WAY</div>
    <div class="correct">✅ [Go] RIGHT_WAY</div>
    <!-- etc. for each language with language-specific pitfalls -->
  </div>
  
  <div class="key-rules">
    <strong>Key Rules:</strong>
    <ul><li>RULE</li>...</ul>
  </div>
  
  <div class="exercises">
    <strong>Practice Exercises (implement in all 5 languages):</strong>
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
    <div data-lang="python"><div class="lang-badge">Python</div><pre><code>KEY_PATTERN</code></pre></div>
    <div data-lang="go"><div class="lang-badge">Go</div><pre><code>KEY_PATTERN</code></pre></div>
    <div data-lang="typescript"><div class="lang-badge">TypeScript</div><pre><code>KEY_PATTERN</code></pre></div>
    <div data-lang="rust"><div class="lang-badge">Rust</div><pre><code>KEY_PATTERN</code></pre></div>
    <div data-lang="cpp"><div class="lang-badge">C++</div><pre><code>KEY_PATTERN</code></pre></div>
  </div>
  <div class="exercises">
    <strong>Challenge (all 5 languages):</strong>
    <div class="exercise">HARDER_EXERCISE</div>
  </div>
  <div class="callout-warning">
    <strong>#1 Pitfall per Language:</strong>
    <ul>
      <li><strong>Python:</strong> PITFALL</li>
      <li><strong>Go:</strong> PITFALL</li>
      <li><strong>TypeScript:</strong> PITFALL</li>
      <li><strong>Rust:</strong> PITFALL</li>
      <li><strong>C++:</strong> PITFALL</li>
    </ul>
  </div>
</div>
```

### Design Requirements

- **Light/dark theme toggle** (default dark, GitHub-dark colors)
- **Language toggle** — global toggle: All | Python | Go | TS | Rust | C++. Default: show all stacked. Each language block has `data-lang="python"`, `data-lang="go"`, `data-lang="typescript"`, `data-lang="rust"`, `data-lang="cpp"`. Persist in `localStorage` (key: `lc-langguide-lang`).
- **Self-contained**: single HTML file, inline CSS/JS, no CDN
- CSS custom properties in `:root` and `[data-theme="light"]`
- localStorage persistence for theme (key: `lc-langguide-theme`)
- Topic badges: blue-tinted inline badges
- Code blocks: monospace, surface2 background, with output sections
- Output sections: slightly different background (green-tinted) to distinguish from code
- **Exercises**: distinct visual style — dashed border, slight indent, exercise number badges
- **Language comparison callouts**: blue left border with insight styling
- Typography: `-apple-system` stack, 16px body, 1.7 line-height
- Responsive: sidebar hidden below 900px
- Review section with distinct background (purple tint)
- **Max-width 920px** for main content (wider than Python guide to accommodate 5 language blocks)

### Critical Rules

- **NEVER include exercise solutions** — only the problem statement and expected I/O
- Code examples must be **runnable** — show actual output, not pseudocode
- ALL code examples must be shown in ALL 5 LANGUAGES — this is a cross-language learning tool
- Each concept must give enough understanding to use it in real code immediately in ANY of the 5 languages
- Show both **what to do** and **what NOT to do** (language-specific anti-patterns are powerful teachers)
- Include language-specific gotchas (Go map iteration order, Rust ownership, C++ iterator invalidation, TS lexicographic sort, Python mutable default args)
- Concepts within each section build on each other — order matters
- Review section comes first, before new material
- **Track and update `lang-guides/review-state.json`** after generating

### State Management

After generating, update `lang-guides/review-state.json`:
- For new concepts introduced today: initialize with EF=2.5, n=0, I=1, last_reviewed=today, next_review=today+1
- For reviewed concepts: advance repetition, update interval per SM-2, assume q=4
- Each concept gets a stable `concept_id` (e.g., `hash_maps_sets`, `iterators_generators`, `error_handling`)

After generating, open with `open lang-guide.html`.
