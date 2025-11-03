This is the detailed summary of my research and development process for the three models built under my project SNI.
Each model represents a major phase of improvement in accuracy, stability, and real-world applicability for a safety gear detection system using YOLO (You Only Look Once).

Model-1 – Baseline Prototype

Objective:
To build an initial prototype and verify the end-to-end workflow of the object detection system.

Research Work:
Model-1 focused on establishing a baseline for the safety gear detection task. I used the YOLOv8-nano (`yolo12n.pt`) architecture, a lightweight and fast object detection model. The research involved setting up the training pipeline, preparing the custom dataset (with classes like Helmet, Mask, Safety-Vest), and training the model for a single epoch.

Outcome:
Model-1 successfully proved that the concept was feasible. It could detect objects in images, but with limited accuracy due to the short training time. This version served as a proof-of-concept and a foundation for more advanced training.

Model-2 – Prediction and Inference Model

Objective:
To use a trained model to perform inference on new images and evaluate its real-world performance.

Research Work:
Model-2 utilizes a pre-trained model (`best.pt`) that was the result of a more extensive training process. The research focused on running the model in a prediction mode on a test dataset of images. This involved loading the saved model weights and using the model to detect objects and draw bounding boxes on the images. The detected classes include "Helmet", "No-Helmet", "No-Safety-Vest", "Safety-vest", "Mask", "Without-Mask", and "Person".

Outcome:
Model-2 represents the deployed version of the model. It can take new images as input and produce predictions with bounding boxes and class labels. This model's performance is a direct result of the training performed in the other stages.

Model-3 – Final Optimized and Deployed Version

Objective:
To improve the accuracy and robustness of the baseline model by training it for a longer duration.

Research Work:
Model-3 builds upon the work of Model-1. The same YOLOv8-nano architecture was used, but the model was trained for 20 epochs. This longer training allows the model to learn the features of the objects in the dataset more thoroughly, leading to better performance.

Outcome:
Model-3 is the optimized version of the training script. The model produced from this training process is expected to have higher accuracy and be more reliable than the baseline Model-1. This is the model that would be saved as `best.pt` and used for inference, as seen in Model-2.
