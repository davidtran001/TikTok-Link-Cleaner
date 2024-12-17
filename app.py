from flask import Flask, request, render_template
from urllib.parse import urlparse, urlunparse

app = Flask(__name__)

def removeParamsFromURL(url: str) -> str:
    parsedURL = urlparse(url)
    if not parsedURL.scheme or not parsedURL.netloc:
        raise ValueError("Invalid URL provided.")
    # Rebuild the URL without the query parameters
    cleanURL = urlunparse((parsedURL.scheme, parsedURL.netloc, parsedURL.path, parsedURL.params, '', parsedURL.fragment))
    return cleanURL

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
    return render_template('index.html', cleaned_url=cleaned_url)

if __name__ == "__main__":
    app.run(debug=True)
