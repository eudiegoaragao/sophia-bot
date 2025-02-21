import os
from openai import OpenAI
from dotenv import load_dotenv
from sophia_prompt import SOPHIA_SYSTEM_PROMPT
from send_sandeco import SendSandeco
import logging

# Configurar logging
logger = logging.getLogger(__name__)

class SophiaBot:
    def __init__(self):
        # Configuração inicial
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.messages = [{"role": "system", "content": SOPHIA_SYSTEM_PROMPT}]
        self.client_name = None
        self.sender = SendSandeco()

    def generate_response(self, user_message):
        """Gera uma resposta usando o OpenAI GPT"""
        try:
            # Adiciona a mensagem do usuário ao histórico
            self.messages.append({"role": "user", "content": user_message})
            
            # Obtém a resposta do modelo
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.messages,
                temperature=0.7,
                max_tokens=300,
                presence_penalty=0.6
            )
            
            # Extrai a resposta do assistente
            assistant_response = response.choices[0].message.content.strip()
            
            # Processa o nome do cliente se presente na mensagem
            if not self.client_name:
                self.extract_client_name(user_message)
            
            # Formata a resposta
            assistant_response = self.format_response(assistant_response)
            
            # Adiciona a resposta ao histórico
            self.messages.append({"role": "assistant", "content": assistant_response})
            
            return assistant_response
        except Exception as e:
            logger.error(f"Erro ao gerar resposta: {str(e)}")
            return "Desculpe, tive um problema ao gerar a resposta. Pode tentar novamente?"

    def extract_client_name(self, message):
        """Extrai o nome do cliente da mensagem"""
        message_lower = message.lower()
        
        # Padrões comuns de apresentação
        if "me chamo" in message_lower:
            self.client_name = message.split("me chamo")[-1].strip()
        elif "meu nome é" in message_lower:
            self.client_name = message.split("meu nome é")[-1].strip()
        elif "sou o" in message_lower:
            self.client_name = message.split("sou o")[-1].strip()
        elif "sou a" in message_lower:
            self.client_name = message.split("sou a")[-1].strip()

    def format_response(self, response):
        """Formata a resposta do bot"""
        # Remove espaços extras e quebras de linha
        response = " ".join(response.split())
        
        # Substitui placeholders de nome se necessário
        if self.client_name:
            response = response.replace("[Nome]", self.client_name)
            response = response.replace("[NOME]", self.client_name)
            response = response.replace("[nome]", self.client_name)
        
        return response

    def send_bot_response(self, message, number=""):
        """Envia a resposta do bot para o número especificado"""
        if number:
            try:
                logger.info(f"Enviando mensagem para {number}: {message}")
                self.sender.textMessage(number, message)
                logger.info("Mensagem enviada com sucesso")
                return True
            except Exception as e:
                logger.error(f"Erro ao enviar mensagem: {str(e)}")
                return False
        return False

if __name__ == "__main__":
    bot = SophiaBot()