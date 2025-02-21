# Sophia-bot

Chatbot inteligente para atendimento automatizado no Whatsapp.

## 📋 Funcionalidades

- Atendimento 24/7 automatizado via WhatsApp
- Resposta a dúvidas frequentes
- Suporte ao cliente com integração de IA

## 🚀 Funcionalidades Futuras

- **🎙️ Transcrição de Áudio**: 
  - Converter mensagens de áudio em texto
  - Processar e responder a comandos de voz

- **📁 Envio de Arquivos**: 
  - Suporte para receber e enviar diversos tipos de arquivos
  - Processamento de documentos, imagens e mídias

- **💾 Integração com Banco de Dados**: 
  - Consultas em tempo real
  - Armazenamento e recuperação de informações de clientes

- **💬 Gerenciamento de Conversas**: 
  - Salvar histórico de mensagens
  - Armazenar informações de contato dos clientes
  - Manter registro de interações anteriores

- **😊 Análise de Sentimento**: 
  - Identificar o tom e a emoção das mensagens
  - Adaptar respostas com base no contexto emocional

- **🤖 Personalização Avançada**: 
  - Aprendizado de preferências individuais
  - Respostas mais contextuais e personalizadas

## 🚀 Tecnologias Utilizadas

- Python 3.8+
- Flask
- OpenAI GPT
- Evolution API (WhatsApp)
- Natural Language Processing (NLP)
- Docker e Docker Compose

## 💻 Pré-requisitos

- Python 3.8+
- Docker e Docker Compose
  - Instalação no Windows:
    1. Baixe o Docker Desktop para Windows no site oficial
    2. Siga as instruções de instalação
    3. Reinicie o computador após a instalação
    4. Verifique a instalação com `docker --version` e `docker-compose --version`
- **Evolution API no Docker**
  - Instalar a Evolution API usando Docker
  - Configurar as credenciais e instância no `.env`
- Chave de API OpenAI
- Credenciais da Evolution API
- Dependências listadas em `requirements.txt`
- Copiar os arquivos `send_sandeco.py` e `message_sandeco.py` da pasta `minha_evolution` para o projeto. Caso não possua encontra-se no grupo CrewAI 2 - Intermediário.
 
## 📚 Material de Referência

- Aula 04 - EvolutionAPI: Envio e Recebimento de Mensagens (Mentoria CrewAI 2 - Nível Intermediário)


## 🚀 Tutorial de Instalação e Configuração

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/eudiegoaragao/sophia-bot.git
cd sophia-bot
```

### Passo 2: Configurar Variáveis de Ambiente

- Copie o arquivo `.env.example` para `.env`
- Edite as configurações conforme necessário

### Passo 3: Instalar Dependências

```bash
docker-compose build
```

### Passo 4: Iniciar o Projeto

```bash
docker-compose up -d
```

### Passo 5: Verificar Logs

```bash
docker-compose logs -f sophia-bot
```

OU no Docker.desktop vá até o container `sophia-bot` e logs: ![Verificar Logs](/docs/images/verificar-logs.png) &nbsp; ![Flask Rodando](/docs/images/flask_rodando.png) &nbsp; 

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/eudiegoaragao/sophia-bot.git
   cd sophia-bot
   ```

2. Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais:
   ```bash
   cp .env.example .env
   ```
   - **Importante**: No `.env`, `EVO_BASE_URL` use o IP do host, NÃO use `localhost`!
     - O `localhost` do Docker pode causar conflitos
     - Substitua por seu endereço IP real (ex: `192.168.1.100`)

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 🐳 Rodando com Docker

1. **Construa e inicie os containers**
   ```bash
   docker-compose up -d
   ```

2. **Verificando se está funcionando**
   - Acesse: http://localhost:5000
   - Deve retornar: 
     ```json
     {
       "message": "Sophia Bot funcionando!",
       "status": "success"
     }
     ```
   - Verifique os logs dos containers

3. **Parando os serviços**
   ```bash
   docker-compose down
   ```

## 🤖 Configuração do Prompt do Sistema

No arquivo `sophia_prompt.py`, substitua o texto `DIGITE SEU PROMPT AQUI` por um prompt personalizado que defina:

1. Identidade do Agente
2. Objetivo Principal
3. Regras de Comunicação
4. Fluxo de Conversa
5. Restrições e Limitações

### Dicas para Criação do Prompt
- Seja específico e detalhado
- Use linguagem clara e direta
- Defina o tom e o estilo de comunicação
- Considere o contexto e propósito do chatbot

## 🎯 Como Usar

1. Configure as variáveis de ambiente no arquivo `.env`
2. Inicie o chatbot
3. Interaja via WhatsApp usando o número configurado

## 👥 Contribuição

Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como contribuir para o projeto.

## 📝 Licença

Projeto licenciado sob MIT. Veja [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

- WhatsApp: (21) 96646-8534 

---
Desenvolvido com 🤖 por Diego Aragão

## 🙏 Agradecimentos Especiais

- [Davidson Gomes](https://github.com/EvolutionAPI) pelo desenvolvimento da Evolution API
- [Sandeco](https://github.com/sandeco/) por disponibilizar os códigos da Evolution em Python
