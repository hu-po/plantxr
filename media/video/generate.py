import numpy as np
import cv2

# Define properties
width = 960
height = 1080
fps = 30  # Use a reasonable fps value instead of 30000
duration = 10 # in seconds
fourcc = cv2.VideoWriter_fourcc(*'VP80')  # Using 'VP80' for WebM format with VP8 codec
output_file = "random_video.webm"

# Create a VideoWriter object
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

for _ in range(fps * duration):
    # Generate a random frame
    frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    out.write(frame)

# Release the VideoWriter object
out.release()

print(f"Random video saved as {output_file}")
