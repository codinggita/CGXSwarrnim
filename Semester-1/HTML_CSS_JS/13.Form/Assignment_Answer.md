#1
<form action="/submit.php" method="post" autocomplete="on"> 
    <label for="name">Name:</label>
     <input type="text" id="name" name="name">

#2

<form action="/search" method="get">
    <input type="search" name="query" placeholder="Search here">
    <button type="submit">Search</button>
</form>

#3

<form action="/submit.php" method="post" novalidate>
    <label for="username3">Username:</label>
    <input type="text" id="username3" name="username" required>

<label for="email3">Email:</label>
<input type="email" id="email3" name="email" required>

<button type="submit">Submit</button>

</form>

#4

<form action="/submit.php" method="post"
      enctype="application/x-www-form-urlencoded">

    <label for="name4">Name:</label>
    <input type="text" id="name4" name="name">

<label for="email4">Email:</label>
<input type="email" id="email4" name="email">

<button type="submit">Submit</button>

</form>

#5

<form action="/upload.php" method="post" enctype="multipart/form-data">
    <label for="file5">Choose a file:</label>
    <input type="file" id="file5" name="file">

<button type="submit">Upload</button>

</form>

#6

<form action="/submit.php" method="post" enctype="text/plain">
    <label for="name6">Name:</label>
    <input type="text" id="name6" name="name">
<label for="message6">Message:</label>
<input type="text" id="message6" name="message">

<!-- text/plain is rarely used in real-world projects. -->
<button type="submit">Submit</button>
</form>

#7
<form action="/submit.php" method="post" name="userForm" target="_blank">
    <label for="name7">Name:</label>
    <input type="text" id="name7" name="name">
<button type="submit">Submit</button>
</form>

#8
<form action="/submit.php" method="post">
    <label for="email">Email Address:</label>
    <input type="email" id="email" name="email">
<button type="submit">Submit</button>
</form>

#9
<form action="/submit.php" method="post">
    <p>Gender:</p>
<input type="radio" id="male" name="gender" value="male" checked>
<label for="male">Male</label>

<input type="radio" id="female" name="gender" value="female">
<label for="female">Female</label>

<button type="submit">Submit</button>
</form>

#10
<form action="/submit.php" method="post">
    <p>Hobbies:</p>
<input type="checkbox" id="reading" name="hobbies" value="reading" checked>
<label for="reading">Reading</label>

<input type="checkbox" id="music" name="hobbies" value="music">
<label for="music">Music</label>

<input type="checkbox" id="sports" name="hobbies" value="sports">
<label for="sports">Sports</label>

<button type="submit">Submit</button>
</form>

#11
<form action="/submit.php" method="post">
    <label for="cars">Choose a car:</label>
    <select name="cars" id="cars">
        <option value="toyota">Toyota</option>
        <option value="honda">Honda</option>
        <option value="ford">Ford</option>
    </select>
<button type="submit">Submit</button>
</form>

#12

<form action="/submit.php" method="post">
    <label for="languages">Choose languages:</label>
    <select name="languages" id="languages" multiple size="3">
        <option value="html">HTML</option>
        <option value="css">CSS</option>
        <option value="javascript">JavaScript</option>
        <option value="python">Python</option>
    </select>
<button type="submit">Submit</button>

</form>

#13
<form action="/submit.php" method="post">
    <label for="fruits">Choose a fruit:</label>
    <select name="fruits" id="fruits">
        <optgroup label="Citrus Fruits">
            <option value="orange">Orange</option>
            <option value="lemon">Lemon</option>
        </optgroup>
    <optgroup label="Tropical Fruits">
        <option value="mango">Mango</option>
        <option value="pineapple">Pineapple</option>
    </optgroup>
</select>

<button type="submit">Submit</button>
</form>

#14
<form action="/submit.php" method="post">
    <label for="comments">Comments:</label>
    <textarea id="comments" name="comments" rows="4" cols="50"
              placeholder="Enter your comments here"></textarea>
<button type="submit">Submit</button>

</form>

#15
<form action="/submit.php" method="post">
    <button type="submit">Submit</button>
    <button type="reset">Reset</button>
    <button type="button">Click Me</button>
</form>

#16
<form action="/submit.php" method="post">
    <fieldset>
        <legend>Personal Information</legend>
    <label for="firstName16">First Name:</label>
    <input type="text" id="firstName16" name="first_name">

    <label for="lastName16">Last Name:</label>
    <input type="text" id="lastName16" name="last_name">
