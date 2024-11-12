#!/usr/bin/env python3

# start with username: natas0, password: natas0
# http://natas0.natas.labs.overthewire.org/

import click
import requests
import re
from bs4 import BeautifulSoup
from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.formatters import TerminalFormatter

YELLOW='\033[33m'
GREEN='\33[92m'
RED='\033[31m'

def get_response_data(username: str, password: str, url_suffix: str):
  url = f'http://{username}.natas.labs.overthewire.org/{url_suffix}'

  response = requests.get(url, auth=(username, password))
  status_code = response.status_code

  if status_code != 200:
    if status_code == 401:
      print(f'\n{RED}Authentication failed.{GREEN}\nStatus code of {YELLOW}{status_code}{GREEN} returned.')
      exit(1)
    else:
      print(f'\n{RED}Something went wrong.{GREEN} Status code of {YELLOW}{status_code}{GREEN} returned.')
      exit(1)
  
  return response.content.decode()

def print_results(prettified_html, password_sentence):
  print(f"\n{prettified_html}")

  if password_sentence:
    print(f"{password_sentence[0]}\n")


def create_url_suffix():
  choice = click.prompt(f"Enter {YELLOW}1{GREEN} to add URL suffix or press {YELLOW}ENTER{GREEN}", 
default="")
  if choice == "1":
    suffix = click.prompt("Enter URL suffix")
    return suffix
  else:
    return ""

print(f"\n{YELLOW}STARTING RECOINNAISSANCE{GREEN}\n")

@click.command()
@click.option('--username', '-u', prompt="Enter username")
@click.option('--password', '-p', prompt="Enter password")

def main(username: str, password: str):
  suffix = create_url_suffix()
  html = get_response_data(username, password, suffix)
  html_content = BeautifulSoup(html, 'html.parser')

  prettified_html = highlight(html_content.prettify(), HtmlLexer(), TerminalFormatter())
  password_sentence = re.findall(r'The password for [^->]*', html)

  print_results(prettified_html, password_sentence)

if __name__  == '__main__':
  main()