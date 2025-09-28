from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
# Format: { user_id: { "name": ..., "email": ... } }
users = {}
next_id = 1  # Auto-incrementing ID


# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# Route to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)


# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    user = {
        'name': data['name'],
        'email': data['email']
    }

    users[next_id] = user
    user_id = next_id
    next_id += 1

    return jsonify({'id': user_id, **user}), 201


# Route to update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = users.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])

    return jsonify(user)


# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    del users[user_id]
    return jsonify({'message': f'User {user_id} deleted'})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
