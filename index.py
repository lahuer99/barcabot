from PIL import Image,ImageDraw,ImageFont
 

field=Image.open("./images/turf/field.jpg")
# border=Image.open("./images/turf/border.png")


fieldn=field


#get input jersey nos from file
inp=open("input.txt","r")
formation=[]
for line in inp.readlines():
	txt=list(map(int,line.split()))
	formation.append(txt)

# sections=len(formation)
# print(sections)

for m in formation:
	print(m)


hforeach=(fieldn.size[1]-350)/len(formation)

hnos=0
for line in formation:
	wforeach=(fieldn.size[0]-200)/len(line)
	wnos=0
	startpos=(wforeach)/2
	for jersno in line:
		border=Image.open("./images/turf/border.png")
		d1=ImageDraw.Draw(border)
		dfont=ImageFont.truetype("./fonts/Roboto-Black.ttf",250)
		if(jersno<10):
			d1.text((170,110),str(jersno),font=dfont,fill=(255,255,255))
		else:
			d1.text((100,110),str(jersno),font=dfont,fill=(255,255,255))
		bordern=border.resize((450,450))
		fieldn.paste(bordern,(int(startpos-105+(wnos*wforeach)),int(700+(hnos*hforeach))),bordern)
		fieldn.save("how.jpg")
		wnos+=1
	hnos+=1



# ---------------------------------------



# {
# #make for loop for creating and putting bordered jersnos
# h=fieldn.size[1]-1500.0


# w=fieldn.size[0]
# wforeach=int(w/4)-150


# j=0
# for jno in txt:
# 	print(jno)
# 	border=Image.open("./images/turf/border.png")
# 	d1=ImageDraw.Draw(border)
# 	dfont=ImageFont.truetype("Roboto-Black.ttf",250)
# 	d1.text((160,110),str(jno),font=dfont,fill=(255,255,255))
# 	bordern=border.resize((450,450))
# 	fieldn.paste(bordern,(580+(j*wforeach),int(h)))
# 	j+=1
# 	fieldn.save("how.jpg")

# }











# ----------------------------------------------------------	

# {
# #draw and paste init
# d1=ImageDraw.Draw(border)
# dfont=ImageFont.truetype("Roboto-Black.ttf",250)

# d1.text((100,110),"12",font=dfont,fill=(255,255,255))

# bordern=border.resize((450,450))
# h=fieldn.size[1]-1500.0

# fieldn.paste(bordern,(580,int(h)))
# fieldn.save("how.jpg")
# }