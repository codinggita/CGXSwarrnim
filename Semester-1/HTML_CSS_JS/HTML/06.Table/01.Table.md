# HTML Table

HTML tables are created using the `<table>` tag to organize data in rows and columns. They are commonly used for tabular data such as schedules, results, or comparisons.

## Table Elements
- `<table>`: Defines the table.
- `<tr>`: Defines a table row.
- `<th>`: Defines a table header cell (bold and centered by default).
- `<td>`: Defines a table data cell.
- `<caption>`: Defines a table caption (usually shown above the table).
- `<thead>`: Groups header content (semantic).
- `<tbody>`: Groups body content (semantic).
- `<tfoot>`: Groups footer content (semantic).

## Table Attributes
- `border` (on `<table>`): Sets the border width in pixels (older attribute; still works in browsers).
- `colspan`: Number of columns a cell should span.
- `rowspan`: Number of rows a cell should span.
- `scope` (on `<th>`): Indicates whether the header applies to a `row`, `col`, `rowgroup`, or `colgroup` (helps accessibility).
- `headers`: Links a `<td>` to one or more `<th>` cells by their `id` values (accessibility).
- `align` / `valign` / `width`: Older attributes (prefer CSS in modern pages, but shown here for completeness).

---

### Basic Table (border attribute)
```html
<table border="1">
  <tr>
    <th>Course</th>
    <th>Duration</th>
  </tr>
  <tr>
    <td>Python at Coding Gita</td>
    <td>3 months</td>
  </tr>
  <tr>
    <td>Data Science at SwamiNarayan University</td>
    <td>6 months</td>
  </tr>
</table>
```

### Table with Caption
```html
<table border="1">
  <caption>Coding Gita Workshop Schedule</caption>
  <tr>
    <th>Workshop</th>
    <th>Date</th>
  </tr>
  <tr>
    <td>JavaScript Basics</td>
    <td>October 2025</td>
  </tr>
</table>
```

### Table with Colspan and Rowspan
```html
<table border="1">
  <tr>
    <th colspan="2">SwamiNarayan University Programs</th>
  </tr>
  <tr>
    <td rowspan="2">AI Research</td>
    <td>Semester 1</td>
  </tr>
  <tr>
    <td>Semester 2</td>
  </tr>
</table>
```

### Table with Scope and Headers (Accessibility)
```html
<table border="1">
  <tr>
    <th id="course" scope="col">Course</th>
    <th id="instructor" scope="col">Instructor</th>
  </tr>
  <tr>
    <td headers="course">Python at Coding Gita</td>
    <td headers="instructor">Dr. Patel</td>
  </tr>
</table>
```

### Table using `<thead>`, `<tbody>`, `<tfoot>`
```html
<table border="1">
  <caption>SwamiNarayan University Results</caption>
  <thead>
    <tr>
      <th scope="col">Student</th>
      <th scope="col">Grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Amit Sharma</td>
      <td>A</td>
    </tr>
    <tr>
      <td>Priya Desai</td>
      <td>B+</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="2">Average Grade: B</td>
    </tr>
  </tfoot>
</table>
```

---

### More Examples of `<thead>`, `<tbody>`, `<tfoot>`

**Example 1 – Student marks with totals**
```html
<table border="1">
  <caption>Coding Gita – Midterm Marks</caption>
  <thead>
    <tr>
      <th>Student</th>
      <th>Python</th>
      <th>HTML</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Rahul</td>
      <td>85</td>
      <td>90</td>
      <td>175</td>
    </tr>
    <tr>
      <td>Sneha</td>
      <td>78</td>
      <td>88</td>
      <td>166</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="3">Class Average</td>
      <td>170.5</td>
    </tr>
  </tfoot>
</table>
```

**Example 2 – Department-wise summary**
```html
<table border="1">
  <thead>
    <tr>
      <th>Department</th>
      <th>Students</th>
      <th>Pass %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Computer Science</td>
      <td>120</td>
      <td>92%</td>
    </tr>
    <tr>
      <td>Data Science</td>
      <td>80</td>
      <td>88%</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Overall</td>
      <td>200</td>
      <td>90%</td>
    </tr>
  </tfoot>
</table>
```

---

### Using `<th>` for Row Headers (scope="row")

When the first cell of a row is a header for that entire row, use `<th scope="row">`.

```html
<table border="1">
  <caption>Course Details – Coding Gita & SwamiNarayan University</caption>
  <thead>
    <tr>
      <th scope="col">Detail</th>
      <th scope="col">Coding Gita</th>
      <th scope="col">SwamiNarayan University</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Duration</th>
      <td>3 months</td>
      <td>6 months</td>
    </tr>
    <tr>
      <th scope="row">Mode</th>
      <td>Online + Offline</td>
      <td>Full-time Campus</td>
    </tr>
    <tr>
      <th scope="row">Focus</th>
      <td>Practical Coding</td>
      <td>Research + Industry</td>
    </tr>
  </tbody>
</table>
```

