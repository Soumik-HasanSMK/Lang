from decouple import config
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient


SECRET_KEY=config("HUGGINGFACE_KEY")
# print(SECRET_KEY)
val=input("Enter poet type: ")

template = "<s>[INST] Suppose you are a poet. Write poem:</s>{question}[/INST]"
prompt_template = PromptTemplate.from_template(template)
formatted_template = prompt_template.format(question=val)

# print(formatted_template)

repo_id="mistralai/Mistral-7B-Instruct-v0.3"

llm_endpoint = InferenceClient(model=repo_id,token=SECRET_KEY)

response = llm_endpoint.text_generation(formatted_template)

print(response)