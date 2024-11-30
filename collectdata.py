import cv2
import os


directory= 'SignImage48x48/'
print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory)
if not os.path.exists(f'{directory}/blank'):
    os.mkdir(f'{directory}/blank')
    

for i in range(65,91):
    letter  = chr(i)
    if not os.path.exists(f'{directory}/{letter}'):
        os.mkdir(f'{directory}/{letter}')




import os
import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/water")),
             'b': len(os.listdir(directory+"/food")),
             'c': len(os.listdir(directory+"/pain")),
             'd': len(os.listdir(directory+"/help")),
             'e': len(os.listdir(directory+"/good")),
             'f': len(os.listdir(directory+"/restroom")),
             'g': len(os.listdir(directory+"/hello")),
             'blank': len(os.listdir(directory+"/blank"))
             }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,300),(255,255,255),2)
    cv2.imshow("data",frame)
    frame=frame[40:300,0:300]
    cv2.imshow("ROI",frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(48,48))
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory+'water/'+str(count['a']))+'.jpg',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(os.path.join(directory+'food/'+str(count['b']))+'.jpg',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(os.path.join(directory+'pain/'+str(count['c']))+'.jpg',frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(os.path.join(directory+'help/'+str(count['d']))+'.jpg',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(directory+'good/'+str(count['e']))+'.jpg',frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(os.path.join(directory+'restroom/'+str(count['f']))+'.jpg',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(os.path.join(directory+'hello/'+str(count['g']))+'.jpg',frame)
    if interrupt & 0xFF == ord('.'):
        cv2.imwrite(os.path.join(directory+'blank/' + str(count['blank']))+ '.jpg',frame)


    