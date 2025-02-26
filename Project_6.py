import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the BLIP Processor & Model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to("cuda" if torch.cuda.is_available() else "cpu")

# Function to generate captions
def generate_caption(image_path):
    if not image_path:
        raise ValueError("Error: Image path is empty.")

    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        raise FileNotFoundError(f"Error: Could not open image. {e}")

    inputs = processor(image, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    caption_ids = model.generate(**inputs, max_length=50, num_beams=5, temperature=1.5)
    caption = processor.decode(caption_ids[0], skip_special_tokens=True)
    
    return caption

# Example Usage
if __name__ == "__main__":
    image_path = "dataset/images/image2.jpg"  # Change to your image path
    caption = generate_caption(image_path)
    print("📝 Generated Caption:", caption)
