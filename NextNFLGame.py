# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 16:43:16 2022

@author: maxwe
"""

import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.espn.com/nfl/schedule"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

Date = soup.find("div", class_="Table__Title")
Teams = soup.find("tbody", class_="Table__TBODY")

print("The next NFL game is on:")
print(Date.text)

Text = Teams.text
Versus = re.split("\s", Text, 5)
TeamTwo = re.split("1|2|3|4|5|6|7|8|9", Versus[4])
Time = re.split(r"\D+", Versus[4])

print(Versus[0] + " VS. " + TeamTwo[0])
print("At " + Time[1] + ":" + Time[2] + " PM")