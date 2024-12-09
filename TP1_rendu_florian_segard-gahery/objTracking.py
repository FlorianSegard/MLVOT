from Detector import detect
from KalmanFilter import KalmanFilter
import cv2
import numpy as np

GREEN = (0, 255, 0)  # Detected circle
BLUE = (255, 0, 0)   # Predicted position
RED = (0, 0, 255)    # Estimated position
BLACK = (0, 0, 0)    # Line

if __name__ == "__main__":
    filter = KalmanFilter(dt=0.1, u_x=1, u_y=1, std_acc=1, x_sdt_meas=0.1, y_sdt_meas=0.1)
    capture=cv2.VideoCapture("randomball.avi") 
    success = True
    frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(capture.get(cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter("tracked_output.avi", 
                        cv2.VideoWriter_fourcc(*'XVID'), 
                        fps, 
                        (frame_width, frame_height))
    trajectory = []
    while success:
        success, image = capture.read() 
        if not success:
            break

        centers = detect(image)
        for z_k in centers:
            predicted, _  = filter.predict()
            filter.update(z_k)
                        
            predicted_position = (int(predicted[0, 0]), int(predicted[1, 0]))
            estimated_position = (int(filter.x_k[0, 0]), int(filter.x_k[1, 0]))
            
            trajectory.append(predicted_position)
            
            if len(trajectory) > 100: # only 100 points to keep it clear
                trajectory.pop(0)

            # Draw detected position
            cv2.circle(image, tuple(z_k.flatten().astype(int)), 10, GREEN, -1)

            # Draw predicted position rectangle
            cv2.rectangle(image, 
                            (predicted_position[0] - 15, predicted_position[1] - 15),
                            (predicted_position[0] + 15, predicted_position[1] + 15),
                            BLUE, 2)

            # Draw estimated position rectangle
            cv2.rectangle(image, 
                            (estimated_position[0] - 15, estimated_position[1] - 15),
                            (estimated_position[0] + 15, estimated_position[1] + 15),
                            RED, 2)
            
        for point in trajectory:
            cv2.circle(image, point, 1, BLACK, -1)

        out.write(image)

    capture.release()
    out.release()
    cv2.destroyAllWindows()

        
