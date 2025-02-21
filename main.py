from flask import Flask, request, jsonify
from message_sandeco import MessageSandeco
from send_sandeco import SendSandeco
from sophia_bot import SophiaBot
import logging
import json

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configurar logs do werkzeug
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)

app = Flask(__name__)
bot = SophiaBot()

@app.route("/", methods=['GET'])
def home():
    logger.info("Recebendo GET na rota /")
    return jsonify({
        "status": "success",
        "message": "Sophia Bot funcionando!"
    }), 200

@app.route("/messages-upsert", methods=['POST'])
def funcao():
    logger.info("\n" + "="*80)
    logger.info("Recebendo POST em /messages-upsert")
    try:
        # Log do cabeçalho da requisição
        logger.debug("Headers da requisição:")
        for key, value in request.headers.items():
            logger.debug(f"  {key}: {value}")
        
        # Obter e validar o JSON
        if not request.is_json:
            logger.error("Requisição não contém JSON")
            return jsonify({
                "status": "error",
                "message": "Content-Type deve ser application/json"
            }), 400
        
        data = request.get_json()
        logger.info("Dados recebidos:")
        logger.info(json.dumps(data, indent=2, ensure_ascii=False))
        
        # Processar a mensagem
        msg = MessageSandeco(data)
        logger.info(f"Mensagem processada:")
        logger.info(f"  Texto: '{msg.text_message}'")
        logger.info(f"  Telefone: '{msg.phone}'")
        logger.info(f"  Nome: '{msg.push_name}'")
    
        # Gerar resposta do bot
        response = bot.generate_response(msg.text_message)
        logger.info(f"Resposta gerada: {response}")
        
        # Enviar resposta via Evolution API
        if msg.phone:
            success = bot.send_bot_response(response, msg.phone)
            logger.info(f"Resposta {'enviada' if success else 'falhou'} para {msg.phone}")
        
        # Retornar resposta HTTP
        return jsonify({
            "status": "success",
            "message": response
        }), 200
        
    except Exception as e:
        error_msg = f"Erro ao processar mensagem: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    print("\n" + "="*80)
    print(" Sophia Bot - Servidor Flask")
    print("="*80)
    print("\nIniciando servidor...")
    print("URL: http://localhost:5000")
    print("Debug: Ativado")
    print("Reloader: Desativado")
    print("\nPressione CTRL+C para encerrar o servidor")
    print("="*80 + "\n")
    
    app.run(
        debug=True, 
        host='0.0.0.0', 
        port=5000, 
        use_reloader=False
    )