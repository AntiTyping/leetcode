Generate a daily TypeScript programming study guide as a dated HTML file.

The guide's purpose: teach the user TypeScript programming concepts through progressive daily lessons with spaced repetition reinforcement. Each day introduces **new concepts** and **reviews previously learned concepts** based on the forgetting curve. The user should read a concept section, study the examples, then attempt the exercises without looking at hints.

## Core Learning Principles

1. **Spaced Repetition (SM-2)**: Previously learned concepts decay from memory. The guide includes a **Review Section** with concepts due for re-study. Each review resets retention.
2. **Retrieval Practice**: Exercises ask the user to write code from memory — not copy examples.
3. **Blocked → Interleaved Practice**: New topics are introduced in groups (e.g., all type system topics together). Once a topic has been seen 2+ times, it's interleaved with other topics in reviews.
4. **Concrete-to-Abstract**: Start with simple examples, build to real-world patterns.
5. **Progressive Curriculum**: Concepts build on each other day-over-day, from intermediate to advanced TypeScript.

## File Naming and History

1. **Get today's date** by running `date +%Y-%m-%d`.
2. **Save** as `typescript-guides/typescript-guide-YYYY-MM-DD.html`.
3. **Create directory** if needed: `mkdir -p typescript-guides`.
4. **Update symlink**: `ln -sf typescript-guides/typescript-guide-YYYY-MM-DD.html typescript-guide.html`.
5. Same-day re-runs overwrite.

Include generation date in header. In the footer, list **all previous guides** found by running `ls typescript-guides/typescript-guide-*.html | sort -r`. For each file, extract the date from the filename and compute the day number (Day 1, Day 2, ...) based on chronological order. Link each entry using `typescript-guides/` prefix (e.g., `typescript-guides/typescript-guide-2026-05-28.html`) so links work when the file is opened via the root symlink `typescript-guide.html`. Mark the current day's entry with "(current)". Example footer list:
```html
<li><a href="typescript-guides/typescript-guide-2026-05-30.html">2026-05-30</a> (current &mdash; Day 3)</li>
<li><a href="typescript-guides/typescript-guide-2026-05-29.html">2026-05-29</a> (Day 2)</li>
<li><a href="typescript-guides/typescript-guide-2026-05-28.html">2026-05-28</a> (Day 1)</li>
```

## Step 0: Gather State

1. **Load review state**: Read `typescript-guides/review-state.json` if it exists. Tracks SM-2 state for each learned concept:
   ```json
   {
     "concept_id": {
       "ef": 2.5,
       "interval": 6,
       "repetition": 2,
       "last_reviewed": "2026-05-28",
       "next_review": "2026-06-03",
       "topic": "type_system",
       "title": "Literal Types & const Assertions"
     }
   }
   ```
   If the file doesn't exist, this is the first guide — initialize it after generating.

2. **Read past guides**: Check `typescript-guides/typescript-guide-*.html` to see what was covered previously. Avoid repeating new concepts that were already introduced.

3. **Determine review queue**: Select 4–6 concepts due for review (next_review <= today), prioritized by most overdue and lowest EF.

### SM-2 Implementation

Same as the LeetCode guide:
- **EF**: starts 2.5, minimum 1.3
- **Intervals**: I(1)=1, I(2)=6, I(n)=round(I(n-1) × EF) for n>2
- Assume q=4 (correct with hesitation) for automatic advancement

## Step 1: Select Today's Concepts

### TypeScript Curriculum (progressive order across days)

**Week 1 — TypeScript Foundations:**
- Type annotations: primitives, arrays, tuples, objects, function signatures
- Union types & narrowing: type guards, `typeof`, `instanceof`, discriminated unions
- Literal types & const assertions: `as const`, template literal types, string enums vs literal unions
- Interfaces vs type aliases: when to use each, extending, merging, implementing
- Enums: numeric, string, const enums, enum alternatives (literal unions)
- Generics basics: generic functions, generic interfaces, generic constraints with `extends`
- Utility types: `Partial`, `Required`, `Pick`, `Omit`, `Record`, `Readonly`

**Week 2 — Advanced Type System:**
- Conditional types: `T extends U ? X : Y`, `infer` keyword, distributive conditionals
- Mapped types: `{ [K in keyof T]: ... }`, key remapping with `as`, template literal keys
- Template literal types: string manipulation at the type level, `Uppercase`, `Lowercase`, `Capitalize`
- `keyof` and indexed access types: `T[K]`, `typeof`, type queries
- Type predicates & assertion functions: `is` keyword, `asserts` keyword, custom type guards
- `satisfies` operator: type checking without widening, const context preservation
- `never` and exhaustiveness: exhaustive switch, unreachable code, bottom type uses

