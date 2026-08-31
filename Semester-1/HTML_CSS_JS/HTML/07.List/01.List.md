# HTML List

HTML lists are used to organize and display items in a structured format, either as ordered (numbered) or unordered (bulleted) lists. HTML provides several elements to create lists, including nested lists and definition lists for specialized use cases.

## List Elements
- `<ul>`: Defines an **unordered list**, typically displayed with bullet points.
- `<ol>`: Defines an **ordered list**, typically displayed with numbers or letters.
- `<li>`: Defines a **list item** within `<ul>` or `<ol>`.
- `<dl>`: Defines a **description list** for terms and their descriptions.
- `<dt>`: Defines a **term** in a description list.
- `<dd>`: Defines a **description** for a term in a description list.

## List Attributes
Below are the key attributes for list elements, as referenced from W3Schools. Note that some attributes (e.g., `type` and `start` for `<ol>`) are still supported.

### `<ul>` Attributes
- `type` (deprecated): Specifies the bullet style (`disc`, `circle`, `square`).

### `<ol>` Attributes
- `type`: Specifies the numbering style (`1` for numbers, `A` for uppercase letters, `a` for lowercase letters, `I` for uppercase Roman numerals, `i` for lowercase Roman numerals).
- `start`: Specifies the starting number/letter of the list (e.g., `start="3"` begins at 3).
- `reversed`: Reverses the order of the list (counts downward).

### `<li>` Attributes
- `value` (for `<ol>` only): Sets a specific value for a list item, overriding the default sequence.

---

## Examples

### Unordered List (`<ul>`)
An unordered list with bullet points for items.
```html
<ul type="disc">
  <!-- ul: unordered list; type="disc": sets bullet style -->
  <li>Python Workshop at Coding Gita</li> <!-- li: list item -->
  <li>Data Science Program at SwamiNarayan University</li>
  <li>JavaScript Bootcamp</li>
</ul>
```
This displays a bulleted list of courses.

### Ordered List (`<ol>`)
An ordered list with numbers and attributes.
```html
<ol type="1" start="2">
  <!-- ol: ordered list; type="1": numeric list; start="2": begins at 2 -->
  <li>Introduction to Programming</li>
  <li>Advanced Python at Coding Gita</li>
  <li>AI Research at SwamiNarayan University</li>
</ol>
```
This displays a numbered list starting at 2 (e.g., 2, 3, 4).

### Ordered List with `reversed`
A reversed ordered list.
```html
<ol reversed type="A">
  <!-- reversed: counts downward; type="A": uppercase letters -->
  <li>Final Project Submission</li>
  <li>Midterm Exam at SwamiNarayan University</li>
  <li>Course Orientation</li>
</ol>
```
This displays a list with uppercase letters in reverse order (e.g., C, B, A).

### Ordered List with `value`
Using `value` to override the sequence.
```html
<ol type="1">
  <li>Python Basics</li>
  <li value="5">Advanced Python</li> <!-- value="5": sets this item to 5 -->
  <li>Web Development at Coding Gita</li> <!-- Continues from 6 -->
</ol>
```
This displays a list where the second item is numbered 5, and the next continues as 6.

### Description List (`<dl>`)
A description list for terms and their descriptions.
```html
<dl>
  <!-- dl: description list -->
  <dt>Coding Gita</dt> <!-- dt: term -->
  <dd>Offers practical coding workshops in Python and JavaScript.</dd> <!-- dd: description -->
  <dt>SwamiNarayan University</dt>
  <dd>Provides degrees in Computer Science and AI.</dd>
</dl>
```
This displays terms with indented descriptions below them.

### Nested Lists
Lists can be nested to create sublists.
```html
<ul type="circle">
  <!-- ul: unordered list; circle bullets -->
  <li>Coding Gita Courses
    <ol type="a">
      <!-- Nested ol: ordered sublist with lowercase letters -->
      <li>Python Basics</li>
      <li>Advanced JavaScript</li>
    </ol>
  </li>
  <li>SwamiNarayan University Programs
    <ul type="square">
      <!-- Nested ul: unordered sublist with square bullets -->
      <li>Data Science</li>
      <li>AI Research</li>
    </ul>
  </li>
</ul>
```
This displays a bulleted list with nested ordered and unordered sublists.

---

## Summary
HTML lists include `<ul>` (unordered, bulleted), `<ol>` (ordered, numbered/lettered), and `<dl>` (description lists for terms and descriptions). Attributes like `type`, `start`, `reversed`, and `value` control list behavior. Nested lists allow hierarchical organization.
