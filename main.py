import cv2
import numpy as np
# import tensorflow as tf
# import matplotlib.pyplot as plt
import collections


def count_person(classarray, photonumber: int) -> str:
    personimage = np.array(classarray)
    countpersonimage = collections.Counter(personimage)[1]
    print("Na zdjęciu", photonumber, " widoczne jest :", countpersonimage, "osob ")
    text = f'Ludzie na zdjeciu - {countpersonimage}'
    return text


def imgboxesdraw(classindexdraw, confidecedraw, bboxdraw, imgtodraw):
    for ci, conf, boxes in zip(classindexdraw.flatten(), confidecedraw.flatten(), bboxdraw):
        if ci == 1:
            cv2.rectangle(imgtodraw, boxes, (80, 220, 100), 2)
            cv2.putText(imgtodraw, classLabels[ci - 1], (boxes[0] + 10, boxes[1] + 40),
                        font, fontScale=font_scale,
                        color=(0, 0, 255), thickness=3)


config_file = 'Models/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'
model = cv2.dnn_DetectionModel(frozen_model, config_file)


file_name = 'Models/Labels.txt'
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rsplit('\n')

model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

img = cv2.imread('Images/persondetectionimage1.jpg')
img2 = cv2.imread('Images/persondetectionimage2.jpg')
img3 = cv2.imread('Images/persondetectionimage3.jpg')

orginalimg = cv2.imread('Images/persondetectionimage1.jpg')
orginalimg2 = cv2.imread('Images/persondetectionimage2.jpg')
orginalimg3 = cv2.imread('Images/persondetectionimage3.jpg')

ClassIndex, confidece, bbox = model.detect(img, confThreshold=0.52)
ClassIndex2, confidece2, bbox2 = model.detect(img2, confThreshold=0.5)
ClassIndex3, confidece3, bbox3 = model.detect(img3, confThreshold=0.54)

print("Indexy widocznych obiektow na zdjeciach:")
print("Zdjecie 1")
print(ClassIndex)
print("Zdjecie 2")
print(ClassIndex2)
print("Zdjecie 3")
print(ClassIndex3)
print("\n")


font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN

imgboxesdraw(ClassIndex, confidece, bbox, img)
imgboxesdraw(ClassIndex2, confidece2, bbox2, img2)
imgboxesdraw(ClassIndex3, confidece3, bbox3, img3)

imgHor = np.hstack((img,orginalimg))
imgHor2 = np.hstack((img2,orginalimg2))
imgHor3 = np.hstack((img3,orginalimg3))

cv2.imshow(count_person(ClassIndex, 1), imgHor)
cv2.imshow(count_person(ClassIndex2, 2), imgHor2)
cv2.imshow(count_person(ClassIndex3, 3), imgHor3)
# plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)) // plot display
cv2.waitKey()
