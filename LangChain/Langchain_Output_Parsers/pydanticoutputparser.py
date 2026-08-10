from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

# Pydantic Schema

class Person(BaseModel):
    name: str=Field(description='Name of the person')
    age: int=Field(gt=18, description='Age of the person')
    city: str=Field(description='Name of the city the person belongs to')

# Parser
parser = PydanticOutputParser(pydantic_object=Person)

# Prompt

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables={
        'format_instructions':parser.get_format_instructions()
    }
)


# Create Prompt
prompt = template.invoke(
    {
        'place':'indian'
    }
)

'''
# LLM
response = model.invoke(prompt)


result = parser.parse(response.content)
'''

chain = template | model | parser

result = chain.invoke({'place':'sri lankan'})
print(result)

#print(result.fact_1)
#print(result.fact_2)
#print(result.fact_3)