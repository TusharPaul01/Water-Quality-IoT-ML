# Water-Quality-IoT-ML
Research paper on this project is already published by Tushar Paul on IEEE Xplore.
Link : https://ieeexplore.ieee.org/abstract/document/10165824

![image](https://github.com/TusharPaul01/Water-Quality-IoT-ML/assets/97314846/c887431e-a396-415c-9415-071bbf8b0bc8)


Project in Brief :
A water quality monitoring system can support environmental protection, local water supply security, and rural areas economic development. This leads to the creation of a system that uses the Internet of Things (IoT) and machine learning to track the water quality. This project explores the properties of water that determine whether it is safe for consumption by people or not. In order to construct a useful model, the pH and turbidity sensors are dipped in water samples that are collected from wells, lakes, rivers, ponds, and other locations. The sensors will transmit the data to the IDE, which will then transmit it to the cloud server. The model successfully takes into account test tables, where 1 denotes that the water is fit for consumption and 0 denotes that it is not. Support Vector Machine, Random Forest, and XG Boost methods are used to validate the model. Using XGBoost, the highest accuracy of 95.12% was noted. Using machine learning and IoT, we have successfully integrated the real-time data for the rural water quality monitoring system that tells us whether the water is fit for drinking or not.

Steps :
1) Intall Arduino IDE on your system
2) Configure Arduino IDE set board type, baurd rate, COM port, etc.
3) Connect the sensors with micro-controller, according to the pins defined
4) Check & upload the code in micro-controller
5) Check the output on serial monitor
6) Create an acount on ThingsSpeak
7) Create a channel & generate API key
8) Enter all the details of ThingSpeak in the arduino code
9) Run the code again
10) Switch on the wifi & let the micro-controller connect to the wifi
11) Real-time data will be displayed on ThingSpeak & can be accessed anywhere through the link
12) Machine Learning is implemented (SVM, RF & XG Boost model)


-- Thank You --

LICENCE : https://github.com/TusharPaul01/Water-Quality-IoT-ML/blob/main/LICENSE 
