# Minikube Playground

## Minikube with Basic Flask App

1. Start docker machine `docker-machine start default`, may need to create beforehand
1. Start MiniKube `minikube start --kubernetes-version=v1.20.2 --vm=true`
1. Use docker machine for Minikube `eval $(minikube docker-env)`
1. Build image in docker machine `./scripts/build.sh`
1. Apply different resources in `k8s/python` folder, start with pod `kubectl apply -f k8s/python/pod.yaml`

### Service Type - LoadBalancer

1. In a separate terminal `minikube tunnel`
1. Uncomment `type` and `nodePort` in `k8s/python/service.yaml`, then `kubectl apply -f k8s/python/service.yaml`

### Service Type - ClusterIP and Ingress

1. `minikube addons enable ingress`
1. Comment out `type` and `nodePort` in `k8s/python/service.yaml`, then `kubectl apply -f k8s/python/service.yaml`
1. `kubectl apply -f k8s/python/ingress.yaml`

### Debug

1. `kubectl exec -it <POD_NAME> -n <NAMESPACE> -- bash`
1. `kubectl logs <POD_NAME> -n <NAMESPACE> -f`

## Minikube with Seldon Core

### Build and test docker image locally

1. `./scripts/build_seldon.sh`
1. `docker-compose -f docker-compose-seldon.yml up`
1. `curl -X POST http://localhost:9000/api/v1.0/predictions -d '{"jsonData": {"data": "Hello, World!"}}' -H "Content-Type: application/json"`
1. `curl http://localhost:9000/health/status`

### Try Seldon Core in Minikube

1. Install `helm` and `istioctl` locally
1. Install Istio in Minikube `istioctl install --set profile=demo -y`
1. Create Seldon playground namespace `kubectl create namespace seldon-app`
1. Apply Istio label in playground namespace `kubectl label namespace seldon-app istio-injection=enabled`
1. Apply Istio gateway `kubectl apply -f k8s/seldon/seldon-gateway.yaml`
1. Create Seldon system namespace `kubectl create namespace seldon-system`
1. Install Seldon operator `helm install seldon-core seldon-core-operator --repo https://storage.googleapis.com/seldon-charts --set usageMetrics.enabled=true --namespace seldon-system --set istio.enabled=true --version=v1.10.0`
1. Build seldon app in docker machine `./scripts/build_seldon.sh`
1. Apply Seldon deployment `kubectl apply -f k8s/seldon/sdep.yaml`

### LoadBalancer

1. In a separate terminal `minikube tunnel`
1. Get ingress host `export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')`
1. Get prediction `curl -X POST http://$INGRESS_HOST/seldon/seldon-app/seldon-serving/api/v1.0/predictions -d '{"jsonData": {"data": "Hello, World!"}}' -H "Content-Type: application/json"`

### Custom Host

1. Override default virtual service for http from Seldon `kubectl apply -f k8s/seldon/virtualservice.yaml`
1. Edit hosts in `/etc/hosts` with `INGRESS_HOST` obtained above
1. Get prediction `curl -X POST http://seldon-app.com/api/v1.0/predictions -d '{"jsonData": {"data": "Hello, World!"}}' -H "Content-Type: application/json"`

## Clean Up

1. `minikube delete`
1. Undo changes in `/etc/hosts`
