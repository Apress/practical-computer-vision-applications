# KivyAndroidClassification
Image Classification for Android using Artificial Neural Network using NumPy and Kivy.

This project runs a pre-trained artificial neural network (ANN) in Android for image classification. The ANN is built using NumPy (Numerical Python). In order to be able to run NumPy in Android, the Kivy framework is used for running NumPy on top of it. Kivy is a cross-platform Python framework which supports packaging Python libraries within the APK file. 

The ANN created using NumPy is trained in a desktop computer using 4 classes from the Fruits360 dataset which are apple Braeburn, lemon Meyer, mango, and raspberry. The weights of the ANN are optimized using the genetic algorithm (GA). The optimized weights are saved in a NumPy binary file (.npy). This file is named **weights.npy**.

After the ANN is trained successfully, a Kivy desktop application is created that invokes this NPY file for predicting the class label of new test images. The application has 2 main files. The first is a KV file that holds the layout of the user interface which is named **first.kv**. The second one is a Python file that reads an image, loads the **weights.npy** file, classify the image, and print its class label on the screen. This file is named **main.py**.

After making sure the desktop application is working successfully, the Kivy application is exported into an Android application using Buildozer and python-4-android. Within it, a test image could be fed into the pre-trained ANN for classifying it. For building the Android application, the **buildozer.spec** file is requirdd. 

The next figure shows the window of the application after running it in Linux.
![5](https://user-images.githubusercontent.com/16560492/57416236-a5933d00-71ff-11e9-8d3a-f87ab14f35ba.png)

For details about building the ANN from scratch in NumPy, extracting the features, optimization using GA, and feature reduction, you can read my previous tutorials that covers these points in details.

[Artificial Neural Network Implementation using NumPy and Classification of the Fruits360 Image Dataset](https://www.linkedin.com/pulse/artificial-neural-network-implementation-using-numpy-fruits360-gad) 

Its GitHub project: https://github.com/ahmedfgad/NumPyANN

[Artificial Neural Networks Optimization using Genetic Algorithm with Python](https://www.linkedin.com/pulse/artificial-neural-networks-optimization-using-genetic-ahmed-gad) 

Its GitHub project: https://github.com/ahmedfgad/NeuralGenetic

[Feature Reduction using Genetic Algorithm with Python](https://www.linkedin.com/pulse/feature-reduction-using-genetic-algorithm-ahmed-gad) 

Its GitHub project: https://github.com/ahmedfgad/FeatureReductionGenetic

## For Contacting Me
* E-mail: ahmed.f.gad@gmail.com
* LinkedIn: https://linkedin.com/in/ahmedfgad/
* Hearbeat: https://heartbeat.fritz.ai/@ahmedfgad
* KDnuggets: https://kdnuggets.com/author/ahmed-gad
* TowardsDataScience: https://towardsdatascience.com/@ahmedfgad
* GitHub: https://github.com/ahmedfgad
