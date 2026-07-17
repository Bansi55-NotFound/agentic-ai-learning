from transformers import pipeline


print("=" * 50)
print("Sentiment Analysis")
print("=" * 50)

sentiment = pipeline("sentiment-analysis")

result = sentiment("I love learning Hugging Face!")
print(result)


print("\n" + "=" * 50)
print("Text Classification")
print("=" * 50)

classifier = pipeline(
    task="text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

result = classifier("This movie is amazing!")
print(result)


print("\n" + "=" * 50)
print("Summarization")
print("=" * 50)

summarizer = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn"
)

text = """
Artificial Intelligence is transforming industries by automating tasks,
improving decision making and enabling intelligent applications across
healthcare, finance, manufacturing and education.
"""

result = summarizer(
    text,
    max_length=40,
    min_length=15
)

print(result)


print("\n" + "=" * 50)
print("Translation")
print("=" * 50)

translator = pipeline(
    task="translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

result = translator("Good Morning! Have a wonderful day.")
print(result)


print("\n" + "=" * 50)
print("Question Answering")
print("=" * 50)

qa = pipeline("question-answering")

result = qa(
    question="Where does Bansi work?",
    context="Bansi works as a Data Engineer at Boeing."
)

print(result)


print("\n" + "=" * 50)
print("Fill Mask")
print("=" * 50)

fill_mask = pipeline(
    task="fill-mask",
    model="bert-base-uncased"
)

result = fill_mask("Paris is the [MASK] of France.")
print(result)


print("\n" + "=" * 50)
print("Named Entity Recognition")
print("=" * 50)

ner = pipeline(
    task="ner",
    grouped_entities=True
)

result = ner("Elon Musk founded SpaceX in the United States.")
print(result)


print("\n" + "=" * 50)
print("Text Generation")
print("=" * 50)

generator = pipeline(
    task="text-generation",
    model="distilgpt2"
)

result = generator(
    "Artificial Intelligence is",
    max_new_tokens=50
)

print(result[0]["generated_text"])