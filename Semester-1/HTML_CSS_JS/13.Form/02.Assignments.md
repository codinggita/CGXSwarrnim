
### 1. Basic Form Structure  
Write a complete basic form that sends data to a server.  

**Guidance:**  
- Use the `<form>` element.  
- Set `action` to `"/submit.php"`.  
- Set `method` to `"post"`.  
- Add `autocomplete="on"`.  
- Include at least one text input and a submit button.

### 2. Form with GET Method  
Create a form that uses the GET method.  

**Guidance:**  
- Use `<form method="get">`.  
- Set a suitable `action`.  
- Include a search-type input.  
- Add a submit button.

### 3. Form without Browser Validation  
Write a form that disables HTML5 validation.  

**Guidance:**  
- Use the `novalidate` attribute on the `<form>`.  
- Include required fields so students can see that validation is skipped.  
- Use method `"post"`.

### 4. Understanding enctype – Default Value  
Create a normal form that uses the default encoding.  

**Guidance:**  
- Explicitly write `enctype="application/x-www-form-urlencoded"`.  
- Include text and email inputs.  
- Explain in a comment why this is the default.

### 5. File Upload Form (Most Important enctype)  
Write a form that can upload a file.  

**Guidance:**  
- Set `method="post"`.  
- Set `enctype="multipart/form-data"`.  
- Include an `<input type="file">`.  
- Add a submit button.  
- This is the required enctype for any file upload.

### 6. Form Using text/plain Encoding  
Create a form that uses plain-text encoding.  

**Guidance:**  
- Use `enctype="text/plain"`.  
- Include two text inputs.  
- Note that this encoding is rarely used in real projects.

### 7. Form with Name and Target  
Write a form that has a name and opens the response in a new tab.  

**Guidance:**  
- Add `name="userForm"`.  
- Add `target="_blank"`.  
- Include at least one input and a submit button.

### 8. Proper Use of Label  
Create a form field with a correctly associated label.  

**Guidance:**  
- Use `<label for="email">`.  
- Give the input `id="email"`.  
- Use `type="email"`.  
- This improves accessibility.

### 9. Radio Button Group with Labels  
Write a gender selection using radio buttons.  

**Guidance:**  
- Use the same `name` for both radios.  
- Give each radio a unique `id`.  
- Associate labels using the `for` attribute.  
- Pre-select one option with `checked`.

### 10. Multiple Checkboxes  
Create a list of hobbies using checkboxes.  

**Guidance:**  
- Use the same `name` for all checkboxes.  
- Give different `value` attributes.  
- Associate each checkbox with its own label.  
- Pre-check at least one option.

### 11. Drop-down List (Single Select)  
Write a simple drop-down for selecting a car brand.  

**Guidance:**  
- Use `<select name="cars">`.  
- Add at least three `<option>` elements.  
- Give each option a `value`.

### 12. Multi-select Drop-down  
Create a select box that allows multiple choices.  

**Guidance:**  
- Add the `multiple` attribute.  
- Set `size="3"`.  
- Include at least four options.

### 13. Grouped Options with optgroup  
Write a select menu that groups fruits into categories.  

**Guidance:**  
- Use two `<optgroup>` elements with `label` attributes.  
- Place related `<option>` elements inside each group.

### 14. Multi-line Text Area  
Create a message box for user comments.  

**Guidance:**  
- Use `<textarea>`.  
- Set `rows="4"` and `cols="50"`.  
- Add a `name` and a placeholder.

### 15. Button Types  
Write three different buttons inside a form.  

**Guidance:**  
- One `type="submit"`.  
- One `type="reset"`.  
- One `type="button"`.  
- Give each a clear visible text.

### 16. Fieldset and Legend  
Group personal information fields together.  

**Guidance:**  
- Use `<fieldset>`.  
- Add a `<legend>` with the text “Personal Information”.  
- Place at least two inputs inside the fieldset.

### 17. Disabled Fieldset  
Create a fieldset that cannot be edited.  

**Guidance:**  
- Add the `disabled` attribute to `<fieldset>`.  
- Include a legend and two inputs (username and password).

### 18. Datalist for Autocomplete Suggestions  
Write an input that offers browser suggestions.  

**Guidance:**  
- Create an `<input list="browsers">`.  
- Create a `<datalist id="browsers">` with at least three options.  
- The input and datalist must be linked by the same id.

### 19. Password Field with Constraints  
Create a secure password input.  

**Guidance:**  
- Use `type="password"`.  
- Add `required`.  
- Add `minlength="8"`.  
- Associate a proper label.

### 20. Email Input with Multiple Values  
Write an email field that accepts more than one address.  

**Guidance:**  
- Use `type="email"`.  
- Add the `multiple` attribute.  
- Add a placeholder explaining that emails should be comma-separated.

### 21. Date Picker with Range  
Create a date input limited to the year 2023.  

**Guidance:**  
- Use `type="date"`.  
- Set `min="2023-01-01"` and `max="2023-12-31"`.

### 22. Number Input with Step  
Write a quantity field that only allows whole numbers between 1 and 10.  

