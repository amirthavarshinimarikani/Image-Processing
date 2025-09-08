import cv2 as cv

img = cv.imread(r'C:\Users\amirt.AMIRTHAVARSHINI\OneDrive\Documents\Pictures\My Pic\Tendral.jpeg')

# Check if image is loaded properly
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()
