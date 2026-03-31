# core/pattern.py

SUSPICIOUS_KEYWORDS = ["login", "verify", "secure", "account", "update"]


def check_patterns(url):
    """
    Detect suspicious patterns in URL
    """

    risk = 0
    flags = []

    # Keyword detection
    for word in SUSPICIOUS_KEYWORDS:
        if word in url:
            risk += 10
            flags.append(f"Contains '{word}'")

    # @ symbol (phishing trick)
    if "@" in url:
        risk += 15
        flags.append("Contains '@' symbol")

    # Too many subdomains
    dot_count = url.count(".")
    if dot_count > 4:
        risk += 10
        flags.append("Too many subdomains")

    # Hyphens (often used in fake domains)
    hyphen_count = url.count("-")
    if hyphen_count > 3:
        risk += 5
        flags.append("Too many hyphens")

    
    if "bit.ly" in url or "tinyurl" in url:
        risk += 35
        flags.append("Shortened URL")

    if "@" in url:
        risk += 25
        flags.append("Contains @ symbol")

    if "http://" in url:
        risk += 10
        flags.append("Not using HTTPS")

    return {"risk": risk, "flags": flags}

    # IMPORTANT: limit influence
    risk = min(risk, 30)

    return {
        "risk": risk,
        "flags": flags
    }