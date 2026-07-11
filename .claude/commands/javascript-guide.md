Generate a daily JavaScript programming study guide as a dated HTML file.

The guide's purpose: teach the user JavaScript programming concepts through progressive daily lessons with spaced repetition reinforcement. Each day introduces **new concepts** and **reviews previously learned concepts** based on the forgetting curve. The user should read a concept section, study the examples, then attempt the exercises without looking at hints.

## Core Learning Principles

1. **Spaced Repetition (SM-2)**: Previously learned concepts decay from memory. The guide includes a **Review Section** with concepts due for re-study. Each review resets retention.
2. **Retrieval Practice**: Exercises ask the user to write code from memory — not copy examples.
3. **Blocked → Interleaved Practice**: New topics are introduced in groups (e.g., all async topics together). Once a topic has been seen 2+ times, it's interleaved with other topics in reviews.
4. **Concrete-to-Abstract**: Start with simple examples, build to real-world patterns.
5. **Progressive Curriculum**: Concepts build on each other day-over-day, from intermediate to advanced JavaScript.

## File Naming and History

1. **Get today's date** by running `date +%Y-%m-%d`.
2. **Save** as `javascript-guides/javascript-guide-YYYY-MM-DD.html`.
3. **Create directory** if needed: `mkdir -p javascript-guides`.
4. **Update symlink**: `ln -sf javascript-guides/javascript-guide-YYYY-MM-DD.html javascript-guide.html`.
5. Same-day re-runs overwrite.

Include generation date in header. In the footer, list **all previous guides** found by running `ls javascript-guides/javascript-guide-*.html | sort -r`. For each file, extract the date from the filename and compute the day number (Day 1, Day 2, ...) based on chronological order. Link each entry using `javascript-guides/` prefix (e.g., `javascript-guides/javascript-guide-2026-06-09.html`) so links work when the file is opened via the root symlink `javascript-guide.html`. Mark the current day's entry with "(current)". Example footer list:
```html
<li><a href="javascript-guides/javascript-guide-2026-06-10.html">2026-06-10</a> (current &mdash; Day 3)</li>
<li><a href="javascript-guides/javascript-guide-2026-06-09.html">2026-06-09</a> (Day 2)</li>
<li><a href="javascript-guides/javascript-guide-2026-06-08.html">2026-06-08</a> (Day 1)</li>
```
Also update the footers of all existing previous guides to include links to the new guide being generated (so all guides cross-link to each other).

## Step 0: Gather State

1. **Load review state**: Read `javascript-guides/review-state.json` if it exists. Tracks SM-2 state for each learned concept:
   ```json
   {
     "concept_id": {
       "ef": 2.5,
       "interval": 6,
       "repetition": 2,
       "last_reviewed": "2026-06-08",
       "next_review": "2026-06-14",
       "topic": "Async",
       "title": "Promises & async/await"
     }
   }
   ```
   If the file doesn't exist, this is the first guide — initialize it after generating.

2. **Read past guides**: Check `javascript-guides/javascript-guide-*.html` to see what was covered previously. Avoid repeating new concepts that were already introduced.

3. **Determine review queue**: Select 4–6 concepts due for review (next_review <= today), prioritized by most overdue and lowest EF.

### SM-2 Implementation

Same as the LeetCode guide:
- **EF**: starts 2.5, minimum 1.3
- **Intervals**: I(1)=1, I(2)=6, I(n)=round(I(n-1) × EF) for n>2
- Assume q=4 (correct with hesitation) for automatic advancement

## Step 1: Select Today's Concepts

### JavaScript Curriculum (progressive order across days)

**Week 1 — Core Language Mastery:**
- Closures deep dive: lexical scoping, closure over loop variables, IIFE pattern, memory implications
- Prototypes & inheritance: prototype chain, `Object.create`, `__proto__` vs `prototype`, property lookup
- `this` binding: default, implicit, explicit (`call`/`apply`/`bind`), `new` binding, arrow functions, binding priority
- Symbols & well-known symbols: `Symbol()`, `Symbol.iterator`, `Symbol.toPrimitive`, `Symbol.hasInstance`
- Property descriptors & `Object.defineProperty`: writable, enumerable, configurable, getters/setters
- Proxy & Reflect: handler traps, `get`/`set`/`has`/`deleteProperty`, meta-programming patterns
- WeakRef & FinalizationRegistry: weak references, garbage collection hooks, caching patterns

**Week 2 — Functions & Iteration:**
- Generators & iterators: `function*`, `yield`, `yield*`, iterator protocol, `Symbol.iterator`
- Async generators & `for await...of`: async iteration, streaming data, backpressure
- Tagged template literals: tag functions, `String.raw`, DSL creation, SQL/HTML sanitization
- Destructuring advanced: nested, default values, computed keys, rest in destructuring
- Spread & rest: `...` in arrays/objects/arguments, shallow copy semantics, ordering
- Optional chaining & nullish coalescing: `?.`, `??`, `??=`, short-circuit behavior
- `Intl` API: `NumberFormat`, `DateTimeFormat`, `Collator`, `PluralRules`, `RelativeTimeFormat`

**Week 3 — Async Mastery:**
- Event loop deep dive: call stack, microtasks vs macrotasks, `queueMicrotask`, `setTimeout(fn, 0)` behavior
- Promise internals: states, `then` chaining, `Promise.all`, `Promise.allSettled`, `Promise.race`, `Promise.any`
- async/await patterns: error handling with try/catch, parallel execution, sequential vs concurrent
- AbortController & AbortSignal: cancelling fetch, cancelling custom async operations, timeout patterns
- Streams API: ReadableStream, WritableStream, TransformStream, piping, backpressure
- Web Workers: `postMessage`, `Transferable`, `SharedArrayBuffer`, `Atomics`
- Service Workers: lifecycle, caching strategies, offline-first patterns

