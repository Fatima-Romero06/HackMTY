import os
import random
import requests
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

NESSIE_API_KEY = "106eefad193d566bb81a53afef0618b2"
NESSIE_URL = "https://api.nessieisreal.com"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AQ.Ab8RN6LbQRC1vfs2NFlkMvMeWPzNvmT9uUV76FZxoSlcp5XMyw")

try:
    client = genai.Client(api_key=GEMINI_API_KEY)
except Exception:
    client = None

# Escenarios de prueba para el Fallback Dinámico
DYNAMIC_FALLBACK_SCENARIOS = [
    {
        "merchant": "CryptoExchange_X",
        "amount": 4850.00,
        "location": "IP Inusual / Proxy Foreign (VPN)",
        "type": "Transferencia de Alto Riesgo",
        "is_fraud": True
    },
    {
        "merchant": "Supermercado Local",
        "amount": 42.50,
        "location": "Terminal Física - León, MX",
        "type": "Compra Habitual en Tienda",
        "is_fraud": False
    },
    {
        "merchant": "Electronics Store Online",
        "amount": 1250.00,
        "location": "IP Inusual (Lagos, NG)",
        "type": "Compra e-Commerce Internacional",
        "is_fraud": True
    },
    {
        "merchant": "Gasolinera Pemex",
        "amount": 35.00,
        "location": "Terminal Física - León, MX",
        "type": "Compra Habitual Gasolina",
        "is_fraud": False
    }
]

@app.get("/api/dashboard/real")
def get_security_sentinel():
    params = {"key": NESSIE_API_KEY}
    
    selected_customer = {"first_name": "Usuario", "last_name": "Demo", "_id": "demo_id"}
    tx = None
    data_source = "FALLBACK_GENERATOR"

    # 1. Intentar consultar datos de Nessie API
    try:
        cust_res = requests.get(f"{NESSIE_URL}/customers", params=params, timeout=3)
        if cust_res.status_code == 200 and cust_res.json():
            customers_list = cust_res.json()
            selected_customer = random.choice(customers_list)
            customer_id = selected_customer.get("_id")

            # Intentar obtener cuentas
            acc_res = requests.get(f"{NESSIE_URL}/customers/{customer_id}/accounts", params=params, timeout=3)
            if acc_res.status_code == 200 and acc_res.json():
                accounts = acc_res.json()
                account_id = accounts[0].get("_id")

                # Intentar obtener compras reales
                p_res = requests.get(f"{NESSIE_URL}/accounts/{account_id}/purchases", params=params, timeout=3)
                if p_res.status_code == 200 and isinstance(p_res.json(), list) and len(p_res.json()) > 0:
                    raw_tx = random.choice(p_res.json())
                    tx = {
                        "merchant": raw_tx.get("description", "Comercio Registrado"),
                        "amount": float(raw_tx.get("amount", 100.0)),
                        "location": f"Merchant ID: {raw_tx.get('merchant_id', 'N/A')}",
                        "type": f"Estado: {raw_tx.get('status', 'completed')}"
                    }
                    data_source = "NESSIE_REAL_DATABASE"
    except Exception as e:
        print(f"Aviso: Fallo conexión Nessie, usando fallback. Error: {e}")

    # 2. Si no había compras en Nessie o falló la API, activar el Fallback Dinámico
    if not tx:
        tx = random.choice(DYNAMIC_FALLBACK_SCENARIOS)

    # 3. Prompt para Gemini 3.6 Flash
    customer_name = f"{selected_customer.get('first_name')} {selected_customer.get('last_name')}"
    prompt = f"""
    Eres un motor de Detección de Anomalías e Inteligencia de Amenazas Bancarias (SOC Sentinel).
    Analiza la siguiente transacción en tiempo real:

    Usuario: {customer_name} (ID: {selected_customer.get('_id')})
    Comercio Target: {tx['merchant']}
    Monto: ${tx['amount']} USD
    Ubicación / Origen: {tx['location']}
    Tipo de Operación: {tx['type']}

    Responde ESTRICTAMENTE con esta estructura:
    1. NIVEL DE RIESGO: [ALTO / MEDIO / BAJO]
    2. SCORE DE RIESGO: [Número de 0 a 100]
    3. ACCIÓN RECOMENDADA: [BLOQUEAR CUENTA / SOLICITAR 2FA / APROBAR]
    4. ANÁLISIS DE ANOMALÍA: (Breve explicación técnica de 2 oraciones sobre por qué representa o no un riesgo).
    """

    # 4. Evaluación de Gemini
    try:
        if client:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=prompt
            )
            ai_analysis = response.text
        else:
            ai_analysis = "Error: Cliente Gemini no configurado."
    except Exception as e:
        # Fallback de respuesta de IA si falla la API key de Gemini
        risk_level = "ALTO" if tx.get("amount", 0) > 500 else "BAJO"
        score = 88 if risk_level == "ALTO" else 12
        ai_analysis = (
            f"NIVEL DE RIESGO: {risk_level}\n"
            f"SCORE DE RIESGO: {score}/100\n"
            f"ACCIÓN RECOMENDADA: {'SOLICITAR 2FA' if risk_level == 'ALTO' else 'APROBAR'}\n"
            f"ANÁLISIS DE ANOMALÍA: Evaluación ejecutada en modo contingencia. Se detectó actividad para el usuario {customer_name} con monto de ${tx['amount']} USD."
        )

    return {
        "customer": customer_name,
        "transaction": tx,
        "data_source": data_source,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "analysis": ai_analysis
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Main_Back:app", host="127.0.0.1", port=8000, reload=True)