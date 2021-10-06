from flask import Flask, request, jsonify
from yeelight import Bulb, BulbException
import logging


app = Flask(__name__)
logger = logging.getLogger('werkzeug')

@app.errorhandler(Exception)
def api_error(error):
  logger.exception(error)
  return "API error", 500

@app.errorhandler(BulbException)
def bulb_error(error):
  logger.exception(error)
  return 'Bulb error', 400

@app.route('/hello')
def hello_world():
  bulb_ip = request.args.get('bulb')
  if bulb_ip:
    bulb = Bulb(bulb_ip)
    bulb.toggle()
    return jsonify(
      ip=bulb_ip
    )
  else:
    return jsonify(
      ip="wala"
    )