#!C:\Python\python.exe
print("Content-type: text/html\n\n")
import view

html=view.head() + view.login() + view.footer()

print(html)