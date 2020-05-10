# Intersection Decision Making




### Software Required
Python3
Yolo
Darknet


### Installing

#### Python3
```
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6
```

#### Darknet
```
git clone https://github.com/pjreddie/darknet.git
cd darknet
make
mkdir -p obj
./darknet
```

#### Yolo
```
wget https://pjreddie.com/media/files/yolov3.weights

To run the detector:
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg

```


## Results
