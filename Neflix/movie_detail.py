#!C:\Python\python.exe
print("Content-type: text/html\n\n")

import view

html=view.head() + view.movie_detail() + view.footer()

print(html)