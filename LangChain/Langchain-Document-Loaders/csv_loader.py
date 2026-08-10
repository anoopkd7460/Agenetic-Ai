from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Langchain-Document-Loaders/Products.csv')

data = loader.load()

print(len(data))
print(data[0].page_content)