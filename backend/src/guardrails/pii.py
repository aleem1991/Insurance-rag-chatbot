import re

try:
    from presidio_analyzer import AnalyzerEngine
    analyzer = AnalyzerEngine()
except Exception:
    analyzer = None

# Fallback regex patterns for PII
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
PHONE_REGEX = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
CREDIT_CARD_REGEX = r"\b(?:\d[ -]*?){13,16}\b"


def detect_pii(text: str) -> bool:
    """
    Detect whether the input text contains supported PII.
    Returns True if PII is found, otherwise False.
    """
    if analyzer is not None:
        try:
            results = analyzer.analyze(
                text=text,
                language="en",
                entities=[
                    "PHONE_NUMBER",
                    "EMAIL_ADDRESS",
                    "CREDIT_CARD",
                ],
            )
            if len(results) > 0:
                return True
        except Exception:
            pass

    # Regex fallback
    if re.search(EMAIL_REGEX, text) or re.search(PHONE_REGEX, text) or re.search(CREDIT_CARD_REGEX, text):
        return True

    return False