from flask import Flask, jsonify, render_template, redirect, url_for
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # スタートページを表示

@app.route('/start', methods=['POST'])
def start_pod():
    session_id = str(uuid.uuid4())  # ユニークなセッションIDを生成
    create_pod(session_id)
    return jsonify({"session_id": session_id, "status": "creating"})  # セッションIDと状態を返す

@app.route('/status/<session_id>')
def check_status(session_id):
    # Podの状態を確認する（ダミーの実装）
    return render_template('status.html', session_id=session_id, status="creating")  # 状態ページを表示

def create_pod(session_id):
    # 実際にPodを作成するロジック
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
