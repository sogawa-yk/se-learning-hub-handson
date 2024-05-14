from flask import Blueprint, jsonify, send_from_directory, request, render_template
from k8s_client import create_pod, get_pod_status
from flask import current_app as app
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    ingress_ip = os.getenv('INGRESS_IP')
    return render_template('index.html', ingress_ip=ingress_ip)

@main.route('/api/start-pod', methods=['POST'])
def start_pod():
    pod_name = request.form['user-name']
    create_pod(pod_name)
    return jsonify({'podName': pod_name}), 200

@main.route('/api/status/<pod_name>', methods=['GET'])
def status(pod_name):
    status = get_pod_status(pod_name)
    return jsonify({'status': status}), 200
