This is a project build for MakeUofT2025

Here are the citations for this project:

**The model training reference is from these websites:**
https://github.com/jzx-gooner/DL-wastesort?tab=readme-ov-file

The trash and recycling category image is from this site:
https://huggingface.co/datasets/garythung/trashnet/tree/main

**Project Description:**

## Inspiration
Our inspiration for this project stems from the increasing need for efficient waste management and environmental sustainability. Improper waste disposal is a significant global issue, leading to pollution, inefficient recycling, and excessive landfill use. Many people struggle to correctly sort their garbage into the appropriate categories—recyclable and general waste—resulting in contamination that reduces the effectiveness of recycling programs.

With advancements in artificial intelligence, robotics, and automation, we saw an opportunity to develop a smart waste sorting system that can automatically detect the type of garbage and place it into the correct bin. By leveraging computer vision and machine learning, our system can analyze waste items in real time and classify them accurately. It integrates AI-driven classification with robotic automation, in aims to contribute to a more sustainable and technologically advanced world.  

## What it does
Our project utilizes machine learning and robotics to automatically classify and sort waste into the correct bin. Key features include garbage identification, AI classification, and automated sorting. When an item enters the system, a camera captures an image of it. A machine learning model analyzes the image and determines whether the item is recyclable or trash. If the item is recyclable, a servo motor-controlled exit directs it to a recycling bin on the side. If it is trash, a second exit opens, allowing it to drop into the general waste bin below.


## How we built it
We collected a dataset of garbage images categorized into recyclable and trash and preprocessed the images using OpenCV and NumPy, applying resizing, normalization, and data augmentation to improve generalization. Using the dataset of garbage images, we developed and trained a train_waste_model using Convolutional Neural Network (CNN) to extract features and classify waste. We substituted a traditional ESP-32 camera and a Raspberry Pi setup with an iphone camera to capture images of incoming waste due to limited materials. It is then connected to the computer running the ML model, which processes the images in real time. The trained model is deployed on to a microcontroller, specifically Arduino Uno, which receives classification results from the computer via USB type-C serial communication, and controls the servo motors.     

Due to limited equipment, we replaced metal plates and the rotary diverter with wooden boards and cardboard. Considering the high friction coefficient of wood, we first built a 30° wooden inclined slope using hot glue and nails to ensure smooth passage of waste samples through the system. Next, we attached the servo motors to our slope using hot glue. Because the connector on the motor's output was too short to drive the rotary diverter (cardboard) directly, we secured the connector to a small wooden stick with zip ties and hot glue, inserted it into the rotary diverte  (cardboard), and reinforced the assembly with additional hot glue.



## Challenges we ran into
One of the main challenges we faced was ensuring accurate waste classification. Training a CNN model with limited datasets initially resulted in lower accuracy, requiring us to expand our dataset and apply techniques like transfer learning to improve performance.

A significant challenge arose with the servo motors during the hardware assembly phase. We encountered issues with connectors that didn’t fit properly and the incompatibility of several provided servo motors with our design requirements. After multiple trials and adjustments, we decided to replace two servo motors with a single, more reliable servo motor. To ensure the sorting mechanism still functioned correctly, we added two additional baffles on top of the original one, allowing one servo motor to efficiently control the sorting process. This required careful recalibration, redesign, and precise assembly, but overcoming these challenges enhanced our understanding of mechanical design and hardware integration.

Another challenge was establishing a reliable connection between the iPhone camera and our classification system. Capturing real-time video from the phone and ensuring seamless integration with zzour machine learning model required careful handling of network configurations and streamin protocols. Additionally, sending the predicted waste label from the classification system to the Arduino Uno for controlling the servo motor was challenging. We had to ensure accurate timing and signal reliability, which involved debugging communication protocols and synchronizing the software and hardware components.

These challenges not only improved our technical capabilities but also taught us the importance of perseverance, debugging, and iterative design.

## Accomplishments that we're proud of
We are proud of successfully building a fully functional SmartBin AI system that integrates machine learning with hardware components. Developing a CNN model that accurately classifies waste into categories, despite starting with a limited dataset, was a significant achievement.

We take pride in overcoming numerous hardware challenges, including designing and assembling a custom bin structure, and optimizing the sorting mechanism with a single servo motor and additional baffles for precise operation. Establishing a reliable connection between the iPhone camera and the machine learning model, and ensuring that the predicted labels were accurately sent to the Arduino Uno for controlling the sorting mechanism, was another highlight of our project.

Additionally, successfully combining AI, mechanical design, and Arduino programming into a single, cohesive system is an accomplishment we are especially proud of. The experience of seeing our SmartBin AI function as intended, sorting waste in real-time, reinforced our belief in the power of interdisciplinary collaboration and innovation.

## What we learned
During the development of SmartBin AI, we gained significant hands-on experience with Convolutional Neural Networks (CNNs) and machine learning model training. We learned how to preprocess images using techniques such as rescaling, shear transformation, zooming, and horizontal flipping to enhance the training dataset. Building CNN architectures with TensorFlow and Keras taught us how to optimize hyperparameters, prevent overfitting using dropout and batch normalization, and evaluate model performance using accuracy and loss metrics.

We implemented core machine learning techniques like transfer learning, where we utilized a pre-trained model as a base and fine-tuned it for waste classification, resulting in improved accuracy and faster training. Our project also included real-time video capture using an iPhone camera, with the classification system sending signals to an Arduino Uno to control LED indicator lights and drive servo motors that operated the bin’s sorting mechanism. The LED lights provided visual feedback on the sorting status, while the servo motors ensured precise and reliable movement of waste items into the correct bins.

Additionally, we learned practical hardware skills like Arduino Uno coding, cutting wood for the bin structure, attaching servo motors securely, and ensuring precise mechanical operations. This combination of AI development, transfer learning, hardware coding, and hands-on construction was an invaluable learning experience that strengthened our technical abilities, teamwork, and problem-solving skills.

## What's next for SmartBin AI
Due to limited camera supply, our prototype utilizes a smartphone as the camera. In future optimized designs, we plan to integrate a camera with a Raspberry Pi, enabling localized AI trash recognition that will significantly enhance both recognition accuracy and operational efficiency. Additionally, we intend to replace the current wooden sliding rails and baffles with smoother metal plates. This change will not only improve the smoothness of the rails but also reduce the slope required for trash to slide down, thereby maximizing the available space within the trash bin. We will also replace our mini servo motor with a higher-torque servo motor to ensure the system's stability and durability. Lastly, by installing a solar panel on top of the trash bin, our system will be able to operate without an external power supply.

