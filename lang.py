from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Load .env file into environment
load_dotenv()

# Initialize ChatGroq
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=512,   # must be an integer
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

def get_response(sentence,language1,language2):
    template=(PromptTemplate(input_variables=["language1","sentence",'language2'], template="I want you to act as a professional translator. Take the following paragraph: {sentence}, which is written in {language1}, and accurately translate it into {language2}. Preserve the meaning, tone, and style of the original text. Only provide the translated paragraph in {language2}, without any explanations or additional commentary."))
    chain=LLMChain(llm=llm,prompt=template)
    # chain1=SequentialChain(chains=[chain],input_variables=["language1","sentence",'language2'])
    response=chain.invoke({"language1":language1,"sentence":sentence,"language2":language2})
    # print(response.keys())
    return (response["text"])

# if __name__=='__main__':
#     get_response("How is it going?","english","hindi")