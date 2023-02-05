import cv2
import numpy as np
import csv

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Define the default screen resolution
screen_resolution = (640, 480)

# Ask the user if they want to change the screen resolution
change_resolution = input("Do you want to change the screen resolution (y/n)? ")

# If the user wants to change the screen resolution
if change_resolution.lower() == 'y':
    # Get the new screen resolution from the user
    screen_resolution = tuple(map(int, input("Enter the new screen resolution (width height): ").split()))

# Set the screen resolution for the video capture
cap.set(3, screen_resolution[0])
cap.set(4, screen_resolution[1])

# Define the parameters for the Canny filter
low_threshold = 50
high_threshold = 150

# Create a CSV file to store the edge coordinates
with open('edge_coordinates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row for the CSV file
    writer.writerow(['x', 'y'])
    
    while True:
        # Capture a frame from the video
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply the Canny filter to the grayscale image
        edges = cv2.Canny(gray, low_threshold, high_threshold)
        
        # Get the coordinates of all the non-zero pixels in the edges image
        coords = np.column_stack(np.where(edges != 0))
        
        # Write the edge coordinates to the CSV file
        writer.writerows(coords)
        
        # Display the edges image
        cv2.imshow("Edges", edges)
        
        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

