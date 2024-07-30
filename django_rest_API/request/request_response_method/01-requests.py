import requests

def main():
    response = requests.get("https://fakestoreapi.com/products/1")

    print("Status Code : ", response.status_code)

    print("Content_type : ", response.headers["Content-Type"])

    print("Json Data : ", response.json())



if __name__ == "__main__":
    main()