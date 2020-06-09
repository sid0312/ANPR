# Automatic Number Plate Recognition (ANPR)

## License Plate detection and recognition on Indian Number Plates using Yolo v3 Darknet and OCR

### Dataset preparation

- Download the JSON from Kaggle. This would serve as our starter dataset

https://www.kaggle.com/dataturks/vehicle-number-plate-detection

- Check out JSON preprocessing to yield the dataset in yolo format

https://github.com/sid0312/ANPR/blob/master/data_preparation.ipynb

- I have uploaded the prepared dataset too

### Clone the darknet repository 
```
git clone https://github.com/pjreddie/darknet
cd darknet
```
- We add our processed data to the data folder in the darknet directory

- After cloning the darknet repository, we run split.py to sgregate the data into training and validation image paths https://github.com/sid0312/ANPR/blob/master/split.py in darknet/data/train.txt and darknet/data/val.txt repectively 


