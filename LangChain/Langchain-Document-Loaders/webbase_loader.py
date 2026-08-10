from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model = 'llama-3.1-8b-instant'
)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text -\n {text}',
    input_variables=['text','question']
)

parser=StrOutputParser()

url='https://www.amazon.in/HP-Micro-Edge-Anti-Glare-Office24-ep1180TU/dp/B0G2BHDDB8/ref=sr_1_1_sspa?crid=1R1GZBCPD341Q&dib=eyJ2IjoiMSJ9.-vT3_gnKHeNZskp8ROzShGu8dHgubbYntUhC5vErn_RAYAejawzVkUANSLIAWJIQeExHMjYvhpRNEWfZ86QNIGszP1g3xydNKfOGUoSMdP9x0YcbzlC9WsyITNUgKx5wkmMGrr4p0ddR1dWwXP6lo2z8KMJumd7-BWG121hjNmz1_6644FQHCkxK5y6pxdk6u6lvhregmQETyl1l-zYPQuCLpZJAB3lNIY4bD_zjIh0.1MOvU-meG8uoY11piY1s3HIgiaYBr-Wke1WXfPeCZHA&dib_tag=se&keywords=hp%2Blaptop%2Bi5%2B13th%2Bgeneration%2B16gb%2Bram&qid=1786189774&sprefix=hp%2B%2Caps%2C439&sr=8-1-spons&aref=1L219pPDi6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'What is the product that we are talking about?', 'text':docs[0].page_content}))
