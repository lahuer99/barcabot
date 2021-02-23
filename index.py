from PIL import Image,ImageDraw,ImageFont
 

field=Image.open("./images/turf/field.jpg")
# border=Image.open("./images/turf/border.png")


fieldn=field

# messi=Image.open("messi.jpg")




#get input jersey nos from file
inp=open("input.txt","r")
txt=list(map(int,inp.read().split()))



#make for loop for creating and putting bordered jersnos
h=fieldn.size[1]-1500.0
w=fieldn.size[0]
print(w)
wforeach=int(w/4)-150
j=0
for jno in txt:
	print(jno)
	border=Image.open("./images/turf/border.png")
	d1=ImageDraw.Draw(border)
	dfont=ImageFont.truetype("Roboto-Black.ttf",250)
	d1.text((160,110),str(jno),font=dfont,fill=(255,255,255))
	bordern=border.resize((450,450))
	fieldn.paste(bordern,(580+(j*wforeach),int(h)))
	j+=1
	fieldn.save("how.jpg")

	

# {
# d1=ImageDraw.Draw(border)
# dfont=ImageFont.truetype("Roboto-Black.ttf",250)

# d1.text((100,110),"12",font=dfont,fill=(255,255,255))

# bordern=border.resize((450,450))
# h=fieldn.size[1]-1500.0

# fieldn.paste(bordern,(580,int(h)))
# fieldn.save("how.jpg")
# }