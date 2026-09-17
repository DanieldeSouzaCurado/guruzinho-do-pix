# 💸 Guruzinho do Pix
> "Porque a sua vida financeira não tem botão de *respawn*."

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![Gemini](https://img.shields.io/badge/Google_Gemini-Generative_AI-8E75B2)

Projeto final desenvolvido para o **Bootcamp Bradesco - GenAI, Dados & Cyber**, em parceria com a **DIO**. O Guruzinho do Pix é um assistente financeiro virtual (MVP) alimentado por Inteligência Artificial Generativa, criado para combater o analfabetismo financeiro da Geração Z através de gamificação, sarcasmo e empatia reversa.

🌐 **[Acesse a aplicação rodando em nuvem aqui!](https://guruzinho-do-pix.streamlit.app/)**

---

## 🎯 O Problema
A educação financeira tradicional falhou com os adolescentes. Dados recentes expõem uma crise silenciosa:
* **PISA (2024):** 45% dos adolescentes brasileiros sofrem de analfabetismo financeiro.
* **CNDL e SPC Brasil (2025):** 47% da Geração Z não controla suas finanças.
* **Os motivos:** Preguiça (18%), não saber como fazer (19%) ou continuar usando métodos obsoletos como bloquinhos de papel (26%). 

Ferramentas bancárias com gráficos de pizza e jargões não funcionam para quem toma decisões baseadas em *trends* do TikTok. Eles estão vivendo no piloto automático, bancando o "NPC" da própria vida.

## 💡 A Solução (A Persona)
Em vez de um gerente engravatado, criamos uma **capivara exausta e implacavelmente sarcástica**. 

O Guruzinho fala a língua dos adolescentes (entende o que é *farmar aura*, *tankar*, *tomar um L colossal*) e não poupa palavras na hora de dar broncas. O grande diferencial técnico é o sistema de **Ancoragem de Sonhos**: a IA cruza o histórico de despesas com o maior objetivo de vida do usuário, mostrando o impacto real de uma decisão impulsiva.

⚠️ **Contexto do MVP (Modo de Teste):**
> O sistema atual está configurado em formato de demonstração para um usuário fixo: **Daniel**, 15 anos, aluno do 9º ano, que sonha em ir ao *Rock in Rio* e comprar o *GTA 6* no lançamento, mas possui finanças desastrosas. Teste a paciência da capivara informando gastos supérfluos!

---

## ⚙️ Funcionalidades
- **Chatbot Imersivo:** Integração com a API do Google Gemini, utilizando Prompt Engineering avançado para manter a persona sarcástica sem perder o caráter educativo.
- **Memória de Contexto:** A IA lembra dos seus sonhos e puxa o seu histórico de vacilos financeiros para te dar broncas personalizadas.
- **Caos Visual (UI/UX):** Injeção de HTML/CSS customizado no Streamlit para criar animações de fundo (manchetes de jornais flutuantes que anunciam a "falência" do usuário).

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem Principal:** Python
- **Inteligência Artificial:** Google Gemini API (LLM)
- **Framework Web:** Streamlit
- **Estilização:** CSS / HTML (injetado via Markdown)
- **Deploy:** Streamlit Community Cloud
- **Conceitos Aplicados (Bootcamp Bradesco):** Modelagem de Bancos de Dados Relacionais, SQL, Python, Lógica de Machine Learning para detecção de fraudes e fundamentos de Cibersegurança.

---

## 🚀 Como rodar o projeto localmente

Se você quiser clonar o repositório e rodar o Guruzinho na sua própria máquina, siga os passos abaixo:

### 1. Pré-requisitos
* Python 3.10 ou superior instalado.
* Uma chave de API gratuita do [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Instalação
Clone este repositório e acesse a pasta do projeto:
```bash
git clone [https://github.com/SEU_USUARIO/guruzinho-do-pix.git](https://github.com/SEU_USUARIO/guruzinho-do-pix.git)
cd guruzinho-do-pix
