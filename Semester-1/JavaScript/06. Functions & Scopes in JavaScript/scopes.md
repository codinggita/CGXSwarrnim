# **Scope in JavaScript**

## **1. What Is Scope?**

Scope defines **where a variable can be accessed** in a program.

In **Unit 1**, JavaScript has only two types of scope for us:

1. Global Scope
2. Function Scope

(Because `var` does not support block scope.)

### **Activity Time**

1. What do you understand by scope in JavaScript?
2. Which two types of scope are covered in this unit?
3. Why doesn't `var` support block scope?

## **2. Global Scope**

A variable declared outside any function is in the **global scope** and can be accessed anywhere.

### **Example:**

```
var college = "CodingGita";

function showCollege() {
    console.log(college);
}

showCollege();        // CodingGita
console.log(college); // CodingGita
```

`college` lives in global memory.

### **Activity Time**

1\. Predict the output:

```
var city = "Ahmedabad";

function displayCity() {
    console.log(city);
}

displayCity();
console.log(city);
```

2. Write a program that declares a global variable `studentName = "Rahul"` and prints it both inside and outside a function.
3. Can a function access a variable declared outside it? Explain with an example.

## **3. Function Scope**

Any variable declared with `var` *inside* a function is available **only inside that function**.

### **Example:**

```
function studentMarks() {
    var marks = 85;
    console.log(marks);
}

studentMarks(); // 85
console.log(marks); // Error: marks is not defined
```

Variables inside a function are **local**.

### **Activity Time**

1\. Predict the output and identify the error:

```
function employeeInfo() {
    var salary = 25000;
    console.log(salary);
}

employeeInfo();
console.log(salary);
```

2. Write a function `calculateAge()` that declares a local variable `age = 20` and prints it.
3. Can a variable declared inside a function be accessed outside that function? Why?

## **4. No Block Scope in Unit 1 (**`var`**&#x20;ignores blocks)**

This is a major point for beginners:

`var` does NOT respect block boundaries.

Blocks include:

- if
- for
- while
- switch
- any `{ }` not belonging to a function

### **Example:**

```
if (true) {
    var x = 10;
}

console.log(x); // 10 (still accessible outside)
```

Even though `x` is inside `{}`, `var` makes it global (or function-scoped if inside a function).

### **Activity Time**

1\. Predict the output:

```
if (true) {
    var marks = 75;
}

console.log(marks);
```

2\. What will be the output? Explain why.

```
if (false) {
    var result = 100;
}

console.log(result);
```

3\. Declare a variable `message` using `var` inside an `if` block and print it outside the block.

## **5. Block Example with Loops**

```
for (var i = 1; i <= 3; i++) {
    console.log("Inside:", i);
}

console.log("Outside:", i);
```

Output:

```
Inside: 1
Inside: 2
Inside: 3
Outside: 4
```

Because `var` is **not block scoped**, `i` exists outside the loop.

### **Activity Time**

1\. Predict the complete output:

```
for (var i = 2; i <= 4; i++) {
    console.log(i);
}

console.log("Final:", i);
```

2. Why can we access the variable `i` after the loop?
3. Write a `for` loop using `var` that prints numbers from 1 to 5 and prints the final value of the loop variable outside the loop.

## **6. Function Scope Inside Loops**

If a loop is inside a function, the variable becomes local to that function.

### **Example:**

```
function test() {
    for (var i = 1; i <= 3; i++) {
        console.log("Inside:", i);
    }

    console.log("After loop inside function:", i);
}

test();
console.log(i); // Error
```

Explanation:

- Inside the function → accessible
- Outside the function → not accessible

### **Activity Time**

1\. Predict the output:

```
function displayNumbers() {
    for (var num = 1; num <= 3; num++) {
        console.log(num);
    }

    console.log("Final:", num);
}

displayNumbers();
```

2\. Which statement will produce an error and why?

```
function test() {
    for (var i = 1; i <= 2; i++) {
        console.log(i);
    }

    console.log(i);
}

test();
console.log(i);
```

3\. Write a function `printTable()` that uses a `for` loop with `var` and prints the loop variable both after the loop and outside the function.

## **7. Hoisting (**`var`**&#x20;only)**

JavaScript **moves variable declarations to the top** of their scope before executing code.

But **only the declaration** is moved, not the assignment.

### **Example:**

```
console.log(a); // undefined
var a = 10;
```

Internally JavaScript behaves like:

```
var a;
console.log(a); // undefined
a = 10;
```

Common mistake:

Students think it should give an error, but it does not.

### **Activity Time**

1\. Predict the output:

```
console.log(name);
var name = "Rahul";
console.log(name);
```

2\. Predict the output:

```
var x = 20;

console.log(x);
var x = 50;

console.log(x);
```

3\. Why does `console.log(a)` print `undefined` instead of producing an error when `var a = 10` is written later?

## **8. Function Declaration Hoisting**

Function declarations are fully hoisted (name + body).

### **Example:**

```
greet();  // Works

function greet() {
    console.log("Hello students of CodingGita");
}
```

### **Activity Time**

1\. Predict the output:

```
welcome();

function welcome() {
    console.log("Welcome to JavaScript");
}
```

2. Write a function `showMessage()` that prints `"Learning JavaScript"` and call it before its declaration.
3. Why can we call a function before its declaration in JavaScript?

## **9. Scope Chain (Very Important)**

When accessing a variable:

1. JavaScript looks inside the current scope.
2. If not found, goes to the next outer scope.
3. Continues until global scope.
4. If not found anywhere → error.

### **Example:**

