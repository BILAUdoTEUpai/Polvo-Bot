
import discord
from discord import app_commands
import random
from datetime import datetime

class Cliente(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.synced = False
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync()  # comandos globais
            self.synced = True
        print(f"✅ Bot conectado como {self.user}")

aclient = Cliente()
tree = aclient.tree

@tree.command(name='teste', description='Testando')
async def teste(interaction: discord.Interaction):
    await interaction.response.send_message("Estou funcionando!", ephemeral=True)

@tree.command(name='ping', description='Veja a latência do bot')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! Latência: {round(aclient.latency * 1000)}ms', ephemeral=True)

@tree.command(name='avatar', description='Veja o avatar de um usuário')
async def avatar(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f'Avatar de {user.mention}: {user.avatar.url}', ephemeral=True)

@tree.command(name='userinfo', description='Veja informações de um usuário')
async def userinfo(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f'Nome: {user.name}\nID: {user.id}\nCriado em: {user.created_at}', ephemeral=True)

@tree.command(name='say', description='Faça o bot repetir sua mensagem')
async def say(interaction: discord.Interaction, mensagem: str):
    await interaction.response.send_message(mensagem)

@tree.command(name='dado', description='Jogue um dado de 6 lados')
async def dado(interaction: discord.Interaction):
    resultado = random.randint(1, 6)
    await interaction.response.send_message(f'Você rolou: {resultado}', ephemeral=True)

@tree.command(name='motivar', description='Receba uma frase motivacional')
async def motivar(interaction: discord.Interaction):
    frases = ["Você consegue!", "Não desista!", "Acredite em você!", "Cada dia é uma nova chance."]
    await interaction.response.send_message(random.choice(frases), ephemeral=True)

@tree.command(name='tempo', description='Veja que horas são')
async def tempo(interaction: discord.Interaction):
    agora = datetime.now().strftime("%H:%M:%S")
    await interaction.response.send_message(f'Hora atual: {agora}', ephemeral=True)

@tree.command(name='inverter', description='Inverter o texto enviado')
async def inverter(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message(texto[::-1], ephemeral=True)

@tree.command(name='calcular', description='Soma dois números')
async def calcular(interaction: discord.Interaction, a: int, b: int):
    await interaction.response.send_message(f'A soma é: {a + b}', ephemeral=True)

@tree.command(name='embed', description='Criar uma embed personalizada')
async def embed(interaction: discord.Interaction, titulo: str, descricao: str, cor: str):
    try:
        cor_convertida = int(cor.replace("#", ""), 16)
        emb = discord.Embed(title=titulo, description=descricao, color=cor_convertida)
        await interaction.response.send_message(embed=emb)
    except ValueError:
        await interaction.response.send_message("Cor inválida. Use formato hexadecimal, ex: `#00ff00`.", ephemeral=True)

# Adicione mais comandos aqui se quiser

from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return '<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Polvo Bot website</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: #0f0f0f;
      color: #f5f5f5;
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      text-align: center;
      overflow-x: hidden;
    }

    h1, p, .btn {
      opacity: 0;
      transform: translateY(20px);
      animation: fadeInUp 0.8s forwards;
    }

    h1 {
      font-size: 3em;
      margin-bottom: 0.2em;
      animation-delay: 0.2s;
    }

    p {
      font-size: 1.3em;
      margin-bottom: 2em;
      color: #cccccc;
      animation-delay: 0.4s;
    }

    .btn {
      background-color: #1e88e5;
      border: none;
      color: white;
      padding: 15px 30px;
      font-size: 1em;
      border-radius: 12px;
      cursor: pointer;
      transition: transform 0.2s ease, background 0.3s ease;
      margin: 10px;
      width: 250px;
    }

    .btn:hover {
      background-color: #1565c0;
      transform: scale(1.05);
    }

    .btn:nth-of-type(1) { animation-delay: 0.6s; }
    .btn:nth-of-type(2) { animation-delay: 0.8s; }
    .btn:nth-of-type(3) { animation-delay: 1s; }

    @keyframes fadeInUp {
      0% {
        opacity: 0;
        transform: translateY(20px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .footer {
      margin-top: 3em;
      font-size: 0.9em;
      color: #666;
      animation: fadeInUp 0.8s forwards;
      animation-delay: 1.2s;
      opacity: 0;
    }
  </style>
</head>
<body>
  <h1>Polvo Bot  🚀</h1>
  <p>meus tentaculos protegem seu servidor!</p>

  <button class="btn" onclick="copyScript()">📋 Copiar comandos</button>
  <button class="btn" onclick="baixarExecutor()">📥 me adicione!</button>
  <button class="btn" onclick="entrarDiscord()">💬 Discord do dono do bot</button>

  <div class="footer">Feito por phgs2456 • 2025</div>

  <script>
    function copyScript() {
      const script = `vo te falar comando nenhum não caba safado se vira adiciona o bot e vê`;
      navigator.clipboard.writeText(script).then(() => {
        alert("comandos copiado para a área de transferência!");
      });
    }

    function baixarExecutor() {
      window.open("https://discord.com/oauth2/authorize?client_id=1385440863408095294&permissions=8&integration_type=0&scope=bot+applications.commands", "_blank");
    }

    function entrarDiscord() {
      window.open("https://discord.gg/8KyfehGUnT", "_blank"); // Troque por seu link real
    }

    // 🚨 Webhook: Notifica o Discord quando alguém entra no site
    fetch("https://discord.com/api/webhooks/1383861604952571985/g661lVIZpJOXtnLDcyXg52QhDqy5GG3h4dR3e96IPijBMmBnGnRCZn4JfkTGxxZ0lKBU", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        content: `🚨 polvo bot notifica Alguém entrou no site do polvo bot!\n📅 ${new Date().toLocaleDateString()} ⏰ ${new Date().toLocaleTimeString()}`
      })
    });
  </script>
</body>
</html>
'

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Iniciar o Flask em uma thread separada
threading.Thread(target=run_flask).start()

import os
aclient.run(os.environ['DISCORD_TOKEN'])
