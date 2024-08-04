import requests

def Client():
    credntials = {
        "username" : "admin",
        "password" : "1234"
    }
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credntials)

    print("Status Code: ", response.status_code)
    response_data = response.json()

    print(response_data)



if __name__ == "__main__":
    Client()




        #   this code is provide by ChatGPT.

# import requests
# import logging

# logging.basicConfig(level=logging.DEBUG)

# def Client():
#     credentials = {
#         "username": "admin",
#         "password": "1234"
#     }
#     try:
#         response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
#         print("Status Code: ", response.status_code)
#         response_data = response.json()
#         print(response_data)
#     except requests.exceptions.RequestException as e:
#         print(f"Request failed: {e}")

# if __name__ == "__main__":
#     Client()