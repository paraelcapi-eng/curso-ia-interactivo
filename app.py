import streamlit as st

st.set_page_config(page_title="IA Academy - Portal", layout="centered")

st.title("🚀 Centro de Experimentación de IA")
st.write("Bienvenido, capi. Aquí puedes organizar tus retos de clase.")

# Menú de selección de reto
reto = st.selectbox("Selecciona el reto del día:", [
    "Reto 01: El Semáforo Humano",
    "Reto 02: Detector de Emociones",
    "Reto 03: Inspector de Frutas",
    "Reto 04: Lector de Mentes"
])

st.subheader(f"Instrucciones para: {reto}")
if reto == "Reto 01: El Semáforo Humano":
    st.write("Instrucción: Entrena tres clases (Rojo, Amarillo, Verde) usando gestos con la mano.")
    st.info("💡 Consejo: Asegúrate de tener buena iluminación.")

# Sección de pruebas externa
st.divider()
st.subheader("🧪 Área de Prueba")
model_url = st.text_input("Pega aquí el enlace de tu modelo entrenado:")

if model_url:
    st.write("¡Modelo listo para probar!")
    st.markdown(f"[Haz clic aquí para abrir tu modelo en una ventana nueva]({model_url})")
    st.warning("Nota: Teachable Machine se abrirá en una nueva pestaña para que pruebes tu cámara ahí.")
