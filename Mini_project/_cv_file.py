from tensorflow import keras
import numpy as np
import cv2

emotion = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

model = keras.models.load_model("C:/Users/admin/Downloads/model.h5")
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)
face_cas = cv2.CascadeClassifier('C:/Users/admin/Downloads/frontalface.xml')
vid = cv2.VideoCapture(0)
# a = 0
while True:
    ret, frame = cam.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray = cv2.flip(gray,1)
        faces = face_cas.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_component = gray[y:y + h, x:x + w]
            fc = cv2.resize(face_component, (48, 48))
            inp = np.reshape(fc, (1, 48, 48, 1)).astype(np.float32)
            inp = inp / 255.
            prediction = model.predict(inp)
            em = emotion[np.argmax(prediction)]
            score = np.max(prediction)
            cv2.putText(frame, em + "  " + str(score * 100) + '%', (x, y), font, 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("image", frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('Error')
emtn = em
cam.release()
cv2.destroyAllWindows()