```
var institute = "CodingGita";

function department() {
    var dept = "CSE";

    function batchInfo() {
        var batch = "2025";

        console.log(batch);     // 2025
        console.log(dept);      // CSE
        console.log(institute); // CodingGita
    }

    batchInfo();
}

department();
```

Inner functions can access variables from:

- Their own scope
- Outer functions
- Global scope

Outer regions cannot access inner scopes.

### **Activity Time**

1\. Predict the output:

```
var country = "India";

function stateInfo() {
    var state = "Gujarat";

    function cityInfo() {
        var city = "Ahmedabad";

        console.log(city);
        console.log(state);
        console.log(country);
    }

    cityInfo();
}

stateInfo();
```

2\. Identify which statement produces an error and explain why:

```
function outer() {
    var x = 10;

    function inner() {
        var y = 20;
        console.log(x);
        console.log(y);
    }

    inner();
}

outer();
console.log(x);
```

3\. Write a nested function program with a global variable `college`, an outer variable `dept`, and an inner variable `studentName`. Print all three from the inner function.

## **10. Variable Shadowing**

A local variable can **override** a global variable with the same name.

### **Example:**

```
var score = 50;

function test() {
    var score = 90; // local shadows global
    console.log(score); // 90
}

test();
console.log(score); // 50
```

The inner value does not overwrite the outer value; it only hides it inside the function.

### **Activity Time**

1\. Predict the output:

```
var marks = 60;

function result() {
    var marks = 95;
    console.log(marks);
}

result();
console.log(marks);
```

2\. Predict the output:

```
var name = "Rahul";

function student() {
    var name = "Jenil";

    function display() {
        console.log(name);
    }

    display();
}

student();
console.log(name);
```

3\. Write a program with a global variable `price = 1000` and a local variable with the same name `price = 500`. Print both values.

## **11. Nested Functions (Pure Function Scope Example)**

### **Example:**

```
function outer() {
    var teacher = "Kartik Sir";

    function inner() {
        var student = "Jenil";
        console.log(student);
        console.log(teacher);
    }

    inner();
}

outer();
```

Inside `inner()` you can access both variables:

- student (local)
- teacher (outer function)

But from outside:

- teacher is not available
- student is not available

### **Activity Time**

1\. Predict the output:

```
function first() {
    var a = 10;

    function second() {
        var b = 20;
        console.log(a + b);
    }

    second();
}

first();
```

2\. Find the error and explain why:

```
function outer() {
    var course = "JavaScript";

    function inner() {
        var duration = "3 Months";
        console.log(course);
    }

    inner();
    console.log(duration);
}

outer();
```

3\. Create an outer function `teacherInfo()` with a variable `teacherName` and an inner function `subjectInfo()` with a variable `subject`. Print both variables inside the inner function.

## **12. Common Errors with var**

### **1. Creating global variables accidentally**

```
function test() {
    x = 100; // missing var → becomes global in non-strict mode
}
```

### **2. Expecting block scope (wrong assumption)**

```
if (true) {
    var x = 20;
}
console.log(x); // 20
```

### **3. Accessing variables before declaration**

```
console.log(a);
var a = 10;
```

### **4. Colliding variable names because var allows redeclaration**

```
var x = 10;
var x = 20; // allowed, but confusing
```

### **Activity Time**

1\. Find and correct the mistake:

```
function student() {
    name = "Rahul";
    console.log(name);
}

student();
```

2\. Predict the output:

```
var age = 18;
var age = 21;

console.log(age);
```

3\. Rewrite this code to avoid redeclaring the same variable:

```
var marks = 70;
var marks = 85;
var marks = 95;

console.log(marks);
```

## **13. Exercises**

### **Activity Time**

**Exercise 1. Predict the output:**

```
var a = 5;

function demo() {
    var a = 10;
    console.log(a);
}

demo();
console.log(a);
```

**Exercise 2. Fix the code:**

Fix this code so `counter` is not accessible outside the function:

```
for (var counter = 1; counter <= 5; counter++) {
    console.log(counter);
}
console.log(counter); // should not be accessible
```

**Exercise 3. Explain the output:**

```
console.log(score);
var score = 40;
```

## **14. Multiple Choice Questions**

### **Activity Time**

**Q1. Which type of scope does&#x20;**`var`**&#x20;have?**

1. Block scope
2. Function scope
3. Lexical scope
4. Module scope

**Q2. What is the output?**

```
console.log(a);
var a = 5;
```

1. Error
2. undefined
3. 5
4. null

**Q3. Variables inside a function are:**

1. Global
2. Available everywhere
3. Local to the function
4. Hoisted globally

**Q4. What is the scope chain?**

1. Searching nested scopes outward
2. Chain of events
3. Chain of functions
4. Loop control

**Q5. What will be the output?**

```
var x = 10;

function test() {
    var x = 20;
    console.log(x);
}

test();
console.log(x);
```

1. 10, 10
2. 20, 20
3. 20, 10
4. Error

**Q6. What happens when a&#x20;**`var`**&#x20;variable is declared inside an&#x20;**`if`**&#x20;block?**

1. It becomes accessible only inside the block.
2. It becomes function-scoped or global, depending on its surrounding scope.
3. It always produces an error.
4. It becomes a constant.

## **15. Mini Assignment**

### **Activity Time**

Create a function `studentInfo()` that:

- Defines a local variable `name`.
- Defines a local variable `course`.
- Defines an inner function `display()`.
- The inner function prints both variables.
- Calls the inner function from the outer function.

This exercise shows **function scope**, **nested scope**, and **scope chain**.
