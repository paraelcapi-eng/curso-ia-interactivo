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

    # Lote 6: Sostenibilidad
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
    # Lote 8: Accesibilidad
    "Reto 71: Lenguaje de Señas (A-B-C)": [
        "Aprender las bases de la comunicación no verbal.",
        "Busca el alfabeto dactilológico y entrena las posiciones de las letras A, B y C.",
        "Haz las señas con la mano contraria a la que usaste para entrenar. ¿La IA es capaz de entender la simetría?"
    ],
    "Reto 72: Lector de Semáforo Peatonal": [
        "Asistir a personas con discapacidad visual en la calle.",
        "Usa imágenes de semáforos peatonales en rojo y verde (puedes buscarlas en internet).",
        "Dibuja un semáforo en un papel y muéstralo. ¿La IA reconoce el concepto o solo las fotos reales?"
    ],
    "Reto 73: Detector de Obstáculos": [
        "Evitar accidentes en el camino de una persona.",
        "Entrena el piso de tu habitación vacío y luego pon objetos como mochilas o zapatos.",
        "¿Qué tan pequeño puede ser el objeto antes de que la IA deje de marcarlo como obstáculo?"
    ],
    "Reto 74: Traductor de Gestos de Ayuda": [
        "Identificar señales de socorro internacionales.",
        "Entrena el gesto de ayuda (Signal for Help) y una mano en posición normal.",
        "Haz el gesto de forma muy veloz o con poca luz. ¿Qué tan confiable es la IA para emergencias?"
    ],
    "Reto 75: Identificador de Billetes": [
        "Ayudar a identificar dinero en efectivo.",
        "Usa dos billetes de diferente valor y color.",
        "Dobla o arruga el billete y muéstralo de nuevo. ¿La IA se basa en el color o en los patrones del papel?"
    ],
    "Reto 76: Alerta de Llanto de Bebé": [
        "Sistema de alerta auditiva para padres con hipoacusia.",
        "Usa modelo de SONIDO. Graba un audio de un bebé llorando y compara con el ruido ambiental.",
        "Pon un audio de un bostezo fuerte o una risa. ¿La IA genera una falsa alarma?"
    ],
    "Reto 77: Navegación por Cabeza": [
        "Controlar una computadora sin usar las manos.",
        "Usa el modelo de POSE. Entrena inclinar la cabeza a la izquierda y a la derecha.",
        "Ponte una gorra o unos lentes oscuros. ¿Sigue detectando los puntos de tu cara correctamente?"
    ],
    "Reto 78: Lector de Braille Visual": [
        "Convertir relieve táctil en información visual.",
        "Dibuja patrones de puntos Braille en tarjetas blancas con marcador negro.",
        "Usa un marcador de color claro (amarillo). ¿La IA pierde la capacidad de 'leer' los puntos?"
    ],
    "Reto 79: Detector de Caídas": [
        "Monitoreo de seguridad para personas mayores.",
        "Entrena la postura de una persona sentada correctamente vs. una persona en el suelo.",
        "Acuéstate en una cama o sillón. ¿La IA confunde estar descansando con haber sufrido una caída?"
    ],
    "Reto 80: Reconocedor de Medicinas II": [
        "Evitar errores en la toma de medicamentos.",
        "Usa un frasco de jarabe y una caja de pastillas.",
        "Muestra los envases por la parte de atrás (sin etiquetas). ¿La IA reconoce el objeto por su silueta?"
    ],
    # Lote 9: Creatividad y Arte
    "Reto 81: Clasificador de Estilos": [
        "Identificar técnicas artísticas básicas.",
        "Entrena un modelo para diferenciar dibujos lineales de pinturas con pinceladas suaves.",
        "Muestra un dibujo a lápiz pero con sombreado intenso. ¿La IA se confunde con la clase de 'pintura'?"
    ],
    "Reto 82: Director de Orquesta": [
        "Controlar dispositivos mediante el ritmo.",
        "Usa un objeto como batuta y entrena ritmos (lento, rápido, pausa).",
        "Haz movimientos circulares en lugar de rítmicos. ¿Qué hace la IA cuando el movimiento no encaja en ninguna clase?"
    ],
    "Reto 83: Inspector de Calidad de Foto": [
        "Evaluar la claridad y estética de una imagen.",
        "Entrena clases de 'Buena Calidad' (nítida) y 'Mala Calidad' (borrosa o desenfocada).",
        "Aplica un filtro de color o sepia a una foto nítida. ¿La IA la marca como mala calidad por el filtro?"
    ],
    "Reto 84: Traductor de Colores a Emociones": [
        "Explorar la psicología del color.",
        "Entrena clases de colores cálidos (rojos/naranjas) vs. fríos (azules/verdes).",
        "Entrena con el color morado. ¿La IA lo clasifica como cálido o frío?"
    ],
    "Reto 85: El Crítico de Caligrafía": [
        "Evaluar la legibilidad del trazo humano.",
        "Entrena un modelo con tu letra clara y otra clase con tu letra hecha muy rápido (garabato).",
        "Escribe con tu mano no dominante. ¿La IA reconoce la letra o se basa en el 'estilo' de tu mano dominante?"
    ],
    "Reto 86: Clasificador de Géneros Musicales": [
        "Analizar patrones rítmicos en audio.",
        "Usa el modelo de SONIDO para Rock, Jazz y Música Clásica.",
        "Pon una canción de Jazz instrumental. ¿La IA nota la diferencia cuando no hay voz?"
    ],
    "Reto 87: Detector de Doodle": [
        "Identificar bocetos rápidos.",
        "Entrena el dibujo de un Sol y una Luna de forma simplificada.",
        "Dibuja ambos elementos en el mismo papel. ¿La IA puede separar los objetos o se bloquea?"
    ],
    "Reto 88: Selector de Diseño": [
        "Diferenciar estilos visuales.",
        "Entrena diseños minimalistas (pocos elementos) vs. diseños complejos (muy cargados).",
        "Usa un diseño minimalista pero con colores neón muy brillantes. ¿Qué pesa más para la IA: la forma o el color?"
    ],
    "Reto 89: Detector de Emoción en el Arte": [
        "Interpretar la intención artística.",
        "Entrena con dibujos que consideres 'Agresivos' (formas punzantes) vs 'Calmados' (curvas).",
        "Muestra una pintura abstracta real. ¿La IA tiene un sesgo hacia formas simples que tú no entrenaste?"
    ],
    "Reto 90: El 'Pose' de Escultura": [
        "Identificar formas corporales artísticas.",
        "Entrena posturas famosas como 'El Pensador'.",
        "¿Existe un sesgo en la IA para reconocer la belleza artística por encima de posturas cotidianas?"
    ],
    # Lote 10: Integración y Futuro
    "Reto 91: El Botón del Futuro": ["Simular automatización básica.", "Entrena gestos de 'Encendido' y 'Apagado'.", "Haz el gesto con una luz tenue. ¿La IA mantiene la precisión?"],
    "Reto 92: IA en la Educación": ["Facilitar el feedback docente.", "Entrena 'Duda' (mano alzada) y 'Entendido' (dedo pulgar).", "Prueba si la IA detecta la duda cuando el alumno está de espaldas."],
    "Reto 93: Seguridad en el Lab": ["Entender autenticación biométrica.", "Entrena solo tu cara.", "Pide a alguien más que se acerque. ¿A qué porcentaje de confianza te confunde con ellos?"],
    "Reto 94: IA y Ética": ["Detectar sesgos en modelos.", "Entrena 'Juguete de niño' y 'Juguete de niña'.", "Muestra un juguete neutro (ej. un cubo de Rubik). ¿Qué sesgo tiene tu modelo?"],
    "Reto 95: Interfaz de Sueños": ["Creatividad abstracta.", "Entrena 'Paz' y 'Caos' con dibujos espontáneos.", "Usa colores opuestos para cada clase. ¿La IA nota la intención artística?"],
    "Reto 96: IA contra el Hackeo": ["Robustez del modelo.", "Entrena un objeto y trata de engañar al modelo con imágenes similares.", "Añade ruido (papel transparente arrugado) frente a la cámara."],
    "Reto 97: El Gemelo Digital": ["Personalización de la IA.", "Entrena una seña exclusiva tuya.", "Crea un modelo que solo reaccione a tu lenguaje corporal específico."],
    "Reto 98: IA de Campo": ["Robótica aplicada.", "Entrena 'Adelante', 'Atrás', 'Girar'.", "Simula que controlas un robot imaginario. ¿La fluidez del movimiento afecta la predicción?"],
    "Reto 99: Reflexión Final": ["Ética profunda.", "Entrena 'IA Amiga' (formas curvas) vs 'IA Peligrosa' (formas angulares).", "Analiza tu bitácora de los 99 retos anteriores. ¿Qué aprendiste?"],
    "Reto 100: El Proyecto Maestro": ["Integración total.", "Crea un sistema con 4 clases que solucione un problema real de tu casa.", "Presenta tu modelo en el 'Salón de la Fama' de la app."]
}

