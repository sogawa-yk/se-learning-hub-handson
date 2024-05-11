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

def create_pod(pod_name):
    # マニフェストファイルからPodを作成
    template_pod_manifest_path = '/config/web-shell.yaml'
    template_svc_manifest_path = '/config/web-shell-service.yaml'
    output_path = '/config/'
    try:
        with open(template_pod_manifest_path, 'r') as file:
            template = file.read()
        pod_manifest_yaml = template.format(pod_name=pod_name)
        
        with open(template_svc_manifest_path, 'r') as file:
            template = file.read()
        svc_manifest_yaml = template.format(pod_name=pod_name)

        pod_manifest_path = output_path + pod_name + '.yaml'
        svc_manifest_path = output_path + pod_name + '-service.yaml'
        
        with open(pod_manifest_path, 'w') as file:
            file.write(pod_manifest_yaml)
        
        with open(svc_manifest_path, 'w') as file:
            file.write(svc_manifest_yaml)

        utils.create_from_yaml(client.ApiClient(), yaml_file=pod_manifest_path, namespace='default')
        utils.create_from_yaml(client.ApiClient(), yaml_file=svc_manifest_path, namespace='default')
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