**Guidance:**  
- Use `type="number"`.  
- Set `min="1"`, `max="10"`, and `step="1"`.

### 23. Range Slider  
Create a volume control slider.  

**Guidance:**  
- Use `type="range"`.  
- Set `min="0"`, `max="100"`, and a default `value`.

### 24. File Input with Restrictions  
Write a file upload field that only accepts PDF and DOCX files.  

**Guidance:**  
- Use `type="file"`.  
- Set `accept=".pdf,.docx"`.  
- Make it required.  
- Remember the form must use `enctype="multipart/form-data"`.

### 25. Hidden Input  
Add a hidden field that stores a session token.  

**Guidance:**  
- Use `type="hidden"`.  
- Give it a `name` and a `value`.  
- It should not be visible to the user.

### 26. Color Picker  
Create a favorite-color selector.  

**Guidance:**  
- Use `type="color"`.  
- Set a default value (e.g., `"#ff0000"`).

### 27. Telephone Input with Pattern  
Write a phone number field with a simple pattern.  

**Guidance:**  
- Use `type="tel"`.  
- Add a `pattern` for a basic format.  
- Add a helpful placeholder.

### 28. URL Input  
Create a website field that requires a valid URL.  

**Guidance:**  
- Use `type="url"`.  
- Add `required`.  
- Add a placeholder starting with `https://`.

### 29. Search Field with Autofocus  
Write a search box that receives focus automatically.  

**Guidance:**  
- Use `type="search"`.  
- Add `autofocus`.  
- Add a placeholder.

### 30. Using the form Attribute (Input Outside Form)  
Create a form and an input that is physically outside the form but still belongs to it.  

**Guidance:**  
- Give the form an `id`.  
- Place an input outside the form tags.  
- Connect them with the `form="id-of-form"` attribute.

### 31. formaction Override  
Write a form with two submit buttons that send data to different URLs.  

**Guidance:**  
- Give the form a default `action`.  
- First button uses the default action.  
- Second button uses `formaction` to send data to a different URL.

### 32. formmethod Override  
Create a form that can be submitted with either POST or GET depending on the button.  

**Guidance:**  
- Form default method is `"post"`.  
- One button keeps the default.  
- Second button uses `formmethod="get"`.

### 33. formnovalidate  
Write a registration form that has a “Save as Draft” button.  

**Guidance:**  
- Make several fields `required`.  
- Normal submit button performs validation.  
- Draft button uses `formnovalidate` so validation is skipped.

### 34. formtarget  
Create a form with a normal submit and a “Preview in new tab” button.  

**Guidance:**  
- Default behaviour opens in the same tab.  
- Second button uses `formtarget="_blank"`.

### 35. Complete Login Form  
Write a realistic login form.  

**Guidance:**  
- Method post, suitable action.  
- Username (text) and password fields – both required.  
- Password must have `minlength="8"`.  
- Proper labels for both fields.  
- Submit button.

### 36. Complete Registration Form with Fieldsets  
Create a user registration form.  

**Guidance:**  
- Use two fieldsets: “Personal Information” and “Preferences”.  
- Include name, email, and a newsletter checkbox.  
- All important fields required.  
- Submit button.

### 37. Contact Us Form  
Write a contact form.  

**Guidance:**  
- Name, email, and message (textarea).  
- All fields required.  
- Suitable rows and cols for the textarea.  
- Submit button with clear text.

### 38. Survey / Feedback Form  
Create a short feedback form.  

**Guidance:**  
- A range slider for satisfaction (1–10).  
- Radio buttons for “Would you recommend us?”.  
- A textarea for comments.  
- Submit button.

### 39. Complete File Upload Form  
Write a form that uploads a resume and a profile photo.  

**Guidance:**  
- `method="post"` and `enctype="multipart/form-data"` (mandatory).  
- One file input accepting `.pdf,.docx`.  
- Second file input accepting images only (`accept="image/*"`).  
- Both fields labelled and the resume required.

### 40. Search Form Using GET  
Create a simple site search form.  

**Guidance:**  
- Method must be `"get"`.  
- Use `type="search"`.  
- Add `autofocus` and a placeholder.  
- Submit button.

### 41. Advanced Form Combining Many Features  
Write a comprehensive job-application form.  

**Guidance:**  
- Use `method="post"` and `enctype="multipart/form-data"`.  
- Fieldset for personal details (name, email, phone).  
- Fieldset for experience (textarea).  
- File input for resume (accept PDF only).  
- Radio buttons for employment type.  
- Checkbox for terms and conditions (required).  
- Two submit buttons: one normal, one with `formnovalidate` for “Save Draft”.  
- All inputs must have proper labels and name attributes.

### 42. Form Demonstrating All Major Override Attributes  
Create one form that shows `formaction`, `formmethod`, `formnovalidate`, and `formtarget` working together.  

**Guidance:**  
- Default action, method, and target on the `<form>`.  
- Four different submit buttons, each overriding one of the attributes listed above.  
- Include at least two required fields so the effect of `formnovalidate` is visible.
