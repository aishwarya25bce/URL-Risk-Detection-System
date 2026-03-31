# core/redirect.py

import requests


def check_redirects(original_url):
    """
    Check how many times URL redirects
    """

    try:
        response = requests.get(
            original_url,
            allow_redirects=True,
            timeout=5
        )

        redirect_count = len(response.history)
        final_url = response.url

        # Risk scoring
        if redirect_count >= 4:
            risk = 30
        elif redirect_count == 3:
            risk = 20
        elif redirect_count == 2:
            risk = 10
        elif redirect_count == 1:
            risk = 5
        else:
            risk = 0

        return {
            "redirect_count": redirect_count,
            "final_url": final_url,
            "risk": risk
        }

    except Exception as e:
        return {
            "redirect_count": 0,
            "final_url": original_url,
            "risk": 0,
            "error": str(e)
        }