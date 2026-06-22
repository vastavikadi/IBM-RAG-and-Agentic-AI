from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain.chat_models import BaseLLM
from langchain_core.output_parsers import StrOutputParser

llm = BaseLLM.generate()

template = """
Tell me a {adjective} joke about {content}"""

prompt = PromptTemplate.from_template(template)

def format_prompt(variables):
    final_prompt = prompt.format(**variables)
    print(final_prompt) # this will print the formatted prompt to the console, allowing us to see the exact prompt that is being sent to the language model. This is useful for debugging and understanding how the input variables are being incorporated into the prompt template.
    return final_prompt


joke_chain = (
    RunnableLambda(format_prompt) | llm | StrOutputParser()
)

response = joke_chain.invoke({"adjective": "funny", "content": "chickens"}) # when the code runs, then runnable lambda takes the input variables, formats the prompt, and passes it to the language model. The language model generates a joke based on the formatted prompt, and the output parser ensures that the response is returned as a string. Finally, we print the response to see the generated joke.

print(response)