import cv2

capture = cv2.VideoCapture(0)

while(True):
    # 获取一帧
    ret, frame = capture.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
