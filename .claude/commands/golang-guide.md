Generate a daily Go (Golang) programming study guide as a dated HTML file.

The guide's purpose: teach the user Go programming concepts through progressive daily lessons with spaced repetition reinforcement. Each day introduces **new concepts** and **reviews previously learned concepts** based on the forgetting curve. The user should read a concept section, study the examples, then attempt the exercises without looking at hints.

## Core Learning Principles

1. **Spaced Repetition (SM-2)**: Previously learned concepts decay from memory. The guide includes a **Review Section** with concepts due for re-study. Each review resets retention.
2. **Retrieval Practice**: Exercises ask the user to write code from memory — not copy examples.
3. **Blocked → Interleaved Practice**: New topics are introduced in groups (e.g., all concurrency topics together). Once a topic has been seen 2+ times, it's interleaved with other topics in reviews.
4. **Concrete-to-Abstract**: Start with simple examples, build to real-world patterns.
5. **Progressive Curriculum**: Concepts build on each other day-over-day, from intermediate to advanced Go.

## File Naming and History

1. **Get today's date** by running `date +%Y-%m-%d`.
2. **Save** as `golang-guides/golang-guide-YYYY-MM-DD.html`.
3. **Create directory** if needed: `mkdir -p golang-guides`.
4. **Update symlink**: `ln -sf golang-guides/golang-guide-YYYY-MM-DD.html golang-guide.html`.
5. Same-day re-runs overwrite.

Include generation date in header. In the footer, list **all previous guides** found by running `ls golang-guides/golang-guide-*.html | sort -r`. For each file, extract the date from the filename and compute the day number (Day 1, Day 2, ...) based on chronological order. Link each entry using `golang-guides/` prefix (e.g., `golang-guides/golang-guide-2026-05-28.html`) so links work when the file is opened via the root symlink `golang-guide.html`. Mark the current day's entry with "(current)". Example footer list:
```html
<li><a href="golang-guides/golang-guide-2026-05-30.html">2026-05-30</a> (current &mdash; Day 3)</li>
<li><a href="golang-guides/golang-guide-2026-05-29.html">2026-05-29</a> (Day 2)</li>
<li><a href="golang-guides/golang-guide-2026-05-28.html">2026-05-28</a> (Day 1)</li>
```
Also update the footers of all existing previous guides to include links to the new guide being generated (so all guides cross-link to each other).

## Step 0: Gather State

1. **Load review state**: Read `golang-guides/review-state.json` if it exists. Tracks SM-2 state for each learned concept:
   ```json
   {
     "concept_id": {
       "ef": 2.5,
       "interval": 6,
       "repetition": 2,
       "last_reviewed": "2026-05-28",
       "next_review": "2026-06-03",
       "topic": "Concurrency",
       "title": "Goroutines & Channels"
     }
   }
   ```
   If the file doesn't exist, this is the first guide — initialize it after generating.

2. **Read past guides**: Check `golang-guides/golang-guide-*.html` to see what was covered previously. Avoid repeating new concepts that were already introduced.

3. **Determine review queue**: Select 4–6 concepts due for review (next_review <= today), prioritized by most overdue and lowest EF.

### SM-2 Implementation

Same as the LeetCode guide:
- **EF**: starts 2.5, minimum 1.3
- **Intervals**: I(1)=1, I(2)=6, I(n)=round(I(n-1) × EF) for n>2
- Assume q=4 (correct with hesitation) for automatic advancement

## Step 1: Select Today's Concepts

### Go Curriculum (progressive order across days)

**Week 1 — Go Foundations:**
- Slices deep dive: make, append, copy, slice expressions, capacity vs length, gotchas
- Maps: creation, iteration (random order!), comma-ok idiom, concurrent map access
- Strings & runes: UTF-8 encoding, `[]byte` vs `[]rune`, `strings` package, `strings.Builder`
- Structs & methods: value vs pointer receivers, embedding, method sets
- Pointers: when to use, pointer vs value semantics, nil pointers, `new()` vs `&T{}`
- Error handling: `error` interface, `fmt.Errorf`, `errors.Is`, `errors.As`, wrapping with `%w`
- Interfaces: implicit satisfaction, empty interface, type assertions, type switches

**Week 2 — Functions & Control Flow:**
- First-class functions: function types, closures, function literals, callbacks
- Defer, panic, recover: stack unwinding, defer ordering (LIFO), named returns with defer
- Init functions: `init()` ordering, package initialization, side effects
- Variadic functions: `...T`, unpacking slices, `append` internals
- Type parameters (generics): `[T any]`, `[T comparable]`, constraints, `~` underlying types
- Custom constraints: interface constraints, type sets, `constraints` package
- Multiple return values: error returns, comma-ok pattern, named returns

**Week 3 — Concurrency:**
- Goroutines: launching, scheduling, `runtime.GOMAXPROCS`, goroutine leaks
- Channels: buffered vs unbuffered, directional channels, closing, range over channel
- Select statement: multiplexing, timeout, default case, non-blocking operations
- sync package: `Mutex`, `RWMutex`, `WaitGroup`, `Once`, `Map`
- Context: `context.Background`, `WithCancel`, `WithTimeout`, `WithValue`, propagation
- Patterns: fan-out/fan-in, pipeline, worker pool, rate limiting, semaphore
- `errgroup`: concurrent error handling, first-error cancellation

