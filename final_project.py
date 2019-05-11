import cv2
import numpy as nmp

#Show original image, convert to png
img = cv2.imread('Castle.jpg')
#cv2.imshow('original',img)
cv2.imwrite("Castle.png", img)

#Show grayscale image, convert to png
gray = cv2.imread('Castle.jpg', 0)
#cv2.imshow('Grayscale',grayscale)
cv2.imwrite("Grayscale.png", gray)

#Define outline
edge = cv2.Canny(gray,450,300)

cv2.imwrite("Edges.png", edge)

#Make invert outline

edge_E = cv2.bitwise_not(edge)
cv2.imwrite("Edge_E.png", edge_E)

#Combine into a single image
background = cv2.imread("Castle.png")
overlay = cv2.imread("Edge_E.png")

result = cv2.addWeighted(background,1,overlay,0.1,0)

cv2.imwrite("Highlighted.png", result)

cv2.imshow("Highlighted.png", img)
