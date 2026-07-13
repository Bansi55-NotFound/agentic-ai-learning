from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("employee_handbook.pdf")

documents = loader.load()

print(documents)