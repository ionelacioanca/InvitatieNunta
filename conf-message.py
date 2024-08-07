from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Tokenul botului de la @BotFather
TELEGRAM_BOT_TOKEN = '7345913311:AAG5pjU2d7mSML1ds-9yr8lme7GjI-zmE_E'
# ID-ul chatului (de exemplu, un grup sau o persoană)
TELEGRAM_CHAT_ID = '5960470289'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'  # pentru a folosi formatarea HTML în mesaj
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.json
    print('Received data:', data)  # Adaugă acest print pentru a vedea ce date sunt primite

    # Verifică dacă datele sunt corect primite
    if not data:
        return "No data received", 400
    data = request.json
    name = data.get('name', 'N/A')
    phone = data.get('phone', 'N/A')
    attending = 'DA' if data.get('attending') else 'NU'
    accommodation = 'DA' if data.get('accommodation') else 'NU'
    companions = 'DA' if data.get('companions') else 'NU'
    children = 'DA' if data.get('children') else 'NU'

    # Valorile implicite pentru numărul de persoane
    num_adults = int(data.get('num_adults', 0))  # asigură-te că valorile sunt numere
    num_children = int(data.get('num_children', 0))  # asigură-te că valorile sunt numere
    custom_message = data.get('custom_message', '')  # Mesajul personalizat
    
    # Calculăm numărul total de persoane
    if companions == 'DA':
        nr_guests = num_adults + num_children
    else:
        nr_guests = 0

    message = (
        f"Confirmare Invitație\n"
        f"Nume: {name}\n"
        f"Telefon: {phone}\n"
        f"Participare: {attending}\n"
        f"Cazare: {accommodation}\n"
        f"Însoțitori: {companions}\n"
        f"Copii: {children}\n"
        f"Număr total persoane: {nr_guests}\n"
        f"Număr adulți: {num_adults}\n"
        f"Număr copii: {num_children}\n"
        f"Mesaj personalizat: {custom_message}"
    )

    response = send_telegram_message(message)
    return response

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=5001, debug=True)
    app.run(host="0.0.0.0", port=5001, debug=True)