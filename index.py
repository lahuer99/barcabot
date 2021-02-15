from __future__ import print_function

from PIL import Image


field=Image.open("./images/turf/field.jpg")
border=Image.open("./images/turf/border.png")
messi=Image.open("messi.jpg")

messi1=messi
# messi1=messi.crop((498,498,498,498))
messi1=messi1.resize((340,340))

print(border.format,border.size,border.mode)
print(field.format,field.size,field.mode)
print(messi.format,messi.size,messi.mode)
print(messi1.format,messi1.size,messi1.mode)

border.paste(messi1,(80,70));

border.save("pasted.png")
# border.show()