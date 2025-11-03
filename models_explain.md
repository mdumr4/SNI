This is the detailed summary of my research and development process for the three models built under my project SNI.
Each model represents a major phase of improvement in accuracy, stability, and real-world applicability.

Model-1 – Baseline Prototype

Objective:
To build an initial prototype and verify the end-to-end workflow of the system.

Research Work:
Model-1 focused on understanding how user data could be processed and used for predictions. I explored basic machine learning algorithms like Logistic Regression and Decision Tree Classifiers to establish a foundation. The research involved analyzing input data, performing data cleaning, normalization, and basic feature extraction, and then passing it through the model for prediction.

Outcome:
Model-1 successfully proved that the concept was feasible. It could take structured data as input and produce basic outputs, validating that the system architecture and logic were sound. However, accuracy and generalization were limited — this version mainly acted as the learning stage to shape the later improvements.

Model-2 – Improved and Tuned Model

Objective:
To improve accuracy, efficiency, and the overall predictive performance of the system.

Research Work:
In Model-2, I conducted deeper research on feature engineering and hyperparameter tuning. I experimented with advanced algorithms like Random Forest and Support Vector Machines (SVM) to handle complex data patterns. The research also focused on optimizing the dataset — removing irrelevant features, balancing data, and using cross-validation to achieve consistent results.

Outcome:
Model-2 delivered significant improvements over the baseline. It was more accurate, faster in prediction, and less prone to overfitting. The findings from this phase guided how to structure data pipelines efficiently and how to evaluate multiple algorithms before final selection.

Model-3 – Final Optimized and Deployed Version

Objective:
To create a deployment-ready model that could be integrated with the Django web application for real-time use.

Research Work:
Model-3 combined all learnings from previous versions and focused on optimization and integration. I explored techniques for improving scalability and response time while maintaining accuracy. This stage also involved testing the model with real or simulated user data and connecting it to the Django backend via APIs. Research included studying deployment challenges, ensuring stable predictions, and minimizing latency for live interaction.

Outcome:
Model-3 became the final and most stable version of the project. It achieved the best balance between accuracy and speed, and it was successfully integrated into the Django web interface. This allowed users to interact with the system, get intelligent interview simulations, and experience real-time AI responses.