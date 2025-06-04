<!--
To view this README with neon colors and professional styling, open it in a Markdown viewer that supports HTML and CSS (such as VS Code with Markdown Preview Enhanced).
-->

<style>
body {
  background: #18181b;
  color: #e0e0e0;
  font-family: 'Segoe UI', Arial, sans-serif;
}
h1, h2, h3 {
  color: #39ff14;
  text-shadow: 0 0 8px #39ff14, 0 0 2px #fff;
}
code, pre {
  background: #23272e;
  color: #00eaff;
  border-radius: 6px;
  padding: 2px 6px;
  font-size: 1em;
}
a {
  color: #ff00cc;
  text-shadow: 0 0 4px #ff00cc;
}
li {
  margin-bottom: 0.3em;
}
strong {
  color: #fffb00;
  text-shadow: 0 0 4px #fffb00;
}
</style>

# <span style="color:#39ff14;">Arabic OCR using pytesseract</span>

This project extracts <strong>Arabic text</strong> from images using <span style="color:#00eaff;">Python</span>, <span style="color:#00eaff;">OpenCV</span>, and <span style="color:#00eaff;">pytesseract</span>.

---

## <span style="color:#ff00cc;">Requirements</span>

- <strong>Python 3.x</strong>
- <strong>Tesseract-OCR</strong> (with Arabic language data)
- <strong>Python packages</strong> (see <code>requirements.txt</code>)

---

## <span style="color:#39ff14;">Installation</span>

<ol>
<li><strong>Install Tesseract-OCR:</strong><br>
  <ul>
    <li>Windows: Download from <a href="https://github.com/UB-Mannheim/tesseract/wiki">UB Mannheim builds</a> and install. Add Tesseract to your <code>PATH</code>.</li>
    <li>Linux (Fedora): <code>sudo dnf install tesseract-langpack-ara</code></li>
    <li>Linux (Ubuntu/Debian): <code>sudo apt install tesseract-ocr tesseract-ocr-ara</code></li>
  </ul>
</li>
<li><strong>Install Python dependencies:</strong><br>
  <pre><code>pip install -r requirements.txt</code></pre>
</li>
<li><strong>Check Arabic language data:</strong><br>
  <pre><code>tesseract --list-langs</code></pre>
  <span style="color:#fffb00;">You should see <code>ara</code> in the list.</span>
</li>
</ol>

---

## <span style="color:#00eaff;">Usage</span>

<ol>
<li>Place your image file (e.g., <code>image.png</code>) in the project directory.</li>
<li>Run the script:<br>
  <pre><code>python ocr.py</code></pre>
</li>
<li>The extracted <span style="color:#39ff14;">Arabic text</span> will be printed to the console.</li>
</ol>

---

## <span style="color:#ff00cc;">Notes</span>

- For <strong>best results</strong>, use high-quality images with clear Arabic text.
- You can adjust <span style="color:#00eaff;">preprocessing steps</span> in the script for different image types.
- If you get a Tesseract error, make sure the Arabic language data is installed and <code>TESSDATA_PREFIX</code> is set if needed.

---

## <span style="color:#fffb00;">License</span>

This project is provided for educational purposes.
