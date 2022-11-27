import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(1)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
mid_y = 0
fi_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id ==20:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    mid_x = screen_width / frame_width * x
                    mid_y = screen_height / frame_height * y
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    fi_x = screen_width / frame_width * x
                    fi_y = screen_height / frame_height * y
                if id ==4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(fi_y - thumb_y) < 40:
                        # pyautogui.click()
                        pyautogui.rightClick()
                        pyautogui.sleep(1)
                    if abs(mid_y - thumb_y) < 40:
                        # pyautogui.click()
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('hands', frame)
    cv2.waitKey(1)