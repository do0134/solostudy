# HackerRank SoftwareEnginner test2

import requests


def getTemperature(name):
    # Write your code here
    url = f"https://jsonmock.hackerrank.com/api/weather?name={name}"
    response = requests.get(url)

    data = response.json().get("data")[0]
    answer = data.get("weather").split(" ")
    return int(answer[0])


if __name__ == '__main__':