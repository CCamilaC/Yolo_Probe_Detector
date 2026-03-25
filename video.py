import pyrealsense2 as rs
import numpy as np
import cv2
from datetime import datetime

# Configure streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

print("Pressione 'a' para começar a gravar, 's' para parar, 'q' para sair")

recording = False
video_count = 0
video_writer = None

try:
    while True:
        # Get frames
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        
        if not color_frame:
            continue
        
        # Convert to numpy array
        color_image = np.asanyarray(color_frame.get_data())
        
        # If recording, write the frame
        if recording and video_writer is not None:
            video_writer.write(color_image)
        
        # Display
        cv2.imshow('RealSense D435i', color_image)
        
        # Key controls
        key = cv2.waitKey(1)

        # Start recording
        if key == ord('a') and not recording:
            video_count += 1
            filename = f"video_{video_count}.mp4"
            fourcc = cv2.VideoWriter_fourcc(*'avc1')
            video_writer = cv2.VideoWriter(filename, fourcc, 30, (1280, 720))
            recording = True
            print(f"Gravação iniciada: {filename}")

        # Stop recording
        elif key == ord('s') and recording:
            recording = False
            video_writer.release()
            video_writer = None
            print("Gravação parada.")

        # Quit program
        elif key == ord('q'):
            break

finally:
    if recording and video_writer is not None:
        video_writer.release()
    pipeline.stop()
    cv2.destroyAllWindows()