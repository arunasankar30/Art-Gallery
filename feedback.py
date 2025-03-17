#!C:/Users/Acer/AppData/Local/Programs/Python/Python311/python.exe
import cgi
import mysql.connector
print("Content-type: text/html\n\n")
print("<html>")
print("<body>")
z = cgi.FieldStorage()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project_art"
)
mycursor=mydb.cursor()
sql="select * from contact"
mycursor.execute(sql)
sql1=mycursor.fetchall()
print('''<style>
          table,th,td{
                width:100%;
                font-size:17px;
                margin-left:300px; 
                border:2px double  #461220;
                border-collapse: collapse;}
          tr:nth-child(odd){
            background-color:white;
            color:#461220;
        }
tr:hover{
            background-color:#461220;
            color:white;
        }
     </style>''')
print(''' <div class="col-md-8"></div>
    <div class="col-md-8" >
    <table><tr><th>Name</th><th>Suggestions</th></tr>''')
for i in sql1:
    print('''<form method="post"><tr>
            <td>%s</td><td>%s</td></form></div>'''
          % (i[1], i[4]))


mydb.commit()
print("</body>")
print("</html>")