def test_create_new_employee(init_employee):
    employee_body ={
        "name": "Alex",
        "organization": "IT",
        "role": "Auto QA"
    }
    response = init_employee.create_employee(employee_body)
    init_employee.assertions.is_equal(response.status_code, 200)
    init_employee.assertions.is_dicts_equal(response.json(), employee_body)

def test_get_single_employee(init_employee):
    employee_id = 3
    response = init_employee.get_single_employee(employee_id)
    init_employee.assertions.is_equal(response.status_code, 200)
    init_employee.assertions.is_dicts_equal(response.json(),
    {
        "name": "Alex",
        "organization": "IT",
        "role": "Auto QA"
    })


def test_get_all_employees(init_employee):
    response = init_employee.get_all_employees()
    init_employee.assertions.is_equal(response.status_code, 200)

def test_update_full_date_of_employee(init_employee):
    employee_id = 1
    new_employee_body = {
            "name": "Gleb",
            "organization": "IT",
            "role": "Dev C++"
    }
    expected_message = "Employee updated"
    response = init_employee.update_full_data_of_employee(employee_id, new_employee_body)
    init_employee.assertions.is_equal(response.status_code, 200)
    init_employee.assertions.is_equal(response.json()["message"], expected_message)

def test_update_single_data_of_employee(init_employee):
    employee_id = 1
    new_data_of_employee_body = {
        "name": "Alex Test"
    }
    expected_message = "Employee updated"
    response = init_employee.update_single_data_of_employee(employee_id, new_data_of_employee_body)
    init_employee.assertions.is_equal(response.status_code, 200)
    init_employee.assertions.is_equal(response.json()["message"], expected_message)

def test_delete_employee(init_employee):
    employee_id = 1
    expected_message = "Employee deleted"
    response = init_employee.delete_employee(employee_id)
    init_employee.assertions.is_equal(response.status_code, 200)
    init_employee.assertions.is_equal(response.json()["message"], expected_message)

def test_get_employee_invalid_id(init_employee):
    expected_message = "Employee not found"
    response = init_employee.get_single_employee(999)
    init_employee.assertions.is_equal(response.status_code, 404)
    init_employee.assertions.is_equal(response.json()["error"], expected_message)

def test_request_without_token(init_employee):
    employee_body = {
        "name": "Gleb",
        "organization": "IT",
        "role": "Dev C++"
    }
    expected_message = "Unauthorized"
    response = init_employee.create_employee(employee_body, without_token=True)
    init_employee.assertions.is_equal(response.status_code, 401)
    init_employee.assertions.is_equal(response.json()["message"], expected_message)
