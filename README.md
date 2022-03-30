# DVFA: Damn Vulnerable Flask App 🕸🐍

The following Flask App is vulnerable to common web vulnerabilities (OWASP Top 10).

Currently supported vulnerabilities are:
- Broken Access Control
- Server-Side Request Forgery (SSRF)
- XSS (stored and reflected)

Upcoming supported vulnerabilities:
- CSRF

I added a small explanation about each vulnerability and a possible way to fix it on the landing page (index/root).
The code might contain more specifics on how to fix the particular vulnerability.

<hr>

## Installation

```python
# We'll be using a virtual environment for installing the dependencies
py -3 -m venv py3-venv
py3-venv\Scripts\activate

# Install dependencies (will soon be replaced by requirements.txt)
pip install flask
pip install flask_wtf

# Start the web app
py app.py
```

<hr>

## Previews
Click on the GIFs to open an enlarged view.

### Broken Access Control

<img src="https://user-images.githubusercontent.com/49280556/160276829-7a6adb9b-b0b5-4d54-b305-1c6caf6e4cb6.gif" width="500" />

### Server-Side Request Forgery (SSRF)

<img src="https://user-images.githubusercontent.com/49280556/160277095-37acf4b8-459c-489d-9224-863828b80ddc.gif" width="500" />

### Cross-Site-Scripting (XSS)

<img src="https://user-images.githubusercontent.com/49280556/160924161-45e574fc-aac2-4923-84fd-77e12f01acde.gif" width="500" />

<hr>

### To-Do's
- [ ] Create requirements.txt
- [ ] Remove Flask debugging
- [ ] Add more vulnerabilities :)
