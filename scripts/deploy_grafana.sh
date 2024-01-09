#!bin/bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm search repo prometheus-community
kubectl create namespace prometheus
helm install stable prometheus-community/kube-prometheus-stack -n prometheus
kubectl get pods -n prometheus
# kubectl edit svc stable-kube-prometheus-sta-prometheus -n prometheus
# Change ClusterIP -> NodePort, LoadBalancer
# kubectl edit svc stable-grafana -n prometheus
# Change ClusterIP -> NodePort, LoadBalancer
kubectl get svc -n prometheus