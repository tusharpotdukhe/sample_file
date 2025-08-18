import google.generativeai as genai
import os
from PIL import Image

# === STEP 1: Set up your API key ===
GOOGLE_API_KEY = "AIzaSyB_ZzFPFGBYnjDdo-29tu8X3b_orUHDx6U"
genai.configure(api_key=GOOGLE_API_KEY)

# === STEP 2: Load the model ===
model = genai.GenerativeModel("gemini-2.0-flash")

# === STEP 3: Load image and prepare prompt ===
def extract_text_from_image(image_path):
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()

    prompt = "Extract all readable text from this image."

    # === STEP 4: Perform OCR with Gemini ===
    response = model.generate_content(
        [prompt, Image.open(image_path)]
    )
    
    return response.text.strip()

# === Example usage ===
if __name__ == "__main__":
    image_path = "D:\Batch_Creation\cm92y1g8w03gf01xsgrbl6wdzcm92y1g8w03gg01xs0iq9a1lq.jpg"  # Replace with your image path
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:\n", extracted_text)
