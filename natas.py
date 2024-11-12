#!/usr/bin/env python3

# start with username: natas0, password: natas0
# http://natas0.natas.labs.overthewire.org/

import click
import requests
import re
import warnings
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.formatters import TerminalFormatter
from requests.cookies import RequestsCookieJar

YELLOW='\033[33m'
GREEN='\33[92m'
RED='\033[31m'
EYES_EMOJI='\U0001F440'

# supress warning related to robots.txt
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

def create_cookie(cookies: RequestsCookieJar):
  cookie = {}
  for field in cookies:
    cookie[field.name] = field.value
  return cookie

def get_response_data(username: str, password: str, suffix: str, headers: dict):
  url = f'http://{username}.natas.labs.overthewire.org/{suffix}'

  print(f'\nSending request to: http://{username}.natas.labs.overthewire.org/{YELLOW}{suffix}{GREEN}')
  print(f'Custom header: {headers}')

  response = requests.get(url, auth=(username, password), headers=headers)
  status_code = response.status_code
  cookie = create_cookie(response.cookies)

  if status_code != 200:
    if status_code == 401:
      print(f'\n{RED}Authentication failed.{GREEN}\nStatus code of {YELLOW}{status_code}{GREEN} returned.')
      exit(1)
    else:
      print(f'\n{RED}Something went wrong.{GREEN} Status code of {YELLOW}{status_code}{GREEN} returned.')
      exit(1)
  
  return response.content.decode(), cookie

def print_results(prettified_html, password_sentence):
  print(f"\n{prettified_html}")

  if password_sentence:
    print(f"{YELLOW}{password_sentence[0]}{GREEN}\n")

option1 = "y"
option2 = "Enter"

styled_option1 = f"{YELLOW}{option1}{GREEN}"
styled_option2 = f"{YELLOW}{option2}{GREEN}"

def create_url_suffix():
  choice = click.prompt(f"Enter {styled_option1} to add URL suffix or press {styled_option2}", 
default="")
  if choice == option1:
    suffix = click.prompt("Enter URL suffix")
    print(f'\nSuffix: {suffix}')
    return suffix
  else:
    return ""

def create_custom_header():
  choice = click.prompt(f'Enter {styled_option1} to add a custom header or press {styled_option2}', default="")
  
  if choice == option1:
    custom_header_key = click.prompt("Enter custom header key")
    custom_header_value = click.prompt("Enter custom header value")
  
    return { custom_header_key : custom_header_value }
  else:
    return {}

def manipulate_cookie(username, password, suffix, headers, cookie):
  url = f'http://{username}.natas.labs.overthewire.org/{suffix}'
  cookie_key = click.prompt("\nEnter cookie key")
  cookie_value = click.prompt("Enter cookie value")

  cookies = {cookie_key : cookie_value}
  response = requests.get(url, auth=(username, password), headers=headers, cookies=cookies)
  
  return response.content.decode()

print(f"\n{YELLOW}STARTING RECOINNAISSANCE{GREEN} {EYES_EMOJI}\n")

@click.command()
@click.option('--username', '-u', prompt="Enter username")
@click.option('--password', '-p', prompt="Enter password")

def main(username: str, password: str):
  suffix = create_url_suffix()
  headers = create_custom_header()
  html, cookies = get_response_data(username, password, suffix, headers)
  
  print(f"Cookies: {cookies}")
  
  if cookies:
    cookie_choice = click.prompt(f'\nEnter {styled_option1} to manipulate cookie or press {styled_option2}', default="")

    if cookie_choice == option1:
      html = manipulate_cookie(username, password, suffix, headers, cookies)

  html_content = BeautifulSoup(html, 'html.parser')

  prettified_html = highlight(html_content.prettify(), HtmlLexer(), TerminalFormatter())
  password_sentence = re.findall(r'The password for [^->]*', html)

  print_results(prettified_html, password_sentence)

if __name__  == '__main__':
  main()