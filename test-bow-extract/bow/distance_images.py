import numpy as np
import cv2


pathimg1 = "train/forest/bost98.jpg"
pathimg2 = "test/forest/text46.jpg"

img1 = cv2.imread(pathimg1,0) # queryImage
img2 = cv2.imread(pathimg2,0) # trainImage

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
bf = cv2.BFMatcher()

matches = bf.knnMatch(des1,des2, k=2)
dbi = 0.0 #distance between 2 images Note : no simetrica 
dbis = 0.0 #distance between 2 images Note: simetrica
good = []
for m,n in matches:
    dbi += m.distance
    dbis += m.distance + n.distance
    if m.distance < 0.75*n.distance:
        good.append(m)

print("Distance Between Images (No simtric)")
print(dbi/len(matches))

#Es mas robusta la medida
print("Distance Between Images (simetric)")
print(dbis/(2*len(matches)))
