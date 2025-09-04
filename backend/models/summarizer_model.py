
# summarizer model placeholder
from transformers import pipeline

# Load summarization model (can replace with T5/BART)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=150):
    if not text:
        return ""
    summary = summarizer(text, max_length=max_length, min_length=40, do_sample=False)
    return summary[0]['summary_text']
