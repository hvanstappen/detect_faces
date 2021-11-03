import os
import face_recognition
import csv
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path to input images")
ap.add_argument("-f", "--faces_report", default="detected_faces.csv",
	help="path to detected faces CSV file")
ap.add_argument("-i", "--image_report", default="detected_per_image.csv",
	help="path to faces per image CSV file")
args = vars(ap.parse_args())

path = args["path"]

files = os.listdir(path)

# csv with coordinates of detected faces
f = open(args["faces_report"],'w')

# csv with faces per image
i = open(args["image_report"],'w')

for jpg in files:

	jpgpath = path+'/'+jpg
	image = face_recognition.load_image_file(jpgpath)

	# choose an option, model cnn is better but slower
	# face_locations = face_recognition.face_locations(image, model="cnn")
	face_locations = face_recognition.face_locations(image)

	# write line for each detected face to csv
	for face in face_locations:
		f.write(str(face))
		f.write(";")
		f.write(jpg)
		f.write("\n")
		
	# draw rectangle on faces
	for face in face_locations:
		# Reading an image
		boximage = cv2.imread(jpgpath)
		print(face)
    
		# Window name in which image is displayed
		window_name = 'Image'
  
		# represents the top left corner of rectangle
		start_point = (face[3], face[0])
   
		# represents the bottom right corner of rectangle
		end_point = (face[1], face[2])
   
		# Green color in BGR
		color = (0, 255, 0)
   
		# Line thickness of 2 px
		thickness = 2
   
		# Using cv2.rectangle() method
		# Draw a rectangle of black color of thickness 1 px
		boximage = cv2.rectangle(boximage, start_point, end_point, color, thickness)
   
		# Displaying the image 
		cv2.imshow(window_name, boximage) 
		cv2.waitKey(0)

	# write result per image to csv
	n = len(face_locations)
	
	i.write(str(jpg))
	i.write(";")
	i.write(str(n))
	i.write("\n")

	print(jpg)
#	print(face_locations)


# print(faces)
	
