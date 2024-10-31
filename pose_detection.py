import cv2
import mediapipe as mp
drawing = mp.solutions.drawing_utils
pose = mp.solutions.pose
p = pose.Pose()
cap=cv2.VideoCapture(0)  #video instead of 0
while True:
    fet, frame = cap.read(0)
    frame = cv2.resize(frame,(600,600))
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = p.process(image)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        drawing.draw_landmarks(image, results.pose_landmarks, pose.POSE_CONNECTIONS)
    cv2.imshow('POSE TRACKING', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

