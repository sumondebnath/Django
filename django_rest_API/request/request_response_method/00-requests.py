
import requests

# Create your views here.


def main():
    response = requests.get("http://www.google.com")
    print("Status Code: ", response.status_code)

    print("Headers : ", response.headers)

    print("Content-Type : ", response.headers["Content-Type"])

    print("Content-Type : ", response.headers["Content-Type"])


if __name__ == "__main__":
    main()