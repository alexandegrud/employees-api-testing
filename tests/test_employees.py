import allure

@allure.title("Добавление нового сотрудника")
@allure.description("Добавим нового сотрудника с полями name, organization, role")
@allure.suite("Post")
def test_create_new_employee(init_employee):
    employee_body ={
        "name": "Alex",
        "organization": "IT",
        "role": "Auto QA"
    }
    response = init_employee.create_employee(employee_body)
    init_employee.assertions.is_equal(response.status_code, 200)
    init_employee.assertions.is_dicts_equal(response.json(), employee_body)

@allure.title("Получение информации о конкретном сотруднике")
@allure.description("Получение всей информации о конкретном сотруднике")
@allure.suite("Get")
def test_get_single_employee(init_employee):
    employee_id = 1
    response = init_employee.get_single_employee(employee_id)
    init_employee.assertions.is_equal(response.status_code, 200)
    init_employee.assertions.is_dicts_equal(response.json(),
    {
        "name": "Alex",
        "organization": "IT",
        "role": "Auto QA"
    })

@allure.title("Получение информации о всех сотрудниках")
@allure.description("Получение информации о всех сотрудниках")
@allure.suite("Get")
def test_get_all_employees(init_employee):
    response = init_employee.get_all_employees()
    init_employee.assertions.is_equal(response.status_code, 200)

@allure.title("Обновление всей информации о сотруднике")
@allure.description("Полное обновление информации о сотруднике")
@allure.suite("Put")
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

@allure.title("Обновление конкретного поля у сотрудника")
@allure.description("Обновление конкретного поля")
@allure.suite("Patch")
def test_update_single_data_of_employee(init_employee):
    employee_id = 1
    new_data_of_employee_body = {
        "name": "Alex Test"
    }
    expected_message = "Employee updated"
    response = init_employee.update_single_data_of_employee(employee_id, new_data_of_employee_body)
    init_employee.assertions.is_equal(response.status_code, 200)
    init_employee.assertions.is_equal(response.json()["message"], expected_message)

@allure.title("Удаление сотрудника")
@allure.description("Удаление сотрудника")
@allure.suite("Delete")
def test_delete_employee(init_employee):
    employee_id = 1
    expected_message = "Employee deleted"
    response = init_employee.delete_employee(employee_id)
    init_employee.assertions.is_equal(response.status_code, 200)
    init_employee.assertions.is_equal(response.json()["message"], expected_message)

@allure.title("Попытка получить несуществующего сотрудника")
@allure.description("Отправляем запрос на получение сотрудника, которого не существует в базе")
@allure.suite("Невалидный запрос")
def test_get_employee_invalid_id(init_employee):
    expected_message = "Employee not found"
    response = init_employee.get_single_employee(999)
    init_employee.assertions.is_equal(response.status_code, 404)
    init_employee.assertions.is_equal(response.json()["error"], expected_message)

@allure.title("Отправляем запрос без токена")
@allure.description("Отправка запроса без токена")
@allure.suite("Невалидный запрос")
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
