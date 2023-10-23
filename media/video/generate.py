import cv2
import numpy as np
import os

# Initialize video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Get the dimensions of the frame
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Ensure the captured width and height matches the requirement
if width != 640 or height != 240:
    print("Error: The captured video dimensions are not as expected.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output_temp.avi', fourcc, 30.0, (960, 1080))

try:
    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            # Split the frame into left and right
            left_frame = frame[:, :width//2]
            right_frame = frame[:, width//2:]
            
            # Resize each half to 960x540
            left_resized = cv2.resize(left_frame, (960, 540))
            right_resized = cv2.resize(right_frame, (960, 540))
            
            # Combine them into a new frame
            combined_frame = np.vstack((left_resized, right_resized))
            out.write(combined_frame)
        else:
            break

    # Release the video objects
    cap.release()
    out.release()


except KeyboardInterrupt:
    # Handle keyboard interruption gracefully
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Convert the AVI file to WebM using FFmpeg
    os.system('ffmpeg -i output_temp.avi output.webm')

    # Optionally, remove the temporary AVI file
    os.remove('output_temp.avi')
