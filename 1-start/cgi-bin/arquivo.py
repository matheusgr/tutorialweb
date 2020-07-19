import cgi

print("Content-Type: text/html")

arq = open('contador', 'r')
id = arq.read()
arq.close()

form = cgi.FieldStorage() 

print()
print("<h1>Olah!</h1>")
print(form.getvalue("nome"))
print("chamada... " + id)

arq = open('contador', 'w')
arq.write(str(int(id) + 1))
arq.close()