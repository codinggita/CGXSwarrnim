# Python String `split()`

## 1. Why Do We Need `split()`?

Suppose we have this string:

```python
text = "Python is easy"
```

Right now, Python sees this as **one string**:

```text
"Python is easy"
```

But sometimes we want to break this string into smaller parts.

For example:

```text
Python
is
easy
```

Python provides a string method called `split()` for this purpose.

---

# 2. What Does `split()` Do?

`split()` **breaks one string into smaller parts** based on a separator.

For example:

```python
text = "Python is easy"

print(text.split())
```

Output:

```text
['Python', 'is', 'easy']
```

Don't worry about `[]` right now.

At this stage, just understand:

```text
"Python is easy"
        ↓
     split()
        ↓
"Python"   "is"   "easy"
```

So, we can say:

> **`split()` breaks a string into smaller pieces.**

---

# 3. How Does `split()` Know Where to Break?

Consider:

```python
text = "Python is easy"
```

There are spaces between the words:

```text
Python | is | easy
       ↑    ↑
      space
```

When we write:

```python
text.split()
```

Python uses **space/whitespace** as the default separator.

So:

```text
"Python is easy"
        ↓
Python | is | easy
```

---

# 4. `split()` Without Any Argument

When we don't give anything inside `split()`:

```python
text = "Python is easy"

print(text.split())
```

Python separates the string wherever there is whitespace.

Example:

```python
text = "I love Python"

print(text.split())
```

Output:

```text
['I', 'love', 'Python']
```

Think of it like:

```text
"I love Python"

     ↓ split()

"I"   "love"   "Python"
```

---

# 5. We Can Tell `split()` Where to Break

We can also provide a separator.

For example:

```python
text = "Python,is,easy"

print(text.split(","))
```

Here we told Python:

> "Break this string wherever you find `,`."

So:

```text
"Python,is,easy"

       ↓

Python | is | easy
```

Output:

```text
['Python', 'is', 'easy']
```

---

# 6. Another Example

```python
date = "09-09-2026"

print(date.split("-"))
```

We told Python to break at `-`.

```text
09-09-2026
   ↓  ↓

09 | 09 | 2026
```

Output:

```text
['09', '09', '2026']
```

---

# 7. Think of `split()` Like a Cutter

A simple way to understand `split()` is to imagine a **cutter**.

### Example

```python
text = "apple,banana,mango"
```

If we use:

```python
text.split(",")
```

Python looks for `,` and cuts there:

```text
apple , banana , mango
      ↑          ↑
     cut        cut
```

Result:

```text
apple
banana
mango
```

So:

> **The separator tells Python where to cut the string.**

---

# 8. Different Separators

We can use different separators depending on the string.

### Space

```python
text = "Python is easy"

print(text.split())
```

Break at spaces.

---

### Comma

```python
text = "A,B,C,D"

print(text.split(","))
```

Break at commas.

---

### Hyphen

```python
text = "10-20-30"

print(text.split("-"))
```

Break at hyphens.

---

### Colon

```python
text = "10:20:30"

print(text.split(":"))
```

Break at colons.

---

# 9. What If the Separator Is Not Present?

Consider:

```python
text = "Python is easy"

print(text.split(","))
```

There is no comma `,` in the string.

So Python cannot find a place to split.

Output:

```text
['Python is easy']
```

The string remains as one piece.

Think:

```text
"Python is easy"

No comma found
      ↓
No splitting
      ↓
"Python is easy"
```

---

# 10. `split()` Does Not Change the Original String

Remember that strings cannot be changed directly.

Example:

```python
text = "Python is easy"

text.split()

print(text)
```

Output:

```text
Python is easy
```

The original string is still the same.

If we want to use the result, we store it in another variable:

```python
text = "Python is easy"

parts = text.split()

print(parts)
```

Output:

```text
['Python', 'is', 'easy']
```

For now, you can think of `parts` as:

> **the pieces obtained after splitting the string.**

---

# 11. Important Observation

Look carefully at these two:

```python
text = "Python is easy"
```

and

```python
parts = text.split()
```

Before splitting:

```text
"Python is easy"
```

After splitting:

```text
['Python', 'is', 'easy']
```

The important idea is:

```text
One String
    ↓
  split()
    ↓
Multiple Pieces
```

Later, when we learn **lists**, we will understand exactly what:

```text
['Python', 'is', 'easy']
```

means.

For now, simply remember that `split()` gives us the separated pieces of a string.

---

# 12. Simple Real-Life Example

Suppose a student's full name is stored as:

```python
name = "Rahul Kumar Sharma"
```

We can split it:

```python
print(name.split())
```

Conceptually:

```text
"Rahul Kumar Sharma"
          ↓
        split()
          ↓
Rahul | Kumar | Sharma
```

This is useful when we want to work with individual words.

---

# 13. Another Real-Life Example

Suppose student data is stored like this:

```python
student = "Rahul,20,BTech"
```

We can split it using comma:

```python
print(student.split(","))
```

Conceptually:

```text
"Rahul,20,BTech"
       ↓
     split(",")
       ↓
Rahul | 20 | BTech
```

---

# 14. Quick Syntax

### Without specifying a separator

```python
string.split()
```

Python splits using whitespace.

### With a separator

```python
string.split(separator)
```

Python splits wherever that separator occurs.

Examples:

```python
text.split()
text.split(",")
text.split("-")
text.split(":")
```

---

# 15. One Important Rule

The separator should match the character present in the string.

For example:

```python
text = "apple,banana,mango"
```

Correct:

```python
text.split(",")
```

Because the string contains `,`.

But:

```python
text.split("-")
```

will not split the string because there is no `-`.

---

# Quick Revision

Remember these three points:

### 1. `split()` breaks a string

```text
"Python is easy"
       ↓
     split()
       ↓
Python | is | easy
```

### 2. The separator tells Python where to break

```python
text.split(",")
```

means:

> Break wherever `,` is found.

### 3. No separator means whitespace

```python
text.split()
```

means:

> Break at whitespace.

---

## One-Line Definition

> **`split()` is a string method used to break a string into smaller parts based on a separator.**