**Week 4 — Data & Collections:**
- Map & Set: vs plain objects, insertion order, reference equality, WeakMap/WeakSet use cases
- Typed arrays & ArrayBuffer: `Int32Array`, `Float64Array`, `DataView`, endianness, binary protocols
- Structured clone: `structuredClone()`, transferable objects, limitations (no functions, no DOM)
- JSON advanced: `replacer`/`reviver`, `toJSON()` method, handling BigInt/Date/undefined
- Regular expressions advanced: named groups, lookbehind/lookahead, `matchAll`, `d` flag (indices), Unicode mode
- Temporal API (stage 3): `Temporal.PlainDate`, `Temporal.ZonedDateTime`, `Temporal.Duration`, comparison with Date
- Records & Tuples (stage 2): immutable data, `#{}`, `#[]`, structural equality

**Week 5 — Modules & Patterns:**
- ES modules deep dive: static imports, dynamic `import()`, `import.meta`, top-level await
- Module patterns: barrel files, circular dependency resolution, tree-shaking implications
- Design patterns: Observer/EventEmitter, Strategy, Command, Chain of Responsibility
- Functional patterns: composition, pipe, curry, partial application, point-free style
- Error handling patterns: custom error classes, `cause` property (ES2022), error boundaries concept
- Pub/Sub & EventTarget: custom events, `addEventListener` options, event delegation, `CustomEvent`
- Mixins & composition: `Object.assign`, class mixins, composition over inheritance

**Week 6 — Browser APIs & DOM:**
- DOM manipulation: `querySelector`, `createElement`, `DocumentFragment`, `MutationObserver`
- IntersectionObserver: lazy loading, infinite scroll, visibility tracking
- ResizeObserver & PerformanceObserver: responsive components, performance monitoring
- Fetch advanced: interceptors pattern, request/response cloning, streaming responses
- Web Storage & IndexedDB: `localStorage`/`sessionStorage` patterns, IndexedDB with promises
- Canvas & requestAnimationFrame: 2D context, animation loop, pixel manipulation
- Web Components: custom elements, Shadow DOM, HTML templates, slots

**Week 7 — Performance & Security:**
- Memory management: garbage collection, memory leaks (detached DOM, closures, event listeners)
- Performance: `requestIdleCallback`, `performance.mark/measure`, lazy evaluation, memoization
- Security: XSS prevention, CSP, `sanitize()`, trusted types, subresource integrity
- WebAssembly interop: loading `.wasm`, `WebAssembly.instantiate`, memory sharing, JS glue
- Debugging: `console` advanced (`table`, `group`, `time`, `trace`), breakpoints, source maps
- V8 internals overview: hidden classes, inline caching, JIT compilation, deoptimization triggers
- Polyfills & transpilation: core-js, Babel, feature detection vs user-agent sniffing

**Week 8+ — Node.js & Runtime:**
- Node.js event loop: phases, `setImmediate` vs `process.nextTick`, `libuv`
- Node.js streams: Readable, Writable, Transform, Duplex, pipeline, backpressure
- Node.js `fs/promises`, `path`, `url`, `crypto`: file system, path utilities, URL parsing, hashing
- `child_process`: `exec`, `spawn`, `fork`, IPC, streaming stdout/stderr
- Deno & Bun overview: permissions model, built-in TS, Web API compatibility
- Package management: npm/pnpm/yarn, `package.json`, `exports` field, peer dependencies
- Testing: Vitest, Jest, Node test runner, assertion styles, mocking ESM

Select **5–7 new concepts** for today based on where the user is in the curriculum. Group them into 2–3 topic sections.

## Step 2: Research Each Concept

For each concept (both new and review), produce:

### New Concept Card:
1. **Title and topic tag** (e.g., "Closures Deep Dive" / Core Language)
2. **Why it matters** — 1-2 sentences on when/why you'd use this in real code
3. **The concept explained** — clear explanation with progressive examples:
   - Start with the simplest possible example
   - Build to an intermediate example
   - Show a real-world usage pattern
4. **Code examples** — 3-5 runnable JavaScript snippets, each with comments explaining what happens. Show both the code AND its output. Examples should be complete and runnable in Node.js or browser console.
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

1. **Header**: "JavaScript Daily Guide", date, concept count
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
    <div class="lang-badge">JavaScript</div>
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
    <div class="lang-badge">JavaScript</div>
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
- localStorage persistence for theme (key: `lc-jsguide-theme`)
- Topic badges: blue-tinted inline badges
- Code blocks: monospace, surface2 background, with output sections
- Output sections: slightly different background to distinguish from code, must use `white-space: pre-wrap` to preserve newlines
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
- Include JavaScript-specific idioms and gotchas (e.g., `this` binding loss, `typeof null === 'object'`, floating point precision, `==` vs `===`, array sort lexicographic default, closure over loop variables)
- Concepts within each section build on each other — order matters
- Review section comes first, before new material
- **Track and update `javascript-guides/review-state.json`** after generating

### State Management

After generating, update `javascript-guides/review-state.json`:
- For new concepts introduced today: initialize with EF=2.5, n=0, I=1, last_reviewed=today, next_review=today+1
- For reviewed concepts: advance repetition, update interval per SM-2, assume q=4
- Each concept gets a stable `concept_id` (e.g., `closures_deep_dive`, `prototypes_inheritance`, `event_loop`)

After generating, open with `open javascript-guide.html`.
