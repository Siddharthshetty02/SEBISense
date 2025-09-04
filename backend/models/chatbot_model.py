# chatbot model placeholder
from transformers import pipeline

# Load a simple QA model
qa_pipeline = pipeline("question-answering")

def answer_query(question, context):
    if not question or not context:
        return "Please provide both question and context."
    result = qa_pipeline(question=question, context=context)
    return result['answer']
