from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Polvo-Bot está rodando com sucesso!"

def run():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run).start()