Another simple row-header example:

```html
<table border="1">
  <tr>
    <th scope="row">Course Name</th>
    <td>Full Stack Development</td>
  </tr>
  <tr>
    <th scope="row">Institute</th>
    <td>Coding Gita</td>
  </tr>
  <tr>
    <th scope="row">Fees</th>
    <td>₹25,000</td>
  </tr>
</table>
```

---


**Notes: `scope` and `headers` Attributes in HTML Tables**

### 1. What is the `scope` Attribute?

The `scope` attribute is used on **header cells** (`<th>`).  
It tells the browser which cells that header is describing.

**Common values:**

| Value         | Meaning                              |
|---------------|--------------------------------------|
| `scope="col"` | Header applies to the entire **column** |
| `scope="row"` | Header applies to the entire **row**    |

---

### Simple Example of `scope`

```html
<table border="1">
  <tr>
    <th scope="col">Name</th>
    <th scope="col">Age</th>
    <th scope="col">City</th>
  </tr>
  <tr>
    <th scope="row">Rahul</th>
    <td>25</td>
    <td>Delhi</td>
  </tr>
  <tr>
    <th scope="row">Priya</th>
    <td>22</td>
    <td>Mumbai</td>
  </tr>
</table>
```

---

### 2. What is the `headers` Attribute?

The `headers` attribute is used on **data cells** (`<td>`).  
It connects a data cell to one or more header cells using their `id`.

**Syntax:**
```html
<td headers="id1 id2">value</td>
```

This is useful in **complex tables** where `scope` alone is not enough.

---

### Simple Example of `headers` Attribute

```html
<table border="1">
  <tr>
    <th id="name">Name</th>
    <th id="age">Age</th>
    <th id="city">City</th>
  </tr>
  <tr>
    <td headers="name">Rahul</td>
    <td headers="age">25</td>
    <td headers="city">Delhi</td>
  </tr>
  <tr>
    <td headers="name">Priya</td>
    <td headers="age">22</td>
    <td headers="city">Mumbai</td>
  </tr>
</table>
```

Here:
- Each `<th>` has an `id`
- Each `<td>` uses the `headers` attribute to point to the correct header

---

### 3. Example Using Both `scope` and `headers`

```html
<table border="1">
  <tr>
    <th id="name" scope="col">Name</th>
    <th id="age" scope="col">Age</th>
    <th id="city" scope="col">City</th>
  </tr>
  <tr>
    <th id="rahul" scope="row">Rahul</th>
    <td headers="age rahul">25</td>
    <td headers="city rahul">Delhi</td>
  </tr>
  <tr>
    <th id="priya" scope="row">Priya</th>
    <td headers="age priya">22</td>
    <td headers="city priya">Mumbai</td>
  </tr>
</table>
```

---

### 4. Why Do We Use `scope` and `headers`?

| Reason                  | Simple Explanation |
|-------------------------|--------------------|
| **Accessibility**       | Screen readers can correctly announce the data with its proper heading (e.g. “Age: 25”) |
| **Clarity**             | Makes relationship between headers and data clear |
| **Complex tables**      | `headers` is especially helpful when one cell belongs to multiple headers |
| **Better understanding**| Helps both humans and assistive technologies |

---

### 5. What Happens If We Don’t Use Them?

| Situation                        | Result |
|----------------------------------|--------|
| No `scope` and no `headers`      | Screen readers just read cells one by one without proper context |
| Only `<th>` without `scope`      | Works in simple tables, but can create confusion in complex tables |
| Missing `headers` in complex tables | Data cells may not be correctly linked to their headers |

**Example of bad practice:**

```html
<table border="1">
  <tr>
    <td>Name</td>
    <td>Age</td>
  </tr>
  <tr>
    <td>Rahul</td>
    <td>25</td>
  </tr>
</table>
```

Screen reader will just say:  
“Name, Age, Rahul, 25” — without clearly connecting the values.

---

### 6. Quick Summary

| Attribute   | Used On     | Purpose |
|-------------|-------------|---------|
| `scope`     | `<th>`      | Tells which column or row the header belongs to |
| `headers`   | `<td>`      | Explicitly links a data cell to one or more header cells using `id` |
| Why use?    | Accessibility + Clarity | Helps screen readers and users understand the table properly |
| If not used | Confusing for assistive technology | Table loses proper meaning |

---

**Best Practice:**
- Use `scope="col"` or `scope="row"` for most tables.
- Use the `headers` attribute when the table is complex or when one cell relates to multiple headers.

### Summary
- Create tables with `<table>`, `<tr>`, `<th>`, `<td>`, `<caption>`, `<thead>`, `<tbody>`, and `<tfoot>`.
- Use the `border` attribute on `<table>` for borders (as requested).
- Use `colspan` / `rowspan` to merge cells.
- Use `scope="col"` for column headers and `scope="row"` when `<th>` acts as a row header.
- Prefer semantic grouping (`thead` / `tbody` / `tfoot`) for larger tables.
