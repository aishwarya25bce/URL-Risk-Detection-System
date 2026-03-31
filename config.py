# config.py

# Trusted domains (can expand)
TRUSTED_DOMAINS = [
    "google.com",
    "youtube.com",
    "github.com",
    "microsoft.com",
    "apple.com",
    "amazon.com"
]

# Suspicious keywords
SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "account",
    "update",
    "bank",
    "password"
]

# Scoring weights
WEIGHTS = {
    "pattern": 1.0,
    "redirect": 1.0,
    "domain": 1.0,
    "google": 1.0,
    "reports": 1.0,
    "ml": 0.4
}

# Risk thresholds
THRESHOLDS = {
    "safe": 40,
    "danger": 70
}