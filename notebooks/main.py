from PIL import Image, ImageDraw, ImageFont
import textwrap

def add_text_to_image(image_path, text, width, font_path, font_size, subtitle):
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Wrap the text
    lines = textwrap.wrap(text, width=width)
    
    # Calculate the total height of the text block
    total_height = sum(font.getbbox(line)[3] for line in lines)
    # Center the text block vertically
    y = (image.height - total_height) / 2
    y = y - 100;
    # Draw each line of text
    for line in lines:
        # draw.text((x, y), line, font=font, fill="black")
        # dray text at the center of the image
        text_width = font.getbbox(line)[2]  # Extract width and height
        # AttributeError: 'ImageDraw' object has no attribute 'textsize'
        # Calculate x, y position for the text
        x_pos = (image.width - text_width) / 2
        y_pos = y
        draw.text((x_pos, y_pos), line, font=font, fill="white")
        
        y += font.getbbox(line)[3]  # [3] gives the height of the text
    
    # Save or show the image
    #image.show()
    subTitleWidth = font.getbbox(subtitle)[2]  # Extract width and height
    subTitleX = (image.width - subTitleWidth) / 2
    draw.text((subTitleX, image.height-350), subtitle, font=font, fill="white")
    return image

def bulkProcess():
    # Bulk Process New Texts with the same Base Image
    #Pick texts from external text file
    with open('assets/texts.txt', 'r') as file:
        texts = file.readlines()
        # Remove newline characters
        texts = [text.strip() for text in texts]

        for i, text in enumerate(texts):    
            image = add_text_to_image(
                image_path='assets/base.png',
                text=text,
                width=40,  # Number of characters per line
                font_path='assets/times.ttf',
                font_size=48, 
                subtitle="ROBERT GREENE"
            )
            image.save(f"assets/outputs/{i}.png")
        # Save the last image

if(__name__=="__main__"):
    bulkProcess()