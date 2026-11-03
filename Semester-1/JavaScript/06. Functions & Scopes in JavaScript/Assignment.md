# Assignment : Functions in JS
---
### Section 1: What Is a Function?
1. Why do we use functions instead of writing the same code again and again? Explain with one simple example.  
2. List any four advantages of functions and write one line for each advantage.  
3. Imagine you have to display a welcome message at 6 different places in your program. How will a function help you here?
4. Show the same code written twice without a function and once with a function.  
5. Give one real-life analogy that explains the idea of a function.  
6. Why do functions make debugging easier? Answer in 1–2 lines.

### Section 2: Function Declaration
1. Create a function declaration named `displayCourse` that returns `"JavaScript Fundamentals"`. Call it and print the result.  
2. Write a function declaration getStudentStatus that returns the string "Active Learner". Store the returned value in a variable and print it.  
3. Write a function declaration and call it before its definition. What happens and why? Explain briefly.

### Section 3: Function Expression
1. Create a function expression named `showMotto` that returns `"Code. Learn. Grow."`. Call it and print the output.  
2. Write a function expression `getSemester` that returns the number `3`. Print the value returned by the function.  
3. Create a function expression and try to call it before writing the expression. What error do you get and why?

### Section 4: Function Calling (Invocation)
1. Write a function declaration `greetStudent` that returns `"All the best for your coding journey!"`. Call this function four times.  
2. Create a function expression `todayFocus` that returns `"Focus on functions today"`. Store the result in a variable and print that variable.  
3. Write one function declaration and one function expression. Call each of them twice and print all four results.



### Section 5: Parameters vs Arguments

**Practical Questions**
1. Write a function declaration `subtract(a, b)` that returns the difference of two numbers. Call it with arguments `50` and `18` and print the result.  
2. Create a function expression `greetUser(name)` that returns `"Welcome, " + name + "!"`. Call it with the argument `"Aarav"`.  
3. Write a function `calculateArea(length, breadth)` that returns the area of a rectangle. Call it twice with different pairs of arguments: `(12, 5)` and `(8, 9)`.

**Theory Questions**

4. What is the difference between a parameter and an argument? Explain with a short example.  
5. Can a function have parameters but be called without arguments? What happens in that case? Explain briefly.

---

### Section 6: Return Statement

**Practical Questions**
1. Write a function `squareOfNumber(n)` that returns the square of the given number. Call it with `9` and print the returned value.  
2. Create a function `isAdult(age)` that returns `true` if age is 18 or above, otherwise returns `false`. Test it with `17` and `20`.  
3. Write a function `getFullName(firstName, lastName)` that returns the full name. Call it with `"Rohit"` and `"Sharma"` and print the result.

**Theory Questions**

4. What does a function return if there is no `return` statement inside it?  
5. Why do we use the `return` statement in a function instead of just using `console.log()` inside the function? Explain in 2–3 lines.

---

### Section 7: Why Use Functions? (Real-world Example)

**Practical Questions**
1. You need to calculate the total marks of three subjects for 4 different students. Write a function `getTotal(m1, m2, m3)` and call it four times with different marks instead of repeating the addition code.  
2. Create a function `calculateSimpleInterest(principal, rate, time)` that returns the simple interest. Use the function to find interest for two different sets of values.  
3. Without using a function, write code to find the average of three numbers twice (for two students). Then rewrite the same logic using a single function `findAverage(a, b, c)` and call it twice.

**Theory Questions**

4. How do functions help in reducing code repetition? Explain with one real-world example.  
5. Mention any three advantages of using functions in a program.


---

### Section 8: Function Scope

**Practical Questions**
1. Create a function `showCity` that declares a local variable `city = "Ahmedabad"` and prints it. After calling the function, try to print `city` outside and note what happens.  
2. Declare a global variable `trainer = "CodingGita Mentor"`. Write a function `displayTrainer` that prints this global variable. Call the function and also print the variable outside the function.  
3. Write a function `demoScope` that contains a local variable `value = 50`. Print the variable inside the function. Then try accessing the same variable outside and explain the output/error.

**Theory Questions**
4. A variable declared inside a function cannot be used outside. Why does JavaScript follow this rule? How does it help in writing better programs?  
5. What will happen if a global variable and a local variable have the same name? Which one will the function use? Explain briefly.

---

### Section 9: Combining Function Concepts

**Practical Questions**
1. Write a function `generateMessage(name, score)` that calculates whether the student has passed (score ≥ 40) and returns a complete sentence like: `"Aarav has scored 65 and the result is Pass"`.  
2. Create a function `billCalculator(item1, item2, item3)` that returns the total amount and also mentions if the customer gets a discount (total ≥ 1000 → "Discount Applied", otherwise "No Discount").  
3. Write a function `performanceReport(student, m1, m2, m3)` that calculates total and average, then returns a formatted string containing name, total, average and a remark ("Excellent" if average ≥ 80, otherwise "Keep Improving").

**Theory Questions**

4. Why is it better to perform multiple related tasks (calculation + decision + message) inside one function instead of writing separate pieces of code?  
5. How does combining concepts like parameters, return and conditions inside a single function improve code quality?

---

### Section 10: Nested Functions

**Practical Questions**
1. Write a function `mainTask` that contains an inner function `helperTask`. The inner function should return `"Task completed successfully"`. Call the inner function from `mainTask` and return its result.  
2. Create a function `calculateFinal(m1, m2)` that has an inner function `getTotal` to add the marks. Use the inner function and return a message: `"Final marks = "` followed by the total.  
3. Write a function `studentStatus(name, marks)` containing an inner function `getGrade`. The inner function returns `"A"` if marks ≥ 80, `"B"` if marks ≥ 60, otherwise `"C"`. Return a final sentence using the name and grade.

**Theory Questions**

4. What is the main advantage of writing a function inside another function? When should we use nested functions?  
5. Can an inner function access variables of the outer function? What about the reverse (outer accessing inner variables)? Explain.
