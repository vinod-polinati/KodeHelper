import requests
import gradio as gr
import json

url="http://localhost:11434/api/generate"

headers={
    
    'Content-Type':'application/json'
}

history=[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt='\n'.join(history)
    data={  
        "model":"Zade",
        "prompt":final_prompt,
        "stream":False
    }
    response=requests.post(url,headers=headers,data=json.dumps(data)) 

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("ERROR:",response.text)

interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your prompt"),
    outputs="text"
)
interface.launch(share=True)