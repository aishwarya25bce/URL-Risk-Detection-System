# core/domain.py

import tldextract

# You can later move this to config.py
TRUSTED_DOMAINS = [
    "google.com",
    "youtube.com",
    "github.com",
    "microsoft.com",
    "apple.com",
    "amazon.com"
]


def extract_domain(url):
    """
    Extract root domain (e.g., google.com)
    """
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"


def check_ssl(url):
    """
    Check if URL uses HTTPS
    """
    return url.startswith("https")


def analyze_domain(url):
    """
    Main domain analysis function
    """

    domain = extract_domain(url)

    is_trusted = domain in TRUSTED_DOMAINS
    has_ssl = check_ssl(url)

    # --- TRUST SCORING ---
    trust_score = 0
    risk = 0
    reasons = []

    # Trusted domain → strong trust
    if is_trusted:
        trust_score += 10
        reasons.append("Trusted domain")

    # SSL → moderate trust
    if has_ssl:
        trust_score += 5
        reasons.append("Uses HTTPS (secure)")

    else:
        risk += 15
        reasons.append("No HTTPS (insecure connection)")

    # Slight penalty for weird domains
    if len(domain) > 25:
        risk += 10
        reasons.append("Unusually long domain name")

    return {
        "domain": domain,
        "is_trusted": is_trusted,
        "has_ssl": has_ssl,
        "trust_score": trust_score,
        "risk": risk,
        "reasons": reasons
    }