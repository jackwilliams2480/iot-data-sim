import requests

class HTTPConnection:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, data, headers=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    base_url = "http://example.com/api"
    endpoint = "data"
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    headers = {
        "Content-Type": "application/json"
    }

    connection = HTTPConnection(base_url)
    response = connection.post(endpoint, data, headers)
    if response:
        print("Response from server:", response)