**Week 3 — Functions & Patterns:**
- Function overloads: overload signatures, implementation signature, when to use vs unions
- Generic constraints & defaults: `extends`, default type parameters, `infer` in constraints
- Decorators (TC39): class decorators, method decorators, parameter decorators, decorator factories
- Builder pattern with types: fluent APIs, method chaining with narrowing return types
- Branded/opaque types: nominal typing in a structural system, `unique symbol`, tagged types
- `this` types & fluent interfaces: polymorphic `this`, method chaining in class hierarchies
- Async patterns: `Promise<T>`, async/await typing, `Awaited<T>`, async iterators

**Week 4 — Modules & Project Structure:**
- Module systems: ESM vs CJS, `import`/`export`, re-exports, barrel files
- Declaration files: `.d.ts`, `declare module`, ambient declarations, `@types` packages
- `tsconfig.json` deep dive: `strict` flags, `paths`, `baseUrl`, `moduleResolution`
- Namespaces vs modules: when namespaces still make sense, module augmentation
- Project references: composite projects, `references`, incremental builds
- Package publishing: `exports` field, dual CJS/ESM packages, `types` resolution

**Week 5 — Runtime Patterns:**
- Zod & runtime validation: schema definition, parsing, type inference from schemas
- Error handling patterns: Result type, tagged errors, `never` for exhaustive error handling
- Discriminated unions in practice: state machines, event systems, API responses
- Immutability patterns: `readonly`, `Readonly<T>`, `ReadonlyArray`, `Object.freeze` typing
- Class patterns: abstract classes, mixins, private fields (`#field`), static blocks
- `Proxy` and `Reflect` typing: handler types, meta-programming with type safety

**Week 6 — Advanced Patterns & Performance:**
- Type-level programming: recursive types, variadic tuple types, `[...T, ...U]`
- `infer` mastery: extracting types from complex structures, conditional inference
- Covariance & contravariance: `in`/`out` modifiers, function parameter types, generic variance
- Performance: avoiding excessive type instantiation, `--generateTrace`, type-level benchmarking
- Module federation typing: shared types across micro-frontends, dynamic imports
- Testing types: `tsd`, `expect-type`, type-level unit tests

**Week 7+ — Ecosystem Deep Dives:**
- React + TypeScript: component props, hooks typing, context, generic components, forwardRef
- Node.js + TypeScript: `@types/node`, streams, worker threads, native ESM
- API typing: tRPC, GraphQL codegen, OpenAPI → TypeScript, Zod integration
- State management typing: Redux Toolkit, Zustand, XState with TypeScript
- Database typing: Prisma, Drizzle, type-safe SQL builders

Select **5–7 new concepts** for today based on where the user is in the curriculum. Group them into 2–3 topic sections.

## Step 2: Research Each Concept

For each concept (both new and review), produce:

### New Concept Card:
1. **Title and topic tag** (e.g., "Literal Types & const Assertions" / Type System)
2. **Why it matters** — 1-2 sentences on when/why you'd use this in real code
3. **The concept explained** — clear explanation with progressive examples:
   - Start with the simplest possible example
   - Build to an intermediate example
   - Show a real-world usage pattern
4. **Code examples** — 3-5 runnable TypeScript snippets, each with comments explaining what happens. Show both the code AND its output (or type errors where relevant).
5. **Common mistakes** — specific anti-patterns with corrections:
   - Show the WRONG way (with ❌ marker)
   - Show the RIGHT way (with ✅ marker)
6. **Key rules** — 2-3 bullet points summarizing when to use (and when NOT to use) this feature
7. **Practice exercises** — 2-3 small coding challenges the user should attempt WITHOUT looking at examples:
   - State the problem clearly
   - Include expected input/output or expected type behavior
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

1. **Header**: "TypeScript Daily Guide", date, concept count
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
    <div class="lang-badge">TypeScript</div>
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
    <div class="lang-badge">TypeScript</div>
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
- localStorage persistence for theme (key: `lc-tsguide-theme`)
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
- **Track and update `typescript-guides/review-state.json`** after generating

### State Management

After generating, update `typescript-guides/review-state.json`:
- For new concepts introduced today: initialize with EF=2.5, n=0, I=1, last_reviewed=today, next_review=today+1
- For reviewed concepts: advance repetition, update interval per SM-2, assume q=4
- Each concept gets a stable `concept_id` (e.g., `union_narrowing`, `generics_basics`, `utility_types`)

After generating, open with `open typescript-guide.html`.
