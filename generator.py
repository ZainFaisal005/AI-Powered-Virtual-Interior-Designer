from diffusers import StableDiffusionPipeline
import torch
import re
import io
from PIL import Image

# Load Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"

pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
pipeline.to(device)

def generate_design(room_type, style, color, dimensions):
    try:
        # Handle color descriptions
        color_description = re.sub(r'\band\b', '&', color)
        
        # Prepare prompt
        prompt = f"A {style} {room_type} with a {color_description} color scheme, detailed and photorealistic."

        # Parse dimensions
        width, height = map(int, dimensions.split("x"))
        
        # Generate image
        image = pipeline(prompt).images[0]
        
        # Resize image to user-defined dimensions
        image = image.resize((width, height))

        # Convert image to byte stream
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        image_bytes.seek(0)

        return image_bytes

    except Exception as e:
        print("Error in generate_design:", e)
        raise
