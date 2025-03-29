eval $(minikube docker-env)

docker build -t ascendion-assignment-app . -f Dockerfile

for filename in k8s/*.yaml; do
  kubectl apply -f $filename
done
