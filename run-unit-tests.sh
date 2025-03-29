docker build -t ascendion-assignment-app . -f Dockerfile
# perform the build locally
docker build --pull=false -t ascendion-assignment-app-test . -f ./Dockerfile.tests
docker container run ascendion-assignment-app-test
