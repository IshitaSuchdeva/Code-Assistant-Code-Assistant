# import requests
# import json
# import gradio as gr

# url="http://localhost:11434/api/generate"

# headers={

#     'Content-Type':'application/json'
# }

# history=[]

# def generate_response(prompt):
#     history.append(prompt)
#     final_prompt="\n".join(history)

#     data={
#         "model":"codegirl",
#         "prompt":final_prompt,
#         "stream":False
#     }

#     response=requests.post(url,headers=headers,data=json.dumps(data))

#     if response.status_code==200:
#         response=response.text
#         data=json.loads(response)
#         actual_response=data['response']
#         return actual_response
#     else:
#         print("error:",response.text)


# interface=gr.Interface(
#     fn=generate_response,
#     inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
#     outputs="text"
# )
# interface.launch()
import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "codegirl",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print("Error:", response.text)
        return "Error in response"

# Define a CSS style to make the interface look glamorous
css = """
body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(135deg, #f3e6e8, #f5b3c4);
    color: #333;
    text-align: center;
    padding: 20px;
    margin: 0;
}

h1 {
    color: #d63384;
    font-size: 3em;
    margin-bottom: 10px;
}

h2 {
    color: #333;
    font-size: 1.5em;
    margin-bottom: 20px;
}

textarea {
    width: 100%;
    height: 150px;
    padding: 15px;
    border-radius: 10px;
    border: 2px solid #d63384;
    font-size: 1.1em;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

#component-1 {
    width: 100%;
}

.output-textbox {
    width: 100%;
    padding: 15px;
    border-radius: 10px;
    border: 2px solid #d63384;
    font-size: 1.1em;
    background-color: #fff;
    margin-top: 20px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

footer {
    margin-top: 40px;
    font-size: 0.9em;
    color: #777;
}
"""

# Create the Gradio interface with custom CSS and layout
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt here...", label="Your Prompt"),
    outputs=gr.Textbox(label="Code Girl's Response", elem_id="output-textbox"),
    title="Code Girl",
    description="A code assistant made by Ishita",
    theme="huggingface",
    css=css
)

interface.launch()

