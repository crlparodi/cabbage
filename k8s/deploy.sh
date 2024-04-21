kubectl delete namespace cabbage
kubectl create namespace cabbage
kubectl apply -f . -n cabbage
kubectl create configmap cabbage-nginx --from-file=nginx.conf -n cabbage
sleep 5
kubectl port-forward svc/cabbage 8000:80 -n cabbage