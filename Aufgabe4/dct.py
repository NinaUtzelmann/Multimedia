#!/usr/bin/python

from PIL import Image
from scipy import fftpack
from scipy.fftpack import dct, idct
import numpy

pixelMatrix = {}
discretCosinusMatrix = {}
SIZE = 8

img = Image.open("baboon.jpg")
WIDTH, LENGTH = img.size

pixelMap = img.load()

quantizationMatrix = numpy.array([16, 11, 10, 16, 24, 40, 51, 61,
								   12, 12, 14, 19, 26, 58, 60, 55,
								   14, 13, 16, 24, 40, 57, 69, 56,
								   14, 17, 22, 29, 51, 87, 80, 62,
								   18, 22, 37, 56, 68, 109, 103, 77,
								   24, 35, 55 ,64, 81, 104, 113, 92,
								   49, 64, 78, 87, 103, 121, 120, 101,
								   72, 92, 95, 98, 112, 100, 103, 99])


def readIn():
	for row in range(0, int(WIDTH/SIZE)): #WIDTH/SIZE = 16
		for column in range(0, int(LENGTH/SIZE)): #LENGTH/SIZE = 16
			columnInBlock = []

			for pixelRow in range(0, SIZE):
				rowInBlock = []

				for pixelColumn in range(0, SIZE):
					newInput = pixelMap[pixelRow + row * SIZE, pixelColumn + column * SIZE]
					rowInBlock.append(float(newInput))

				columnInBlock.append(rowInBlock)

			pixelMatrix[row, column] = columnInBlock


def discretCosTrans():
	for key, value in pixelMatrix.items():
		discretCosinusMatrix[key] = dct(value, norm='ortho')

def quantization():
	i = 0
	for key, value in discretCosinusMatrix.items():
		a = []
		for liste in value:
			b = []
			for pixel in liste:
				if i == len(value):
					i = 0
				pixel = round(pixel/quantizationMatrix[i])
				b.append(pixel)
				i += 1
			a.append(b)
		discretCosinusMatrix[key] = a

def decode():
	i = 0
	for key, value in discretCosinusMatrix.items():
		a = []
		for liste in value:
			b = []
			for pixel in liste:
				if i == len(value):
					i = 0
				pixel = pixel * quantizationMatrix[i]
				b.append(pixel)
			a.append(b)
		discretCosinusMatrix[key] = a

def indiscretCosTrans():
	for key, value in discretCosinusMatrix.items():
		discretCosinusMatrix[key] = idct(value, norm='ortho')

def writeOut():
	imgOut =  Image.new('L', (WIDTH, LENGTH))
	for key, value in discretCosinusMatrix.items():
		x = 0
		for liste in value:
			y = 0
			for pixel in liste:
				xy = (x + key[0] * SIZE, y + key[1] * SIZE)
				imgOut.putpixel(xy, int(pixel))
				y += 1
			x += 1

	imgOut.save("ImageOut.jpg")


if __name__ == "__main__":
	readIn()
	discretCosTrans()
	quantization()
	decode()
	indiscretCosTrans()
	writeOut()


