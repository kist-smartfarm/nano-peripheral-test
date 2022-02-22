# redtiger@kist.re.kr 
# reference : https://github.com/groupgets/purethermal1-uvc-capture
#
try:
    import cv2
except ImportError:
    print ("[ERROR] python-opencv must be installed")
    exit(1)

def test_uvcs(): 
    for i in reversed(range(4)): 
        print ("Testing for presense of camera #{0}...".format(i))
        cv2_cap = cv2.VideoCapture(i)
        if cv2_cap.isOpened(): 
            print(f'[LOG] Camera {i} has connection------------')
            break 
    
    if not cv2_cap.isOpened(): 
        print('No Camera found by cv2.. aborting') 
        exit(1) 
    
    cv2.namedWindow("UVC device testing", cv2.WINDOW_NORMAL)
    print ("Running, ESC or CTRL+C to exit...")
    while True:
        ret, img = cv2_cap.read()
        if ret == False:
            print ("Error reading image") 
            break

        cv2.imshow("image", cv2.resize(img, (640, 480)))
        
        if cv2.waitKey(5) == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    test_uvcs() 
