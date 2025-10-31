#!/usr/bin/env python3
import requests
import time

def check_website_status(url):
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return "UP  - Website is working properly"
        else:
            return f"DOWN  - HTTP Status Code: {response.status_code}"
            
    except requests.exceptions.RequestException as e:
        return f"DOWN  - Error: {str(e)}"

def main():
    # You can change this URL to any website you want to check
    websites = [
        "https://www.google.com",
        "https://www.github.com", 
        "https://www.example.com"
    ]
    
    print("=== APPLICATION HEALTH CHECKER ===")
    print(f"Check Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    for website in websites:
        status = check_website_status(website)
        print(f"{website} - {status}")
        
    # Save report to file
    with open("website_status_report.txt", "w") as report_file:
        report_file.write("Website Status Report\n")
        report_file.write("=====================\n")
        for website in websites:
            status = check_website_status(website)
            report_file.write(f"{website} - {status}\n")
    
    print("\n Report saved to 'website_status_report.txt'")

if __name__ == "__main__":
    main()
