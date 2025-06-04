# !pip install opencv-python mediapipe

import cv2
import mediapipe as mp
import os
import csv

videos_dir = './videos_data_set' 
output_dir = './data_set_videos_csv'
os.makedirs(output_dir, exist_ok=True)

# Inicializar MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Función para procesar un solo video
def process_video(video_path, label):
    cap = cv2.VideoCapture(video_path)
    data_rows = []

    frame_index = 0
    while True:
        success, frame = cap.read()
        if not success:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        if results.pose_landmarks:
            row = [frame_index]
            for landmark in results.pose_landmarks.landmark:
                row.extend([landmark.x, landmark.y, landmark.z])
            row.append(label)
            data_rows.append(row)

        frame_index += 1

    cap.release()
    return data_rows

# Crear cabecera del CSV
header = ['frame']
for i in range(33):
    header += [f'x{i}', f'y{i}', f'z{i}']
header += ['label']

# Procesar todos los videos
for filename in os.listdir(videos_dir):
    if filename.endswith('.mp4'):
        print(f"Procesando: {filename}")
        video_path = os.path.join(videos_dir, filename)
        
        label = "_".join(os.path.splitext(filename)[0].split("_")[:1])

        data = process_video(video_path, label)

        # Guardar en CSV
        csv_filename = filename.replace('.mp4', '.csv')
        output_path = os.path.join(output_dir, csv_filename)

        with open(output_path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)

        print(f"Guardado: {output_path}")
