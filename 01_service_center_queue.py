import queue
import random
import time
from datetime import datetime

class Request:
    def __init__(self, request_id: int, description: str, priority: int, timestamp: str):
        self.request_id = request_id
        self.description = description
        self.priority = priority
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f"Request {self.request_id}: {self.description}, Priority: {self.priority}, Time: {self.timestamp}"

request_queue: queue.Queue = queue.Queue()

def generate_request(request_id: int) -> None:
    descriptions = [
        "Fix login issue",
        "Update user profile page",
        "Improve search functionality",
        "Resolve payment gateway error",
        "Add new feature to dashboard"
    ]
    description: str = random.choice(descriptions)
    priority: int = random.randint(1, 5)
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    request = Request(request_id, description, priority, timestamp)
    print(f"Generated: {request}")
    request_queue.put(request)

def process_request() -> None:
    if not request_queue.empty():
        request: Request = request_queue.get()
        print(f"Processing: {request}")
        request_queue.task_done()
    else:
        print("Queue is empty, no requests to process.")

def main() -> None:
    request_id: int = 1
    try:
        while True:
            if random.random() > 0.5:
                generate_request(request_id)
                request_id += 1

            process_request()

            time.sleep(1)

    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
