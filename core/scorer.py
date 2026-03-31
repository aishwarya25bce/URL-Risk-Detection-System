# core/scorer.py

def calculate_risk(
    pattern_result,
    redirect_result,
    domain_result,
    google_result,
    report_result,
    ml_result=None
):
    """
    Combines all signals into a final risk score
    """

    total_risk = 0
    reasons = []

    # ---------------------------
    # 1. PATTERN (LOW WEIGHT)
    # ---------------------------
    pattern_risk = pattern_result.get("risk", 0)
    total_risk += pattern_risk
    reasons.extend(pattern_result.get("flags", []))

    # ---------------------------
    # 2. REDIRECT (MEDIUM)
    # ---------------------------
    redirect_risk = redirect_result.get("risk", 0)
    total_risk += redirect_risk

    if redirect_result.get("redirect_count", 0) > 1:
        reasons.append(f"{redirect_result['redirect_count']} redirects detected")

    # ---------------------------
    # 3. GOOGLE SAFE BROWSING (HIGH)
    # ---------------------------
    google_risk = google_result.get("risk", 0)
    total_risk += google_risk

    if google_result.get("flagged"):
        reasons.append("Flagged by Google Safe Browsing")

    # ---------------------------
    # 4. USER REPORTS (DYNAMIC)
    # ---------------------------
    report_risk = report_result.get("risk", 0)
    total_risk += report_risk

    if report_result.get("report_count", 0) > 0:
        reasons.append(
            f"Domain reported {report_result['report_count']} times"
        )

   # ------------------------
    # 5. ML MODEL (INTELLIGENCE LAYER)
    # ------------------------
    ml_risk = 0

    if ml_result is not None:
        prediction = ml_result.get("prediction", 0)

        if prediction == 1:   # 1 = risky
            ml_risk = 25      # weight (tunable)
            total_risk += ml_risk
            reasons.append("ML model flagged this URL as suspicious")

    # ---------------------------
    # 6. DOMAIN TRUST (CRITICAL)
    # ---------------------------
    trust_score = domain_result.get("trust_score", 0)
    total_risk -= min(trust_score, 15)  # reduce risk

    reasons.extend(domain_result.get("reasons", []))

    # ---------------------------
    # 7. DOMAIN RISK (if any)
    # ---------------------------
    domain_risk = domain_result.get("risk", 0)
    total_risk += domain_risk

    # IP-based URL
    if "http://" in str(pattern_result) and any(char.isdigit() for char in str(pattern_result)):
        if "://" in str(pattern_result):
            total_risk += 40
            reasons.append("Suspicious numeric URL (possible IP)")

    # Shortened URL
    if "bit.ly" in str(pattern_result) or "tinyurl" in str(pattern_result):
        total_risk += 35
        reasons.append("URL shortener detected")

    # No HTTPS
    if "http://" in str(pattern_result):
        total_risk += 10
        reasons.append("Not using HTTPS")

    # ---------------------------
    # FINAL NORMALIZATION
    # ---------------------------
    total_risk = max(0, min(total_risk, 100))

    return {
        "score": total_risk,
        "reasons": reasons
    }