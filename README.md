# 🧠 Factorial API Assistant (Demo)

Este proyecto te ayuda a aprender y practicar la integración con la API demo de Factorial usando Python, OAuth2, Flask, SQLite y webhooks.

---

## 🚀 ¿Qué hace este proyecto?

- Se conecta a la API pública de demo de Factorial (`https://api.demo.factorial.dev`)
- Autentica mediante OAuth2 y refresca tokens automáticamente
- Crea una suscripción a un webhook (por ejemplo: creación de empleados)
- Escucha el webhook con un servidor Flask
- Guarda la información recibida en una base de datos SQLite
- Usa ngrok para exponer el servidor local y recibir los callbacks

---

## 🛠️ Requisitos

- Python 3.10+
- [Ngrok](https://ngrok.com/download) (para exponer localmente tu servidor Flask)
- GitHub Codespaces o entorno local con terminal habilitada

---

## 📁 Estructura del proyecto

├── app.py # Servidor Flask que escucha webhooks
├── token_manager.py # Módulo para gestionar el token OAuth2
├── empleados.db # Base de datos SQLite
├── start_ngrok.sh # Script para iniciar ngrok automáticamente
├── oauth_token.json # Archivo donde se guardan los tokens
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo


---

## 🔐 Autenticación OAuth2

1. Ir a:  
   `https://api.demo.factorial.dev/oauth/authorize?client_id=<CLIENT_ID>&redirect_uri=<REDIRECT_URI>&response_type=code`

2. Copiar el `authorization_code` y usar `token_manager.py` para obtener tu access token.

3. El access token se guarda en `oauth_token.json` y se refresca automáticamente.

---

## 🪝 Webhook de ejemplo: empleados con contrato

Este webhook te notificará cuando se cree un nuevo empleado con contrato:

- `subscription_type`: `employees/employee/create_with_contract`
- `target_url`: La URL generada por ngrok (ej: `https://abcd1234.ngrok-free.app/webhook/empleado`)

---

## 🧪 Cómo probar localmente

1. Levanta el servidor Flask:
   ```bash
   python app.py
./start_ngrok.sh



from token_manager import get_valid_token
# usa requests.post para crear la suscripción con el token y el target_url

