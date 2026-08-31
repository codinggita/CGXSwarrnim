## Introduction to HTML and CSS

### What is HTML?
HTML is the standard markup language used to create and structure the content of web pages. It defines the structure of a webpage by using various elements (tags) such as headings, paragraphs, images, links, lists, tables, and forms. Browsers read HTML code and display the content accordingly. HTML is not a programming language; it is a markup language that tells the browser *what* content to show and how it is organized.

**Full Form of HTML:**  
**HyperText Markup Language**

- **HyperText**: Refers to text that contains links (hyperlinks) to other documents or resources.
- **Markup**: Means that the language uses special tags (markup) to define the structure and meaning of the content.
- **Language**: It is a standardized way of writing code that browsers understand.

### What is CSS?
CSS is the language used to style and design web pages. While HTML provides the structure and content, CSS controls the presentation — how the content looks. It allows you to change colors, fonts, sizes, spacing, layout, backgrounds, borders, and create responsive designs that work on different screen sizes. CSS separates the design from the content, making websites easier to maintain and update.

**Full Form of CSS:**  
**Cascading Style Sheets**

- **Cascading**: Refers to the way styles are applied in a hierarchical order (from general to specific rules, and how multiple style sheets can override each other).
- **Style Sheets**: A collection of rules that define how HTML elements should be displayed.

### Relationship Between HTML and CSS
- **HTML** → Builds the structure (the skeleton of the webpage).
- **CSS** → Adds the style and layout (the design and appearance).

Together, HTML and CSS form the foundation of almost every website on the internet.

**Notes on the Structure of HTML**

Every HTML document follows a standard basic structure. This structure tells the browser that the file is an HTML document and defines where the important information and visible content should go.

Here is the basic skeleton of an HTML page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <!-- All visible content goes here -->
</body>
</html>
```

### Explanation of Each Part

### 1. `<!DOCTYPE html>`
- This is called the **Document Type Declaration**.
- It tells the browser that this document is written in **HTML5**.
- It must be the very first line in the HTML file.
- It is **not** an HTML tag; it is an instruction to the browser.

**Example:**
```html
<!DOCTYPE html>
```

---

### 2. `<html>` ... `</html>`
- This is the **root element** of the entire HTML document.
- Everything else (head and body) is written inside this tag.
- The `lang` attribute is commonly added to specify the language of the page (e.g., `lang="en"` for English).

**Example:**
```html
<html lang="en">
    ...
</html>
```

---

### 3. `<head>` ... `</head>`
- The **head** section contains information **about** the webpage.
- This information is **not** displayed on the page itself.
- It includes metadata, title, links to CSS files, scripts, etc.

**Common things written inside `<head>`:**

#### a) `<meta charset="UTF-8">`
- Defines the character encoding of the page.
- `UTF-8` supports almost all languages and special characters.

#### b) `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Makes the webpage responsive (looks good on mobile devices).
- Tells the browser to set the width according to the device screen.

#### c) `<title>` ... `</title>`
- Sets the **title** of the webpage.
- This title appears in the browser tab and is used by search engines.

**Example of head section:**
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Webpage</title>
</head>
```

---

### 4. `<body>` ... `</body>`
- The **body** section contains all the **visible content** of the webpage.
- Everything the user sees (text, images, links, headings, paragraphs, buttons, etc.) is written inside the `<body>` tag.

**Example:**
```html
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a paragraph of text.</p>
    <img src="photo.jpg" alt="A photo">
</body>
```

---

### Complete Basic Structure (Ready to Use)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Webpage</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>This is my first HTML page.</p>
</body>
</html>
```

---

### Quick Summary

| Part                  | Purpose                                      | Visible on Page? |
|-----------------------|----------------------------------------------|------------------|
| `<!DOCTYPE html>`     | Declares HTML5 document                      | No               |
| `<html>`              | Root container of the whole page             | No               |
| `<head>`              | Contains metadata and page information       | No               |
| `<title>`             | Sets browser tab title                       | No (shows in tab)|
| `<meta>`              | Provides extra information (encoding, etc.)  | No               |
| `<body>`              | Contains all visible content                 | Yes              |

This structure is the foundation of every webpage. Always start with this basic skeleton when creating a new HTML file.



**HTML Basic Technical Terms**

Here are clear notes on the fundamental technical terms used in HTML, with definitions and proper examples.

### 1. Tag
A **tag** is a special keyword enclosed in angle brackets (`< >`) that tells the browser how to structure or display content.

- Tags usually come in pairs: an **opening tag** and a **closing tag**.
- Opening tag: starts with `<`
- Closing tag: starts with `</`

**Example:**
```html
<p>This is a paragraph.</p>
```
- `<p>` → Opening tag  
- `</p>` → Closing tag  

---

### 2. Element
An **element** is the complete structure formed by an opening tag, content (if any), and a closing tag.

**Formula:**  
**Element = Opening Tag + Content + Closing Tag**

**Example:**
```html
<h1>Welcome to HTML</h1>
```
- Entire thing (`<h1>Welcome to HTML</h1>`) is called an **element**.
- `<h1>` and `</h1>` are tags.
- `Welcome to HTML` is the content.

---

### 3. Attribute
An **attribute** provides extra information about an HTML element. It is written inside the opening tag and usually comes in name-value pairs.

**Syntax:**  
`attribute_name="value"`

**Example:**
```html
<img src="photo.jpg" alt="A beautiful landscape" width="300">
```
- `src`, `alt`, and `width` are **attributes**.
- `"photo.jpg"`, `"A beautiful landscape"`, and `"300"` are their values.

Common attributes: `id`, `class`, `src`, `href`, `alt`, `style`, `title`, etc.

---

### 4. Closing Tag
A **closing tag** marks the end of an HTML element. It is written with a forward slash (`/`) before the tag name.

**Example:**
```html
<p>This is a paragraph of text.</p>
```
- `</p>` is the **closing tag**.

Without a closing tag (in most cases), the browser may not display the content correctly.

---

### 5. Self-Closing Tag (Void Element)
Some HTML tags do **not** need a closing tag because they do not contain any content. These are called **self-closing tags** or **void elements**.

In modern HTML (HTML5), you can write them simply as `<tag>` or with a slash `<tag />` (both are valid).

**Common Self-Closing Tags:**
| Tag     | Purpose                  | Example                          |
|---------|--------------------------|----------------------------------|
| `<br>`  | Line break               | `Hello<br>World`                 |
| `<hr>`  | Horizontal line          | `<hr>`                           |
| `<img>` | Image                    | `<img src="pic.jpg" alt="Photo">`|
| `<input>` | Form input field       | `<input type="text">`            |
| `<meta>` | Metadata               | `<meta charset="UTF-8">`         |
| `<link>` | External resource      | `<link rel="stylesheet" href="style.css">` |

**Example:**
```html
<img src="logo.png" alt="Website Logo">
<br>
<hr>
```

---

### Quick Summary Table

| Term              | Definition                                      | Example                          |
|-------------------|-------------------------------------------------|----------------------------------|
| **Tag**           | Keyword inside `<>`                             | `<p>`, `</p>`                    |
| **Element**       | Opening tag + content + closing tag             | `<p>Hello</p>`                   |
| **Attribute**     | Extra information inside opening tag            | `src="image.jpg"`                |
| **Closing Tag**   | Ends an element (`</tag>`)                      | `</h1>`, `</div>`                |
| **Self-Closing**  | Tag that needs no closing tag                   | `<br>`, `<img>`, `<hr>`          |

These are the core building blocks of every HTML document. Understanding them clearly will help you write correct and clean HTML code.
