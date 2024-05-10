from kubernetes import client, config, utils
import os
import yaml
import sys

def init_k8s_client():
    # クラスター内から実行されているかどうかに応じて設定をロード
    try:
        config.load_incluster_config()
    except config.ConfigException:
        # クラスター外から実行されている場合はkubeconfigをロード
        print('Out of Cluster.')
        config.load_kube_config()

# APIインスタンスの初期化
init_k8s_client()

def create_pod(manifest_path):
    # マニフェストファイルからPodを作成
    try:
        utils.create_from_yaml(client.ApiClient(), yaml_file=manifest_path, namespace='default')
        return "Pod creation initiated successfully."
    except Exception as e:
        print(f"Failed to create pod: {str(e)}", file=sys.stderr)
        return f"Failed to create pod: {str(e)}"


def get_pod_status(pod_name, namespace='default'):
    # 特定のPodのステータスを取得
    try:
        pod = client.CoreV1Api().read_namespaced_pod(name=pod_name, namespace=namespace)
        return pod.status.phase
    except client.exceptions.ApiException as e:
        if e.status == 404:
            print('Pod not found', file=sys.stderr)  # 標準エラー出力にログを表示
            return 'Pod not found'
        elif e.status == 403:
            print('Permission denied. Please check your access rights.', file=sys.stderr)  # 標準エラー出力にログを表示
            return 'Permission denied. Please check your access rights.'
        else:
            print(f"Exception when calling CoreV1Api->read_namespaced_pod: {str(e)}", file=sys.stderr)  # 標準エラー出力にログを表示
            return str(e)
    except Exception as e:
        print(f"Error in getting pod status: {str(e)}", file=sys.stderr)  # 標準エラー出力にログを表示
        return str(e)