</fieldset>

<button type="submit">Submit</button>

</form>

#17
<form action="/submit.php" method="post">
    <fieldset disabled>
        <legend>Login Information</legend>
    <label for="username17">Username:</label>
    <input type="text" id="username17" name="username">

    <label for="password17">Password:</label>
    <input type="password" id="password17" name="password">
</fieldset>

<button type="submit">Submit</button>

</form>

#18
<form action="/submit.php" method="post">
    <label for="browser">Choose a browser:</label>
    <input list="browsers" id="browser" name="browser">
<datalist id="browsers">
    <option value="Chrome">
    <option value="Firefox">
    <option value="Edge">
    <option value="Safari">
</datalist>

<button type="submit">Submit</button>
</form>

#19
<form action="/submit.php" method="post">
    <label for="password19">Password:</label>
    <input type="password" id="password19" name="password"
           required minlength="8">
<button type="submit">Submit</button>

</form>

#20
<form action="/submit.php" method="post">
    <label for="emails">Email Addresses:</label>
    <input type="email" id="emails" name="emails" multiple
           placeholder="Enter emails separated by commas">
<button type="submit">Submit</button>
</form>

#21
<form action="/submit.php" method="post">
    <label for="date21">Select a date in 2023:</label>
    <input type="date" id="date21" name="date"
           min="2023-01-01" max="2023-12-31">
<button type="submit">Submit</button>
</form>

#22
<form action="/submit.php" method="post">
    <label for="quantity22">Quantity:</label>
    <input type="number" id="quantity22" name="quantity"
           min="1" max="10" step="1">
<button type="submit">Submit</button>
</form>

#23
<form action="/submit.php" method="post">
    <label for="volume">Volume:</label>
    <input type="range" id="volume" name="volume"
           min="0" max="100" value="50">
<button type="submit">Submit</button>
</form>

#24
<form action="/upload.php" method="post" enctype="multipart/form-data">
    <label for="document24">Upload PDF or DOCX:</label>
    <input type="file" id="document24" name="document"
           accept=".pdf,.docx" required>
<button type="submit">Upload</button>
</form>

#25
<form action="/submit.php" method="post">
    <input type="hidden" name="session_token" value="ABC123XYZ">
<button type="submit">Submit</button>
</form>

#26
<form action="/submit.php" method="post">
    <label for="color">Favorite Color:</label>
    <input type="color" id="color" name="favorite_color" value="#ff0000">
<button type="submit">Submit</button>

</form>

#27
<form action="/submit.php" method="post">
    <label for="phone27">Phone Number:</label>
    <input type="tel" id="phone27" name="phone"
           pattern="[0-9]{10}" placeholder="Enter 10-digit phone number">
<button type="submit">Submit</button>
</form>

#28
<form action="/submit.php" method="post">
    <label for="website">Website:</label>
    <input type="url" id="website" name="website"
           placeholder="https://example.com" required>
<button type="submit">Submit</button>
</form>

#29
<form action="/search" method="get">
    <label for="search29">Search:</label>
    <input type="search" id="search29" name="query"
           placeholder="Search the website" autofocus>
<button type="submit">Search</button>
</form>

#30
<form id="externalForm" action="/submit.php" method="post">
    <button type="submit">Submit</button>
</form>
<input type="text" name="outside_input"
    form="externalForm" placeholder="Input outside the form">

#31
<form action="/default.php" method="post">
    <input type="text" name="name">
<button type="submit">Send to Default</button>
<button type="submit" formaction="/alternative.php">
    Send to Alternative
</button>
</form>

#32
<form action="/submit.php" method="post">
    <input type="text" name="name">
<button type="submit">Submit with POST</button>
<button type="submit" formmethod="get">Submit with GET</button>
</form>

#33
<form action="/register.php" method="post">
    <label for="name33">Name:</label>
    <input type="text" id="name33" name="name" required>
<label for="email33">Email:</label>
<input type="email" id="email33" name="email" required>

<button type="submit">Register</button>
<button type="submit" formnovalidate>Save as Draft</button>
</form>

#34
<form action="/preview.php" method="post">
    <label for="message34">Message:</label>
    <input type="text" id="message34" name="message">
