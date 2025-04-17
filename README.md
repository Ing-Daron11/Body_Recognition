
# Proyecto Final - Inteligencia Artificial 1 (2025-1)

**Universidad ICESI**  
Ingeniería de Sistemas  

## Integrantes
* Daron Mercado
* Santiago Arboleda
* Miguel Martinez

## 🎯 Objetivo

Desarrollar una herramienta de software capaz de analizar actividades humanas específicas como caminar hacia la cámara, caminar de regreso, girar, sentarse y ponerse de pie. Todo esto mediante el seguimiento de movimientos articulares y posturales en video en tiempo real.

## 📥 Entradas

- Video en tiempo real capturado por cámara.

## 📤 Salidas

- Clasificación de la actividad en tiempo real.
- Análisis de inclinaciones laterales.
- Seguimiento de movimientos de articulaciones clave (muñecas, rodillas, caderas).

## 🔧 Herramientas y Tecnologías

- **MediaPipe** o **OpenPose** para el seguimiento de articulaciones.
- Herramientas de anotación: [LabelStudio](https://labelstud.io/) o [CVAT](https://medium.com/cvat-ai/cvat-vs-labelstudio-which-one-is-better-b1a0d333842e)

## 📊 Flujo de Desarrollo (CRISP-DM Adaptado)

### 1. Recolección y Anotación de Datos
- Captura de videos desde diferentes perspectivas.
- Anotación manual o automática de actividades.

### 2. Seguimiento Articular
- Seguimiento de: cadera, rodillas, tobillos, muñecas, hombros, cabeza.
- Medición de inclinaciones y ángulos articulares.

### 3. Preprocesamiento
- Normalización de coordenadas.
- Filtrado de ruido.
- Generación de características como velocidad, inclinación y ángulos relativos.

### 4. Entrenamiento del Clasificador
- Modelos supervisados: SVM, Random Forest, XGBoost.
- División de datos: entrenamiento/prueba.
- Ajuste de hiperparámetros.

### 5. Inferencia en Tiempo Real
- Visualización de actividades y mediciones posturales en una interfaz gráfica.

### 6. Evaluación
- Pruebas con diferentes personas.
- Métricas: precisión, recall, F1-score.

## 🧪 Entregables

- **Entrega 1 (Semana 12)**: Pregunta de interés, metodología, métricas, análisis exploratorio, estrategias de ampliación de datos, y aspectos éticos.
- **Entrega 2 (Semana 14)**: Estrategias de recolección, preprocesamiento, entrenamiento, resultados iniciales y plan de despliegue.
- **Entrega 3 (Semana 17)**: Reducción de características, despliegue final, evaluación final, entrega al cliente, video de presentación.

## 🧾 Estructura del Reporte Final

1. Título  
2. Resumen  
3. Introducción  
4. Teoría  
5. Metodología  
6. Resultados  
7. Análisis de Resultados  
8. Conclusiones y Trabajo Futuro  
9. Referencias Bibliográficas (formato IEEE)

