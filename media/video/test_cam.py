import cv2

# Change the index to test different cameras
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Camera Test", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Could not capture an image.")
        break

cap.release()
cv2.destroyAllWindows()
