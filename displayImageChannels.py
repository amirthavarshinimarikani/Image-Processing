import cv2
import numpy as np

image = cv2.imread(r"C:\Users\amirt.AMIRTHAVARSHINI\OneDrive\Desktop\Amir_Learn\ImageProcessing\Color and Camera Imaging Basics\peppers.png")

if image is None:
    print("The image is not loaded correctly")
else:
    b,g,r = cv2.split(image)
    zero_channel = np.zeros(image.shape[:2],dtype ="uint8")

    red_channel = cv2.merge([zero_channel,zero_channel,r])
    blue_channel = cv2.merge([b,zero_channel,zero_channel])
    green_channel = cv2.merge([zero_channel,g,zero_channel])

    cv2.imshow("original Image",image)
    cv2.imshow("Red Channel(Gray)",r)
    cv2.imshow("Green Channel(Gray)",g)
    cv2.imshow("Blue Channel(Gray)",b)

    cv2.imshow("Red Channel(Colorized)",red_channel)
    cv2.imshow("Blue Channel(Colorized)",blue_channel)
    cv2.imshow("Green Channel(Colorized)",green_channel)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