# --- INTERFAZ DE USUARIO ---
st.title("🚀 IA Academy: Panel de Control")
st.markdown("---")

# --- SECCIÓN DE AYUDA RÁPIDA (INSTRUCCIONES) ---
with st.expander("📖 ¿Cómo usar Teachable Machine? (Guía Paso a Paso)"):
    st.markdown("""
    ### 🛠️ Guía para Entrenar tu IA
    Sigue estos pasos en la pestaña de [Teachable Machine](https://teachablemachine.withgoogle.com/):
    
    1. **Crear Clases:** Ponle nombre a tus categorías (ej: 'Mano Abierta', 'Puño').
    2. **Capturar Datos:** Mantén presionado el botón 'Hold to Record' para tomar fotos o audio. 
       * *Tip de Pro:* Toma al menos **50 muestras** variando ángulos y distancias.
    3. **Entrenar (Train):** Haz clic en 'Train Model'. **No cambies de pestaña** mientras carga, ¡ten paciencia!
    4. **Exportar (Export):** * Ve al botón **'Export Model'**.
       * Selecciona la pestaña **'Tensorflow.js'**.
       * Haz clic en el botón azul **'Upload my model'** (Cargar mi modelo).
    5. **Copiar Link:** Una vez cargado, aparecerá un link tipo `https://teachablemachine.withgoogle.com/models/XXXX/`. 
    
    **¡Ese es el link que debes pegar aquí abajo en la Arena de Pruebas!**
    """)
    st.image("https://teachablemachine.withgoogle.com/assets/img/content/home/home-hero-visual.png", caption="Flujo de trabajo en Teachable Machine")

