import requests
import socket

def get_public_ipv4():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        if response.status_code == 200:
            return response.json()['ip']
        else:
            return "-Failed to retrieve IP"
    except requests.RequestException:
        return "-Failed to connect to the server"

def get_ip_from_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return "Incorrect Domain"