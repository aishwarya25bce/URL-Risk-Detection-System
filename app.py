# app.py

from flask import Flask, render_template, request

# Core modules
from core.normalizer import normalize_url
from core.pattern import check_patterns
from core.redirect import check_redirects
from core.domain import analyze_domain
from core.reports import get_report_score, add_report
from core.scorer import calculate_risk
from core.decision import make_decision
from core.explain import generate_explanation
from model.predictor import predict

app = Flask(__name__)

# 🔥 Report threshold (show button)
REPORT_THRESHOLD = 70


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        user_url = request.form.get("url")

        if not user_url:
            return render_template("index.html", error="Please enter a URL")

        # -----------------------------
        # 1. Normalize
        # -----------------------------
        normalized_url = normalize_url(user_url)

        # -----------------------------
        # 2. Core Checks
        # -----------------------------
        pattern_result = check_patterns(normalized_url)
        redirect_result = check_redirects(user_url)  # original URL
        domain_result = analyze_domain(normalized_url)
        report_score = get_report_score(normalized_url)

        # Placeholder (can add later)
        google_result = {"flagged": False, "risk": 0}
        ml_result = None

        # -----------------------------
        # 3. Scoring
        # -----------------------------
        result = calculate_risk(
            pattern_result,
            redirect_result,
            domain_result,
            google_result,
            report_score,
            ml_result
        )

        # -----------------------------
        # 4. Decision + Explanation
        # -----------------------------
        decision_data = make_decision(result["score"])

        reasons = generate_explanation(result)
        
        show_report=result["score"] >= 70
        # -----------------------------
        # 5. Send to UI
        # -----------------------------
        return render_template(
            "index.html",
            url=user_url,
            decision=decision_data["label"],
            level=decision_data["level"],
            score=result["score"],
            reasons=reasons,
            show_report=show_report
        )

    return render_template("index.html")


# 🔥 REPORT ROUTE
@app.route("/report", methods=["POST"])
def report_url():

    url = request.form.get("url")

    if url:
        add_report(url)

    return render_template(
        "index.html",
        decision="⚠ URL REPORTED SUCCESSFULLY",
        level="medium",
        score="—",
        reasons=["This domain will now be treated as suspicious"],
        show_report=False
    )


if __name__ == "__main__":
    app.run(debug=True)