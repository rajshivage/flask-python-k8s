# flask-python-k8s

### Clone the repo
```
git clone https://github.com/rajshivage/flask-python-k8s.git
cd flask-python-k8s/templates/overlays/development
```
### Kustomize - Bases and Overlays
##### Kustomize has the concepts of bases and overlays. A base is a directory with a kustomization.yaml, which contains a set of resources and associated customization. An overlay is a directory with a kustomization.yaml that refers to other kustomization directories as its bases. A base has no knowledge of an overlay and can be used in multiple overlays. An overlay may have multiple bases and it composes all resources from bases and may also have customization on top of them.
##### You can find example in this repo

### Deploy app using kustomize
```
kubectl apply -k .
```

### Verify if deployment is complete
```
kubectl get all -n dev
```
### Verify if app is deployed and running
```
kubectl port-forward service/flask-api-service 8080:8000 -n dev
curl http://127.0.0.1:8080/ ##### It should display a message "Hello, world!" as response
```
