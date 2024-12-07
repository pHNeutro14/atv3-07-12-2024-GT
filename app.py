from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fazerpedido')
def fazerpedido():
    return render_template('fazerpedido.html')

@app.route('/confirmar_pedido', methods=["POST"])
def confirmar_pedido():
    recheio = request.form.get('recheio')
    molho = request.form.get('molho')
    massa = request.form.get('massa')
    return render_template('confirmar_pedido.html', recheio = recheio, molho = molho, massa = massa)