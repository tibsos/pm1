import requests
import time

def make_request(url):
    try:

        response = requests.get(url)

        if response.status_code == 200:
        
            print(f"Request successful: {response.url}")
        
        else:
        
            print(f"Request failed with status code: {response.status_code}")

    except requests.RequestException as e:
        
        print(f"Request failed: {e}")

if __name__ == "__main__":

    url = "https://bloknot-ik.ru/check-subscription-expiration/"  # Change this to your desired URL

    while True:

        make_request(url)
        time.sleep(1)  # Pause for 1 second before making the next request