import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

video_capture = cv2.VideoCapture(0)

Mutahir_image = face_recognition.load_image_file("PROJECTS/photos/Mutahir.jpg")
Mutahir_encoding = face_recognition.face_encodings(Mutahir_image)[0]

Ali_image = face_recognition.load_image_file("PROJECTS/photos/Ali.jpg")
Ali_encoding = face_recognition.face_encodings(Ali_image)[0]

Christian_image = face_recognition.load_image_file("PROJECTS/photos/Christian.jpg")
Christian_encoding = face_recognition.face_encodings(Christian_image)[0]

Darshan_image = face_recognition.load_image_file("PROJECTS/photos/Darshan.jpg")
Darshan_encoding = face_recognition.face_encodings(Darshan_image)[0]

Jhon_image = face_recognition.load_image_file("PROJECTS/photos/Jhon.jpg")
Jhon_encoding = face_recognition.face_encodings(Jhon_image)[0]

Jurica_image = face_recognition.load_image_file("PROJECTS/photos/Jurica.jpg")
Jurica_encoding = face_recognition.face_encodings(Jurica_image)[0]

Kevin_image = face_recognition.load_image_file("PROJECTS/photos/Kevin.jpg")
Kevin_encoding = face_recognition.face_encodings(Kevin_image)[0]

Roman_image = face_recognition.load_image_file("PROJECTS/photos/Roman.jpg")
Roman_encoding = face_recognition.face_encodings(Roman_image)[0]

Sibtain_image = face_recognition.load_image_file("PROJECTS/photos/Sibtain.jpg")
Sibtain_encoding = face_recognition.face_encodings(Sibtain_image)[0]

Timothy_image = face_recognition.load_image_file("PROJECTS/photos/Timothy.jpg")
Timothy_encoding = face_recognition.face_encodings(Timothy_image)[0]

Zee_image = face_recognition.load_image_file("PROJECTS/photos/Zee.jpg")
Zee_encoding = face_recognition.face_encodings(Zee_image)[0]

known_face_encodings = [
    Mutahir_encoding,
    Ali_encoding,
    Christian_encoding,
    Darshan_encoding,
    Jhon_encoding,
    Jurica_encoding,
    Kevin_encoding,
    Roman_encoding,
    Sibtain_encoding,
    Timothy_encoding,
    Zee_encoding]

known_face_names = [
    "Mutahir",
    "Ali",
    "Christian",
    "Darshan",
    "Jhon",
    "Jurica",
    "Kevin",
    "Roman",
    "Sibtain",
    "Timothy",
    "Zee"]

Mutahirs = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date + '.csv', 'w+', newline='')
lnwrite = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
            if name in Mutahirs:
                Mutahirs.remove(name)
                print(Mutahirs)
                current_time = now.strftime("%H-%M-%S")
                lnwrite.writerow([name, current_time])

    cv2.imshow("attendance system", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
