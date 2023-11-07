#! /usr/bin/python3

import psutil

def find_process_by_name(process_name):
    matching_processes = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == process_name:
            matching_processes.append(process.info)
    return matching_processes

if __name__ == "__main__":
    process_name = input("Enter the process name to search for: ")
    matching_processes = find_process_by_name(process_name)

    if matching_processes:
        print(f"Found {len(matching_processes)} processes with the name '{process_name}':")
        for process in matching_processes:
            print(f"PID: {process['pid']} - Name: {process['name']}")
    else:
        print(f"No processes found with the name '{process_name}'")

