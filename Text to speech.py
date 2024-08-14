from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1-hd",
    voice="nova",
    input="Hello, World!",
)

with open("output.flac", "wb") as f:
    f.write(response.content)