with st.sidebar:
    st.header("📖 Listado de Retos")
    seleccion = st.selectbox("Elige tu ejercicio:", list(diccionario_retos.keys()))
    st.divider()
    st.write("**Instrucción del Reto:**")
    st.info(diccionario_retos[seleccion])

st.subheader(f"Trabajando en: {seleccion}")
st.write("1. Ve a [Teachable Machine](https://teachablemachine.withgoogle.com/) y entrena tu modelo.")
st.write("2. Exporta el modelo como 'Update Cloud Model' y copia el link.")

# --- ENTRADA DEL MODELO ---
st.subheader("🔗 Entrega de Resultados")

# Caja para que el alumno pegue su URL
url_modelo = st.text_input("Pega aquí el enlace de tu modelo (URL):", 
                           placeholder="https://teachablemachine.withgoogle.com/models/...")

# --- LÓGICA DE ACTIVACIÓN (Aquí va lo que preguntaste) ---
if url_modelo:
    # Si el alumno ya pegó algo, mostramos el éxito y el botón
    st.success("🎯 ¡Modelo detectado y listo para evaluación!")
    st.link_button("🚀 INICIAR PRUEBA DE CAMPO", url_modelo)
else:
    # Si la caja está vacía, mostramos tu mensaje de guía
    st.warning("⚠️ Pega el enlace de tu modelo arriba para activar los sensores de prueba.")

st.markdown("---")
# Pie de página opcional
st.info("💡 Tip: Recuerda que el modelo debe estar publicado como 'Tensorflow.js' en Teachable Machine.")

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
