import cv2
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
#img = cv2.imread('city.jpeg')
#czytanie ze zdjecia
#img=cv2.imread('zippi.jpg')
#print(type(img))
#print(img.shape)

#wyswietlanie
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#black
#img_convert = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('image',img_convert)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#plt.imshow(img)
#plt.show()

#txt = pytesseract.image_to_string(img)

#img1 = Image.open('zdj1.png')
#img2 = Image.open('zdj2.png')
#img3 = Image.open('zdj3.png')
#img4 = Image.open('zd4.jpg')
#img5 = Image.open('zad5.png')

#img1t = pytesseract.image_to_string(img1)
#img2t = pytesseract.image_to_string(img2)
#img3t = pytesseract.image_to_string(img3)
#img4t = pytesseract.image_to_string(img4)
#img5t = pytesseract.image_to_string(img5)

#print("zdj1")
#print(img1t)
#print("zdj2")
#print(img2t)
#print("zdj3")
#print(img3t)
#print("zdj4")
#print(img4t)
#print("zdj5")
#print(img5t)

#

captchaImg = Image.open('captcha.JPG')
captchaImgT = pytesseract.image_to_string(captchaImg)
print("captcha.jpg :")
print(captchaImgT)


#print(txt)
img = cv2.imread('sample.png')
captchasampleImg = Image.open('sample.png')
captchasampleImgT = pytesseract.image_to_string(captchasampleImg)
print("captcha.jpg :")
print(captchasampleImgT)
image8 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
converted_img1 = cv2.threshold(cv2.GaussianBlur(image8, (5, 5), 0), 0, 255, cv2.THRESH_BINARY
+ cv2.THRESH_OTSU)[1]

converted_img2 = cv2.threshold(cv2.bilateralFilter(image8, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
converted_img3 = cv2.threshold(cv2.medianBlur(image8, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
converted_img4 = cv2.adaptiveThreshold(cv2.GaussianBlur(image8, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
converted_img5 = cv2.adaptiveThreshold(cv2.bilateralFilter(image8, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
converted_img6 = cv2.adaptiveThreshold(cv2.medianBlur(image8, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

cv2.imshow('image',converted_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image',converted_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image',converted_img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image',converted_img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image',converted_img5)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image',converted_img6)
cv2.waitKey(0)
cv2.destroyAllWindows()
