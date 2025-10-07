# f=open("demo.txt","a")
# f.write("file doesnt exist but appended")
# f.close()
# f=open("demo.txt","r")
# print(f.read());

# with open("demo.txt","r") as f:
#     x=(f.read());
#     #print("Within with clause", x)
#     print(f.closed)

# print(f.closed)
# print(x)

# import requests # type: ignore
# # response= requests.get("https://api.thedogapi.com/v1/breeds")
# # print(response.status_code)
# # print(response.json())
# from datatime import date # type: ignore

# from urllib.request import urlopen
# url = "http://olympus.realpython.org/profiles/aphrodite"
# page = urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# #Now you can print the HTML to see the contents of the web page:
# print(html)


# import re
# # match_results = re.search("ab*c", "ABC", re.IGNORECASE)

# # print(match_results.group())
# string = "Everything is <replaced> if it's in <tags>."

# print(re.sub("<.*>", "ELEPHANTS", string))

# string

from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
