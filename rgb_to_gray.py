import cv2 as cv

original_image = cv.imread(r'C:\Users\amirt.AMIRTHAVARSHINI\OneDrive\Documents\Pictures\starryNight.jpg')
gray_image = cv.cvtColor(original_image,cv.COLOR_BGR2GRAY)

cv.imshow('Origin',original_image)
cv.imshow('Gray',gray_image)
