# preprocessing placeholder
import re
import string

def clean_text(text):
    """
    Clean and preprocess the text for NLP tasks.
    Steps:
    - Remove extra whitespace
    - Remove HTML tags
    - Remove special characters and numbers
    - Convert text to lowercase
    """
    if not text:
        return ""

    # Remove HTML tags
    text = re.sub(r'<.*?>', ' ', text)

    # Remove numbers and punctuation
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    # Convert to lowercase
    text = text.lower().strip()

    return text

def split_into_paragraphs(text):
    """
    Split text into paragraphs based on line breaks or periods.
    Useful for summarization or context chunks for chatbot.
    """
    paragraphs = [p.strip() for p in re.split(r'\n+|\.\s+', text) if p.strip()]
    return paragraphs

# Example usage
if __name__ == "__main__":
    sample_text = """
    <p>SEBI has issued a new circular regarding compliance deadlines.</p>
    All investors must follow the guidelines by 30th September 2025.
    """
    cleaned = clean_text(sample_text)
    print("Cleaned Text:", cleaned)
    print("Paragraphs:", split_into_paragraphs(cleaned))
