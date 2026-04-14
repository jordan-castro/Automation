from PIL import Image
from glob import glob


images = glob("*.jpg")

image_list = []

for img in images:
    image = Image.open(img).convert('RGB')
    width, height = image.size
    if width > height:
        image = image.rotate(90, expand=True)
    image_list.append(image)

# Save all as a single multi-page PDF
# result = Image.new('RGB', image_list[1].size)
image_list[0].save('EvelynRodriguez.pdf', save_all=True, append_images=image_list[1:])
