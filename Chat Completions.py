import shutil
from openai import OpenAI

client = OpenAI()

def Chat():
    conversation_history = []

    while True:
        user_input = input("User: ")
        
        if user_input.lower() in ["exit", "quit"]:
            break

        conversation_history.append({"role": "user", "content": user_input})
        
        stream = client.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=conversation_history,
            stream=True,
        )

        response_content = ""
        print("Assistant: ", end="")
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
                response_content += chunk.choices[0].delta.content
        
        terminal_width = shutil.get_terminal_size().columns
        print("\n" + "-" * terminal_width)
        
        conversation_history.append({"role": "assistant", "content": response_content})

if __name__ == "__main__":
    Chat()
