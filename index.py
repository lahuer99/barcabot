from __future__ import print_function

from PIL import Image,ImageDraw,ImageFont
 

field=Image.open("./images/turf/field.jpg")
border=Image.open("./images/turf/border.png")


fieldn=field

# messi=Image.open("messi.jpg")

d1=ImageDraw.Draw(border)
dfont=ImageFont.truetype("Roboto-Black.ttf",250)

d1.text((100,110),"12",font=dfont,fill=(255,255,255))

bordern=border.resize((450,450))
# bordern.save("nos.png")
h=fieldn.size[1]-1500.0

fieldn.paste(bordern,(580,int(h)))
fieldn.save("how.jpg")
# messi1=messi
# messi1=messi1.resize((340,340))

# print(border.format,border.size,border.mode)
# print(field.format,field.size,field.mode)
# print(messi.format,messi.size,messi.mode)
# print(messi1.format,messi1.size,messi1.mode)

# border.paste(messi1,(80,70));

# border.save("pasted.png")
