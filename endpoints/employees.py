from base.base_api import BaseApi
import allure

class Employees(BaseApi):

    _endpoint = '/employees'

    def __init__(self, session, endpoint, token):
        super().__init__(session, endpoint)
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

    @allure.step("Отправляем запрос на получение всех сотрудников")
    def get_all_employees(self):
        response = self.get(self._endpoint, headers=self.headers)
        return response

    @allure.step("Отправляем запрос на получение конкретного сотрудника")
    def get_single_employee(self, employee_id):
        response = self.get(self._endpoint + f'/{employee_id}', headers=self.headers)
        return response

    @allure.step("Отправляем запрос на создание сотрудника")
    def create_employee(self, employee_body, without_token=False):
        if without_token:
            response = self.post(self._endpoint, json=employee_body)
            return response
        else:
            response = self.post(self._endpoint, json=employee_body, headers=self.headers)
            return response

    @allure.step("Отправляем запрос на полное обновление данных у сотрудника")
    def update_full_data_of_employee(self, employee_id, full_data_body):
        response = self.put(self._endpoint + f'/{employee_id}', json=full_data_body, headers=self.headers)
        return response

    @allure.step("Отправляем запрос на обновление конкретного поля у сотрудника")
    def update_single_data_of_employee(self, employee_id, single_data_body):
        response = self.patch(self._endpoint + f'/{employee_id}', json=single_data_body, headers=self.headers)
        return response

    @allure.step("Отправляем запрос на удаление сотрудника/всех сотрудников")
    def delete_employee(self, employee_id, delete_all=False):
        if delete_all:
            employees = self.get_all_employees().json()
            response = None
            for employee in employees:
                employee_id = employee['employeeId']
                response = self.delete(self._endpoint + f'/{employee_id}', headers=self.headers)
            return response
        else:
            response = self.delete(self._endpoint + f'/{employee_id}', headers=self.headers)
            return response

