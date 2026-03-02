import streamlit as st
from teachable_machine_lite import TeachableMachineModel
import cv2
import numpy as np

st.set_page_config(page_title="IA Academy - Arena de Pruebas", layout="wide")

st.title("🚀 Centro de Experimentación de IA")
st.subheader("Capi, bienvenido a tu laboratorio interactivo")

# Sidebar para configuración
with st.sidebar:
    st.header("Configuración del Reto")
    model_url = st.text_input("Pega el enlace de tu modelo de Teachable Machine:", 
                             placeholder="https://teachablemachine.withgoogle.com/models/...")
    
    ejercicio_num = st.selectbox("Selecciona el Ejercicio:", 
                                [f"Reto {i}: " for i in range(1, 101)])

if model_url:
    st.success("✅ Modelo cargado correctamente. ¡Inicia la cámara!")
    
    # Lógica simplificada de cámara y predicción
    img_file_buffer = st.camera_input("Toma una foto para que la IA la analice")

    if img_file_buffer is not None:
        # Aquí la app procesa la imagen con el modelo del alumno
        st.write("### 🧠 Resultado de la IA:")
        st.info("Simulando análisis... (Aquí aparecerá la clase con mayor probabilidad)")
else:
    st.warning("👈 Por favor, entrena tu modelo en Teachable Machine y pega el link en la izquierda para comenzar.")

st.markdown("---")
st.caption("Diseñado por tu Consultor de IA para el curso de Capi.")
