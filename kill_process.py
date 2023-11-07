#! /usr/bin/python3

import psutil

def kill_process_by_pid(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()  # Sends a terminate signal
        # If the process does not terminate, you can use process.kill() to forcefully kill it
        print(f"Process with PID {pid} terminated successfully.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")

# Example usage
if __name__ == "__main__":
    try:
        pid = int(input("Enter the process ID to kill: "))
        kill_process_by_pid(pid)
    except ValueError:
        print("Invalid input. Please enter a valid process ID.")

