# detect_faces
 detect faces in image with face_recognition

Usage: 
1. create folder with:
    - folder with images ('examples')
    - empty folder for result with boxed faces
    - this script
2. in terminal: '# python facedetection_batch -p path/to/input/images -o pat/to/output/images [-f detected_faces.csv -i detected_per_image.csv]
3. results are written to 
    - 'detected_faces.csv' (each face on one line
    - 'detected_per_images.csv' (number of faces per image)

To change the model, choose one of (model cnn is better but slower):

	\#face_locations = face_recognition.face_locations(image, model="cnn")
	\# face_locations = face_recognition.face_locations(image)
 
To preview the result, uncomment:

	\# cv2.imshow(window_name, boximage)
	\# cv2.waitKey(0)
