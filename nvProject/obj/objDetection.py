from imageai.Detection import VideoObjectDetection
import os
import glob 

#https://heartbeat.fritz.ai/detecting-objects-in-videos-and-camera-feeds-using-keras-opencv-and-imageai-c869fe1ebcdb
directory = '/home/kivi/nvProject/obj'
os.chdir(directory)

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()

directory = '/home/kivi/nvProject/obj'
os.chdir(directory)

for file in glob.glob('*.MOV'): 
	print(file)
	#os.chdir(directory)
	video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, file),
		                        output_file_path=os.path.join(execution_path, file + "detected_1")
		                        , frames_per_second=29, log_progress=True)
	print(video_path)

