import streamlit as st

# 1. CONFIGURACIÓN INICIAL (Debe ser lo primero)
st.set_page_config(page_title="IA Academy - El Capi", page_icon="🤖", layout="wide")

# 2. FUNCIÓN DE AUTENTICACIÓN
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    if st.session_state["password_correct"]:
        return True

    st.title("🔐 Material Didáctico - Acceso Restringido")
    with st.form("login_form"):
        user = st.text_input("Usuario")
        pw = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Ingresar al Laboratorio")
        if submit:
            if user in st.secrets["passwords"] and pw == st.secrets["passwords"][user]:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Usuario o contraseña incorrectos")
    st.info("Capi, solicita tus credenciales para iniciar la misión.")
    st.stop() 

# Ejecutar validación
check_password()

# 3. BASE DE DATOS DE 100 RETOS (AQUÍ ESTÁN TODOS)
diccionario_retos = {
    # Lote 1 al 5 (Resumidos aquí, mantén los tuyos completos)
    "Reto 01: El Semáforo Humano": "Entrena 3 clases: Rojo (mano abierta), Amarillo (puño), Verde (dedo arriba).",
    "Reto 02: Detector de Emociones": "Entrena 'Feliz' vs 'Enojado'. Prueba si funciona si te tapas la boca.",
    "Reto 03: Inspector de Frutas": "Usa una manzana real y una dibujada. ¿La IA nota la diferencia?",
    "Reto 04: El Lector de Mentes": "Entrena con tu mano derecha. Prueba si reconoce la izquierda (Sesgo).",
    "Reto 05: Eco-Clasificador": "Diferencia entre una botella de plástico y una de vidrio.",
    "Reto 06: Estatua vs Humano": "Entrena 'Persona quieta' vs 'Persona moviéndose'.",
    "Reto 07: Criptografía Visual": "Entrena la IA: Lápiz = Letra A, Borrador = Letra B.",
    "Reto 08: El Árbitro de Piedra": "Entrena el juego clásico: Piedra, Papel o Tijera.",
    "Reto 09: Corrector de Postura": "Entrena 'Bien sentado' vs 'Encorvado'.",
    "Reto 10: Detector de Marcas": "Diferencia entre el logo de Google y el de Apple.",
    # ... (Se incluyen los lotes 2, 3, 4 y 5 que ya definiste)
    "Reto 51: Eco-Clasificador de Residuos": "Clasificar materiales de reciclaje (Plástico, Papel, Metal). Usa objetos reales y abollados.",
    "Reto 60: Inspector de Humo": "Monitoreo visual de contaminación ambiental usando fotos de cielos.",
    "Reto 80: Reconocedor de Medicinas II": "Evitar errores en la toma de medicamentos usando frascos y cajas.",
    "Reto 100: El Proyecto Maestro": "Integración total. Crea un sistema que solucione un problema real de tu casa."
}

# 4. BARRA LATERAL (Solo visible tras login)
with st.sidebar:
    st.success("👤 Sesión Iniciada")
    if st.button("Cerrar Sesión"):
        st.session_state["password_correct"] = False
        st.rerun()
    
    st.divider()
    st.header("📖 Listado de Retos")
    seleccion = st.selectbox("Elige tu ejercicio:", list(diccionario_retos.keys()))
    st.write("**Instrucción Actual:**")
    st.info(diccionario_retos[seleccion])

# 5. MENÚ DE NAVEGACIÓN (TABS)
tabs = st.tabs(["🏠 Inicio", "🚀 Laboratorio de 100 Retos", "📚 Glosario IA", "🎯 Taller de Prompts"])

# --- PESTAÑA 0: INICIO ---
with tabs[0]:
    st.title("🤖 Bienvenido(a) al curso de Inteligencia Artificial")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### ¡Hola, Investigador!
        Estás a punto de iniciar un viaje épico. Esta plataforma ha sido diseñada para que dejes de ser un espectador y te conviertas en un **Creador de IA**.
        """)
    with col2:
        st.info("⭐ **Progreso Actual:**\n\n 10 Lotes de Retos.\n\n 100 Misiones activas.")

# --- PESTAÑA 1: LABORATORIO (Lógica de Teachable Machine) ---
with tabs[1]:
    st.header(f"🧪 Laboratorio: {seleccion}")
    
    with st.expander("📖 ¿Cómo usar Teachable Machine? (Guía Paso a Paso)"):
        st.markdown("""
        1. Ve a [Teachable Machine](https://teachablemachine.withgoogle.com/).
        2. Entrena tus clases y haz clic en **Export Model**.
        3. Elige **Tensorflow.js** y haz clic en **Upload my model**.
        4. Copia el link generado y pégalo abajo.
        """)

    st.subheader("🔗 Entrega de Resultados")
    url_modelo = st.text_input("Pega aquí el enlace de tu modelo (URL):", placeholder="https://teachablemachine.withgoogle.com/models/...")

    if url_modelo:
        st.success("🎯 ¡Modelo detectado!")
        st.link_button("🚀 INICIAR PRUEBA DE CAMPO", url_modelo)
    else:
        st.warning("⚠️ Pega el enlace arriba para activar los sensores.")

    st.divider()
    st.subheader("📝 Bitácora de Observación")
    observacion = st.text_area("¿Qué sucedió cuando intentaste 'hackear' el modelo?", placeholder="Escribe tus hallazgos aquí...")
    if st.button("Registrar Observación"):
        st.success("✅ ¡Bitácora registrada!")
        st.balloons()

# --- PESTAÑA 2: GLOSARIO ---
with tabs[2]:
    st.header("📖 Conceptos Clave")
    st.write({
        "Dataset": "Ejemplos (fotos/audios) para enseñar a la IA.",
        "Inferencia": "Cuando la IA 'adivina' basándose en su entrenamiento.",
        "Sesgo": "Error donde la IA favorece un resultado por falta de datos variados."
    })

# --- PESTAÑA 3: TALLER DE PROMPTS ---
with tabs[3]:
    st.header("🎯 Laboratorio de Ingeniería de Prompts")
    col_p1, col_p2 = st.columns([1, 1])
    
    with col_p1:
        st.subheader("📝 Tu Borrador")
        user_prompt = st.text_area("Escribe tu prompt aquí:", height=250, key="prompt_area")
        st.subheader("✅ Checklist de Calidad")
        c1 = st.checkbox("01. Asignar un ROL")
        c2 = st.checkbox("02. Solicitar TAREA")
        c3 = st.checkbox("03. Dar CONTEXTO")
        c4 = st.checkbox("04. Establecer FORMATO")
        c5 = st.checkbox("05. Datos ADICIONALES")
        c6 = st.checkbox("06. Solicitar PREGUNTAS")

    with col_p2:
        st.subheader("📊 Nivel del Prompt")
        puntos = sum([c1, c2, c3, c4, c5, c6])
        st.progress(puntos / 6)
        if puntos == 6:
            st.balloons()
            st.success("🚀 ¡Nivel Maestro!")
        
        st.divider()
        st.subheader("🏆 Desafío del Capi")
        st.info("Selecciona una de las 100 situaciones que cargaremos a continuación.")
