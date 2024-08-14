from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO

client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="Spotify",
  size="1024x1024", #1024x1024, 1024x1792, 1792x1024
  quality="hd", #standard, hd
  n=1,
)

image_url = response.data[0].url
print(image_url)

response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.save("output.png")
