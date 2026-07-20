from extractor import extract_text
from analyzer import analyze_document


# Extract text from PDF
document = extract_text("uploads/resume.pdf")


# Analyze document
analysis = analyze_document(document)


print(analysis)