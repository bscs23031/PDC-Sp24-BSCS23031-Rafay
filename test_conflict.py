import requests
import threading

BASE = "http://localhost:8000"

# Both users fetch same version
initial = requests.get(f"{BASE}/document").json()
version = initial["version"]

def user_a():
    response = requests.put(
        f"{BASE}/document",
        json={
            "content": "Updated by User A",
            "version": version
        }
    )

    print("User A:")
    print(response.status_code)
    print(response.text)

def user_b():
    response = requests.put(
        f"{BASE}/document",
        json={
            "content": "Updated by User B",
            "version": version
        }
    )

    print("User B:")
    print(response.status_code)
    print(response.text)

thread1 = threading.Thread(target=user_a)
thread2 = threading.Thread(target=user_b)

thread1.start()
thread2.start()

thread1.join()
thread2.join()