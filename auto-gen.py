import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')

def generator():
    client = OpenAI(
        base_url="https://api.studio.nebius.ai/v1",
        api_key=os.getenv('N_KEY')
    )

    prompt = """
        Hi, we have an application in flask which works on our localhost:5000 to be accesible on our virtual machine in the cloud. 
        please prepare docker file and create github actions for us to run new deployment on virtual machine we are commiting something in master
    """
    response = client.chat.completions.create(
        model="Qwen/Qwen2-VL-72B-Instruct",
        messages=[{
            "role":"user",
            "content": [
                {"type": "text",
                 "text": prompt}
            ],
        }],
        max_tokens=10000,
    )

    print(f"Response:{response.choices[0].message.content}")

generator()