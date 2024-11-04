import requests
import os

# Hugging Face API token and Stable Diffusion endpoint
API_TOKEN = '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'
url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Prompt to generate an image
prompt = "a futuristic cityscape at sunset with flying cars and neon lights"
payload = {"inputs": prompt}

# Send request to Hugging Face API
response = requests.post(url, headers=headers, json=payload)

# Check response status and output image data
if response.status_code == 200:
    with open("generated_image.png", "wb") as f:
        f.write(response.content)
    print("Image generated successfully!")
else:
    print(f"Error: {response.status_code}", response.text)
