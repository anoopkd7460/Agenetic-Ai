from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model = 'llama-3.1-8b-instant'
)

prompt = PromptTemplate(
    template='Write a summary of the following poem -\n {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

loader = TextLoader('Langchain-Document-Loaders/cricket.txt', encoding='utf8')

docs = loader.load()

print(docs)
print(len(docs))

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))