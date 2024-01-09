"""Module for checking FPS of screen capturing."""

import cv2
import time
import numpy as np
import mss


def capture_screen(x, y, width, height):
    """Captures screen region using mss."""
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        return np.asarray(sct.grab(monitor))


def add_fps_to_frame(frame, fps):
    """Adds FPS to frame image."""
    cv2.putText(frame, f"FPS: {fps:.0f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)


def display_frame(frame):
    """Displays the captured frame."""
    cv2.imshow("Captured Screen", frame)


def check_fps(x, y, width, height):
    """Calculates fps for captured screenshot."""
    # Variables for FPS calculation
    start_time = time.time()
    frames_count = 0

    while True:
        # Capture screen
        frame = capture_screen(x, y, width, height)

        # Calculate FPS
        frames_count += 1
        elapsed_time = time.time() - start_time
        fps = frames_count / elapsed_time

        # Display frame with FPS
        add_fps_to_frame(frame, fps)
        display_frame(frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    # Set the region to capture (adjust these values according to your needs)
    screen_x = 100
    screen_y = 100
    screen_width = 800
    screen_height = 600

    # press q to finish
    check_fps(screen_x, screen_y, screen_width, screen_height)
    # Release resources
    cv2.destroyAllWindows()
