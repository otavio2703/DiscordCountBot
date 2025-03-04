import discord
import json
import os
import csv
from discord import Intents

# Configurações
TOKEN = ""
CHANNEL_ID = 
DIRETORIO_VMIX = r"C:\Users\otavio\Downloads\dados"
ARQUIVO_JSON = os.path.join(DIRETORIO_VMIX, "vmix_data.json")
ARQUIVO_CSV = os.path.join(DIRETORIO_VMIX, "votacao.csv")

# Verificar/Criar diretório e arquivos
if not os.path.exists(DIRETORIO_VMIX):
    os.makedirs(DIRETORIO_VMIX)

# Inicializar JSON com estrutura de tabela
if not os.path.exists(ARQUIVO_JSON):
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump([
            {"Opção": "Apenas um Show", "Votos": 0, "Porcentagem": "0.0%"},
            {"Opção": "Gravity Falls", "Votos": 0, "Porcentagem": "0.0%"}
        ], f, indent=4, ensure_ascii=False)

# Inicializar CSV
if not os.path.exists(ARQUIVO_CSV):
    with open(ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Opção", "Votos", "Porcentagem"])
        writer.writerow(["Apenas um Show", 0, "0.0%"])
        writer.writerow(["Gravity Falls", 0, "0.0%"])

def atualizar_votos(opcao):
    # Atualizar JSON
    with open(ARQUIVO_JSON, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        
        # Converter estrutura antiga para nova se necessário
        if isinstance(data, dict):
            data = [
                {"Opção": "Apenas um Show", "Votos": data.get("Opção 1", {}).get("votos", 0), "Porcentagem": f"{data.get('Opção 1', {}).get('porcentagem', 0.0):.1f}%"},
                {"Opção": "Gravity Falls", "Votos": data.get("Opção 2", {}).get("votos", 0), "Porcentagem": f"{data.get('Opção 2', {}).get('porcentagem', 0.0):.1f}%"}
            ]
        
        # Atualizar votos
        for item in data:
            if item["Opção"] == opcao:
                item["Votos"] += 1
        
        # Calcular porcentagens
        total = sum(item["Votos"] for item in data)
        for item in data:
            porcentagem = (item["Votos"] / total * 100) if total > 0 else 0.0
            item["Porcentagem"] = f"{porcentagem:.1f}%"
        
        # Salvar JSON
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()

    # Atualizar CSV
    with open(ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Opção", "Votos", "Porcentagem"])
        for item in data:
            writer.writerow([item["Opção"], item["Votos"], item["Porcentagem"]])

    return data

intents = Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == CHANNEL_ID:
        # Normalizar o texto para comparação
        conteudo = message.content.strip().upper().replace(" ", "").translate(
            str.maketrans("ÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜÝ", "AAAAAAEEEEIIIIOOOOOUUUUY")
        )
        
        # Mapear comandos
        opcao = None
        if any(palavra in conteudo for palavra in ["APS", "APENASUMSHOW", "APENAUMSHOW", "Apénas um Show", "Apenas um Xou" , "Apenas um sho", "Apena um Show", "Apenas um Shou", "Apenas um Shouw", "Apenaz um Show", "Apenas un Show", "aps"]):
            opcao = "Apenas um Show"
        elif any(palavra in conteudo for palavra in ["GF", "gravity", "Gravity", "gf", "gravityfalls", "gravity Falls"]):
            opcao = "Gravity Falls" 
        
        if opcao:
            dados_atualizados = atualizar_votos(opcao)
            
            # Enviar confirmação
            await message.reply(f"Voto em **{opcao}** registrado! 🎉")
            
            # Log detalhado
            print(f"\n[VOTO] {message.author.name}: {opcao}")
            print("-" * 30)
            for item in dados_atualizados:
                print(f"{item['Opção']}: {item['Votos']} votos ({item['Porcentagem']})")
            print()

client.run(TOKEN)
