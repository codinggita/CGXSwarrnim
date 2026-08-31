## Paragraph (`<p>`) Tag & Heading Tags (`<h1>`–`<h6>`)

### 1. Paragraph Tag – `<p>`

**Purpose**  
The `<p>` tag is used to define a **paragraph** of text. Browsers automatically add some space (margin) before and after a paragraph.

**Basic Syntax**
```html
<p>This is a paragraph of text.</p>
```

**Key Points**
- It is a **block-level** element (starts on a new line and takes full available width).
- You should **not** put block-level elements (like headings, lists, or other paragraphs) inside a `<p>` tag.
- Closing the tag (`</p>`) is required in HTML5 for best practice (though some browsers may auto-close it).

**Common Attributes for `<p>`**

| Attribute     | Description                                      | Example |
|---------------|--------------------------------------------------|---------|
| `title`       | Tooltip text shown on hover                      | `<p title="Extra info">...</p>` |
| `lang`        | Language of the paragraph content                | `<p lang="en">...</p>` |
| `dir`         | Text direction (`ltr` or `rtl`)                  | `<p dir="rtl">...</p>` |
| `align`       | Text alignment (**Deprecated** – use CSS instead)| `<p align="center">...</p>` |

> **Note**: Prefer CSS (`text-align`, `margin`, `padding`, etc.) over the old `align` attribute.

---

### 2. Heading Tags – `<h1>` to `<h6>`

**Purpose**  
Heading tags define **headings** of different importance levels.  
They create a clear structure for both users and search engines (SEO).

**Hierarchy**
| Tag   | Level          | Typical Use                  | Default Size (approx.) |
|-------|----------------|------------------------------|------------------------|
| `<h1>` | Most important | Main page title              | Largest                |
| `<h2>` | Second level   | Major section headings       | Large                  |
| `<h3>` | Third level    | Sub-section headings         | Medium-large           |
| `<h4>` | Fourth level   | Smaller sub-headings         | Medium                 |
| `<h5>` | Fifth level    | Minor headings               | Small-medium           |
| `<h6>` | Least important| Least significant headings   | Smallest               |

**Basic Syntax**
```html
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<h3>Sub-sub Heading</h3>
<!-- ... up to h6 -->
```

**Key Points**
- Headings are **block-level** elements.
- Use them in **logical order** (don’t skip levels randomly, e.g., don’t jump from `<h1>` to `<h4>` without reason).
- There should normally be **only one `<h1>`** per page (main title).
- Search engines give higher weight to content inside higher-level headings.

**Common Attributes for Heading Tags (`<h1>`–`<h6>`)**

| Attribute     | Description                                      | Example |
|---------------|--------------------------------------------------|---------|
| `title`       | Tooltip on hover                                 | `<h2 title="Click for more">...</h2>` |
| `lang`        | Language of the heading                          | `<h1 lang="hi">...</h1>` |
| `dir`         | Text direction                                   | `<h1 dir="rtl">...</h1>` |
| `align`       | Text alignment (**Deprecated**)                  | `<h1 align="center">...</h1>` |

---

### Quick Comparison

| Feature              | `<p>` Tag                          | `<h1>`–`<h6>` Tags                     |
|----------------------|------------------------------------|----------------------------------------|
| Purpose              | Paragraph of text                  | Hierarchical headings                  |
| SEO Importance       | Low                                | High (especially `<h1>` & `<h2>`)      |
| Default Spacing      | Margin above & below               | Larger margins + bold by default       |
| Can contain          | Inline elements + text             | Inline elements + text                 |
| Best Practice        | Use for body text                  | Use for document structure             |

---
