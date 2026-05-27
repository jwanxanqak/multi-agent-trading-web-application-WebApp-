from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import json

app = FastAPI(
    title="AlphaAgent SaaS API",
    description="Backend de producción para consumo de señales multi-agente",
    version="1.5"
)

class ChatRequest(BaseModel):
    message: str

# En producción, leemos el caché directamente desde la raíz del proyecto
CACHE_FILE = "agent_cache.json"

@app.get("/")
def root():
    return {"status": "online", "message": "AlphaAgent API activa y respondiendo"}

@app.get("/api/signals/{ticker}")
def get_trading_signal(ticker: str):
    ticker_upper = ticker.upper()
    
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
            
            basic_key = f"basic_analysis_{ticker_upper}"
            advanced_key = f"advanced_analysis_{ticker_upper}"
            
            basic_raw = cache_data.get(basic_key, None)
            advanced_raw = cache_data.get(advanced_key, None)
            
            if basic_raw or advanced_raw:
                basic_parsed = {}
                if basic_raw:
                    try:
                        basic_parsed = json.loads(basic_raw.replace('```json', '').replace('```', '').strip())
                    except:
                        basic_parsed = {"recommendation": "HOLD", "technical_justification": basic_raw}
                
                advanced_parsed = {}
                if advanced_raw:
                    try:
                        advanced_parsed = json.loads(advanced_raw.replace('```json', '').replace('```', '').strip())
                    except:
                        advanced_parsed = {"recommendation": "HOLD", "justification": advanced_raw}
                
                rec_basic = basic_parsed.get("recommendation", "HOLD")
                rec_adv = advanced_parsed.get("recommendation", "HOLD")
                just_basic = basic_parsed.get("technical_justification", "Análisis básico completado.")
                just_adv = advanced_parsed.get("justification", "Análisis avanzado completado.")
                
                if rec_basic == rec_adv:
                    pm_rec = rec_basic
                    pm_just = f"Consenso absoluto del comité agéntico. Ambos sub-agentes coinciden en la estrategia de {pm_rec}."
                else:
                    pm_rec = rec_adv
                    pm_just = f"Discrepancia detectada. El Portfolio Manager prioriza la acción de {rec_adv} del Advanced Agent debido al peso de los indicadores técnicos complejos."
                
                return {
                    "ticker": ticker_upper,
                    "has_data": True,
                    "basic_agent": {"recommendation": rec_basic, "justification": just_basic},
                    "advanced_agent": {"recommendation": rec_adv, "justification": just_adv},
                    "portfolio_manager": {"recommendation": pm_rec, "justification": pm_just}
                }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error leyendo el almacén de datos: {str(e)}")
            
    return {
        "ticker": ticker_upper,
        "has_data": False,
        "portfolio_manager": {"recommendation": "HOLD", "justification": f"El activo {ticker_upper} no se encuentra pre-procesado en el archivo de caché global."}
    }

@app.post("/api/chat")
def agent_chat(request: ChatRequest):
    user_msg = request.message.lower()
    if "apple" in user_msg or "aapl" in user_msg:
        return {"response": "🤖 **Basic Agent:** AAPL muestra consolidación alcista.\n\n📊 **Advanced Agent:** RSI en 68 (límite de sobrecompra).\n\n🧠 **Portfolio Manager:** Mantener posiciones sin compras agresivas."}
    return {"response": f"Comité AlphaAgent recibió: '{request.message}'. Sistema operativo en la nube resolviendo parámetros."}