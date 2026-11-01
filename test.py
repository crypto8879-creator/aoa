import requests
import pyperclip
url="https://aoa-prj.netlify.app/radix.py"
response=requests.get(url)
pyperclip.copy(response.text)


