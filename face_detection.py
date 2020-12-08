import cv2 as cv
import numpy as np

print('Face_detection_begin')
net = cv.dnn.readNet('face-detection-adas-0001.xml','face-detection-adas-0001.bin')
net.setPreferableTarget(cv.dnn.DNN_TARGET_MYRIAD)

# Catch pircture from camera
cap = cv.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    frame = cv.resize(frame,(480,320),interpolation = cv.INTER_CUBIC)
    blob = cv.dnn.blobFromImage(frame,size=(672,384), ddepth = cv.CV_8U)
    net.setInput(blob)
    out = net.forward()

#Circle the target

    for detection in out.reshape(-1, 7):
        confidence = float(detection[2])
        xmin = int(detection[3] * frame.shape[1])
        ymin = int(detection[4] * frame.shape[0])
        xmax = int(detection[5] * frame.shape[1])
        ymax = int(detection[6] * frame.shape[0])
        if confidence > 0.5:
            cv.rectangle(frame, (xmin, ymin), (xmax, ymax), color=(0, 255, 0))
    cv.imshow("capture",frame)
    if cv.waitKey(1)&0xff == ord('q'):
        cv.imwrite('out.png',frame)
        print("save one image done!")
        break

cap.release()

print("Finished")
