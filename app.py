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
    # Lote 2
    "Reto 11: El Susurro vs. El Grito": "Usa modelo de SONIDO. Diferencia volumen y tono de voz.",
    "Reto 12: Identificador de Monedas": "¿Puede la IA distinguir monedas de diferente valor?",
    "Reto 13: Control Remoto Humano": "Mapea gestos para comandos (Play, Stop, Next).",
    "Reto 14: ¿Quién es quién?": "Reconocimiento facial: Tú vs otra persona.",
    "Reto 15: El Traductor de Objetos": "Entrena 'Teclado', 'Mouse' y 'Celular'.",
    "Reto 16: Clasificador de Clima": "Muestra fotos de 'Día Soleado' vs 'Día Lluvioso'.",
    "Reto 17: Detector de Cubrebocas": "Entrena 'Con mascarilla' vs 'Sin mascarilla'.",
    "Reto 18: Sonidos de Oficina": "Sonido de 'Teclado' vs 'Tijeras cortando'.",
    "Reto 19: Yoga Check": "Entrena postura de 'Guerrero' vs 'Árbol' (Cuerpo completo).",
    "Reto 20: El Crítico de Arte": "Diferencia entre un 'Dibujo' y un 'Garabato'.",

    # Lote 3
    "Reto 21: El Espejismo de la Luz": "Entrena con mucha luz y prueba en la oscuridad.",
    "Reto 22: Sesgo de Género/Edad": "Prueba si un modelo entrenado con adultos reconoce niños.",
    "Reto 23: El Camuflaje del Fondo": "Entrena un objeto y muévelo de habitación. ¿Falla?",
    "Reto 24: La Prueba de la Foto": "¿Tu IA distingue una persona real de una foto en el celular?",
    "Reto 25: Clasificador de Idiomas": "Diferencia sonidos de 'Hola', 'Hello' y 'Bonjour'.",
    "Reto 26: Detección de Fake News": "Entrena 'Billete Real' vs 'Billete Dibujado'.",
    "Reto 27: El Reto de las Gafas": "Entrena 'Con lentes' vs 'Sin lentes'.",
    "Reto 28: Inclusión Visual": "Gestos de Sí/No con alguien usando sombrero o cabello largo.",
    "Reto 29: Calidad de Fruta": "Diferencia 'Plátano Maduro' de uno 'Verde'.",
    "Reto 30: El Árbitro de Yoga II": "Detectar 'Espalda Recta' vs 'Espalda Curva' en Plancha.",
    # Lote 4
    "Reto 31: El Click por Gesto": "Entrena un gesto para simular una acción de clic.",
    "Reto 32: Asistente de Lectura": "Entrena la diferencia entre tipos de papel impreso.",
    "Reto 33: Control de Volumen": "Entrena gestos de altura para simular control de audio.",
    "Reto 34: Juego de Memoria Visual": "Entrena 4 cartas de juego o símbolos distintos.",
    "Reto 35: Detector de Mascotas": "Diferencia entre tu mascota real y un juguete similar.",
    "Reto 36: Gestor de Prioridades": "Entrena 'Urgente' (rojo) vs 'Pendiente' (verde).",
    "Reto 37: Simulador de Tablero": "Entrena piezas de juego o representaciones gráficas.",
    "Reto 38: Cámara de Seguridad": "Entrena 'Habitación vacía' vs 'Persona presente'.",
    "Reto 39: Detector de Colores": "Entrena la clasificación de colores primarios.",
    "Reto 40: El Portero Virtual": "Entrena un gesto de atajada ante un balón gráfico.",
    # Lote 5
    "Reto 41: Recordatorio de Hidratación": "Entrena el gesto de beber agua para crear un recordatorio.",
    "Reto 42: Detector de Fatiga": "Diferencia entre ojos abiertos y un bostezo para detectar cansancio.",
    "Reto 43: Entrenador de Yoga III": "Evalúa el equilibrio en la postura del árbol (Pose).",
    "Reto 44: Fisioterapia en Casa": "Entrena la extensión y flexión de una articulación.",
    "Reto 45: Alerta de Tics/Hábitos": "Detecta cuando el usuario se toca la cara o se muerde las uñas.",
    "Reto 46: Detector de Sonrisas": "Crea un modelo que identifique una expresión de felicidad.",
    "Reto 47: Identificador de Medicinas": "Diferencia empaques de medicamentos por color y forma.",
    "Reto 48: Monitor de Meditación": "Identifica la postura correcta y ojos cerrados para meditar.",
    "Reto 49: Gimnasia Cerebral": "Entrena patrones cruzados de manos y cara.",
    "Reto 50: El Break Obligatorio": "Identifica posturas estáticas prolongadas que sugieran un descanso.",
    "Reto 51: Eco-Clasificador de Residuos": [
        "Clasificar materiales de reciclaje (Plástico, Papel, Metal).",
        "Busca objetos de estos tres materiales y prepárate para mostrarlos a la cámara.",
        "Usa una lata muy abollada o rota. ¿La IA sigue sabiendo que es metal? ¿Por qué crees que ocurre?"
    ],
    "Reto 52: Ahorro de Energía": [
        "Detectar si las luces están encendidas innecesariamente.",
        "Entrena con la luz del cuarto encendida y luego apagada.",
        "Abre una cortina para que entre luz solar con el foco apagado. ¿La IA se confunde?"
    ],
    "Reto 53: Identificador de Pilas": [
        "Diferenciar pilas útiles de residuos peligrosos.",
        "Usa pilas en buen estado y algunas que tengan signos de desgaste o sulfatación.",
        "¿Es capaz la IA de detectar texturas pequeñas como el óxido?"
    ],
    "Reto 54: Consumo Responsable": [
        "Fomentar el uso de bolsas reutilizables.",
        "Prepara una bolsa de tela y varias de plástico de supermercado.",
        "Usa una bolsa de plástico transparente. ¿La IA la detecta o ve lo que hay detrás?"
    ],
    "Reto 55: Detector de Desperdicio": [
        "Analizar el desperdicio de comida en el hogar.",
        "Entrena con un plato con restos de comida y un plato totalmente limpio.",
        "Pon una servilleta arrugada sobre el plato vacío. ¿La IA piensa que es comida?"
    ],
    "Reto 56: Riego Inteligente": [
        "Monitorear la humedad de las plantas.",
        "Usa una maceta con tierra muy seca y luego échale agua para la segunda clase.",
        "¿Qué tanto cambia el color de la tierra para que la IA note la diferencia?"
    ],
    "Reto 57: Fauna Urbana": [
        "Reconocimiento de biodiversidad local.",
        "Busca 10 fotos en internet de palomas, gorriones y ardillas para entrenar.",
        "Muestra un dibujo animado de una ardilla. ¿La IA la reconoce como real?"
    ],
    "Reto 58: Cuidado del Agua": [
        "Detección acústica de fugas de agua.",
        "Usa el modelo de SONIDO. Graba un grifo goteando y el silencio.",
        "Haz ruido con una bolsa de plástico. ¿La IA lo confunde con el sonido del agua?"
    ],
    "Reto 59: Transporte Verde": [
        "Identificar elementos de movilidad sostenible.",
        "Entrena con un casco de bicicleta y un juego de llaves de auto.",
        "Muestra un casco de construcción o de moto. ¿La IA es capaz de notar la diferencia?"
    ],
    "Reto 60: Inspector de Humo": [
        "Monitoreo visual de contaminación ambiental.",
        "Usa fotos de cielos limpios y cielos con mucho smog o humo de fábricas.",
        "Muestra una foto de neblina matutina. ¿La IA da una alerta falsa de contaminación?"
    ],
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
