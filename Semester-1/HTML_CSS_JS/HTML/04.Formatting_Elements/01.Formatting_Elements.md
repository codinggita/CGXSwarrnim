# HTML Formatting Elements

HTML provides various formatting elements to style and structure text content on a webpage. These elements enhance the presentation and semantics of text, making it more readable and visually appealing. Below is an explanation of common HTML formatting elements.

## 1. `<b>` - Bold Text
The `<b>` element makes text bold, emphasizing its visual weight without implying semantic importance.

- **Purpose**: Visually highlights text.
- **Example**:
  ```html
  <p>Learn programming at <b>Coding Gita</b> to master web development.</p>
  ```
  The text "Coding Gita" appears bold.

## 2. `<i>` - Italic Text
The `<i>` element italicizes text, often used for emphasis or to denote special terms.

- **Purpose**: Adds visual emphasis or denotes alternate voice/style.
- **Example**:
  ```html
  <p>SwamiNarayan University offers courses in <i>Computer Science</i>.</p>
  ```
  The text "Computer Science" appears in italics.

## 3. `<strong>` - Important Text
The `<strong>` element indicates text with strong importance, typically displayed as bold, but with semantic significance.

- **Purpose**: Emphasizes important content for accessibility and SEO.
- **Example**:
  ```html
  <p><strong>Coding Gita</strong> provides hands-on coding workshops for beginners.</p>
  ```
  The text "Coding Gita" is bolded and marked as important.

## 4. `<em>` - Emphasized Text
The `<em>` element emphasizes text, typically displayed as italicized, indicating stress or importance.

- **Purpose**: Adds semantic emphasis, often for tone or stress.
- **Example**:
  ```html
  <p>At SwamiNarayan University, students are <em>encouraged</em> to innovate.</p>
  ```
  The text "encouraged" appears italicized with semantic emphasis.

## 5. `<mark>` - Highlighted Text
The `<mark>` element highlights text, usually with a yellow background, to draw attention.

- **Purpose**: Marks text as relevant or noteworthy.
- **Example**:
  ```html
  <p>Join <mark>Coding Gita</mark> for the latest AI programming course!</p>
  ```
  The text "Coding Gita" is highlighted with a yellow background.

## 6. `<small>` - Smaller Text
The `<small>` element reduces the font size of text, often used for fine print or side notes.

- **Purpose**: Denotes secondary or less prominent information.
- **Example**:
  ```html
  <p>SwamiNarayan University offers degrees. <small>Apply by December!</small></p>
  ```
  The text "Apply by December!" appears in a smaller font size.

## 7. `<del>` - Deleted Text
The `<del>` element marks text as deleted, typically displayed with a strikethrough.

- **Purpose**: Indicates text that has been removed or is no longer valid.
- **Example**:
  ```html
  <p>Coding Gita's old course fee: <del>$100</del>. New fee: $80.</p>
  ```
  The text "$100" appears with a strikethrough.

## 8. `<ins>` - Inserted Text
The `<ins>` element marks text as inserted, typically underlined, indicating new content.

- **Purpose**: Highlights newly added text.
- **Example**:
  ```html
  <p>SwamiNarayan University now offers <ins>Data Science</ins> programs.</p>
  ```
  The text "Data Science" appears underlined.

## 9. `<sub>` - Subscript Text
The `<sub>` element formats text as subscript, often used for chemical formulas or footnotes.

- **Purpose**: Displays text below the baseline.
- **Example**:
  ```html
  <p>Coding Gita teaches algorithms like A<sub>n</sub> for sorting.</p>
  ```
  The text "n" appears as subscript.

## 10. `<sup>` - Superscript Text
The `<sup>` element formats text as superscript, often used for exponents or ordinals.

- **Purpose**: Displays text above the baseline.
- **Example**:
  ```html
  <p>SwamiNarayan University's 2<sup>nd</sup> annual tech fest is coming!</p>
  ```
  The text "nd" appears as superscript.
