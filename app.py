from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta de ejemplo para obtener todos los elementos
@app.route('/api/elementos', methods=['GET'])
def obtener_elementos():
    # Aquí puedes realizar la lógica para obtener los elementos de tu aplicación
    elementos = ['elemento1', 'elemento2', 'elemento3']
    return jsonify(elementos)

# Ruta de ejemplo para agregar un nuevo elemento
@app.route('/api/elementos', methods=['POST'])
def agregar_elemento():
    nuevo_elemento = request.json['elemento']
    # Aquí puedes realizar la lógica para agregar el nuevo elemento a tu aplicación
    # ...
    return jsonify({'mensaje': 'Elemento agregado correctamente'})

# Ruta de ejemplo para obtener un elemento por ID
@app.route('/api/elementos/<id>', methods=['GET'])
def obtener_elemento_por_id(id):
    # Aquí puedes realizar la lógica para obtener el elemento con el ID especificado
    elemento = {'id': id, 'nombre': 'Elemento'}
    return jsonify(elemento)

# Ruta de ejemplo para actualizar un elemento por ID
@app.route('/api/elementos/<id>', methods=['PUT'])
def actualizar_elemento(id):
    # Aquí puedes realizar la lógica para actualizar el elemento con el ID especificado
    elemento_actualizado = {'id': id, 'nombre': 'Elemento actualizado'}
    return jsonify(elemento_actualizado)

# Ruta de ejemplo para eliminar un elemento por ID
@app.route('/api/elementos/<id>', methods=['DELETE'])
def eliminar_elemento(id):
    # Aquí puedes realizar la lógica para eliminar el elemento con el ID especificado
    # ...
    return jsonify({'mensaje': 'Elemento eliminado correctamente'})

if __name__ == '__main__':
    app.run()
    print('Host started')
