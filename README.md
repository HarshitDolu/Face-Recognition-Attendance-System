# Face-Recognition-Attendance-System

Simple openCv application for taking real time attendance.<br>
Purpose: learning opencv<br>
main task : Facial Recognition and importing present students into excel sheet<br>
I have used pycharm editor.<br>

First install C++ desktop developement service in VScode.<br>
After installing above service, install cmake, dlib 19.18.0, opencv, numpy and face_recognition packages<br>

About face_recognition library<br>
It finds face and perform facial landmark detection. On passing the test image through pretrained model, 128 measurements of a single image is captured as output.<br>
It includes faceLocations, face encodings.<br>

Steps:<br>

step 1: Save images in list and keep new similar image as test img, for facial recognition<br>
step 2: convert BGR 2 RGB<br>
step 3: find face locations, as it will help to draw bounding box on the face<br>
step 4: find encodings( 128 measurements) of all images in list as well as for test image.<br>
step 5: compare the test encoding with encodings which are there in list.<br>
step 6: find facial distance<br>
one having low facial distance, will have high similarity, Hence Recognition done....<br>

