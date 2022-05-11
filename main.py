from rembg import remove
import cv2
import matplotlib.pyplot as plt
from PIL import Image


def quitarFondo(imagen,ruta):
    input = Image.open(imagen)
    output = remove(input)
    output.save(ruta)


input_path = 'Images/Training/IMG_0008.JPG'
output_path = 'output2.png'


imagen_problematica = "output.png"


quitarFondo(imagen_problematica, output_path)



'''
a2 = plt.imread(imagen_problematica)
input = cv2.imread(input_path)
output = remove(input)
plt.imsave("salida.jpg",output)
cv2.imwrite(output_path, output)
'''
