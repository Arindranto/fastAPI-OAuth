import re


def tokenize_text(text: str) -> list[str]:
    """
    Splits the input text into a list of words.
    - Converts text to lowercase.
    - Uses a regular expression to find sequences of alphabetic characters.
    """
    # Convert text to lowercase for consistent tokenization
    text = text.lower()
    # Find all sequences of alphabetic characters (words)
    words = re.findall(r'\b[a-z]+\b', text)
    return words