**Week 4 — Standard Library Mastery:**
- `fmt`: verbs (`%v`, `%+v`, `%#v`, `%T`), `Stringer` interface, `Formatter` interface
- `io`: `Reader`, `Writer`, `io.Copy`, `io.TeeReader`, `io.Pipe`, composition
- `os` & `filepath`: file operations, path manipulation, environment variables
- `encoding/json`: struct tags, `Marshal`/`Unmarshal`, custom marshalers, `json.RawMessage`, streaming
- `net/http`: handlers, `ServeMux`, middleware pattern, `http.Client`, timeouts
- `sort`: `sort.Slice`, `sort.SliceStable`, `sort.Search`, implementing `sort.Interface`
- `time`: `Duration`, `Timer`, `Ticker`, `time.After`, parsing/formatting with reference time

**Week 5 — Testing & Tooling:**
- `testing` package: table-driven tests, subtests, `t.Run`, `t.Parallel`, `t.Helper`
- Benchmarks: `b.N`, `b.ResetTimer`, `b.ReportAllocs`, sub-benchmarks
- Test fixtures: `TestMain`, `t.TempDir`, `t.Cleanup`, golden files
- `httptest`: testing HTTP handlers, `httptest.NewServer`, `httptest.NewRecorder`
- Mocking: interfaces for testability, `//go:generate`, mock generation tools
- `go vet`, `staticcheck`, `golangci-lint`: static analysis, common linting rules
- Profiling: `pprof`, CPU profiling, memory profiling, trace tool

**Week 6 — Advanced Patterns:**
- Functional options pattern: `Option` type, `With*` functions, default configuration
- Middleware chains: `http.Handler` wrapping, composable middleware, `alice`-style chains
- Builder pattern: fluent APIs in Go, method chaining with pointer receivers
- Repository pattern: interface-based data access, testable with mocks
- `reflect` package: `TypeOf`, `ValueOf`, struct tags, dynamic dispatch
- `unsafe` package: `Pointer`, `Sizeof`, `Offsetof`, when (not) to use
- Code generation: `go generate`, `stringer`, `enumer`, template-based generation

**Week 7 — I/O & Networking:**
- `bufio`: buffered reading, `Scanner`, line-by-line processing, custom split functions
- `regexp`: compiled patterns, named groups, `FindAllStringSubmatch`
- `database/sql`: connection pools, prepared statements, transactions, `sql.Null*` types
- gRPC & protobuf: service definitions, code generation, streaming, interceptors
- WebSocket: `gorilla/websocket` patterns, concurrent read/write, ping/pong
- TCP servers: `net.Listener`, connection handling, graceful shutdown

**Week 8+ — Production Go:**
- Graceful shutdown: signal handling, `context` cancellation, drain connections
- Configuration: `viper`, environment variables, `envconfig`, 12-factor app
- Logging: `log/slog` (structured logging), levels, handlers, context-aware logging
- Observability: OpenTelemetry, tracing, metrics, span propagation
- Memory management: escape analysis, stack vs heap, `sync.Pool`, reducing allocations
- Module management: `go.mod`, versioning, replace directives, workspaces
- Cross-compilation: `GOOS`/`GOARCH`, build tags, conditional compilation

Select **5–7 new concepts** for today based on where the user is in the curriculum. Group them into 2–3 topic sections.

## Step 2: Research Each Concept

For each concept (both new and review), produce:

### New Concept Card:
1. **Title and topic tag** (e.g., "Goroutines & Channels" / Concurrency)
2. **Why it matters** — 1-2 sentences on when/why you'd use this in real code
3. **The concept explained** — clear explanation with progressive examples:
   - Start with the simplest possible example
   - Build to an intermediate example
   - Show a real-world usage pattern
4. **Code examples** — 3-5 runnable Go snippets, each with comments explaining what happens. Show both the code AND its output. Examples should be complete `main()` programs where practical.
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

1. **Header**: "Go Daily Guide", date, concept count
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
    <div class="lang-badge">Go</div>
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
    <div class="lang-badge">Go</div>
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
- localStorage persistence for theme (key: `lc-goguide-theme`)
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
- Include Go-specific idioms and gotchas (e.g., loop variable capture, nil slice vs empty slice, goroutine leaks, map concurrent access panic)
- Concepts within each section build on each other — order matters
- Review section comes first, before new material
- **Track and update `golang-guides/review-state.json`** after generating

### State Management

After generating, update `golang-guides/review-state.json`:
- For new concepts introduced today: initialize with EF=2.5, n=0, I=1, last_reviewed=today, next_review=today+1
- For reviewed concepts: advance repetition, update interval per SM-2, assume q=4
- Each concept gets a stable `concept_id` (e.g., `slices_deep_dive`, `goroutines_basics`, `channels_patterns`)

After generating, open with `open golang-guide.html`.
