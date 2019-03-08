#from numba import jit
import numpy as np
import cv2
import random
import time
import sys, getopt

imgW = 0
imgH = 0
done = []

def center(cir):
    centers = []
    for c in cir:
        M = cv2.moments(c)
        cx = int(M["m10"]/M["m00"])
        cy = int(M["m01"]/M["m00"])
        centers.append((cx,cy))
    return centers

def sec(val):
    return val[0][0][0][1]

def sec1(val):
    return val[0][0][0][0]

def first(val):
    return val[0][0][0]

def first1(val):
    return val[0][0][1]

#@jit(nopython=True)
def fr(cir, centers):
    visited = []
    groups = []
    for c, cen in zip(cir, centers):
        if cen not in visited:
            temp = []
            visited.append(cen)
            temp.append(c)
            for c1, cen1 in zip(cir, centers):
                if cen1 not in visited:
                    if (abs(cen[1]-cen1[1]) < (imgH*0.00591)):
                        visited.append(cen1)
                        temp.append(c1)
            groups.append(temp)
    return groups

def findRows(cir):
    centers = center(cir)
    groups = fr(cir, centers)
    groups.sort(key = sec)
    return groups

#@jit(nopython=True)
def fc(cir, centers):
    visited = []
    groups = []
    for c, cen in zip(cir, centers):
        if cen not in visited:
            temp = []
            visited.append(cen)
            temp.append(c)
            for c1, cen1 in zip(cir, centers):
                if cen1 not in visited:
                    if (abs(cen[0]-cen1[0]) < (imgW*0.00456)):
                        visited.append(cen1)
                        temp.append(c1)
            groups.append(temp)
    return groups

def findColumns(cir):
    centers = center(cir)
    groups = fc(cir, centers)
    groups.sort(key = sec1)
    return groups

def questions(x):
    ret = []
    for row in x:
        centers = center(row)
        n = []
        visited = []
        for r, c in zip(row, centers):
            if c not in visited and c not in done:
                temp = []
                tempvisit = []
                visited.append(c)
                tempvisit.append(c)
                temp.append(r)
                for rr,cc in zip(row, centers):
                    if cc not in tempvisit and cc not in done:
                        if abs(c[0] - cc[0]) < (imgW*0.0363):
                            temp.append(rr)
                            tempvisit.append(cc)
                if (len(temp) == 5):
                    for x in tempvisit:
                        done.append(x)
                    n.append(temp)
        if n:
            for r, c in zip(row, centers):
                if c not in done:
                    temp = []
                    tempvisit = []
                    tempvisit.append(c)
                    temp.append(r)
                    for rr,cc in zip(row, centers):
                        if cc not in tempvisit and cc not in done:
                            if abs(c[0] - cc[0]) < (imgW*0.0363):
                                temp.append(rr)
                                tempvisit.append(cc)
                    if (len(temp) == 3) or (len(temp) == 4):
                        for x in tempvisit:
                            done.append(x)
                        n.append(temp)
        n.sort(key = sec1)
        ret.append(n)
    return ret

def names(x):
    ret = []
    for col in x:
        n = []
        visited = []
        centers = center(col)
        for co, c in zip(col, centers):
            if c not in visited and c not in done:
                temp = []
                tempvisit = []
                visited.append(c)
                tempvisit.append(c)
                temp.append(co)
                for coo,cc in zip(col, centers):
                    if cc not in tempvisit and cc not in done:
                        if abs(c[1] - cc[1]) < (imgH*0.2667995):
                            temp.append(coo)
                            tempvisit.append(cc)
                if (len(temp) == 27):
                    for x in tempvisit:
                        done.append(x)
                    n.append(temp)
        ret.append(n)
    return ret

def gradeEDU(x):
    ret = []
    for col in x:
        n = []
        visited = []
        centers = center(col)
        for co, c in zip(col, centers):
            if c not in visited and c not in done:
                temp = []
                tempvisit = []
                visited.append(c)
                tempvisit.append(c)
                temp.append(co)
                for coo,cc in zip(col, centers):
                    if cc not in tempvisit and cc not in done:
                        if abs(c[1] - cc[1]) < (imgH*0.16797):
                            temp.append(coo)
                            tempvisit.append(cc)
                if (len(temp) == 17):
                    for x in tempvisit:
                        done.append(x)
                    n.append(temp)
        ret.append(n)
    return ret

