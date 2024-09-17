from PIL import Image, ImageDraw, ImageFont


def write(image_path: str, output_path: str, text: str):
    img = Image.open(image_path)
    I = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial", size=65)

    I.text((28, 36), text, fill=(0, 0, 0), font=font)
    img.save(output_path)


if __name__ == "__main__":
    write()
