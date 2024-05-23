import requests


def check_expected_respond_code(response, expected):
    return response.status_code == expected


def create_user(name: str, job: str):
    payload = {
        "name": name,
        "job": job
    }
    response = requests.post("https://reqres.in/api/users",json=payload)
    return response


def get_user(id: int):
    user = requests.get(f"https://reqres.in/api/users/{id}")
    return user



def update_user(id: int, name: str,job: str):
    payload = {
        "name": name,
        "job": job
    }
    user = requests.put(f"https://reqres.in/api/users/{id}", json=payload)
    return user





