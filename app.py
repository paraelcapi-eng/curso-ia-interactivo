import streamlit as st

st.title("¡Hola, capi! Mi primera App de IA")
st.write("Esta aplicación está conectada con GitHub y Streamlit Cloud.")

nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.write(f"Mucho gusto, {nombre}. ¡Estamos listos para empezar el curso!")
