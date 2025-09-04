from utils.preprocess import clean_text, split_into_paragraphs
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization")

# Sample SEBI circular text
sample_text = """
SEBI has issued a new circular regarding compliance deadlines.
All investors must follow the guidelines by 30th September 2025.
Non-compliance may attract penalties.
"""

# Preprocess text
cleaned_text = clean_text(sample_text)
paragraphs = split_into_paragraphs(cleaned_text)

# Summarize each paragraph
for i, para in enumerate(paragraphs):
    summary = summarizer(para, max_length=60, min_length=20, do_sample=False)
    print(f"Paragraph {i+1} Summary: {summary[0]['summary_text']}")

# Example Q&A
qa_pipeline = pipeline("question-answering")
question = "What is the deadline mentioned?"
context = cleaned_text
answer = qa_pipeline(question=question, context=context)
print("Answer:", answer['answer'])
