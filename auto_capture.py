import pyrealsense2 as rs
import numpy as np
import cv2
from datetime import datetime
import time

# Configure streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)
print("Capturing photo every 1 second. Press 'q' to quit")

last_capture_time = time.time()

try:
    while True:
        # Get frames
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        
        if not color_frame:
            continue
        
        # Convert to numpy array
        color_image = np.asanyarray(color_frame.get_data())
        
        # Auto-capture every 1 second
        current_time = time.time()
        if current_time - last_capture_time >= 2.0:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"capture_{timestamp}.png"
            cv2.imwrite(filename, color_image)
            print(f"Saved: {filename}")
            last_capture_time = current_time
        
        # Display
        cv2.imshow('RealSense D435i', color_image)
        
        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()
