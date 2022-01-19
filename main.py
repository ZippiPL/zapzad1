import cv2
import numpy as np
# import tensorflow as tf
# import matplotlib.pyplot as plt
import collections
import glob


def count_person(classarray, photonumber: int) -> str:
    personimage = np.array(classarray)
    countpersonimage = collections.Counter(personimage)[1]
    print("Na zdjęciu", photonumber+1, " widoczne jest :", countpersonimage, "osob ")
    text = f'Zdjecie numer  {photonumber+1} Ludzie na zdjeciu - {countpersonimage}'
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

path = glob.glob("Images/*.jpg")
file_name = 'Models/Labels.txt'
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rsplit('\n')

model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

images = []
orginalimage = []
confThreshold = 0.52

font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN
i = 0
for file in path:
    images.append(cv2.imread(file))
    orginalimage.append(cv2.imread(file))
    ClassIndex, confidece, bbox = model.detect(images[i], confThreshold)
    print("\n")
    print("Indexy widocznych obiektow na zdjeciach:")
    print(ClassIndex)
    imgboxesdraw(ClassIndex, confidece, bbox, images[i])
    imgHor = np.hstack((images[i], orginalimage[i]))
    cv2.imshow(count_person(ClassIndex, i), imgHor)
    i += 1
    cv2.waitKey()
