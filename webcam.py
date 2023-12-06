import cv2
import time
import datetime

cap = cv2.VideoCapture(0)  # multiple video sources can be indexed using 0, 1, 2, ect

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

recording = True
detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETEC = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v") # our recording will be saved as a mp4


while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, 1.3, 5
    )  # gray is going to be the image, scale factor determines number and speed of algo, 5 represents how many frames we need to confirm that the face is a face

    bodies = body_cascade.detectMultiScale(
        gray, 1.3, 5
    )  # gray is going to be the image, scale factor determines number and speed of algo, 5 represents how many frames we need to confirm that the face is a face

    for x, y, width, height in faces:
        cv2.rectangle(
            frame, (x, y), (x + width, y + height), (255, 0, 0), 3
        )  # (x, y) => top left, (x + width, y + height) => my bottom right, (255, 0, 0), 3) => BGR. color and 3 is the thicknessS

    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False # since were detecting a body, we dont want the timer to start, if we weren't already detecting, lets start a new video
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") # Saving our video as the current date and time
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
    elif detection: # when detection stops, we want to wait incase the camera recognized a body or face again before starting a new recording
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETEC:
                detection = False
                timer_started = False
                out.release()
                print("Stopped Recording!")
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord("q"):  # When q is pressed, program terminates
        break

out.release()
cap.release()
cv2.destroyAllWindows()
