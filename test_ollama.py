import ollama

try:
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    )
    print("Success! Ollama is working.")
    print("Response from Llama 3:", response['message']['content'])
except Exception as e:
    print("An error occurred:", e)