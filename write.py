from PIL import Image, ImageDraw, ImageFont
import os

# Создаем изображение с белым фоном
img = Image.new('RGB', (500, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Создаем шрифт по умолчанию, если файл не найден
font_path = "handwriting.ttf"
if not os.path.exists(font_path):
    font = ImageFont.load_default()
else:
    font = ImageFont.truetype(font_path, 40)

# Пишем текст
text = "Hello, this is handwritten!"
draw.text((50, 50), text, fill=(0, 0, 0), font=font)

# Сохраняем изображение
output_path = "handwriting_text.png"
img.save(output_path)

print(f"Файл {output_path} успешно создан!")
