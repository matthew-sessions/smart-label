import cv2

cap = cv2.VideoCapture('/Users/msessions/Desktop/workspace/tflow/tacomavid.mp4')
count = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # cv2.imwrite('frame{:d}.jpg'.format(count), frame)
        count += 1 # i.e. at 30 fps, this advances one second
        if count == 500:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 19)

        cv2.imshow('Frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        
        break
cap.release()
cv2.destroyAllWindows()