# HTML Quotation and Citation Elements

HTML provides several elements for quoting, citing, and providing additional context to content, such as abbreviations and contact information. These elements include `<blockquote>`, `<q>`, `<abbr>`, `<address>`, `<cite>`, and `<bdo>`. Below is an explanation of each element, including their attributes and usage, with examples.

## 1. `<blockquote>` Element
The `<blockquote>` element defines a section quoted from another source, typically rendered with indentation by browsers. It is a block-level element, used for longer quotations.

- **Attributes**:
  - `cite`: Specifies the URL of the source of the quotation (not visible in browsers but accessible to scripts or screen readers).
- **Example**:
  ```html
  <p>From a recent Coding Gita workshop:</p>
  <blockquote cite="https://codinggita.com/workshops">
    Our practical sessions focus on real-world coding projects to enhance student skills.
  </blockquote>
  ```
  This displays the quoted text indented, with the `cite` attribute linking to the workshop page.

## 2. `<q>` Element
The `<q>` element defines a short, inline quotation. Browsers typically insert quotation marks around the content.

- **Attributes**:
  - `cite`: Specifies the URL of the source of the quotation, similar to `<blockquote>`.
- **Example**:
  ```html
  <p>SwamiNarayan University’s mission is: <q cite="https://swaminarayanuniversity.ac.in/about">To foster innovation through practical learning.</q></p>
  ```
  The text within `<q>` is displayed with quotation marks, and the `cite` attribute provides the source URL.

## 3. `<abbr>` Element
The `<abbr>` element defines an abbreviation or acronym, with the `title` attribute providing the full description, shown on hover.

- **Attributes**:
  - `title`: Specifies the full form or description of the abbreviation/acronym.
- **Example**:
  ```html
  <p>Coding Gita collaborates with <abbr title="SwamiNarayan University">SNU</abbr> for advanced tech programs.</p>
  ```
  Hovering over "SNU" displays the tooltip "SwamiNarayan University".

## 4. `<address>` Element
The `<address>` element defines contact information for the author or owner of a document or article, typically rendered in italics with line breaks before and after.

- **Attributes**: Supports global attributes (e.g., `class`, `id`).
- **Example**:
  ```html
  <address>
    Coding Gita<br>
    Shree Swaminarayan Vishvamangal Gurukul<br>
    Ahmedabad-Mehsana Highway, Saij, Kalol<br>
    Gandhinagar, Gujarat 382725
  </address>
  ```
  The contact information is displayed in italics, with line breaks as shown.

## 5. `<cite>` Element
The `<cite>` element defines the title of a creative work (e.g., book, article, course), typically rendered in italics. Note: A person's name is not considered a work title.

- **Attributes**: Supports global attributes.
- **Example**:
  ```html
  <p><cite>Full Stack Development 2025</cite> is a flagship course by Coding Gita.</p>
  ```
  The text "Full Stack Development 2025" is displayed in italics, indicating the course title.

## 6. `<bdo>` Element
The `<bdo>` (Bi-Directional Override) element overrides the text direction, useful for languages written right-to-left (e.g., Arabic, Hebrew).

- **Attributes**:
  - `dir`: Specifies the text direction (`ltr` for left-to-right or `rtl` for right-to-left).
- **Example**:
  ```html
  <p>SwamiNarayan University supports multilingual coding sessions, e.g., <bdo dir="rtl">કોડિંગ</bdo> for Gujarati.</p>
  ```
  The text "કોડિંગ" (coding in Gujarati) is displayed from right to left.




  The `<blockquote>` and `<cite>` elements are often confused because they are related to quotations, but they serve **different purposes**.

---

# 1. `<blockquote>` – For long quotations

Use `<blockquote>` when you are quoting a **large section of text** from another source.

### Real-life use cases

### Use Case 1: Quoting a famous person

