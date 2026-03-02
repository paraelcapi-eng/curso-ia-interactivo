import streamlit as st

st.set_page_config(page_title="IA Academy - Capi", page_icon="🤖", layout="wide")

# --- BASE DE DATOS DE RETOS (Aquí agregamos los nuevos) ---
diccionario_retos = {
    # Lote 1
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
}

# --- INTERFAZ DE USUARIO ---
st.title("🚀 IA Academy: Panel de Control")
st.markdown("---")

with st.sidebar:
    st.header("📖 Listado de Retos")
    seleccion = st.selectbox("Elige tu ejercicio:", list(diccionario_retos.keys()))
    st.divider()
    st.write("**Instrucción del Reto:**")
    st.info(diccionario_retos[seleccion])

st.subheader(f"Trabajando en: {seleccion}")
st.write("1. Ve a [Teachable Machine](https://teachablemachine.withgoogle.com/) y entrena tu modelo.")
st.write("2. Exporta el modelo como 'Update Cloud Model' y copia el link.")
st.write("3. Pégalo aquí abajo para verificar tu trabajo.")

url_modelo = st.text_input("Enlace del modelo (URL):", placeholder="https://teachablemachine.withgoogle.com/models/...")

if url_modelo:
    st.success("¡Modelo listo para evaluación!")
    st.link_button("🎯 PROBAR MODELO AHORA", url_modelo)
else:
    st.warning("Capi, pega el link para activar el botón de prueba.")

st.markdown("---")
st.caption("Plataforma de capacitación técnica - Capi 2026")

# --- EN EL CUERPO PRINCIPAL DE TU APP ---

st.divider()

# Sección de Reflexión (Bitácora)
st.subheader("📝 Bitácora de Observación del Estudiante")
st.write("Antes de pasar al siguiente reto, completa tu bitácora de investigador:")

# Campos de la bitácora
observacion = st.text_area("¿Qué sucedió cuando intentaste 'hackear' el modelo?", 
                           placeholder="Ejemplo: La IA falló cuando usé la mano izquierda...")

if observacion:
    st.success("✅ ¡Bitácora registrada! Tus observaciones son clave para mejorar la IA.")
    st.balloons() # ¡Pequeño premio visual por documentar!

st.markdown("---")
st.caption("Plataforma de Investigación en IA - Capi 2026")
