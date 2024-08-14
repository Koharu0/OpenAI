from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1-hd", #tts-1, tts-1-hd
    voice="nova", #alloy, echo, fable, onyx, nova, shimmer
    input="Hello, World!",
)

with open("output.flac", "wb") as f: #Opus, AAC, FLAC, WAV, PCM
    f.write(response.content)
