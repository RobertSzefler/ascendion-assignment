curl -w "\n" $1/employees_by_salary?min_salary=4000
curl -w "\n" $1/employees_by_salary?max_salary=4500
curl -w "\n" "$1/employees_by_salary?min_salary=333&max_salary=4599"
curl -w "\n" $1/employees_by_salary?aaa=bbb
curl -w "\n" $1/employees_by_salary?min_