```html
<blockquote>
    The greatest glory in living lies not in never falling,
    but in rising every time we fall.
</blockquote>
```

---

### Use Case 2: Customer testimonial

```html
<blockquote>
    This course completely changed my career.
    I got my first developer job within three months.
</blockquote>
```

---

### Use Case 3: Book excerpt

```html
<blockquote>
    It was the best of times,
    it was the worst of times...
</blockquote>
```

---

### Use Case 4: News article

```html
<blockquote>
    The minister announced that new education policies
    will come into effect next year.
</blockquote>
```

---

### Use Case 5: Research paper

```html
<blockquote>
    Artificial Intelligence has become one of the fastest
    growing technologies in recent years.
</blockquote>
```

---

# 2. `<cite>` – To mention the source or title

`<cite>` **does not contain the quote itself**. It identifies the **title of a creative work** (or is commonly used to show the source of a quotation).

### Use Case 1: Book name

```html
<p>I recently read <cite>Atomic Habits</cite>.</p>
```

---

### Use Case 2: Movie title

```html
<p>My favorite movie is <cite>Interstellar</cite>.</p>
```

---

### Use Case 3: Website name

```html
<p>According to <cite>MDN Web Docs</cite>, the picture element...</p>
```

---

### Use Case 4: Research paper title

```html
<p>The findings are discussed in
<cite>Deep Learning for Image Recognition</cite>.</p>
```

---

### Use Case 5: Painting

```html
<p><cite>Mona Lisa</cite> was painted by Leonardo da Vinci.</p>
```

---

# Using both together (Most common)

```html
<blockquote>
    Stay hungry. Stay foolish.
</blockquote>

<cite>Steve Jobs – Stanford Commencement Speech (2005)</cite>
```



---

# When NOT to use `<blockquote>`

❌ For short quotes inside a sentence.

```html
<p>Steve Jobs said, "Stay hungry. Stay foolish."</p>
```

For short, inline quotations, use the `<q>` element:

```html
<p>Steve Jobs said, <q>Stay hungry. Stay foolish.</q></p>
```

---

| Situation                                                                         | Element                 |
| --------------------------------------------------------------------------------- | ----------------------- |
| Long quote from a book, speech, article, interview                                | `<blockquote>`          |
| Short quote inside a sentence                                                     | `<q>`                   |
| Mention the title of a book, movie, song, website, research paper, painting, etc. | `<cite>`                |
| Mention who or what the quotation came from (often inside `<figcaption>`)         | `<cite>` (common usage) |

---

## Example Combining Multiple Elements
```html
<p>According to the <abbr title="SwamiNarayan University">SNU</abbr>:</p>
<blockquote cite="https://swaminarayanuniversity.ac.in/news">
  <p>Our practical sessions integrate real-world projects for hands-on learning.</p>
  <cite>— University Newsletter, 2025</cite>
</blockquote>
<p>Contact us at:</p>
<address>
  Coding Gita Campus<br>
  Ahmedabad-Mehsana Highway, Saij, Kalol<br>
  Gandhinagar, Gujarat 382725
</address>
<p>The workshop emphasized: <q cite="https://codinggita.com/mission">Coding is a skill for the future.</q></p>
<p>For multilingual support, see <bdo dir="rtl">ગુજરાતી</bdo> integration.</p>
```
This example combines `<abbr>`, `<blockquote>`, `<cite>`, `<address>`, `<q>`, and `<bdo>` to create a structured, accessible quotation with additional context for Coding Gita and SwamiNarayan University.

## Summary
The `<blockquote>`, `<q>`, `<abbr>`, `<address>`, `<cite>`, and `<bdo>` elements provide semantic ways to handle quotations, abbreviations, contact information, and text direction in HTML. The `<blockquote>` and `<q>` elements support the `cite` attribute for sourcing, `<abbr>` uses the `title` attribute for descriptions, `<address>` structures contact de
