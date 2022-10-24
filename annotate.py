import cv2

lst=[]
box_width=0
box_height=0
centerx=0
centery=0
click=0

#Function to draw bounding rectangle using mouse clicks
'''
def click_event(event, x, y, flags, params):
    global lst,box_width,box_height,centerx,centery,click
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print('(',x, ',',y,')')
        lst.append([x,y])
        click+=1
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, '(' +str(x) + ',' +str(y)+ ')' , (x,y), font,1, (255, 0, 0), 2)
        if(click%2==0):
            cv2.rectangle(img, (lst[0][0],lst[0][1]), (lst[1][0],lst[1][1]), (255,240,0), thickness=3)
            box_width=lst[1][0]-lst[0][0]
            box_height=lst[1][1]-lst[0][1]
            centerx=lst[0][0]+box_width/2
            centery=lst[0][1]+box_height/2
        cv2.imshow('image', img)
        with open('dog.txt','w')as f:
            f.write('0'+' '+str(centerx)+' '+str(centery)+' '+str(box_width)+' '+str(box_height))
        
'''

#Function to draw bounding rectangle by dragging the mouse
def click_event(event, x, y, flags, params):
    global lst,box_width,box_height,centerx,centery,click
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        #if the left mouse button was clicked record the starting coordinates
        # displaying the coordinates
        # on the Shell
        print('(',x, ',',y,')')
        lst.append([x,y])
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, '(' +str(x) + ',' +str(y)+ ')' , (x,y), font,1, (255, 0, 0), 2)
    elif event==cv2.EVENT_LBUTTONUP:
        #check if the left mouse button was released
        #record the ending coordinates
        lst.append([x,y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, '(' +str(x) + ',' +str(y)+ ')' , (x,y), font,1, (255, 0, 0), 2)
        if(click%2==0):
            cv2.rectangle(img, (lst[0][0],lst[0][1]), (lst[1][0],lst[1][1]), (255,240,0), thickness=3)
            box_width=lst[1][0]-lst[0][0]
            box_height=lst[1][1]-lst[0][1]
            centerx=lst[0][0]+box_width/2
            centery=lst[0][1]+box_height/2
        cv2.imshow('image', img)
        with open('dog.txt','w')as f:
            f.write('0'+' '+str(centerx)+' '+str(centery)+' '+str(box_width)+' '+str(box_height))
      
# driver function
if __name__=="__main__":
    # reading the image
    img = cv2.imread('dog.jpg', 1) 
    # displaying the image
    cv2.imshow('image', img) 
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event) 
    # wait for a key to be pressed to exit
    cv2.waitKey(0) 
    # close the window
    cv2.destroyAllWindows()
    print(lst)
    print("box_width:",box_width)
    print("box_height:",box_height)
    print("center_x:",centerx)
    print("center_y:",centery)
