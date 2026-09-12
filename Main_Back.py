import os
import random
import requests
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

@app.get("/api/dashboard/real")
def get_real_dashboard():
    params = {"key": NESSIE_API_KEY}
    
    cust_res = requests.get(f"{NESSIE_URL}/customers", params=params, timeout=3)
    if cust_res.status_code != 200 or not cust_res.json():
        return {"error": "No se pudieron obtener clientes de Nessie."}
    
    customers_list = cust_res.json()
    
    # Seleccionamos un cliente al azar de la lista para tener variedad en cada clic
    selected_customer = random.choice(customers_list)
    customer_id = selected_customer["_id"]

    # Obtener cuentas del cliente seleccionado
    acc_res = requests.get(f"{NESSIE_URL}/customers/{customer_id}/accounts", params=params, timeout=2)
    selected_accounts = acc_res.json() if acc_res.status_code == 200 and len(acc_res.json()) > 0 else []

    # Si el cliente elegido no tiene cuentas, asignamos datos de demostración
    if not selected_accounts:
        selected_accounts = [{"balance": round(random.uniform(500, 3500), 2), "type": "Checking"}]
        selected_purchases = [
            {"medium": "balance", "amount": 85.20, "description": "Supermercado"},
            {"medium": "balance", "amount": 45.00, "description": "Restaurante"},
            {"medium": "balance", "amount": 15.50, "description": "Cafetería"}
        ]
    else:
        account_id = selected_accounts[0]["_id"]
        pur_res = requests.get(f"{NESSIE_URL}/accounts/{account_id}/purchases", params=params, timeout=2)
        if pur_res.status_code == 200 and len(pur_res.json()) > 0:
            selected_purchases = pur_res.json()
        else:
            selected_purchases = [
                {"medium": "balance", "amount": 110.00, "description": "Amazon"},
                {"medium": "balance", "amount": 55.00, "description": "Gasolinera"},
                {"medium": "balance", "amount": 24.99, "description": "Suscripción Digital"}
            ]

    # Prompt para Gemini
    prompt = f"""
    Eres un asesor financiero experto de Capital One. Analiza los datos del usuario:
    Cliente: {selected_customer.get('first_name')} {selected_customer.get('last_name')}
    Cuentas: {selected_accounts}
    Últimas Compras: {selected_purchases}

    Da una recomendación ejecutiva de 2 a 3 oraciones sobre sus hábitos de consumo y su salud financiera.
    """
    
    try:
        if client:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=prompt
            )
            ai_data = response.text
        else:
            ai_data = f"Análisis Financiero: El cliente {selected_customer.get('first_name')} registra un saldo de ${selected_accounts[0]['balance']} USD."
    except Exception:
        ai_data = (
            f"Diagnóstico Inteligente (CapitalOne AI): El usuario {selected_customer.get('first_name')} {selected_customer.get('last_name')} "
            f"mantiene un saldo de ${selected_accounts[0]['balance']} USD. Se observa una liquidez estable "
            f"con capacidad para destinar un porcentaje a instrumentos de ahorro."
        )

    return {
        "customer": selected_customer,
        "accounts": selected_accounts,
        "purchases": selected_purchases,
        "analysis": ai_data
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Main_Back:app", host="127.0.0.1", port=8000, reload=True)