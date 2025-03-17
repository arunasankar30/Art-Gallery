#!C:\Users\Acer\AppData\Local\Programs\Python\Python311\python.exe
import cgi
import mysql.connector
print("Content-type: text/html\n\n")
print("<html>")
print("<body>")
form = cgi.FieldStorage()
CName = form.getvalue("name")
Email =form.getvalue("email")
Phone_Number = form.getvalue("phone")
Suggestions = form.getvalue("message")
print("<h1>",CName,Email,Phone_Number,Suggestions,"</h1>")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project_art"
)
mycursor=mydb.cursor()
datas=(CName,Email,Phone_Number,Suggestions)
sql="INSERT INTO contact (Name,Email,Phone_Number,Suggestions) VALUES (%s,%s,%s,%s)"
mycursor.execute(sql,datas)
mydb.commit()
print("</body>")
print("</html>")
