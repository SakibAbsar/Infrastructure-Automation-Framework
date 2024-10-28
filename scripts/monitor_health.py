
import requests

def check_health():
    try:
        response = requests.get("http://localhost:5000/health")
        if response.status_code == 200:
            print("Application is healthy")
        else:
            print("Application health check failed")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_health()
