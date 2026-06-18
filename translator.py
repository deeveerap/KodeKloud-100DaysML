import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def translate_to_language(text: str, language: str) -> str:
    prompt=f"""
        You are a translator.
        Translate the text {text} into language {language}
        """
    
    response = client.chat.completions.create (
        model="openai/gpt-4.1-mini",
        temperature=0.7,
        max_tokens=100,
        messages = [
            {"role":"user", "content":prompt}
        ]
    )
    print (response.choices[0].message.content)
    return response.choices[0].message.content
if __name__ == "__main__":
    input_msg="Good morning, how are you?"

    translate_to_language(input_msg,"Spanish")
    translate_to_language(input_msg,"French")
