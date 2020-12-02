#!C:\Python\python.exe
print("Content-type: text/html\n\n")
import mysql.connector
import json

db= mysql.connector.connect(host="localhost", user='root', passwd="", database="Netflix")

if db.is_connected:
    print('database connected')
else:
    print("not connected")
# sql="select * from nf_movies"
# cur=db.cursor()
# cur.execute(sql)
# for result in cur:
#     print(result)

def sign_up(para):
    cur=db.cursor()
    sql="insert into nf_users(email,password,created_at,name) values('"+str(para['email'])+"','"+str(para['passwd'])+"','"+str(para['date'])+"','"+str(para['name'])+"') "
    try:
        cur.execute(sql)
        db.commit()
        response={'status':200, 'Message': "data posted sucessfully"}
        db.close()
        return json.dumps(response)
    except:
        db.rollback()
        response={'status':400, 'message':'data not posted sucessfully'}
        db.close()
        return json.dumps(response)

def sign_in(para):
    cur=db.cursor()
    sql= "Select * from nf_users where email='%s' and password='%s' "
    try:
        cur.execute(sql,(para['email'], para['passwd']), multi=True)
        response={'status':200, 'Message': "data posted sucessfully"}
        db.close()
        return json.dumps(response)
    except Exception as e:
        db.rollback()
        response={'status':400, 'message':str(e)}
        db.close()
        return json.dumps(response)
    # try:
    #     cur.execute(sql)
    #     result= cur.fetchall
    #     print(result)
    #     db.commit()
    #     response={'status':200, 'Message': "data posted sucessfully"}
    #     db.close()
    #     return json.dumps(response)
    # except:
    #     db.rollback()
    #     response={'status':400, 'message':'data not posted sucessfully'}
    #     db.close()
    #     return json.dumps(response)

    

# BAD EXAMPLES. DON'T DO THIS!
# cursor.execute("SELECT admin FROM users WHERE username = '" + username + '");
# cursor.execute("SELECT admin FROM users WHERE username = '%s' % username);
# cursor.execute("SELECT admin FROM users WHERE username = '{}'".format(username));
# cursor.execute(f"SELECT admin FROM users WHERE username = '{username}'");

# SAFE EXAMPLES. DO THIS!
# cursor.execute("SELECT admin FROM users WHERE username = %s'", (username, ));
# cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});


# # $sql = "SELECT count(*) FROM users WHERE  
# #               username = '{$_POST['username']}'AND  
# #               password = '...'"; ?> 

# # stmt = sql.SQL("""
# #             SELECT
# #                 count(*)
# #             FROM
# #                 {table_name}
# #         """).format(
# #             table_name = sql.Identifier(table_name),
# #         )
# #         cursor.execute(stmt)
# #         result = cursor.fetchone()
# def count_rows(table_name: str) -> int:
#     with connection.cursor() as cursor:
#         cursor.execute("""
#             SELECT
#                 count(*)
#             FROM
#                 %(table_name)s
#         """, {
#             'table_name': table_name,
#         })
#         result = cursor.fetchone()

#     rowcount, = result
#     return rowcount
    
#     def count_rows(table_name: str) -> int:
#         with connection.cursor() as cursor:
#         stmt = sql.SQL("""
#             SELECT
#                 count(*)
#             FROM
#                 {table_name}
#         """).format(
#             table_name = sql.Identifier(table_name),
#         )
#         cursor.execute(stmt)
#         result = cursor.fetchone()