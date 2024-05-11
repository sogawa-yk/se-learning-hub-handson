from flask import Blueprint, jsonify, send_from_directory, request
from k8s_client import create_pod, get_pod_status
from flask import current_app as app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@main.route('/api/start-pod', methods=['POST'])
def start_pod():
    pod_name = request.form['user-name']
    create_pod(pod_name)
    return jsonify({'podName': pod_name}), 200

@main.route('/api/status/<pod_name>', methods=['GET'])
def status(pod_name):
    status = get_pod_status(pod_name)
    return jsonify({'status': status}), 200
