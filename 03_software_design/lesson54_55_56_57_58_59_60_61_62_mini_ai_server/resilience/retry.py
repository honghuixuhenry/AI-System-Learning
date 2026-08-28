import time 
import random

def retry(func, max_attempts = 3):
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise e
            delay = 2 ** attempt + random.uniform(0,1)
            print(
                f"Attempt failed. "
                f"Retrying in {delay}s"
            )
            time.sleep(delay)