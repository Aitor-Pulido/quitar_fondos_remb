from rembg import remove
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import sys


def quitarFondo(imagen,ruta):
    input = Image.open(imagen)
    print("Dentro del metodo")
    output = remove(input)
    output.save(ruta)
    return "ya esta"

output_path = "C:\\Users\\Carlos\\PycharmProjects\\remb\\output2.png"


imagen = "C:\ProyectOCR\Data\Fotos Lápidas\IMG_0001.JPG"
print("prueba desde python")

imagen = str(sys.argv[1])
output_path = str(sys.argv[2])

print("Desde python")
print(imagen)
print(output_path)

quitarFondo(imagen, output_path)
print("prueba desde python2")



'''
a2 = plt.imread(imagen_problematica)
input = cv2.imread(input_path)
output = remove(input)
plt.imsave("salida.jpg",output)
cv2.imwrite(output_path, output)
'''
