
import argparse
from PIL import Image


""" 
import iconConvert
reload(iconConvert)
startImage = r'Insert path here, Ex: r'C:\Users\Marisa\Documents\cgCircuit\screenCaptures\oval.png'
resultImage = startImage.replace('.png','.jpeg')
iconConvert.processScreenCapture(startImage, resultImage)

NOTE: Must be Anaconda2 directory!
python iconConvert.py -ip "C:\Users\Marisa\Documents\cgCircuit\screenCaptures\oval.png" -irp "C:\Users\Marisa\Documents\cgCircuit\screenCaptures\oval.jpeg"

"""


parser = argparse.ArgumentParser(description='Converts any size png to a 400x400 jpeg')
parser.add_argument('-ip', '--imagePath', dest='imagePath', help='path to the starting icon.png')
parser.add_argument('-irp', '--imageResultPath', dest='imageResultPath', help='path to where the image will be stored' )

args = parser.parse_args()


def processScreenCapture(imagePath=None,imageResultPath=None):

	im = Image.open(imagePath)
	width, height = im.size


	left = int(width * 0.5 - 200)
	top  = int(height * 0.5 - 200)
	right = left + 400
	bottom = top + 400


	croppedImg = im.crop((left,top,right,bottom))
	croppedImg.save(imageResultPath)




if __name__ == '__main__':
	# if command line then run it!
	processScreenCapture(imagePath=args.imagePath, imageResultPath=args.imageResultPath)



