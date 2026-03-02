import streamlit as st

# Configuración profesional de la página
st.set_page_config(page_title="IA Academy - Capi", page_icon="🤖", layout="wide")

st.title("🤖 IA Academy: Laboratorio Interactivo")
st.markdown("---")

# Panel Lateral con los 100 Retos (Ejemplo de los primeros 10)
with st.sidebar:
    st.header("📚 Panel de Retos")
    reto_seleccionado = st.selectbox("Selecciona tu ejercicio:", [
        "Reto 01: El Semáforo Humano",
        "Reto 02: Detector de Emociones",
        "Reto 03: Inspector de Frutas",
        "Reto 04: Lector de Mentes",
        "Reto 05: Eco-Clasificador",
        "Reto 06: Estatua vs Humano",
        "Reto 07: Criptografía Visual",
        "Reto 08: El Árbitro de Piedra",
        "Reto 09: Corrector de Postura",
        "Reto 10: Detector de Marcas"
    ])
    st.info("Instrucción: Entrena tu modelo en Teachable Machine y pega el link abajo.")

# Cuerpo principal
st.subheader(f"🚀 {reto_seleccionado}")

# Lógica de instrucciones dinámicas
if "01" in reto_seleccionado:
    st.write("**Objetivo:** Diferenciar 3 estados usando gestos (Rojo, Amarillo, Verde).")
elif "02" in reto_seleccionado:
    st.write("**Objetivo:** Reconocer expresiones faciales (Feliz vs Enojado).")
else:
    st.write("Sigue las instrucciones de tu guía de ejercicios para este reto.")

st.divider()

# Sección de Interacción
st.subheader("🔗 Prueba tu Modelo")
url_modelo = st.text_input("Pega el enlace de tu modelo (https://teachablemachine...):")

if url_modelo:
    st.success("¡Modelo detectado!")
    st.write("Para probarlo, haz clic en el siguiente botón. Se abrirá la interfaz oficial de prueba de Google para que uses tu cámara sin errores:")
    st.link_button("👉 Abrir Probador de IA", url_modelo)
else:
    st.warning("Esperando enlace del modelo para comenzar la evaluación...")

st.markdown("---")
st.caption("Plataforma educativa diseñada por Capi - 2026")
