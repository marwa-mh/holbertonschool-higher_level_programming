#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""
import requests
import json
import csv


def fetch_and_print_posts():
    """fetches all post from JSONPlaceholder. and print it"""
    url = 'https://jsonplaceholder.typicode.com/todos'
    rq = requests.get(url)
    status_code = rq.status_code
    print(f"Status Code: {status_code}")
    if status_code == requests.codes.ok:
        posts = rq.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """fetches all post from JSONPlaceholder. and save it to csv file"""
    url = 'https://jsonplaceholder.typicode.com/todos'
    rq = requests.get(url)
    status_code = rq.status_code
    if status_code == requests.codes.ok:
        posts = rq.json()
        dic: dict
        list_of_posts: list[dict] = [{}]
        for post in posts:
            dic = {'id': post['id'], 'title': post['title']}
            list_of_posts.append(dic)
        fieldnames = ['id', 'title']
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_of_posts)
