import serial
import time
import cv2
import numpy as np
import tensorflow as tf

# Set up the serial communication (make sure to use the correct port)
ser = serial.Serial('/dev/tty.usbmodem1101', 9600, timeout=1)  # Added timeout for non-blocking
time.sleep(2)  # Wait for Arduino to initialize

# Send an initial message to Arduino (optional)
ser.write(b'Recycle\n')

# Load the trained model
model = tf.keras.models.load_model('waste_classifier_v1.h5')

def preprocess_frame(frame):
    """Preprocess the frame for the model."""
    img = cv2.resize(frame, (150, 150))  # Resize the frame to 150x150 pixels
    img = img / 255.0  # Normalize the image to [0, 1]
    img = np.expand_dims(img, axis=0)  # Expand dims to match model input
    return img

def main():
    """Main function to capture video and classify waste."""
    cap = cv2.VideoCapture(0)  # Open the webcam (0 is usually the default camera)
    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    start_time = time.time()  # Track the start time for the 5-second segment
    predictions = []  # Store predictions to average them over 5 seconds

    while True:
        ret, frame = cap.read()  # Capture frame from webcam
        if not ret:
            break  # Break the loop if frame capture fails

        processed_frame = preprocess_frame(frame)  # Preprocess frame for model
        prediction = model.predict(processed_frame)  # Predict the class for the frame
        predictions.append(prediction)

        elapsed_time = time.time() - start_time  # Calculate elapsed time since last segment
        cv2.imshow('Waste Detection', frame)  # Display the webcam feed

        if elapsed_time > 5:  # If 5 seconds have passed
            # Average the predictions over the 5-second period
            final_prediction = np.mean(predictions, axis=0)
            classes = ['Recycle', 'Trash']  # Define your classes
            label = classes[np.argmax(final_prediction)]  # Get the predicted class

            try:
                # Send the result to Arduino
                ser.write(label.encode())  # Send the label as bytes
                print(f"Sent to Arduino: {label}")
            except Exception as e:
                print(f"Error in serial communication: {e}")

            # Reset for the next 5-second segment
            predictions = []
            start_time = time.time()

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup and release resources
    cap.release()
    cv2.destroyAllWindows()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()

# Don't forget to close the serial connection when done!
ser.close()

