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

- Docker Compose
- Evolution API no Docker
- Credenciais da Evolution API
- Chave de API OpenAI
- Credenciais da Evolution API

 
## 📚 Material de Referência

- Aula 04 - EvolutionAPI: Envio e Recebimento de Mensagens (Mentoria CrewAI 2 - Nível Intermediário)


## 🚀 Tutorial de Instalação e Configuração Sophia Bot

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/eudiegoaragao/sophia-bot.git
cd sophia-bot
```
### Passo 2: 

- Copiar os arquivos `send_sandeco.py` e `message_sandeco.py` da pasta `minha_evolution` para o projeto. 

- (***Caso não possua encontra-se no grupo CrewAI 2 - Intermediário.***)

### Passo 3: Criar um ambiente virtual e instalar as dependências.

- Você pode instalar as dependências localmente para facilitar as alterações posteriores no projeto.

- Crie o ambiente virtual

```bash
python -m venv venv
```
- Ative o ambiente virtual

```bash
./venv/Scripts/activate
```

- Instale as dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar Variáveis de Ambiente

- No arquivo `docker-compose.yml`, defina as variáveis de ambiente conforme suas credenciais da Evolution API e OpenAI.

### Passo 5: Instalar Dependências

- O comando `docker-compose build` constrói a imagem Docker do serviço `sophia-bot` com base no Dockerfile.

```bash
docker-compose build 
```

### Passo 6: Iniciar o Projeto

```bash
docker-compose up -d 
```

### Passo 7: Verificar no navegador se está funcionando

- Verificando se está funcionando
   - Acesse: http://localhost:5000
   - Deve retornar: 
  
     ```json
     {
       "message": "Sophia Bot funcionando!",
       "status": "success"
     }
     ```

### Passo 8: Verificar Logs
```bash

docker-compose logs -f sophia-bot
```

OU no Docker.desktop vá até o container `sophia-bot` e logs: ![Verificar Logs](/docs/images/verificar-logs.png) &nbsp; ![Flask Rodando](/docs/images/flask_rodando.png) &nbsp; 

   
Caso precise parar os serviços, use o comando abaixo:

   ```bash
   docker-compose down
   ```

## Configuração Evolution API

### Passo 9: Configurar a URL da Evolution API

- Utilize no Webhook a URL:

```bash 
http://sophia-bot:5000/
```
![evo_url](/docs/images/evo_url.png) &nbsp;

 

### Passo 10: No terminal teste a comunicação entre os contêineres   

```bash
docker exec -it sophia-bot curl http://evolution_api:8081 
```
- Testa a comunicação entre a Evo e a Sophia.

[testar comunicacao](/docs/images/testar-comunicacao.png) &nbsp;



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

## Teste no Whatsapp

- Envie uma mensagem no whatsapp para a instancia configurada no arquivo `docker-compose.yml`

- Verifique se a resposta foi gerada pelo bot


## 🧐 Testes

## ⚠️ **ATENÇÃO!!!!**

- **Caso não receba a resposta, verifique os logs do contêiner `sophia-bot` e da `evolution_api`.**
- **Caso a `evolution_api` não esteja respondendo, verifique as credenciais no arquivo `docker-compose.yml`.**
- **Faça um teste usando a URL do `webhook.site` na `evolution_api`.**

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
