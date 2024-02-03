from openai import OpenAI

def chat_with_athena(prompt):
    # Point to the local server
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

    history = [
        {"role": "system", "content": "You are an intelligent therapist. You always provide well-reasoned  answers and keep engaging users."},
        {"role": "user", "content": f"Hello,"},
        {"role": "system", "content": f"Hello, I am Athena, an intelligent therapist."},
        {"role": "user", "content": prompt }
    ]

    while True:
        completion = client.chat.completions.create(
            model="local-model",
            messages=history,
            temperature=0.7,
            stream=True,
        )

        new_message = {"role": "assistant", "content": ""}

        for chunk in completion:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=False)
                new_message["content"] += chunk.choices[0].delta.content

        history.append(new_message)

        return new_message["content"]

