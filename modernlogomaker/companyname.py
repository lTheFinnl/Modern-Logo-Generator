import os
import random
from PIL import Image, ImageDraw, ImageFont

VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

fonts = []

for font in os.listdir(os.path.dirname(__file__) + '/fonts/'):
    fonts.append(os.path.dirname(__file__) + '/fonts/' + font)

def confirm():
    if input('Generate logo? (y/n): ') == 'y':
        generate_logo()
    else:
        quit()

def ask_for_save(name, image):
    if input('Save "' + name + '" to saved_logos folder? (y/n): ') == 'y':
        print("Saving...")
        image.save(os.path.dirname(__file__) + '/saved_logos/' + name + '.PNG')
        print("Saved.")
    confirm()

def generate_logo():

    print('Generating. Logo will appear shortly.')
    
    image = Image.new('RGB',(10000,10000), (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    draw = ImageDraw.Draw(image)

    vowel_positions = []
    name = []
    name_length = 4
    vowel_amount = 2
    vowel_positions.append(random.randint(1,2))
    
    for vowel in range(vowel_amount - 1):
        try_position = random.randint(1,name_length)
        while try_position in vowel_positions or try_position + 1 in vowel_positions or try_position - 1 in vowel_positions:
            try_position = random.randint(1,name_length)
        vowel_positions.append(try_position)
    
    for letter in range(name_length):
        if letter + 1 in vowel_positions:
            name.append(VOWELS[random.randint(0,len(VOWELS) - 1)])
        else:
            name.append(CONSONANTS[random.randint(0,len(CONSONANTS) - 1)])
    
    if random.randint(1,2) == 1:
        name.append('.')

    fnt = ImageFont.truetype(fonts[random.randint(0,3)], size=3200)
    draw.text((random.randint(500,1500),(random.randint(500,5500))),''.join(name),font=fnt,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    
    print('Success.')
    
    image.show()

    ask_for_save(''.join(name), image)

confirm()
