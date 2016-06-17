import cv2 kkk
import numpy as np
import os
def readimage():
    image = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE) # reading image
    if image is None:
        print 'Can not find the image!'
        exit(-1)
    return image

#-------------------------------------------------------------------------------------
image=readimage ()   
ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
N = 3
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (N, N))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#----------------------------------------------------------------------------------
#cv2.imshow('thresh', thresh)
cv2.imwrite('thresh.jpg',thresh)
im = cv2.imread('thresh.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,100,255,0)
thresh,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#-------------------------------5--------------------------------------------------
cnt = contours[0]
area = cv2.contourArea(cnt)
M = len(contours)
#print M
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]
max_index=np.zeros(M)
for i in range (M):
    areas = [cv2.contourArea(c) for c in contours]
    if i == 0:
        max_index[i] = np.argmax(areas)
    else :
        if max_index[i-1] == max_index[i]:
            max_index[i] = np.argmax(areas)
#print max_index
#------------------------------------------------------------------------------------
height,width,channels = im.shape
print height,width
#-------------------------------------------------------------------------------------
#number=0

crop=0
pic=np.zeros(5,int)
for i in range(M):
    x,y,w,h = cv2.boundingRect(contours[i])
    if h >= 100 :
        if w >= (w*0.3):
            #print x,y
            piccopy=np.zeros((w,h),int)
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),1)
            #cv2.imshow("Show",im)
            crop_img = im[y-15:y+h+15, x-15:x+w+15]
            if x>=0 and x<= (width*0.2):
                crop=1
                crop_img=np.invert(crop_img)
                cv2.imwrite('crop'+str(crop)+'.tif',crop_img)
                os.system("tesseract crop1.tif crop1 -psm 10 digits")
                
            elif x>=(width*0.2)+1 and x<= (width*0.4):
                crop=2
                crop_img=np.invert(crop_img)
                cv2.imwrite('crop'+str(crop)+'.tif',crop_img)
                os.system("tesseract crop2.tif crop2 -psm 10 digits")

            elif x>=(width*0.4)+1 and x<= (width*0.6):
                crop=3
                crop_img=np.invert(crop_img)
                cv2.imwrite('crop'+str(crop)+'.tif',crop_img)
                os.system("tesseract crop3.tif crop3 -psm 10 digits")
                
            elif x>=(width*0.6)+1 and x<= (width*0.8):
                crop=4
                crop_img=np.invert(crop_img)
                cv2.imwrite('crop'+str(crop)+'.tif',crop_img)
                os.system("tesseract crop4.tif crop4 -psm 10 digits")
                
            elif x>=(width*0.8)+1 and x<= width:
                crop=5
                cv2.imwrite('crop'+str(crop)+'.tif',crop_img)
                os.system("tesseract crop5.tif crop5 -psm 10 digits")
            
            #crop_img=np.invert(crop_img)
            #cv2.imshow('crop '+str(crop),crop_img)
            #cv2.imwrite('crop'+str(crop)+'.tif',crop_img)
            #number=number+1 
#--------------------------------------------------------------------------------------
#os.remove()
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
