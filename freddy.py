from PIL import Image,ImageDraw,ImageFont
from datetime import datetime

def get_ordinal_suffix(day: int) -> str:
    return str(day) + {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th') if day not in (11, 12, 13) else 'th'

def fnaf():
    # sample text and font
    font = ImageFont.truetype("./assets/fonts/five-nights-at-freddys.ttf", 64, encoding="unic")
    # create a blank canvas with extra space between lines
    canvas = Image.new('RGB', (1280, 720), "black")

    # today's day
    todays_day = datetime.now()
    day = int(todays_day.strftime("%d"))
    formatted_day = get_ordinal_suffix(day)

    # draw the text onto the text canvas, and use blue as the text color
    draw = ImageDraw.Draw(canvas)
    draw.text((546,270), f'12: 00  AM', 'white', font, align='center') 
    draw.text((533,336), f'{formatted_day}  Night', 'white', font, align='center')

    # save the blank canvas to a file
    canvas.save("./assets/images/fnaf.png", "PNG")
    return canvas
fnaf()