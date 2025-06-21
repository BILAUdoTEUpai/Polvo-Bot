
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

import os
bot.run(os.environ['DISCORD_TOKEN'])
