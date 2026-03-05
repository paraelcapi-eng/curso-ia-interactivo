import streamlit as st

# 1. SIEMPRE PRIMERO: Configuración de la página
st.set_page_config(page_title="Curso Inteligencia Artificial", page_icon="🤖", layout="wide")

# 2. Función de Autenticación
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
    st.info("Solicita tus credenciales para iniciar la misión.")
    st.stop() 

check_password()

# 3. BASE DE DATOS (Ponla aquí para que esté disponible en toda la app)
diccionario_retos = {
    # ... (Aquí deja todos tus 100 retos que ya tienes escritos) ...
    "Reto 01: El Semáforo Humano": "Entrena 3 clases: Rojo, Amarillo, Verde.",
    "Reto 100: Proyecto Maestro": "Integración total de conocimientos."
}

# 4. BARRA LATERAL (Sidebar)
with st.sidebar:
    st.success(f"👤 Sesión Iniciada")
    if st.button("Cerrar Sesión"):
        st.session_state["password_correct"] = False
        st.rerun()
    
    st.divider()
    st.header("📖 Listado de Retos")
    seleccion = st.selectbox("Elige tu ejercicio:", list(diccionario_retos.keys()))
    st.info(diccionario_retos[seleccion])

# 5. MENÚ DE PESTAÑAS
tabs = st.tabs(["🏠 Inicio", "🚀 Laboratorio de 100 Retos", "📚 Glosario IA", "🎯 Taller de Prompts"])

# --- PESTAÑA 0: INICIO ---
with tabs[0]:
    st.title("🤖 ¡Bienvenido(a) al curso de Inteligencia Artificial")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### ¡Hola, Investigador! 
        Esta plataforma ha sido diseñada para que seas un **Creador de IA**.
        """)
    with col2:
        st.image("https://teachablemachine.withgoogle.com/assets/img/content/home/home-hero-visual.png")

# --- PESTAÑA 1: LABORATORIO (Aquí va la lógica de Teachable Machine) ---
with tabs[1]:
    st.header(f"🧪 Laboratorio: {seleccion}")
    
    with st.expander("📖 ¿Cómo usar Teachable Machine?"):
        st.markdown("Instrucciones de entrenamiento...")

    # Entrada de URL y Lógica del botón
    url_modelo = st.text_input("Pega aquí el enlace de tu modelo (URL):", key="url_tm")
    if url_modelo:
        st.success("🎯 ¡Modelo detectado!")
        st.link_button("🚀 INICIAR PRUEBA DE CAMPO", url_modelo)
    else:
        st.warning("⚠️ Pega el enlace arriba para activar la prueba.")

    st.divider()
    # Bitácora (Dentro de la pestaña 1)
    st.subheader("📝 Bitácora de Observación")
    observacion = st.text_area("¿Qué sucedió al hackear el modelo?", key="bitacora")
    if st.button("Registrar Observación"):
        st.success("✅ ¡Bitácora registrada!")
        st.balloons()

# --- PESTAÑA 2: GLOSARIO ---
with tabs[2]:
    st.header("📖 Conceptos que debes dominar")
    st.write({"Dataset": "Ejemplos para enseñar.", "Clase": "Categorías."})

# --- PESTAÑA 3: TALLER DE PROMPTS ---
with tabs[3]:
    st.header("🎯 Laboratorio de Ingeniería de Prompts")
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        user_prompt = st.text_area("Escribe tu prompt aquí:", height=250, key="area_prompt")
        st.subheader("✅ Checklist de Calidad")
        c1 = st.checkbox("01. ¿Asignaste un ROL?")
        c2 = st.checkbox("02. ¿Solicitaste la TAREA?")
        c3 = st.checkbox("03. ¿Diste CONTEXTO?")
        c4 = st.checkbox("04. ¿Estableciste FORMATO?")
        c5 = st.checkbox("05. ¿Diste DATOS ADICIONALES?")
        c6 = st.checkbox("06. ¿Solicitaste PREGUNTAS?")
    with col_p2:
        puntos = sum([c1, c2, c3, c4, c5, c6])
        st.progress(puntos/6)
        if puntos == 6: st.balloons(); st.success("🚀 ¡Nivel Maestro!")
        st.divider()
        st.subheader("🏆 Desafío del Capi")
        st.info("Aquí aparecerán las 100 situaciones próximamente.")
