from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import numpy as np
import joblib
import pickle
import os

app = Flask(__name__)

MODELS_DIR = os.path.join(os.path.dirname(__file__), "Entrega_3", "scripts")
scaler = joblib.load(os.path.join(MODELS_DIR, "scaler.pkl"))
pca = joblib.load(os.path.join(MODELS_DIR, "pca.pkl"))

MODELS_DIR = os.path.join(os.path.dirname(__file__), "Entrega_3", "scripts")
modelos = {
    "RandomForest": joblib.load(os.path.join(MODELS_DIR, "modelo_RandomForest.pkl")),
    "SVM": joblib.load(os.path.join(MODELS_DIR, "modelo_SVM.pkl")),
    "XGBoost": joblib.load(os.path.join(MODELS_DIR, "modelo_XGBoost.pkl"))
}

modelo_actual = "SVM" 

# Cargar clases (etiquetas)
try:
    le = joblib.load(os.path.join(MODELS_DIR, "label_encoder.pkl"))
    label_classes = le.classes_
except:
    with open(os.path.join(MODELS_DIR, "label_classes.pkl"), 'rb') as f:
        label_classes = pickle.load(f)

# Inicializar MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

def extract_features(landmarks):
    features = []
    for lm in landmarks:
        features.extend([float(lm.x), float(lm.y), float(lm.z)])
    return features

def generate_frames():
    cap = cv2.VideoCapture(0)  # Accede a la cámara
    if not cap.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo leer el frame de la cámara.")
            break

        # Convertir el frame a RGB para MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            features = extract_features(landmarks)
            input_features = np.array(features, dtype=np.float64).reshape(1, -1)
            input_features_scaled = scaler.transform(input_features)
            input_features_pca = pca.transform(input_features_scaled)
            try:
                prediction = modelos[modelo_actual].predict(input_features_pca)[0]
                # Mapear predicción a etiqueta
                if isinstance(prediction, str):
                    activity = prediction
                else:
                    activity = label_classes[int(prediction)] if int(prediction) < len(label_classes) else "Desconocido"
                cv2.putText(frame, f'Actividad: {activity}', (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            except Exception as e:
                print(f"Error en el procesamiento: {str(e)}")
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Codificar el frame para el stream
        ret, encoded_frame = cv2.imencode('.jpg', frame)
        frame = encoded_frame.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    """Página principal."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Endpoint del video en streaming."""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)