def month(x):
    ret = []
    for col in x:
        n = []
        visited = []
        centers = center(col)
        for co, c in zip(col, centers):
            if c not in visited and c not in done:
                temp = []
                tempvisit = []
                visited.append(c)
                tempvisit.append(c)
                temp.append(co)
                for coo,cc in zip(col, centers):
                    if cc not in tempvisit and cc not in done:
                        if abs(c[1] - cc[1]) < (imgH*0.12305):
                            temp.append(coo)
                            tempvisit.append(cc)
                if (len(temp) == 12):
                    for x in tempvisit:
                        done.append(x)
                    n.append(temp)
        ret.append(n)
    return ret

def dateID(x):
    ret = []
    for col in x:
        n = []
        visited = []
        centers = center(col)
        for co, c in zip(col, centers):
            if c not in visited and c not in done:
                temp = []
                tempvisit = []
                visited.append(c)
                tempvisit.append(c)
                temp.append(co)
                for coo,cc in zip(col, centers):
                    if cc not in tempvisit and cc not in done:
                        if abs(c[1] - cc[1]) < (imgH*0.1015):
                            temp.append(coo)
                            tempvisit.append(cc)
                if (len(temp) == 10):
                    for x in tempvisit:
                        done.append(x)
                    n.append(temp)
        ret.append(n)
    return ret

def date1(x):
    ret = []
    for col in x:
        n = []
        visited = []
        centers = center(col)
        for co, c in zip(col, centers):
            if c not in visited and c not in done:
                temp = []
                tempvisit = []
                visited.append(c)
                tempvisit.append(c)
                temp.append(co)
                for coo,cc in zip(col, centers):
                    if cc not in tempvisit and cc not in done:
                        if abs(c[1] - cc[1]) < (imgH*0.041):
                            temp.append(coo)
                            tempvisit.append(cc)
                if (len(temp) == 4):
                    for x in tempvisit:
                        done.append(x)
                    n.append(temp)
        ret.append(n)
    return ret

def gender(x):
    ret = []
    for col in x:
        n = []
        visited = []
        centers = center(col)
        for co, c in zip(col, centers):
            if c not in visited and c not in done:
                temp = []
                tempvisit = []
                visited.append(c)
                tempvisit.append(c)
                temp.append(co)
                for coo,cc in zip(col, centers):
                    if cc not in tempvisit and cc not in done:
                        if abs(c[1] - cc[1]) < (imgH*0.021484):
                            temp.append(coo)
                            tempvisit.append(cc)
                if (len(temp) == 2):
                    for x in tempvisit:
                        done.append(x)
                    n.append(temp)
        ret.append(n)
    return ret

#@jit(nopython=True)
def fd(cir, centers):
    filt = []
    visited = []
    for x, y in zip(cir, centers):
        if y not in visited:
            visited.append(y)
            filt.append(x)
            for a,b in zip(cir, centers):
                if b not in visited: 
                    if abs(y[0] - b[0]) < (imgW*0.00910194) and abs(y[1] - b[1]) < (imgH*0.01172):
                        visited.append(b)
    return filt
    
def filterDublicates(cir):
    centers = center(cir)
    return fd(cir, centers)

def findCircles(contour):
    cir = []
    for cont in contour:
        approx = cv2.approxPolyDP(cont, 0.0303*cv2.arcLength(cont, True), True)
        area = cv2.contourArea(cont)
        if ((len(approx) > 6) and (area > (imgW*imgH*0.000065))):
            (x,y,w,h) = cv2.boundingRect(cont)
            ratio = float(w)/ float(h)
            if ((ratio >= .833) and (ratio <= 1.267)):
                cir.append(cont)
    return cir

def findSelectedQ(qG):
    bubbled = []
    for i,row in enumerate(qG):
        bubbled.append([])
        for j,group in enumerate(row):
            group.sort(key = first)
            bubbled[i].append((0,None))
            if (len(group) == 5) :
                for k,c in enumerate(group):
                    mask = np.zeros(img.shape, dtype="uint8")
                    cv2.drawContours(mask, [c], -1, 255, -1)

                    mask = cv2.bitwise_and(img, img, mask=mask)
                    total = cv2.countNonZero(mask)

                    if total > bubbled[i][j][0] and total > (imgW*imgH*0.000036):
                        bubbled[i][j] = (total, k)
            else:
                bubbled[i][j] = (0, -1)
    return bubbled

def findSelected(g):
    bubbled = []
    for i,col in enumerate(g):
        bubbled.append([])
        for j,group in enumerate(col):
            group.sort(key = first1)
            bubbled[i].append((0,None))
            for k,c in enumerate(group):
                mask = np.zeros(img.shape, dtype="uint8")
                cv2.drawContours(mask, [c], -1, 255, -1)

                mask = cv2.bitwise_and(img, img, mask=mask)
                total = cv2.countNonZero(mask)

                if total > bubbled[i][j][0] and total > (imgW*imgH*0.000065):
                    bubbled[i][j] = (total, k)
    return bubbled

