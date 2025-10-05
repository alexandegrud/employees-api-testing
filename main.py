# import requests
#
# BASE_URL = "https://employees-api-i9ae.onrender.com"
# GENERATE_TOKEN_URL = f"{BASE_URL}/generate-token"
# EMPLOYEES_EMP_URL = f"{BASE_URL}/employees"
#
# def generate_token():
#     login_body = {
#         "username": "admin",
#         "password": "admin"
#     }
#     response = requests.post(GENERATE_TOKEN_URL, json=login_body)
#     return response.json()["token"]
#
# def add_employee(employee : dict):
#     requests.post(EMPLOYEES_EMP_URL, json=employee, headers=headers)
#
# def get_employees():
#     response = requests.get(EMPLOYEES_EMP_URL, headers=headers)
#     return response.json()
#
# def get_single_employee(employee_id : int):
#     endpoint = f"{EMPLOYEES_EMP_URL}/{employee_id}"
#     response = requests.get(endpoint, headers=headers)
#     return response.json()
#
# def update_full_employee(update_info : dict, employee_id : int):
#     endpoint = f"{EMPLOYEES_EMP_URL}/{employee_id}"
#     requests.patch(endpoint, json=update_info, headers=headers)
#
# def update_single_data(update_info : dict, employee_id : int):
#     endpoint = f"{EMPLOYEES_EMP_URL}/{employee_id}"
#     requests.patch(endpoint, json=update_info, headers=headers)
#
# def delete_employees(employee_id=0, delete_all=False):
#     if delete_all:
#         employees = get_employees()
#         for employee in employees:
#             employee_id = employee["employeeId"]
#             requests.delete(f"{EMPLOYEES_EMP_URL}/{employee_id}", headers=headers)
#     else:
#         endpoint = f"{EMPLOYEES_EMP_URL}/{employee_id}"
#         requests.delete(endpoint, headers=headers)
#
#
# token = generate_token()
# headers = {
#     "Authorization": f"Bearer {token}",
#     "Content-Type": "application/json"
# }
#
#
# employee1 = {
#         "name": "Alex",
#         "organization": "IT",
#         "role": "Auto QA"
#     }
# employee2 = {
#     "name": "Peter",
#     "organization": "IT",
#     "role": "Developer C++"
# }
#
# # add_employee(employee1)
# # add_employee(employee2)
# # print(get_employees())
# # print(get_single_employee(1))
#
# employee_full_update_info = {
#     "name": "Andrey",
#     "organization": "IT",
#     "role": "Developer C#"
# }
#
# employee_single_data_update_info = {
#     "name": "Tom",
# }
#
#
# # update_full_employee(employee_full_update_info, 1)
# # update_single_data(employee_single_data_update_info, 1)
# #delete_employees(delete_all=True)
