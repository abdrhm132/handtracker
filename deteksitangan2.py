import cv2
import mediapipe as mp

# Inisialisasi modul MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()


# Inisialisasi VideoCapture
cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=3,
                  min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        # Baca frame dari kamera
        ret, frame = cap.read()
        if not ret:
            continue

        # Konversi frame ke warna RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Proses hand tracking
        results = hands.process(rgb_frame)

        # Cek apakah ada tangan terdeteksi
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Gambar landmarks pada tangan
                for landmark in hand_landmarks.landmark:
                    h, w, _ = frame.shape
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
      
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (1510,670))
        # Tampilkan frame
        cv2.imshow("Hand Tracking", frame)

        # Keluar dari loop jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Tutup VideoCapture dan jendela OpenCV
cap.release()
cv2.destroyAllWindows()
