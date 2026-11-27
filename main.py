import subprocess
import time
try:
    res = subprocess.run(
        ["git","version"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("\033[32m[X]\033[90m Git found\033[0m")
except FileNotFoundError:
    print("Git executable not found in PATH.")
except Exception as e:
    print(f"An error occurred while checking for Git: {e}")

while True:
    
    # git fetch origin
    res = subprocess.run(
        ["git","fetch","origin"],
        capture_output=True,
        text=True,
        check=True,
    )
    res = subprocess.run(
        ["git","status"],
        capture_output=True,
        text=True,
        check=True,
    )
    print(res.stdout)
    time.sleep(60)