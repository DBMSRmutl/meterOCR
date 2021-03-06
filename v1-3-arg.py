import cv2
import numpy as np
import os
import sys
import time
#from uploadToGDrive import main_upload
#import uploadToGDrive

def readimage(filename):
    print filename
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) # reading image
    if image is None:
        print 'Can not find the image!'
        sys.stdin.read(1)
        exit(-1)
    return image
    
#-------------------------------------------------------------------------------------
def createFolder(directory):
	directory = directory + time.strftime("-%Y-%m-%d-%H-%M-%S")
	if not os.path.exists(directory):
		os.makedirs(directory)
		print 'OK! can create directory '+directory
	else:
		print 'Error cannot create directory '+directory
	return directory
#------------------------------------------------------------------------------------
print "sys \n"
print "\n".join(sys.argv)
filename=sys.argv[1]
foldername=sys.argv[2]
#print 'foldername '+foldername
resultDirectory = createFolder(foldername)
print 'resultDirectory = '+resultDirectory
# remove parent directory name
folderNameLength = foldername.index('/')+1
print 'folderNameLength = '+str(folderNameLength)
onlyFolderName = resultDirectory[folderNameLength:]
print 'onlyFolderName = '+onlyFolderName

image=readimage (filename)
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
imageview, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
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
            #cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),1)
            #cv2.imshow("Show",im)
            crop_img = im[y-15:y+h+15, x-15:x+w+15]
            if x>=0 and x<= (width*0.2):
                crop=1
                crop_img=np.invert(crop_img)
                cv2.imwrite(resultDirectory+'/'+'crop'+str(crop)+'.tif',crop_img)
		tCommand = 'tesseract '+resultDirectory+'/crop1.tif' + ' '+resultDirectory+'/crop1 -psm 10 digits'
		print 'tCommand = '+tCommand
                os.system(tCommand)
		# cat crop1.txt to numberVariable
		with open(resultDirectory+'/'+'crop'+str(crop)+'.txt', 'r') as myfile:
			data=myfile.read().replace('\n', '')
		print 'data crop'+str(crop)+'.txt ='+data
		# insert resultDirectory crop1 to google spreadsheet
                
            elif x>=(width*0.2)+1 and x<= (width*0.4):
                crop=2
                crop_img=np.invert(crop_img)
                cv2.imwrite(resultDirectory+'/'+'crop'+str(crop)+'.tif',crop_img)
		tCommand = 'tesseract '+resultDirectory+'/crop2.tif' + ' '+resultDirectory+'/crop2 -psm 10 digits'
                print 'tCommand = '+tCommand
                os.system(tCommand)
		 # cat crop2.txt to numberVariable
                with open(resultDirectory+'/'+'crop'+str(crop)+'.txt', 'r') as myfile:
                        data=myfile.read().replace('\n', '')
                print 'data crop'+str(crop)+'.txt ='+data

            elif x>=(width*0.4)+1 and x<= (width*0.6):
                crop=3
                crop_img=np.invert(crop_img)
                cv2.imwrite(resultDirectory+'/'+'crop'+str(crop)+'.tif',crop_img)
		tCommand = 'tesseract '+resultDirectory+'/crop3.tif' + ' '+resultDirectory+'/crop3 -psm 10 digits'
                print 'tCommand = '+tCommand
                os.system(tCommand)
                
            elif x>=(width*0.6)+1 and x<= (width*0.8):
                crop=4
                crop_img=np.invert(crop_img)
                cv2.imwrite(resultDirectory+'/'+'crop'+str(crop)+'.tif',crop_img)
		tCommand = 'tesseract '+resultDirectory+'/crop4.tif' + ' '+resultDirectory+'/crop4 -psm 10 digits'
                print 'tCommand = '+tCommand
                os.system(tCommand)
                
            elif x>=(width*0.8)+1 and x<= width:
                crop=5
                cv2.imwrite(resultDirectory+'/'+'crop'+str(crop)+'.tif',crop_img)
		tCommand = 'tesseract '+resultDirectory+'/crop5.tif' + ' '+resultDirectory+'/crop5 -psm 10 digits'
                print 'tCommand = '+tCommand
                os.system(tCommand)
            
            #crop_img=np.invert(crop_img)
            #cv2.imshow('crop '+str(crop),crop_img)
            #cv2.imwrite('crop'+str(crop)+'.tif',crop_img)
            #number=number+1 
#--------------------------------------------------------------------------------------
exit('ohoh')

k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
