from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Python is one of the most popular programming languages in the world. It is widely used for Artificial Intelligence, Machine Learning, Deep Learning, Web Development, Data Engineering, Automation, and many other domains.
"""

splitter = RecursiveCharacterTextSplitter(

    chunk_size=60,

    chunk_overlap=20

)

chunks = splitter.create_documents([text])

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i+1}\n")

    print(chunk.page_content)