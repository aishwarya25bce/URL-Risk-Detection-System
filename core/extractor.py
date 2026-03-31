# core/extractor.py

import re
import tldextract

SUSPICIOUS_KEYWORDS = ["login", "verify", "secure", "account", "update"]


def has_ip(url):
    """
    Check if URL contains an IP address instead of domain
    """
    pattern = r"(http[s]?://)?(\d{1,3}\.){3}\d{1,3}"
    return 1 if re.search(pattern, url) else 0


def count_digits(url):
    return sum(c.isdigit() for c in url)


def has_suspicious_keywords(url):
    for word in SUSPICIOUS_KEYWORDS:
        if word in url:
            return 1
    return 0


def extract_features(url):
    """
    Main feature extraction function
    Returns a list of numeric features
    """

    # Basic features
    length = len(url)
    num_dots = url.count(".")
    num_hyphens = url.count("-")

    # Security indicators
    has_https = 1 if url.startswith("https") else 0
    has_at = 1 if "@" in url else 0

    # Content features
    digit_count = count_digits(url)
    has_keyword = has_suspicious_keywords(url)

    # Domain features
    ext = tldextract.extract(url)
    domain_length = len(ext.domain)
    subdomain_count = len(ext.subdomain.split(".")) if ext.subdomain else 0

    # IP usage
    ip_flag = has_ip(url)

    return {
    "url_length": length,
    "num_dots": num_dots,
    "num_hyphens": num_hyphens,
    "has_https": has_https,
    "has_at": has_at,
    "digit_count": digit_count,
    "has_keyword": has_keyword,
    "domain_length": domain_length,
    "subdomain_count": subdomain_count,
    "ip_flag": ip_flag
}