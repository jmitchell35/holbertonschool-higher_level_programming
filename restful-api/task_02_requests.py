#!/usr/bin/python3
import requests
import json
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    resp_list = response.json()
    for i in resp_list:
        print(i['title'])
    
def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    resp_list = response.json()
    filtered_list = [
        {"id": post["id"], 
         "title": post["title"], 
         "body": post["body"]}
        for post in resp_list
        ]
    fieldnames = filtered_list[0].keys()  # extract fieldnames
    with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header (column names)
        writer.writeheader()

        # Write the data
        writer.writerows(filtered_list)