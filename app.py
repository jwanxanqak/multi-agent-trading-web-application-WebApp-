import streamlit as st
import requests
import os

st.set_page_config(page_title="AlphaAgent SaaS", layout="wide", page_icon="📈")
 
st.title("📈 AlphaAgent — Plataforma Multi-Agente de Trading")
st.caption("Fase 5: Despliegue Externo de Producción (FastAPI + Streamlit)")
st.markdown("---")

# Ajuste de DevOps: Si Render nos entrega el host privado puro, le añadimos el protocolo http://
if API_URL and not API_URL.startswith("http://") and not API_URL.startswith("https://"):
    API_URL = f"http://{API_URL}"

st.sidebar.header("⚙️ Configuración")
tickers_input = st.sidebar.text_input("Ingresa los Tickers separados por coma:", "AAPL, MSFT")
tickers_list = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

tab_monitor, tab_risk, tab_chat = st.tabs(["🖥️ Monitor de 3 Agentes", "🛡️ Control de Riesgo", "💬 Chat Agéntico"])

with tab_monitor:
    st.subheader("🔍 Desglose de Capas por Activo")
    for ticker in tickers_list:
        with st.expander(f"📊 Auditoría: {ticker}", expanded=True):
            try:
                response = requests.get(f"{API_URL}/api/signals/{ticker}", timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("has_data", False):
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.markdown("### 🤖 Basic AI Agent")
                            st.metric("Técnico", data["basic_agent"]["recommendation"])
                            st.caption(data["basic_agent"]["justification"])
                        with col2:
                            st.markdown("### 📊 Advanced AI Agent")
                            st.metric("Avanzado", data["advanced_agent"]["recommendation"])
                            st.caption(data["advanced_agent"]["justification"])
                        with col3:
                            st.markdown("### 🧠 Portfolio Manager")
                            rec_pm = data["portfolio_manager"]["recommendation"]
                            if "BUY" in rec_pm: st.success(rec_pm)
                            elif "SELL" in rec_pm: st.error(rec_pm)
                            else: st.warning(rec_pm)
                            st.info(data["portfolio_manager"]["justification"])
                    else:
                        st.warning(data["portfolio_manager"]["justification"])
                else:
                    st.error("Error en respuesta del servidor.")
            except Exception as e:
                st.error(f"Conectando al backend en: {API_URL}... (Asegúrate de que el Backend no esté dormido)")

with tab_risk:
    st.subheader("🛡️ Umbrales de Mitigación")
    c1, c2 = st.columns(2)
    c1.metric("Exposición Máxima", "12.5%")
    c2.metric("Estado de Alertas", "BAJO")

with tab_chat:
    st.subheader("💬 Consola del Comité Corporativo")
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
            
    if user_prompt := st.chat_input("Consulta a tus agentes:"):
        with st.chat_message("user"): st.markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})
        
        try:
            res = requests.post(f"{API_URL}/api/chat", json={"message": user_prompt}, timeout=10)
            reply = res.json().get("response", "Sin respuesta.") if res.status_code == 200 else "Error del servidor."
        except:
            reply = "Backend inaccesible."
            
        with st.chat_message("assistant"): st.markdown(reply)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})