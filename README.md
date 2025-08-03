HOW IT WILL WORK<img width="876" height="193" alt="image" src="https://github.com/user-attachments/assets/44030e55-6df4-4c39-8fc4-8f2861306e71" />
This project aims to achieve the identification of fruits using a camera. It will be implemented with Python. The goal is to label and print the name of the fruit shown by the camera. The program will automatically prepare a dataset in YOLOv8 format. After obtaining the required data, the program will separate them into files necessary for training. In the final stage, the training process will commence, and the model will be tested with the camera
<img width="6875" height="81" alt="image" src="https://github.com/user-attachments/assets/72861887-9ce2-46e1-b54b-fad2e3cdb4d0" />


PROGRAMS TO BE USED<img width="857" height="158" alt="image" src="https://github.com/user-attachments/assets/f18a2567-cb8c-476b-83d4-6d47bbf4d4cc" />
Anaconda 
Visual studio code 
Yolov8 
Python 
<img width="367" height="338" alt="image" src="https://github.com/user-attachments/assets/cda6ddd5-cad9-4507-bd74-af10b5ee00af" />


REQUIRED PYTHON LIBRARIES
<img width="1003" height="158" alt="image" src="https://github.com/user-attachments/assets/f42e6dc3-950a-4d03-9955-5746dc151629" />
OpenCv
Ultralytics
<img width="246" height="146" alt="image" src="https://github.com/user-attachments/assets/fbb2691c-9be8-4ce2-ba5a-a2a80fe4f7a0" />


Creating Dataset<img width="731" height="193" alt="image" src="https://github.com/user-attachments/assets/864aaef1-327d-4b97-98cd-b25720e7d280" />
It creates the necessary data set to recognize my fruits.
We need to create a separate dataset for each fruit.
We create a folder called Dataset where our dataset creation file is located. We create a folder called DataCollect inside our Dataset folder.
We need to use different IDs for each fruit we will define.
We need to enter the correct address from classNames for the dataset to be created for each fruit.

<img width="3574" height="459" alt="image" src="https://github.com/user-attachments/assets/b66332eb-59ff-479c-a1a5-117a37724dae" />


Separate<img width="442" height="193" alt="image" src="https://github.com/user-attachments/assets/4deeb8b7-bd6a-44bd-b52d-f199f62b0f4c" />
After collecting the initial data in a single folder, we need to make a separation for training.
It automatically separates the data to be used for training into 'train', 'val' and 'test' folders.
After this separation process, we must ensure that the training takes place according to the IDs we have determined for our inclinations. For this, a data.yml file is automatically created.
We continue by specifying the 'train', 'val' and 'test' folder paths in the data.yml file.
<img width="4695" height="375" alt="image" src="https://github.com/user-attachments/assets/a59cf1d0-d918-4e4f-b1a7-a41ffa3b3bcc" />


Train<img width="288" height="193" alt="image" src="https://github.com/user-attachments/assets/e67d9e5a-9b17-4462-9fad-cc061bdd9e4c" />
After completing the separation process, we must now start our training.
We continue by specifying the path to the data.yml file created for our training program to access the created test, train and val files.
In this training process, we want the dfl_loss value to be around 0.3-0.4 and the mAP value to be close to 1.
We should do this by increasing the epochs value or creating more datasets.
<img width="3385" height="375" alt="image" src="https://github.com/user-attachments/assets/a9975ee1-ee4d-4bbb-a27e-da2f1c12eb0c" />


Final<img width="289" height="193" alt="image" src="https://github.com/user-attachments/assets/05a8a422-92a4-4dfd-b762-dd4e8e1c5e43" />
When I tried the training with 10 different fruits, I observed that very similar fruits were mixed together.
I think this is because the camera cannot fully detect the details.
In my later training, I observed that it gave better results when I tried it with 11 different fruits.
<img width="2633" height="291" alt="image" src="https://github.com/user-attachments/assets/54bf28d1-1378-4cb1-8078-a5e883086329" />
<img width="1642" height="67" alt="image" src="https://github.com/user-attachments/assets/1e435199-5b86-46d8-a34a-9cad3434f4e1" />
After our training is completed, two files are created for us: best and last.
These files are trained files.
We test our training with our camera by running these files with our main file.
<img width="2009" height="291" alt="image" src="https://github.com/user-attachments/assets/2ada098a-48d2-46e3-a4e9-a04e454f256e" />
<img width="386" height="308" alt="image" src="https://github.com/user-attachments/assets/ef057864-ae02-43d0-b999-c0ff5190cd7c" />      <img width="362" height="303" alt="image" src="https://github.com/user-attachments/assets/8ea0b0e1-1035-43e9-8c05-5b8af9abab36" />


Programs We Write<img width="822" height="193" alt="image" src="https://github.com/user-attachments/assets/26d230b4-6019-43e4-8517-401244f96390" />
create_a_dataset.py (automatic dataset creation)
splitdata.py (splitting the dataset into test, train and val)
train_offline.py (training)
main.py (application)

<img width="1497" height="375" alt="image" src="https://github.com/user-attachments/assets/4a12aad7-0cdf-4984-8b24-287c07b24ad8" />



