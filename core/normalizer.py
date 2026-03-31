# core/normalizer.py

def normalize_url(url):
    """
    Clean and standardize URL input
    """
    if not url:
        return ""

    url = url.strip().lower()

    # Add scheme if missing
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    return url
