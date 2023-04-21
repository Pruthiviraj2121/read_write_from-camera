import cv2 

# This index either can be filled up with the file of video or else the camera 
# And 0 indicates the default camera of the system
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# This here is for the captured 
# The file, the bytes, frame rate, and the size
cap_save = cv2.VideoWriter('ouput.avi', fourcc, 20.0, (640,480))
# This while loop is used for the continuos capture of photo
while True:
    # And the ret stres the true and false value while the frame captures the photo frame that is been captured
    ret,frame = cap.read()
    if ret == True:
        # This gives the height and width of the frame 
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # Change the frame to coloured to grey
        # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # This will show the frame inside the window
        cap_save.write(frame)
        cv2.imshow("Phutooo",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# After the break statement we need to release the video i.e cap
cap.release()
cap_save.release()
cv2.destroyAllWindows()