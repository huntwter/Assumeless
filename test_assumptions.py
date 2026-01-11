import os

def process_data(data):
    # This is a good function
    print(data)

def risky_business():
    # TEST CASE 1: Hardcoded Path (System Risk, Explicit)
    config_path = "/etc/myapp/config.json"
    windows_path = "C:\\Users\\Admin\\secret.txt"
    
    try:
        with open(config_path) as f:
            pass
    # TEST CASE 2: Silent Failure (Buried, Silent)
    except:
        pass

def another_silent_one():
    try:
        x = 1 / 0
    except Exception: # assumeless: ignore
        pass
