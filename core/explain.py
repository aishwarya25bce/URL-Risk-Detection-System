# core/explain.py

def generate_explanation(reasons):
    """
    Format reasons into clean readable output
    """

    if not reasons:
        return ["No major risk factors detected"]

    # remove duplicates
    unique_reasons = list(set(reasons))

    # sort for cleaner output (optional)
    unique_reasons.sort()

    return unique_reasons