<img width="399" height="88" alt="image" src="https://github.com/user-attachments/assets/9ba4892a-0a24-45b7-9a4c-5992e4569915" />



This project aims to achieve the identification of fruits using a camera. It will be implemented with Python. The goal is to label and print the name of the fruit shown by the camera. The program will automatically prepare a dataset in YOLOv8 format. After obtaining the required data, the program will separate them into files necessary for training. In the final stage, the training process will commence, and the model will be tested with the camera
<img width="6875" height="81" alt="image" src="https://github.com/user-attachments/assets/72861887-9ce2-46e1-b54b-fad2e3cdb4d0" />


<img width="476" height="88" alt="image" src="https://github.com/user-attachments/assets/707d592f-f14f-4112-8e5d-c27070a7042d" />


Anaconda 

Visual studio code 

Yolov8 

Python 




<img width="560" height="88" alt="image" src="https://github.com/user-attachments/assets/45342434-c44e-406f-8713-7c8ddffc15f7" />


OpenCv

Ultralytics



<img width="335" height="88" alt="image" src="https://github.com/user-attachments/assets/f2d1db9a-637d-42b6-895d-b4227e616062" />


It creates the necessary data set to recognize my fruits.

We need to create a separate dataset for each fruit.

We create a folder called Dataset where our dataset creation file is located. We create a folder called DataCollect inside our Dataset folder.

We need to use different IDs for each fruit we will define.

We need to enter the correct address from classNames for the dataset to be created for each fruit.




<img width="203" height="88" alt="image" src="https://github.com/user-attachments/assets/418fcd3b-c831-4a2d-92db-9a8e069e2210" />

After collecting the initial data in a single folder, we need to make a separation for training.

It automatically separates the data to be used for training into 'train', 'val' and 'test' folders.

After this separation process, we must ensure that the training takes place according to the IDs we have determined for our inclinations. For this, a data.yml file is automatically created.

We continue by specifying the 'train', 'val' and 'test' folder paths in the data.yml file.



<img width="131" height="88" alt="image" src="https://github.com/user-attachments/assets/1d31881e-61c3-450f-bf08-96bc51480aed" />

After completing the separation process, we must now start our training.

We continue by specifying the path to the data.yml file created for our training program to access the created test, train and val files.

In this training process, we want the dfl_loss value to be around 0.3-0.4 and the mAP value to be close to 1.

We should do this by increasing the epochs value or creating more datasets.



<img width="131" height="88" alt="image" src="https://github.com/user-attachments/assets/fc8c36c5-6aa7-4d98-8fd7-1f1c8a607e6b" />

When I tried the training with 10 different fruits, I observed that very similar fruits were mixed together.

I think this is because the camera cannot fully detect the details.

In my later training, I observed that it gave better results when I tried it with 11 different fruits.

<img width="1642" height="67" alt="image" src="https://github.com/user-attachments/assets/f38e068b-9cd7-4e84-82c5-2a7853080036" />


After our training is completed, two files are created for us: best and last.

These files are trained files.

We test our training with our camera by running these files with our main file.

<img width="386" height="308" alt="image" src="https://github.com/user-attachments/assets/d732a93b-f71d-4780-a636-44e7d4d94070" />   <img width="362" height="303" alt="image" src="https://github.com/user-attachments/assets/dd7511ac-a81e-469a-9dc7-e18e6f76c38c" />






<img width="375" height="88" alt="image" src="https://github.com/user-attachments/assets/61fedfec-2dc9-4897-b1eb-50750fa8a8a7" />

create_a_dataset.py (automatic dataset creation)

splitdata.py (splitting the dataset into test, train and val)

train_offline.py (training)

main.py (application)






