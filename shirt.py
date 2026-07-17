import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

valid = ['.jpg', '.jpeg', '.png']

if not any(sys.argv[1].lower().endswith(ext) for ext in valid):
    sys.exit ('Invalid input')
if not any(sys.argv[2].lower().endswith(ext) for ext in valid):
    sys.exit('Invalid output')
if sys.argv[1].split('.')[-1] != sys.argv[2].split('.')[-1]:
    sys.exit('Input and output have different extensions')

try:
    from PIL import Image, ImageOps
    input_img = Image.open(sys.argv[1])
    shirt = Image.open('shirt.png')
    input_img = ImageOps.fit(input_img, shirt.size)
    input_img.paste(shirt, mask=shirt)
    input_img.save(sys.argv[2])
except FileNotFoundError:
    sys.exit('Input does not exist')
