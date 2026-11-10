from flask import Flask, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def inicio():
    return jsonify({
        "mensaje": "¡Bienvenido al backend de La Cueva de Petra!",
        "estado": "Servidor Flask funcionando correctamente"
    })

@app.route('/test-db')
def test_db():
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({"estado": "Conectado a PostgreSQL exitosamente"})
    else:
        return jsonify({"estado": "Error al conectar a la base de datos"}), 500

if __name__ == '__main__':
    # debug=True permite que el servidor se reinicie solo cuando guardas cambios
    app.run(debug=True, port=5000)