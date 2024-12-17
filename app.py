from flask import Flask, request, render_template_string
from urllib.parse import urlparse, urlunparse

app = Flask(__name__)

def removeParamsFromURL(url: str) -> str:
    parsedURL = urlparse(url)
    if not parsedURL.scheme or not parsedURL.netloc:
        raise ValueError("Invalid URL provided.")
    # Rebuild the URL without the query parameters
    cleanURL = urlunparse((parsedURL.scheme, parsedURL.netloc, parsedURL.path, parsedURL.params, '', parsedURL.fragment))
    return cleanURL

# We'll use a simple HTML template directly in the code for demonstration.
# For larger projects, create a separate templates folder with .html files.
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>URL Cleaner</title>
</head>
<body>
    <h1>Enter a URL to clean</h1>
    <form method="POST">
        <input type="text" name="url" placeholder="Enter URL here" style="width:300px;">
        <input type="submit" value="Clean URL">
    </form>

    {% if cleaned_url %}
    <h2>Cleaned URL:</h2>
    <p>{{ cleaned_url }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    cleaned_url = None
    if request.method == 'POST':
        user_url = request.form.get('url', '')
        if user_url:
            try:
                cleaned_url = removeParamsFromURL(user_url)
            except ValueError:
                cleaned_url = "Invalid URL provided."
    return render_template_string(HTML_TEMPLATE, cleaned_url=cleaned_url)

if __name__ == "__main__":
    # Run locally; on PythonAnywhere, just call 'flask run' or rely on WSGI file
    app.run(debug=True)
