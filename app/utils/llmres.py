from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI()

def llmres (documents, prompt, model):
    promptarr = []
    sysprompt = {"role":"system", "content": "You are an assistant that looks through the provided information to best answer the question presented"}
    
    print("model: ", model)
    
    if model == "gpt3_5":
        print("gpt3 model path hit")
        promptarr.append(sysprompt)

        for document in documents:
            promptmsg = {"role":"system", "content": document}
            promptarr.append(promptmsg)

        promptarr.append({"role":"user", "content": prompt})
        
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= promptarr
        )
        
        llm_response = response.choices[0].message.content
        return llm_response
    elif model == "gpt4o":
        print("gpt4o model path hit")
        promptarr.append(sysprompt)

        for document in documents:
            promptmsg = {"role":"system", "content": document}
            promptarr.append(promptmsg)

        promptarr.append({"role":"user", "content": prompt})

        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages= promptarr
        )        

        llm_response = response.choices[0].message.content
        return llm_response
    elif model == "gpt4o_mini":
        promptarr.append(sysprompt)

        for document in documents:
            promptmsg = {"role":"system", "content": document}
            promptarr.append(promptmsg)

        promptarr.append({"role":"user", "content": prompt})

        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages= promptarr
        )        

        llm_response = response.choices[0].message.content
        return llm_response
    elif model == "gpt4_turbo":
        promptarr.append(sysprompt)

        for document in documents:
            promptmsg = {"role":"system", "content": document}
            promptarr.append(promptmsg)

        promptarr.append({"role":"user", "content": prompt})
        response = openai_client.chat.completions.create(
            model="gpt-4-turbo",
            messages= promptarr
        )        

        llm_response = response.choices[0].message.content
        return llm_response
        
    elif model == "gpt4_turbo":
        pass
    elif model == "titan":
        pass
    else:
        pass