start = time.time()

questionN = 100
fileName = "scan.jpg" #SKM_C55819022211330.pdf-1

try:
    opts, args = getopt.getopt(sys.argv[1:], "hf:n:", ["file=","number="])
except getopt.GetoptError:
    print("-f filename, -n number of questions")
    sys.exit(2)
for opt, arg in opts:
    if opt == "-h":
        print("-f filename, -n number of questions")
        system.exit()
    elif opt in ("-f", "--file"):
        fileName = arg
    elif opt in ("-n", "--number"):
        questionN = arg

img = cv2.imread(fileName)
imgW = img.shape[1]
imgH = img.shape[0]
kernel = np.ones((5,5), np.uint8)
#img = cv2.resize(img, (imgW, imgH), interpolation = cv2.INTER_AREA)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.namedWindow("e", cv2.WINDOW_NORMAL)
#cv2.imshow("e", img)
#img = cv2.filter2D(img, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))
#img = cv2.GaussianBlur(img, (3,3), 0)
img = cv2.bilateralFilter(img, 7, 40, 40)
#img = cv2.bilateralFilter(img, 1, 40, 40)
dark = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)[1]
#img = cv2.threshold(img, 1, 255, cv2.THRESH_TOZERO)[1]
#cv2.namedWindow("e", cv2.WINDOW_NORMAL)
#cv2.imshow("e", img)
dark = cv2.Canny(dark, 1, 36)
#dark = cv2.morphologyEx(dark, cv2.MORPH_CLOSE, kernel)
edges = cv2.Canny(img, 1, 60)
#kernel = np.ones((5,5), np.uint8)
#edges = cv2.dilate(edges,kernel, iterations=1)
#edges = cv2.erode(edges,kernel, iterations=1)
edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

con = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
contours = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
co = cv2.findContours(dark, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]

contours = np.append(contours, co, axis=0)
contours = np.append(contours, con, axis=0)

img1 = cv2.imread(fileName)
#img1 = cv2.resize(img1, (imgW, imgH), interpolation = cv2.INTER_AREA)
#cv2.drawContours(img1, contours, -1, (0, 250, 250), 2)

circles = findCircles(contours)

circles = filterDublicates(circles)

#cv2.drawContours(img1, circles, -1, (0, 0, 255), 3)

rows = findRows(circles)
columns = findColumns(circles)

nameGroup = names(columns)

##for i in nameGroup:
##   for j in i:
##       cv2.drawContours(img1, j, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)
    
eduGroup = gradeEDU(columns)

##for i in eduGroup:
##   for j in i:
##       cv2.drawContours(img1, j, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)

monthGroup = month(columns)

##for i in monthGroup:
##   for j in i:
##       cv2.drawContours(img1, j, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)

dateIDGroup = dateID(columns)

##for i in dateIDGroup:
##   for j in i:
##       cv2.drawContours(img1, j, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)

queGroup = questions(rows)

##for i in queGroup:
##   for j in i:
##       cv2.drawContours(img1, j, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)

dateGroup = date1(columns)

##for i in dateGroup:
##   for j in i:
##       cv2.drawContours(img1, j, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)

genderGroup = gender(columns)

##for i in genderGroup:
##   for j in i:
##       cv2.drawContours(img1, j, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)

bubbledQue = findSelectedQ(queGroup)

i = -1
for z in bubbledQue:
    if z:
        i += 1
        for j,w in enumerate(z):
            print(str(i) + "-" + str(j) + " " + str(w[1]))

bubbledName = findSelected(nameGroup)

for z in bubbledName:
    for w in z:
        print("name " + str(w[1]))

bubbledEDU = findSelected(eduGroup)

for z in bubbledEDU:
    for w in z:
        print("EDUgrade " + str(w[1]))

bubbledMonth = findSelected(monthGroup)

for z in bubbledMonth:
    for w in z:
        print("month " + str(w[1]))

bubbledDate = findSelected(dateGroup)

for z in bubbledDate:
    for w in z:
        print("date " + str(w[1]))

bubbledDateID = findSelected(dateIDGroup)

for z in bubbledDateID:
    for w in z:
        print("dateID " + str(w[1]))

bubbledGender = findSelected(genderGroup)

for z in bubbledGender:
    for w in z:
        print("gender " + str(w[1]))

##cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
##cv2.imshow("edges", img1)
##cv2.namedWindow("edges1", cv2.WINDOW_NORMAL)
##cv2.imshow("edges1", dark)
##cv2.namedWindow("edges2", cv2.WINDOW_NORMAL)
##cv2.imshow("edges2", edges)

print(time.time() - start)
cv2.waitKey(0)
cv2.destroyAllWindows()
