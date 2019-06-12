import pymysql

def edu_pyMySql(sql,host='localhost',port=3306,user='edu',password='edu',db='edu'):

    conn=pymysql.connect(host=host,port=port,user=user,password=password,db=db)
    cuer=conn.cursor()
    cuer.execute(sql)
    r = cuer.fetchone()
    conn.close()
    cuer.close()
    return r

# print(edu_pyMySql('select * from xsmart_users where username="123456789"'))