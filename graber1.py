from bs4 import Beautifulsoup
import requests

with open("https://musbonrealestate.com/Musbon/Index.aspx?gclid=CjwKCAjw6fCCBhBNEiwAem5SO-Wemf1LQRCWoRKmi84e-ZyZGt6T9w0Hn4tBp_oCShnirLwJhKEJUhoCzP8QAvD_BwE") as html_file:


 soup = Beautifulsoup(html_file, 'lxml')

print(soup)
