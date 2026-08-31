
### 1.  
Write a complete HTML document that embeds the website `https://www.example.com` inside an iframe.  
a) Set the width to `100%` and height to `400`.  
b) Add a meaningful `title` attribute.  
c) Make sure the iframe has no border.

### 2.  
Create an HTML page that contains a clickable link and an iframe.  
a) The link text should be “Open Example Site”.  
b) When clicked, the link must load `https://www.example.com` **inside** the iframe (use the `name` attribute correctly).  
c) Give the iframe width `100%` and height `300`.

### 3.  
Write the HTML code for an iframe that embeds a YouTube-style video.  
a) Use any valid YouTube embed URL.  
b) Set width to `560` and height to `315`.  
c) In the `allow` attribute use **only** `fullscreen` and `gyroscope`.  
d) Also add the `allowfullscreen` attribute.

### 4.  
Write a complete HTML + CSS example that creates a responsive iframe.  
a) Use a CSS class named `.responsive-iframe`.  
b) The iframe must stretch to full width, have a height of `400px`, no border, and a margin of `10px`.  
c) Embed `https://www.example.com` using that class.

### 5.  
Write an iframe that requests only the `fullscreen` permission.  
a) Embed any map or video URL of your choice.  
b) Set width to `800` and height to `450`.  
c) Include a proper `title`.

### 6.  
Write an iframe that requests only the `gyroscope` permission.  
a) Choose a suitable interactive content URL.  
b) Set dimensions to `100%` width and `500` height.  
c) Add a descriptive `title`.

### 7.  
Write an iframe that requests only the `usb` permission.  
a) Use a placeholder URL such as `https://device.example.com`.  
b) Set width `600` and height `400`.  
c) Include a `title` attribute.

### 8.  
Combine multiple allowed permissions.  
Write an iframe that uses **all three** allowed values (`fullscreen`, `gyroscope`, `usb`) in the `allow` attribute.  
a) Separate the values correctly with semicolons.  
b) Embed any suitable URL.  
c) Set reasonable width and height and add a title.

### 9.  
Write two separate iframes side by side.  
a) The first iframe must request only `fullscreen`.  
b) The second iframe must request only `gyroscope`.  
c) Both should have width `48%` and height `350`.  
d) Add appropriate titles.

### 10.  
Create a page that contains a navigation menu of three links and one iframe.  
a) Each link must target the same named iframe.  
b) The three links should load three different example websites.  
c) The iframe must be `100%` wide and `400` high.

### 11.  
Write the complete code for a video-style iframe that also allows gyroscope access.  
a) Use only `fullscreen` and `gyroscope` in the `allow` attribute.  
b) Include `allowfullscreen`.  
c) Set classic video dimensions `560 × 315`.

### 12.  
Write an iframe that has **no** `allow` attribute at all (most restrictive).  
a) Embed `https://www.example.com`.  
b) Make it full-width and 300 pixels high.  
c) Add a title.

### 13.  
Write CSS and HTML so that an iframe becomes fully responsive (maintains aspect ratio).  
a) Use the common “padding-bottom” technique or modern aspect-ratio CSS.  
b) Embed any website.  
c) Make sure the iframe itself has no border.

### 14.  
Write a complete HTML page that contains:  
- A heading  
- A paragraph of text  
- An iframe that uses only the `usb` permission  
- A second iframe that uses only the `fullscreen` permission  
Give both iframes proper titles and different sizes.

### 15.  
Fix / complete the following incomplete code so that it works correctly and follows the rules:  
```html
<iframe src="https://www.example.com" width="100%" height="400" allow="..." title="...">
```  
a) Fill in a valid `allow` value using only the permitted permissions.  
b) Add a good title.  
c) Make the border disappear.

### 16.  
Write an iframe that can go fullscreen and also access gyroscope data.  
a) Use the correct `allow` syntax.  
b) Add the boolean `allowfullscreen` attribute.  
c) Embed a placeholder interactive demo URL.

### 17.  
Create a simple “device control” style page:  
a) One iframe that requests `usb`.  
b) One iframe that requests `gyroscope`.  
c) Both iframes should be 45% wide and placed next to each other using CSS.

### 18.  
Write the HTML for an iframe that is deliberately given the most minimal permissions possible while still allowing fullscreen.  
a) Only `fullscreen` may appear in the `allow` attribute.  
b) Height 500px, width 100%.  
c) Meaningful title.

### 19.  
Write a complete document that demonstrates the difference between an iframe with `allow="fullscreen"` and an iframe with no `allow` attribute.  
a) Place both iframes on the same page.  
b) Give them the same size.  
c) Use different titles so they can be distinguished.

### 20.  
Write CSS that styles an iframe with a subtle shadow, rounded corners, and no default border.  
a) Apply the style to an iframe that embeds any website.  
b) The iframe must also request only the `gyroscope` permission.  
c) Set a fixed height of 420px.

### 21.  
Create a page with a button-like link that loads content into a named iframe.  
a) The link must use `target="myDeviceFrame"`.  
b) The iframe must request the `usb` permission.  
c) Add a clear title to the iframe.

### 22.  
Write an iframe that combines `fullscreen` and `usb` permissions only.  
a) Correct semicolon syntax required.  
b) Width 700px, height 450px.  
c) Proper title and no border.

### 23.  
Write a responsive “video player” iframe that also allows gyroscope.  
a) Use only `fullscreen` and `gyroscope`.  
b) Make the width 100% on mobile (use a media query or percentage).  
c) Keep the classic 16:9 ratio if possible.

### 24.  
Create three iframes on one page:  
- First: only `fullscreen`  
- Second: only `gyroscope`  
- Third: only `usb`  
Give each a different size and a clear, unique title.

### 25.  
Write the HTML + CSS for a full-page layout that contains a header and a large iframe below it.  
a) The iframe must request all three permitted permissions (`fullscreen; gyroscope; usb`).  
b) The iframe should fill the remaining viewport height.  
c) Add a good title.

### 26.  
Complete / correct this code so that it only uses allowed permissions and is properly written:  
```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ"
  allow="autoplay; camera; microphone; fullscreen"
  title="Video">
```  
Rewrite the entire tag correctly.

### 27.  
Write a page that contains a list of three links.  
Each link must load a different URL into the **same** named iframe.  
The iframe itself must request only the `fullscreen` permission.

### 28.  
Create an iframe that is styled to look like a modern card (shadow, border-radius, padding around it).  
a) Inside the iframe request only `gyroscope`.  
b) Width 90%, max-width 800px, height 400px.  
c) Center the whole card on the page.

### 29.  
Write two versions of the same iframe side-by-side:  
- Version A: `allow="fullscreen"`  
- Version B: `allow="fullscreen; gyroscope; usb"`  
Both must embed the same URL and have identical sizes. Add clear titles.

### 30.  
Write a complete, valid HTML5 document that demonstrates best-practice iframe usage:  
a) One iframe embedding a normal webpage (no special permissions).  
b) One iframe that needs fullscreen + gyroscope.  
c) One iframe that needs usb access.  
d) All iframes must have titles, sensible sizes, and no unnecessary borders.  
e) Add a short comment above each iframe explaining why those particular permissions were chosen.
