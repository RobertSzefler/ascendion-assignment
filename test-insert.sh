curl -w "\n" -X POST -H "Content-Type: application/json" --data '{"name":"John Rambo","born":"1947-07-06","salary":4701.5}' $1/employees
curl -w "\n" -X POST -H "Content-Type: application/json" --data '{"name":"Sub Zero","born":"2025-12-12","salary":4000.3}' $1/employees
curl -w "\n" -X POST -H "Content-Type: application/json" --data '{"name":"Scorpion","born":"2029-03-11","salary":3950.3}' $1/employees

curl -w "\n" -X POST -H "Content-Type: application/json" --data '{"name":"Bad1","born":"2029-03-11"}' $1/employees
curl -w "\n" -X POST -H "Content-Type: application/json" --data '{"name":"Bad2","born":"2029-03-11","salary":"aaaa"}' $1/employees
curl -w "\n" -X POST -H "Content-Type: application/json" --data '{"name":"Bad2","born":"abcdef","salary":777.5}' $1/employees
