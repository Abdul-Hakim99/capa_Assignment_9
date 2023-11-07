#! /usr/bin/python3

import psutil

def list_running_processes():
    print("PID\t| Name\t| CPU Usage (%) | Memory Usage (MB)")
    print("*" * 50)
    for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            pid = process.info['pid']
            name = process.info['name']
            cpu_percent = process.info['cpu_percent']
            memory_usage = process.info['memory_info'].rss / (1024 * 1024)  # Convert to MB
            print(f"{pid}\t| {name}\t| {cpu_percent:.2f}\t\t  | {memory_usage:.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

list_running_processes()

