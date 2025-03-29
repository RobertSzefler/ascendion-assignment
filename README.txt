*** General comments

The app runs in a Kubernetes cluster (tested with minikube on my laptop). The API server uses
FastAPI, PostgreSQL as the db, and SQLAlchemy+SQLModel for convenient data manipulation. The
code has been written asynchronously where possible.

*** Deploying with minikube

1. Install minikube and helm
2. minikube start
2. ./setup-cluster.sh (install Prometheus & Grafana)
3. ./run-minikube.sh
4. minikube service web --url
  -> returns the URL of the running app
5. ./test-insert.sh ${URL_FROM_STEP_4}
  -> should print {"status":"ok"} several times and some error messages for failed insert requests
6. ./test-query.sh ${URL_FROM_STEP_4}
  -> should print query endpoint results

*** Input validation

This is mostly done automatically by enforcing appropriate pydantic models for API
endpoint request payloads. The only place that actually needs extra manual checks
is app.get_by_salary.

*** Tests

To run unit tests, ./run-tests.sh (these run outside minikube, in a standalone container).

There's just one example test, the code is simple enough that it's hard to come up with
sensible unit tests.

*** Observability

The application provides Prometheus metrics (under ${APP_URL}/metrics).

A perfect extension would be to use Grafana with a Prometheus operator, but this project
is already getting complex.
