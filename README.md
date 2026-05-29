# 📈 AlphaAgent — Multi-Agent Trading Web Application

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Deployment - Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=flat-square&logo=render&logoColor=white)](https://render.com/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

**AlphaAgent** es una plataforma analítica SaaS orientada al mercado financiero que implementa una arquitectura jerárquica multi-agente de Inteligencia Artificial para el análisis técnico y la toma de decisiones de inversión automatizadas. El sistema simula un Comité Corporativo de Inversión dividiendo la carga cognitiva en capas especializadas (Análisis Básico, Análisis Avanzado y Dirección de Portafolio).

## 🔗 Enlaces del Proyecto

* **Repositorio GitHub:** [multi-agent-trading-web-application-WebApp-](https://github.com/jwanxanqak/multi-agent-trading-web-application-WebApp-/tree/main)
* **Aplicación en Vivo (Frontend):** [AlphaAgent Web Dashboard](https://multi-agent-trading-web-application-c44n.onrender.com/)
* **Servicio de Producción (Backend API):** [AlphaAgent API Core](https://multi-agent-trading-web-application.onrender.com/)

---

## 🏗️ Arquitectura del Sistema y Capas Agénticas

La plataforma descentraliza el flujo analítico mediante tres entidades lógicas pre-procesadas en un almacén de caché optimizado (`agent_cache.json`):

1.  **Basic Analysis Agent:** Evalúa tendencias de corto plazo (ventanas de 15 días), calcula rangos promedio de volatilidad diaria y analiza la correlación entre la acción del precio y las divergencias de volumen transaccional básico.
2.  **Advanced Analysis Agent:** Procesa ventanas temporales extendidas e infiere dinámicamente el comportamiento de indicadores técnicos estandarizados como medias móviles simples (SMA_10, SMA_20) y el Índice de Fuerza Relativa (RSI_14) para identificar zonas de sobrecompra o sobreventa.
3.  **Portfolio Manager Agent (Consolidador):** Actúa como el filtro supervisor. Modera las discrepancias analíticas entre los agentes de soporte e integra políticas corporativas para emitir una recomendación final unificada (`BUY`, `HOLD`, `SELL`) con su debida justificación ejecutiva.

---

## ⚡ Características Clave

* **Arquitectura Desacoplada (Decoupled SaaS):** Backend construido sobre una API REST robusta y asíncrona con FastAPI, y un Frontend interactivo de alta disponibilidad implementado con Streamlit.
* **Análisis Técnico Estructurado:** Extracción automatizada de métricas clave, sugerencias detalladas para la generación de gráficos (series temporales, histogramas de volumen) y reportes automatizados en formato JSON.
* **Control de Riesgo y Simulación de Umbrales:** Módulo frontend dedicado al monitoreo visual de métricas de mitigación de riesgo financiero (ej. umbrales de exposición máxima).
* **Consola de Comité Agéntico (Interactive Chat):** Chat interactivo simulado que permite interrogar dinámicamente el criterio técnico del comité de agentes de IA para activos seleccionados.

---

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.11, FastAPI, Pydantic v2 (Validación de tipos de datos de entrada).
* **Frontend:** Streamlit, Requests (Consumo asíncrono de microservicios).
* **Persistencia Analítica:** Caché estructurado JSON optimizado para la eliminación de redundancias de tokens y latencia de inferencia.
* **DevOps / Infraestructura:** Render Blueprint Spec (`render.yaml`), Uvicorn (ASGI Web Server).

---
## 📁 Estructura del Repositorio

```text
├── agent_cache.json   # Base de conocimiento estructurada con análisis técnicos pre-calculados.
├── app.py             # Frontend interactivo construido en Streamlit (Monitor, Riesgo y Chat).
├── main.py            # Orquestador del Backend (FastAPI Core) con enrutamiento de señales y chat.
├── render.yaml        # Infraestructura como Código (IaC) para el despliegue orquestado en la nube.
└── requirements.txt   # Manifiesto de dependencias con versiones fijadas para producción.
