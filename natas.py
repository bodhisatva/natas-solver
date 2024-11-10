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

def get_response_data(username: str, password: str):
  url = f'http://{username}.natas.labs.overthewire.org/'

  response = requests.get(url, auth=(username, password))
  status_code = response.status_code

  if status_code != 200:
    if status_code == 401:
      print(f'Authentication failed.\nStatus code of {status_code} returned.')
      exit(1)
    else:
      print(f'Something went wrong. Status code of {status_code} returned.')
      exit(1)
  
  return response.content.decode()

def print_response_results(prettified_html, password_sentence):
    print(prettified_html)
  
    if password_sentence:
      print(password_sentence[0])

@click.command()
@click.option('--username', '-u', prompt="Enter username")
@click.option('--password', '-p', prompt="Enter password")

def main(username: str, password: str):
  html = get_response_data(username, password)
  html_content = BeautifulSoup(html, 'html.parser')

  prettified_html = highlight(html_content.prettify(), HtmlLexer(), TerminalFormatter())
  password_sentence = re.findall(r'The password for [^->]*', html)

  print_response_results(prettified_html, password_sentence)

if __name__  == '__main__':
  main()