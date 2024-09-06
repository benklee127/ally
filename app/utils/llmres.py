from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI()

def llmres (documents, prompt, model):
    promptarr = []
    sysprompt = {"role":"system", "content": "You are an assistant that looks through the provided information to best answer the question presented"}
    
    
    if model == "gpt3_5":
        promptarr.append(sysprompt)

        for document in documents:
            promptmsg = {"role":"system", "content": document}
            promptarr.append(promptmsg)

        promptarr.append({"role":"user", "content": prompt})
        
        completion = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= promptarr
        )
        
        llm_response = completion.choices[0].message.content
        return llm_response
    elif model == "gpt4":
        pass
    elif model == "gpt4o":
        pass
    elif model == "titan":
        pass
    else:
        pass

