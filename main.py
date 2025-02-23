from flask import Flask, request, jsonify
from utils.message_receiver import MessageReceiver
from utils.message_sender import MessageSender
from sophia_bot import SophiaBot
from utils.llm_connector import LLMConnector
import logging
import json

# Configuração de logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ajusta o nível de logging do werkzeug
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)

app = Flask(__name__)
llm = LLMConnector.groq_llama3_70b
bot = SophiaBot(llm_model=llm)

@app.route("/", methods=['GET'])
def home():
    logger.info("Recebendo GET na rota /")
    return jsonify({
        "status": "success",
        "message": "Sophia Bot funcionando!"
    }), 200

@app.route("/messages-upsert", methods=['POST'])
def process_message():
    logger.info("\n" + "="*80)
    logger.info("Recebendo POST em /messages-upsert")
    try:
        # Log dos headers da requisição
        logger.debug("Headers da requisição:")
        for key, value in request.headers.items():
            logger.debug(f"  {key}: {value}")
        
        # Verifica se o conteúdo é JSON
        if not request.is_json:
            logger.error("Requisição não contém JSON")
            return jsonify({
                "status": "error",
                "message": "Content-Type deve ser application/json"
            }), 400
        
        data = request.get_json()
        logger.info("Dados recebidos:")
        logger.info(json.dumps(data, indent=2, ensure_ascii=False))
        
        # Processa a mensagem usando MessageReceiver
        msg = MessageReceiver(data)
        logger.info("Mensagem processada:")
        logger.info(f"  Texto: '{msg.get_text()}'")
        logger.info(f"  Telefone: '{msg.phone}'")
        logger.info(f"  Nome: '{msg.push_name}'")
        logger.info(f"  Mensagem direta: {msg.is_direct}")
    
        # Só gera resposta se a mensagem for direta
        if not msg.is_direct:
            logger.info("Mensagem não direcionada ao bot; ignorando resposta.")
            return jsonify({
                "status": "ignored",
                "message": "Mensagem não direcionada ao bot."
            }), 200
        
        # Gera resposta do bot
        response = bot.generate_response(msg.get_text())
        logger.info(f"Resposta gerada: {response}")
        
        # Envia resposta via Evolution API se houver telefone
        if msg.phone:
            success = bot.send_bot_response(response, msg.phone)
            logger.info(f"Resposta {'enviada' if success else 'falhou'} para {msg.phone}")
        
        return jsonify({
            "status": "success",
            "message": response
        }), 200
        
    except Exception as e:
        error_msg = f"Erro ao processar mensagem: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    print("\n" + "=" * 80)
    print("\n Sophia Bot - Servidor Flask")
    print("=" * 80)
    print("\n Iniciando servidor...")
    print("URL: http://localhost:5000")
    print("Debug: Ativado")
    print("Reloader: Desativado")
    print("\n Pressione CTRL+C para encerrar o servidor")
    print("=" * 80 + "\n")
    
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        use_reloader=False
    )