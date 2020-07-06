# -----Python example program for applying minimum filter to a Digital Image-----

 

# import the required PIL Modules

from PIL import Image

from PIL import ImageFont

from PIL import ImageDraw

from PIL import ImageFilter

 

# Draw text on the image

def writeText(baseImage, imageDescription, textSize, textX, textY, fontFileLocation):

    baseImage = baseImage.convert('RGBA');   

    textImage = Image.new('RGBA', baseImage.size, (255,255,255,0));

 

    # Select a font for the text

    font = ImageFont.truetype(fontFileLocation, textSize);

    draw = ImageDraw.Draw(textImage);

    draw.text((textX,textY), imageDescription, font=font, fill=(255,0,0,255));

 

    # Do an alpha composite of the two images and return

    return Image.alpha_composite(baseImage, textImage);   

    

# Text size and location

textSize = 50;

textX    = 10;

textY    = 30;

 

fontFileLocation    = "/opt/X11/share/fonts/TTF/luxirr.ttf";

imageFilePath       = "./image2.jpg";

imageText           = "Marca de agua";

 

# Create an image object from a file

imageInstance = Image.open(imageFilePath);

originalImage = writeText(imageInstance, imageText, textSize, textX, textY, fontFileLocation);
originalImage = writeText(imageInstance, imageText, textSize, 400, 200, fontFileLocation);

originalImage.show();

 