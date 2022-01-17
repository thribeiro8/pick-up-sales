# importar pandas e flask
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# funcionalidades
@app.route('/')
def homepage():
  return 'A API está no ar'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('arquivo.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)

# startar a API
app.run(host='0.0.0.0')