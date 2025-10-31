#!/usr/bin/env python3
import psutil
import datetime

def check_system_health():
    alerts = []
    
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        alerts.append(f"HIGH CPU USAGE: {cpu_usage}%")
    
    # Check Memory usage
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    if memory_percent > 80:
        alerts.append(f"HIGH MEMORY USAGE: {memory_percent}%")
    
    # Check Disk space
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    if disk_percent > 80:
        alerts.append(f"LOW DISK SPACE: {disk_percent}%")
    
    # Show results
    print(f"\n=== SYSTEM HEALTH CHECK ===")
    print(f"Time: {datetime.datetime.now()}")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_percent}%")
    print(f"Disk Usage: {disk_percent}%")
    
    if alerts:
        print("\nALERTS:")
        for alert in alerts:
            print(f"  {alert}")
    else:
        print("\n All systems normal!")
    
    # Save to log file
    with open("system_health.log", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - CPU: {cpu_usage}%, Memory: {memory_percent}%, Disk: {disk_percent}%\n")
        if alerts:
            log_file.write(f"ALERTS: {alerts}\n")

if __name__ == "__main__":
    check_system_health()