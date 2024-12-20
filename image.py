import cv2
import numpy as np

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Allow the camera to warm up
print("Please stand away from the camera while the background is being captured...")
cv2.waitKey(2000)

# Capture the background frame
print("Capturing background...")
for i in range(60):
    ret, background = cap.read()
if not ret:
    print("Failed to capture background. Exiting...")
    cap.release()
    exit()
background = np.flip(background, axis=1)  # Flip the background frame horizontally

# Load the replacement image
replacement_image = cv2.imread("replacement.jpg")
if replacement_image is None:
    print("Failed to load replacement image. Exiting...")
    cap.release()
    exit()

# Resize the replacement image to match the frame dimensions
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
replacement_image = cv2.resize(replacement_image, (frame_width, frame_height))

print("Background captured. You can now use the cloak!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for consistency
    frame = np.flip(frame, axis=1)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the color to be replaced (e.g., red)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create masks to detect the red color
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Refine the mask to reduce noise and smooth edges
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    mask = cv2.GaussianBlur(mask, (15, 15), 0)

    # Invert the mask to segment out the red color
    mask_inverted = cv2.bitwise_not(mask)

    # Segment the replacement image where the red color is detected
    res1 = cv2.bitwise_and(replacement_image, replacement_image, mask=mask)

    # Segment the rest of the frame
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inverted)

    # Combine the two results to get the final frame
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Display the final output
    cv2.imshow("Invisibility Cloak", final_output)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()
