## SelfDrivingCar
This code helps in getting the steering angle of self driving car. The inspiraion is taken from [Udacity Self driving car](https://github.com/udacity/CarND-Behavioral-Cloning-P3) module as well [End to End Learning for Self-Driving Cars](https://devblogs.nvidia.com/deep-learning-self-driving-cars/) module from NVIDIA

The End to End Learning for Self-Driving Cars research paper can be found at (https://arxiv.org/abs/1604.07316)
This repository uses convnets to predict steering angle according to the road. 

### Description
An autonomous car (also known as a driverless car, self-driving car, and robotic car) is a vehicle that is capable of sensing its environment and navigating without human input. Autonomous cars combine a variety of techniques to perceive their surroundings, including radar, laser light, GPS, odometry, and computer vision. Advanced control systems interpret sensory information to identify appropriate navigation paths, as well as obstacles and relevant signage


### Python Implementation
1) Network Used- Convolutional Network
2) Inspiration - End to End Learning for Self-Driving Cars by Nvidia


##### pip install requirements.txt

### Dataset
Download the datasets from
* https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584f6edd_data/data.zip and,
* https://github.com/SullyChen/driving-datasets  and extract into the repository folder
* Rename 2.2GB dataset as dataset_2
* Rename the 3.1GB dataset as dataset_3. Then run strip_data.py for this dataset only.

### Procedure

1) First, run `LoadData.py` which will get dataset from folder and store it in a pickle file after preprocessing.
2) Now you need to have the data, run `TrainModel.py` which will load data from pickle. After this, the training process begins.
3) For testing it on the video, run `TestDrive.py`

<img src="https://github.com/ashutoshkumar19/Self_Driving_Car/blob/master/working.gif">


## Autopilot V2 (NVIDIA Dataset based on real world)

### References:
 
 - Mariusz Bojarski, Davide Del Testa, Daniel Dworakowski, Bernhard Firner, Beat Flepp, Prasoon Goyal, Lawrence D. Jackel, Mathew Monfort, Urs Muller, Jiakai Zhang, Xin Zhang, Jake Zhao, Karol Zieba. [End to End Learning for Self-Driving Cars](https://arxiv.org/abs/1604.07316)
 - [Behavioral Cloning Project](https://github.com/udacity/CarND-Behavioral-Cloning-P3) 
 - This implementation also took a lot of inspiration from the Sully Chen github repository: https://github.com/SullyChen/Autopilot-TensorFlow  





