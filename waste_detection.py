import os
import cv2
import numpy as np
import tensorflow as tf
import time

# Load the trained model
model = tf.keras.models.load_model('waste_classifier_v1.h5')

def preprocess_frame(frame):
    img = cv2.resize(frame, (150, 150))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    start_time = time.time()
    predictions = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = preprocess_frame(frame)
        prediction = model.predict(processed_frame)
        predictions.append(prediction)

        elapsed_time = time.time() - start_time
        cv2.imshow('Waste Detection', frame)

        if elapsed_time > 5:  # 5-second video segment
            final_prediction = np.mean(predictions, axis=0)
            classes = ['Recycle', 'Trash']
            label = classes[np.argmax(final_prediction)]
            print(f"Final Label for this segment: {label}")

            predictions = []
            start_time = time.time()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
