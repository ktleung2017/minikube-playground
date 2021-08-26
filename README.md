# Useful K8s commands

## Start `minikube`

1. `minikube start --vm=true`

## Use local docker images:

1. `eval $(minikube docker-env)`

## LoadBalancer

1. `minikube tunnel`

## Ingress

1. `minikube addons enable ingress`

## Debug

1. `kubectl exec -it <POD_NAME> -n <NAMESPACE> -- bash`
1. `kubectl logs <POD_NAME> -n <NAMESPACE> -f`
