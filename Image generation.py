import requests
from openai import OpenAI
from PIL import Image
from io import BytesIO

def generations():
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt="Spotify",
        size="1024x1024",  # 1024x1024, 1024x1792, 1792x1024
        quality="hd",  # standard, hd
        n=1,
    )
    image_url = response.data[0].url
    print(image_url)

    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.save("output.png")

def edits():
    client = OpenAI()
    response = client.images.edit(
        model="dall-e-2",
        image=open("image.png", "rb"),  # must be a .png
        mask=open("mask.png", "rb"),  # must be a .png
        prompt="pancakes topped with strawberries",
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    print(image_url)

    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.save("output.png")

def variations():
    client = OpenAI()
    response = client.images.create_variation(
        model="dall-e-2",
        image=open("image.png", "rb"),
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    print(image_url)

    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.save("output.png")

while True:
    user_input = input("Enter 'Generations', 'Edits', or 'Variations': ")
    
    if user_input.lower() == 'generations':
        generations()
        break
    elif user_input.lower() == 'edits':
        edits()
        break
    elif user_input.lower() == 'variations':
        variations()
        break
    else:
        print("Invalid input. Please enter 'Generations', 'Edits', or 'Variations'.")
