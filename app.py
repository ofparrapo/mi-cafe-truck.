import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configura tu API Key de AI Studio
genai.configure(api_key="TU_CLAVE_AQUI")
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Cafe Truck IA", layout="centered")
st.title("☕ Asistente Café Truck")

# Pestañas para organizar
tab1, tab2 = st.tabs(["💬 Chat de Control", "📊 Ver Inventario"])

with tab1:
    st.write("Dime qué vendiste o qué compraste hoy:")
    user_input = st.chat_input("Ej: Vendí 5 cafés y compré 2kg de azúcar")
    
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        
        # La IA procesa la información
        response = model.generate_content(f"Soy dueño de un Cafe Truck. Registra esto y dime el balance: {user_input}")
        
        with st.chat_message("assistant"):
            st.write(response.text)

with tab2:
    st.write("Aquí puedes ver tus registros actuales (se puede conectar a un Excel)")
    # Aquí puedes subir un archivo o mostrar una tabla vacía por ahora
    df = pd.DataFrame(columns=["Insumo", "Cantidad"])
    st.table(df)
