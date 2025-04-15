from PIL import Image
import os

# orginal image folder
input_folder = os.path.join(os.getcwd(),"images")
# new folder store resized images
output_folder = os.path.join(os.getcwd(),"images_224")
os.makedirs(output_folder, exist_ok=True)

# new size
new_size = (224, 224)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        image_path = os.path.join(input_folder, filename)
        with Image.open(image_path) as img:
            resized_img = img.resize(new_size)
            save_path = os.path.join(output_folder, filename)
            resized_img.save(save_path)