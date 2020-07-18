import cgi
print("Content-Type: text/html")

form = cgi.FieldStorage() 

print()
print("<h1>Olah!</h1>")
print(form.getvalue("nome"))