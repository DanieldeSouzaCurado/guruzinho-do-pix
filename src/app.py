import streamlit as st
import google.generativeai as genai
import pandas as pd
import json
import os
from dotenv import load_dotenv

# 1. Carregar variáveis de ambiente (API Key)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Cravando exatamente o modelo que o Google pediu no erro!
modelo_escolhido = "gemini-3.6-flash"
model = genai.GenerativeModel(modelo_escolhido)

# 2. Configurações da Página Streamlit
st.set_page_config(page_title="Guruzinho do Pix", page_icon="🤎", layout="centered")

# --- ANIMAÇÃO DE FUNDO: JORNAIS DO GURUZINHO ---
css_jornais = """
<style>
/* Container fantasma: fica na frente (z-index: 999) mas ignora o mouse (pointer-events: none) */
.bg-jornais {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 999; 
    pointer-events: none; 
    overflow: hidden;
    opacity: 0.20; /* Ajustei um pouquinho para dar mais destaque */
}

/* Estilo do jornalzinho de papel */
.jornal {
    position: absolute;
    font-family: 'Courier New', Courier, monospace;
    background: #fcf5e5;
    color: #000;
    padding: 15px;
    border: 2px solid #555;
    border-radius: 5px;
    box-shadow: 4px 4px 0px rgba(0,0,0,0.8);
    font-size: 14px;
    font-weight: bold;
    width: 220px;
    text-align: center;
}

/* Animações: Subindo e descendo */
@keyframes subir {
    0% { transform: translateY(110vh) rotate(-10deg); }
    100% { transform: translateY(-30vh) rotate(15deg); }
}

@keyframes descer {
    0% { transform: translateY(-30vh) rotate(10deg); }
    100% { transform: translateY(110vh) rotate(-15deg); }
}

/* Posições na tela */
.j1 { left: 2%; animation: subir 15s linear infinite; }
.j2 { left: 20%; animation: descer 20s linear infinite 2s; }
.j3 { right: 20%; animation: subir 18s linear infinite 5s; }
.j4 { right: 2%; animation: descer 22s linear infinite 1s; }
</style>

<div class="bg-jornais">
    <div class="jornal j1">📰 EXTRA: Guruzinho desmaia ao ver fatura!</div>
    <div class="jornal j2">📰 URGENTE: Jovem gasta tudo em skin e choca a economia!</div>
    <div class="jornal j3">📰 CAOS: Capivara declara falência emocional.</div>
    <div class="jornal j4">📰 GOLPE? Prometeu economizar, mas era mentira!</div>
</div>
"""
st.markdown(css_jornais, unsafe_allow_html=True)
# ----------------------------------------------

# Adiciona a imagem gigante no topo do aplicativo
st.image("logo.jpg", use_container_width=True)

# Truque com HTML para centralizar o Título e o Subtítulo
st.markdown("<h1 style='text-align: center;'>Guruzinho do Pix</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 14px;'>O Seu Guru Financeiro</p>", unsafe_allow_html=True)

# 3. Função para carregar os dados
@st.cache_data
def carregar_dados():
    with open('data/perfil_usuario.json', 'r', encoding='utf-8') as f:
        perfil = json.load(f)
    with open('data/dicionario_guruzinho.json', 'r', encoding='utf-8') as f:
        dicionario = json.load(f)
    historico = pd.read_csv('data/historico_despesas.csv')
    return perfil, dicionario, historico

perfil, dicionario, historico = carregar_dados()

# 4. Construir o Contexto (Injetado diretamente para compatibilidade universal)
contexto_dados = f"""
[INSTRUÇÃO ESTRITA: Você é o Guruzinho do Pix, uma capivara exausta e sarcástica.]
Usuário: {perfil['dados_pessoais']['nome']} ({perfil['dados_pessoais']['idade']} anos).
Sonho: {perfil['dados_pessoais']['sonho_principal']}
Saldo atual: R$ {perfil['saude_financeira']['saldo_atual']}
Gírias obrigatórias: 'farmar aura', 'L colossal', 'bancar o NPC', 'F no chat'.
Regras: Nunca invente dados. Seja fofo, porém passivo-agressivo. Ancore as broncas financeiras no sonho do usuário.
Histórico de Gastos Recentes:
\n{historico.tail(3).to_string()}
-----------------------------------
MENSAGEM DO USUÁRIO: 
"""

# 5. Inicializar o histórico do chat na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Mensagem inicial do Guruzinho
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Oiii! 💖 Eu sou o Guruzinho do Pix. Sinceramente? Eu tava quase tirando um cochilo, mas o pedido de socorro do seu saldo bancário me deu insônia. ✨ Bora parar de bancar o NPC e começar a farmar aura hoje?"
    })

# 6. Exibir histórico de mensagens
for msg in st.session_state.messages:
    # Volta para o emoji nativo
    icone = "🦦" if msg["role"] == "assistant" else "🧑‍💻"
    with st.chat_message(msg["role"], avatar=icone):
        st.markdown(msg["content"])

# 7. Capturar nova mensagem do usuário
if prompt_usuario := st.chat_input("Conte um gasto ou peça ajuda..."):
    st.session_state.messages.append({"role": "user", "content": prompt_usuario})
    
    # Mostra a sua mensagem
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt_usuario)
        
    # Mostra a resposta do bot com o emoji da Capivara
    with st.chat_message("assistant", avatar="🦦"):
        historico_gemini = [
            {"role": "user", "parts": ["Oi, aja como o Guruzinho do Pix!"]},
            {"role": "model", "parts": ["Pode deixar! ✨"]}
        ]
        
        for m in st.session_state.messages[1:-1]:
            role_gemini = "user" if m["role"] == "user" else "model"
            historico_gemini.append({"role": role_gemini, "parts": [m["content"]]})
        
        chat = model.start_chat(history=historico_gemini)
        mensagem_final = contexto_dados + prompt_usuario
        
        try:
            resposta = chat.send_message(mensagem_final)
            st.markdown(resposta.text)
            st.session_state.messages.append({"role": "assistant", "content": resposta.text})
        except Exception as e:
            st.error(f"A capivara tropeçou no servidor do Google: {e}")