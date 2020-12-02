#!C:\Python\python.exe
print("Content-type: text/html\n\n")

import view

html=view.head() + view.sign_up() + view.footer()

print(html)