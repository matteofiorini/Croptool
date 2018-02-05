from PIL import Image
##inserire altezza e larghezza del crop che si desidera ottenere
l_gap = 400
h_gap = 400
##inserire dimensione della sovrapposizione che si desidera avere
l_up = 71
h_up = 43
##inserire nome immagine che si desidera tagliare
img = Image.open("2D.CE.DR.1.A.png")
width = img.size[0]
height = img.size[1]
l=0
k=0
x=0
y=0
t=0
print("Larghezza immagine: \n\t")
print width
print("Lunghezza immagine: \n\t")
print height
while (y <= (height - h_gap)):
	x = 0
	while (x <= (width-l_gap)):
		print x, x+l_gap, y, y+h_gap, k
		immagine = img.crop((x, y, x+l_gap, y+h_gap))
		immagine.save("img_6113570064_C_" + str(k) + ".JPEG")
		x = x+l_gap-l_up
		k = k+1
		if(x>(width-l_gap)):
			print width-l_gap, width, y, y+h_gap, k
			immagine = img.crop((width-l_gap, y, width, y+h_gap))
			immagine.save("img_6113570064_C_" + str(k) + ".JPEG")
			k=k+1
	y = y+ h_gap-h_up
	if(y>(height-h_gap)):
			x=0
			while (x <= (width-l_gap)):
				print x, x+l_gap, height-h_gap, height, k
				immagine = img.crop((x, height-h_gap, x+l_gap, height))
				immagine.save("img_6113570064_C_" + str(k) + ".JPEG")
				t=t+1
				x = x+l_gap-l_up
				k = k+1
				if(x>(width-l_gap)):
					print width-l_gap, width, height-h_gap, height, k
					immagine = img.crop((width-l_gap, height-h_gap, width, height))
					immagine.save("img_6113570064_C_" + str(k) + ".JPEG")
					k=k+1
					t=t+1
print("\nLarghezza del crop:")
print l_gap
print("\naltezza del crop:")
print h_gap
print("\nNumero di crop eseguiti:")
print k
print t
