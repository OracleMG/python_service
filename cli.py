#!/usr/bin/env python3
"""A simple CLI tool to fetch weather information for a given location using the wttr.in service. 
"""
import sys
import requests


def main():
    """
    Fetch weather information for a given location.
    """
    location = sys.argv[1]
    url = f"https://wttr.in/{location}"
    response = requests.get(url, timeout=10)
    print(response.text)


if __name__ == "__main__":
    main()
