# core/reports.py

import json
import os
import tldextract

REPORTS_FILE = "data/reports.json"


def extract_domain(url):
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"


def load_reports():
    """
    Load reports from JSON file
    """
    if not os.path.exists(REPORTS_FILE):
        return {}

    with open(REPORTS_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return {}


def save_reports(data):
    """
    Save reports to JSON file
    """
    os.makedirs("data", exist_ok=True)

    with open(REPORTS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_report_score(url):
    """
    Used DURING scoring
    Returns risk based on previous reports
    """
    domain = extract_domain(url)
    reports = load_reports()

    count = reports.get(domain, 0)

    # Risk calculation (balanced)
    risk = min(count * 10, 50)

    return {
        "domain": domain,
        "report_count": count,
        "risk": risk
    }


def add_report(url):
    """
    Used AFTER scoring
    Stores domain into reports DB
    """
    domain = extract_domain(url)
    reports = load_reports()

    reports[domain] = reports.get(domain, 0) + 1

    save_reports(reports)

    return {
        "domain": domain,
        "new_count": reports[domain]
    }