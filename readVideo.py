import cv2 as cv

capture = cv.VideoCapture(r'C:\Users\amirt.AMIRTHAVARSHINI\Videos\WhatsApp Video 2025-08-20 at 20.18.21.mp4')

if not capture.isOpened():
    print("Video Does Not Loaded Correctly...")

while True:
    ref,frame = capture.read()
    if not ref:
        break

    cv.imshow('Jack',frame)

    if cv.waitKey(15) & 0xff == ord('a'):
        break

capture.release()
cv.destroyAllWindows()