<button type="submit">Submit</button>
<button type="submit" formtarget="_blank">
</button>

</form>

#35
<form action="/login.php" method="post">
    <label for="username35">Username:</label>
    <input type="text" id="username35" name="username" required>
<label for="password35">Password:</label>
<input type="password" id="password35" name="password"
       required minlength="8">

<button type="submit">Log In</button>

</form>

#36
<form action="/register.php" method="post">
    <fieldset>
        <legend>Personal Information</legend>
    <label for="name36">Name:</label>
    <input type="text" id="name36" name="name" required>

    <label for="email36">Email:</label>
    <input type="email" id="email36" name="email" required>
</fieldset>

<fieldset>
    <legend>Preferences</legend>

    <input type="checkbox" id="newsletter36"
           name="newsletter" value="yes">
    <label for="newsletter36">Subscribe to newsletter</label>
</fieldset>

<button type="submit">Register</button>
</form>

#37
<form action="/contact.php" method="post">
    <label for="name37">Name:</label>
    <input type="text" id="name37" name="name" required>
<label for="email37">Email:</label>
<input type="email" id="email37" name="email" required>

<label for="message37">Message:</label>
<textarea id="message37" name="message"
          rows="6" cols="50" required></textarea>

<button type="submit">Send Message</button>

</form>

#38
<form action="/feedback.php" method="post">
    <label for="satisfaction">Satisfaction (1–10):</label>
    <input type="range" id="satisfaction" name="satisfaction"
           min="1" max="10" value="5">
<p>Would you recommend us?</p>

<input type="radio" id="recommendYes" name="recommend"
       value="yes">
<label for="recommendYes">Yes</label>

<input type="radio" id="recommendNo" name="recommend"
       value="no">
<label for="recommendNo">No</label>

<label for="comments38">Comments:</label>
<textarea id="comments38" name="comments"
          rows="4" cols="50"></textarea>

<button type="submit">Submit Feedback</button>

</form>

#39
<form action="/upload-resume.php" method="post"
      enctype="multipart/form-data">
<label for="resume39">Resume:</label>
<input type="file" id="resume39" name="resume"
       accept=".pdf,.docx" required>

<label for="photo39">Profile Photo:</label>
<input type="file" id="photo39" name="profile_photo"
       accept="image/*">

<button type="submit">Upload</button>

</form>

#40
<form action="/search" method="get">
    <label for="siteSearch">Search:</label>
    <input type="search" id="siteSearch" name="query"
           autofocus placeholder="Search the site">
<button type="submit">Search</button>

</form>

#41
<form action="/apply.php" method="post"
      enctype="multipart/form-data">
<fieldset>
    <legend>Personal Details</legend>

    <label for="name41">Name:</label>
    <input type="text" id="name41" name="name" required>

    <label for="email41">Email:</label>
    <input type="email" id="email41" name="email" required>

    <label for="phone41">Phone:</label>
    <input type="tel" id="phone41" name="phone" required>
</fieldset>

<fieldset>
    <legend>Experience</legend>

    <label for="experience41">Work Experience:</label>
    <textarea id="experience41" name="experience"
              rows="6" cols="50"></textarea>
</fieldset>

<label for="resume41">Resume:</label>
<input type="file" id="resume41" name="resume"
       accept=".pdf" required>

<p>Employment Type:</p>

<input type="radio" id="fullTime41" name="employment_type"
       value="full-time">
<label for="fullTime41">Full-Time</label>

<input type="radio" id="partTime41" name="employment_type"
       value="part-time">
<label for="partTime41">Part-Time</label>

<br>

<input type="checkbox" id="terms41" name="terms"
       value="accepted" required>
<label for="terms41">I agree to the terms and conditions.</label>

<br><br>

<button type="submit">Submit Application</button>
<button type="submit" formnovalidate>Save Draft</button>

</form>

#42
<form action="/default.php" method="post" target="_self">
    <label for="name42">Name:</label>
    <input type="text" id="name42" name="name" required>
<label for="email42">Email:</label>
<input type="email" id="email42" name="email" required>

<button type="submit">Default Submit</button>

<button type="submit" formaction="/other.php">
    Different Action
</button>

<button type="submit" formmethod="get">
    Use GET
</button>

<button type="submit" formnovalidate>
    Skip Validation
</button>

<button type="submit" formtarget="_blank">
    Open in New Tab
</button>

</form>
