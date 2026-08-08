from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='Langchain-Document-Loaders',
    glob='*.pdf',  # defines the file pattern to match PDF files
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))
print(docs[1].page_content)
