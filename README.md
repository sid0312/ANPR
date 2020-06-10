# Automatic Number Plate Recognition (ANPR)

## License Plate detection and recognition on Indian Number Plates using Yolo v3 Darknet and Pytesseract


## Detection

 
<p align="center">  
  <img src="https://media.giphy.com/media/9rpdP0huNtf2pOqvjs/giphy.gif">
</p>

 
### Dataset Preparation


<p align="center">  
  <img src="https://media.giphy.com/media/xTiTnJo7hCVlHyOag8/giphy.gif">
</p>

- Download the starter dataset in JSON format from https://www.kaggle.com/dataturks/vehicle-number-plate-detection
   
 This would serve as our starter dataset


- Check out JSON preprocessing to yield the dataset in yolo format [here](https://github.com/sid0312/ANPR/blob/master/data_preparation.ipynb)

  

- I have uploaded the prepared dataset too

### Clone the darknet repository 
```
git clone https://github.com/pjreddie/darknet
cd darknet
```
- We add our processed data to the data folder in the darknet directory

- After cloning the darknet repository, we run split.py to segregate the data into training and validation image paths https://github.com/sid0312/ANPR/blob/master/split.py in darknet/data/train.txt and darknet/data/val.txt repectively 

## Let us train now !!!
<p align="center">                     
  <img src="https://thumbs.gfycat.com/MetallicNimbleDodo-size_restricted.gif">
</p>

The entire training process has been explained [here](https://github.com/sid0312/ANPR/blob/master/notebooks/train.ipynb)

We train on YOLO v3 Darknet in Google Colaboratory. Notice the darknet forlder in the repository shows the files to be added to the cloned repository from Pjreddie.
<p align="center">   
  <img src="https://github.com/sid0312/ANPR/blob/master/weights/checkpoints/checkpoint_img.JPG">
</p>

## Time for detection
<p align="center">   
  <img src="https://media.giphy.com/media/q6OWziPni6sQE/200_d.gif">
</p>

```
git clone https://github.com/sid0312/ANPR
cd ANPR
python test.py -i /path/to/image -c /path/to/config_file -w /path/to/weights/ -cl /path/to/obj.names
```
# Results for detection
![](screenshots/capture1.JPG)


