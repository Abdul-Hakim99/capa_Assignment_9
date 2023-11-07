#! /usr/bin/python3

import psutil

def display_process_info(pid):
    try:
        process = psutil.Process(pid)
        print(f"Process ID: {process.pid}")
        print(f"Process Name: {process.name()}")
        print(f"Process Status: {process.status()}")
        print(f"Parent Process ID: {process.ppid()}")
        print(f"Process Memory Info: {process.memory_info()}")
        print(f"Process CPU Times: {process.cpu_times()}")
    except psutil.NoSuchProcess:
        print(f"No process found with PID: {pid}")

if __name__ == "__main__":
    try:
        pid = int(input("Enter the PID of the process to display information: "))
        display_process_info(pid)
    except ValueError:
        print("Invalid input. Please enter a valid integer PID.")

