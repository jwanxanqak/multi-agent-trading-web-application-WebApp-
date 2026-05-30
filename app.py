import streamlit as st
import requests
import os

st.set_page_config(page_title="AlphaAgent SaaS - Multi-Agent Dashboard", layout="wide", page_icon="📈")
 
st.title("📈 AlphaAgent — Multi-Agent Trading Platform")
st.caption("Visual Modules for Asset Monitoring, Portfolio Monitoring and Interactive Chat (LLM))")
st.markdown("---")

# 1️⃣ FIRST WE DEFINE THE VARIABLE
API_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
).rstrip("/")

# DevOps Adjustment: If Render delivers the pure private host, we add the http:// protocol
if API_URL and not API_URL.startswith("http://") and not API_URL.startswith("https://"):
    API_URL = f"http://{API_URL}"

# --- SIDEBAR: Dynamic Selection ---
st.sidebar.header("⚙️ Control Panel")

# 1. Definition of the set of 30 assets
AVAILABLE_ASSETS = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META", "TSLA", "NVDA", "NFLX", "AMD", "INTC",
    "ECOPETROL", "PFBCOLOM", "BVC", "GRUPOSURA", "NUTRESA", "JPM", "BAC", "WMT",
    "PG", "XOM", "CVX", "JNJ", "PFE", "V", "MA", "DIS", "NKE", "HD", "COST", "PEP"
]

# 2. Quick option to select the entire universe of assets
select_all = st.sidebar.checkbox("🌍 Select all 30 assets")

# 3. Ticker list assignment logic
if select_all:
    # If you check the box, all assets will be automatically selected
    tickers_list = AVAILABLE_ASSETS
    st.sidebar.info(f"Selected: All {len(AVAILABLE_ASSETS)} assets.")
else:
    # Otherwise, allow a custom selection using multiselect
    tickers_list = st.sidebar.multiselect(
        "Select the tickers to query:",
        options=AVAILABLE_ASSETS,
        default=["AAPL", "MSFT", "AMZN", "GOOGL"]  # Default initial values
    )

# Keep the chat history initialization under the selection
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- VISUAL MODULES (Updated Sprint 5 Tabs) ---
tab_monitor, tab_risk, tab_chat = st.tabs(["🖥️ Multi-Agent Asset Monitor", "🛡️ Portfolio Monitoring Panel", "💬 Interactive Chat (LLM)"])

with tab_monitor:
    st.subheader("🔍 Recommendation from each agent")
    st.markdown("Individual recommendations from the **Basic AI Agent**, **Advanced AI Agent**, and final decision from the **Portfolio Manager Agent**:")
    for ticker in tickers_list:
        with st.expander(f"📊 Multi-Agent Technician Report: {ticker}", expanded=True):
            try:
                response = requests.get(f"{API_URL}/api/signals/{ticker}", timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("has_data", False):
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.markdown("### 🤖 Basic AI Agent")
                            st.metric("Technical", data["basic_agent"]["recommendation"])
                            st.caption(data["basic_agent"]["justification"])
                        with col2:
                            st.markdown("### 📊 Advanced AI Agent")
                            st.metric("Advanced Indicators", data["advanced_agent"]["recommendation"])
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
                    st.error("❌ Critical infrastructure error: Unable to connect to the API backend. Details:")
            except Exception as e:
                st.error(f"Connecting to the backend at: {API_URL}... (Make sure the backend is not asleep)")

# PORTFOLIO MONITORING PANEL
with tab_risk:
    st.subheader("🛡️ Trading rules")

    col_r1, col_r2, col_r3 = st.columns(3)
    with col_r1:
        st.metric(label="Suggested Capital Exposure (Max)", value="18.600.000", delta="15% this week")
    with col_r2:
        st.metric(label="Status Control Rules (DuckDB)", value="LOW RISK", delta_color="inverse")
    with col_r3:
        st.metric(label="Recorded Maximum Drawdown", value="1.86%")

    st.markdown("---")
    st.warning("⚠️ **Automated System Rule:** If the Technical Agent detects a sudden drop in transaction volume concurrent with a negative moving average crossover or RSI overbought crossover, the **Portfolio Manager Agent** will force the automatic closure of the position to mitigate losses in the fund.")

# 3. INTERACTIVE CHAT (LLM)
with tab_chat:
    st.subheader("💬 Chat Console with Multi-Agent Ecosystem & LLM")
    st.markdown("Converse directly with AI Multi-Agents to generate technical analyses or perform quick queries on DuckDB:")

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_prompt := st.chat_input("For example: What is the stance of the 3 agents for Apple today?"):
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        try:
            res = requests.post(f"{API_URL}/api/chat", json={"message": user_prompt})
            if res.status_code == 200:
                bot_reply = res.json().get("response", "Unanswered.")
            else:
                bot_reply = "Error processing message with multi-agent system."
        except Exception:
            bot_reply = "⚠️ Critical error: The FastAPI backend (port 8000) is not responding."

        with st.chat_message("assistant"):
            st.markdown(bot_reply)
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
