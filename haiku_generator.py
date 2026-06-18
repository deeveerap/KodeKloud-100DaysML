import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def generate_haiku(topic: str) -> str:
    user_prompt=f"""
        generates three-line haikus (5-7-5 syllable pattern) based on a given topic {topic}
       """
    
    response = client.chat.completions.create (
        model="openai/gpt-4.1-mini",
        temperature=0.0,
        max_tokens=60,
        messages = [
            {"role":"user", "content":user_prompt}
        ]
    )
    print (response.choices[0].message.content)
    return response.choices[0].message.content
if __name__ == "__main__":
    input_msg="sky"
    generate_haiku(input_msg)

-----------------------------------------------------
import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def generate_haiku(topic: str) -> str:
    user_prompt=f"""
        You are a strict Haiku generator. Generate a 3-line haiku about the topic '{topic}' using a strict 5-7-5 syllable pattern.
Rules:
1. Do not include any introductory text, confirmation, or explanations. 
2. Print ONLY the 3 lines of poetry.
3. Line 1 and line 3  should have 5 syllable
4. Line 2 should have 7 syllable
Haiku for topic '{topic}':"""
    
    response = client.chat.completions.create (
        model="openai/gpt-4.1-mini",
        temperature=0.0,
        max_tokens=60,
        messages = [
            {"role":"user", "content":user_prompt}
        ]
    )
    print (response.choices[0].message.content)
    return response.choices[0].message.content
if __name__ == "__main__":
    input_msg="sky"
    generate_haiku(input_msg)
