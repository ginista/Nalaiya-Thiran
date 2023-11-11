import ibm_db

hostname="8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud:30120"
uid = "zdg80277"
pwd="Wx12PEbrlgQcZosi"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="30426"
protocol="TCPIP"
cert="Certificate.crt"
dsn=(
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5};"
).format(db,hostname,port,uid,cert,pwd)

print(dsn)

try: 
    print("Trying to connect")
  #  db2=ibm_db.connect(dsn,",")
    conn = ibm_db.connect(dsn,"","")     
    print("connected to database")
except:
    print("no connection:", ibm_db.conn_errormsg())