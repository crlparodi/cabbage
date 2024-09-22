kubectl delete namespace cabbage
kubectl delete pv cabbage-pvc -n cabbage
kubectl create namespace cabbage
kubectl create configmap cabbage-nginx --from-file=nginx.conf -n cabbage
kubectl apply -f . -n cabbage
sleep 5
kubectl port-forward svc/cabbage 8000:80 -n cabbage