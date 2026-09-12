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

# Lista de PyMEs simuladas para dar contexto B2B
BUSINESS_NAMES = [
    "TechCraft Solutions (Software)",
    "Panadería El Molino (Retail)",
    "Logística del Norte (Servicios)",
    "Café & Co. (Restaurantero)"
]

@app.get("/api/dashboard/real")
def get_real_dashboard():
    params = {"key": NESSIE_API_KEY}
    
    cust_res = requests.get(f"{NESSIE_URL}/customers", params=params, timeout=3)
    customers_list = cust_res.json() if cust_res.status_code == 200 and cust_res.json() else []
    
    # Datos simulados de negocio si falla Nessie
    business_name = random.choice(BUSINESS_NAMES)
    
    # Calculamos finanzas de PyME (Capital Líquido y Buffer)
    total_revenue = round(random.uniform(15000, 45000), 2)
    total_expenses = round(random.uniform(8000, 22000), 2)
    liquid_capital = round(total_revenue - total_expenses, 2)
    capital_buffer_target = round(total_expenses * 3, 2) # Buffer recomendado: 3 meses de operacion
    buffer_coverage = round((liquid_capital / capital_buffer_target) * 100, 1) if capital_buffer_target > 0 else 0

    # Compras/Gastos recientes
    selected_purchases = [
        {"vendor": "Proveedor de Materia Prima", "category": "Inventario", "amount": 4200.00, "date": "2026-03-01"},
        {"vendor": "Servicios de Nube / AWS", "category": "Tecnología", "amount": 850.50, "date": "2026-03-02"},
        {"vendor": "Renta de Local Comercial", "category": "Fijo", "amount": 3500.00, "date": "2026-03-03"},
        {"vendor": "Nómina Temporal", "category": "Operación", "amount": 2900.00, "date": "2026-03-04"}
    ]

    # Prompt enfocado a B2B y Tesorería
    prompt = f"""
    Eres un CFO Virtual experto para PyMEs. Analiza el estado financiero del negocio:
    Empresa: {business_name}
    Ingresos Mensuales: ${total_revenue} USD
    Gastos Mensuales: ${total_expenses} USD
    Capital Líquido Disponible: ${liquid_capital} USD
    Meta de Capital Buffer (Reserva de Emergencia): ${capital_buffer_target} USD (Cobertura actual: {buffer_coverage}%)
    Gastos recientes: {selected_purchases}

    Proporciona un diagnóstico ejecutivo breve (3 oraciones máximo):
    1. Evalúa si el Capital Líquido y el Capital Buffer son adecuados para mantener la operación.
    2. Da una recomendación concreta de acción o inversión inmediata para optimizar la tesorería.
    """
    
    try:
        if client:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=prompt
            )
            ai_data = response.text
        else:
            ai_data = f"Diagnóstico de Tesorería: La empresa {business_name} cuenta con un capital líquido de ${liquid_capital} USD."
    except Exception:
        ai_data = (
            f"Diagnóstico B2B (CapitalOne AI): {business_name} mantiene una liquidez saludable de ${liquid_capital} USD. "
            f"Su Capital Buffer cubre un {buffer_coverage}% de la reserva recomendada de 3 meses de operación. "
            f"Se sugiere mover $2,000 USD sobrantes a un fondo de inversión líquida a corto plazo."
        )

    return {
        "business_name": business_name,
        "metrics": {
            "revenue": total_revenue,
            "expenses": total_expenses,
            "liquid_capital": liquid_capital,
            "capital_buffer_target": capital_buffer_target,
            "buffer_coverage": buffer_coverage
        },
        "purchases": selected_purchases,
        "analysis": ai_data
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Main_Back:app", host="127.0.0.1", port=8000, reload=True)