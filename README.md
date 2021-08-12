# Object-Detection-Assignment-For-LuxAI
### Explanation
The implementation is completely based on YOLOV3 architecture and the model is trained by using transfer learning technique .
Provided data is not sufficient for training purposes so I used image augmentation technique for random image creation . 
Here is the procedure for running this application .
I trained this model on 40 epochs .

### Process
1. Clone this repository to your local system .
2. create a virtual env and install all the requrements libraries .

tensorflow==2.3.1,
Keras==2.4.3,
pillow,
matplotlib,
pandas,
opencv-python,
progressbar2,
wandb,
black,

3. Placed the Data.zip file into the  TrainYourOwnYOLO derectory .
4. Move to the directory TrainYourOwnYOLO/Data/Source_Images/Test_Images
5. Place your image files into that Test_Images folder .
6. Then run the file which is inside the TrainYourOwnYOLO/3_Inference/Detector.py i.e python Detector.py
7. Then see your output in TrainYourOwnYOLO/Data/Source_Images/Test_Image_Detection_Results folder . 

### Description

For image augmentation I use Augmentor library . I trained this model with 100+ images . I don't have a strong system and due to the lack of time I trained this images in TinyYOLO architecture and 40 epochs, so for that the accuracy is quite low . 
