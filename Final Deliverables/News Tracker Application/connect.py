import ibm_db

dsn_hostname = "19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
dsn_uid = "czd87943"        # e.g. "abc12345"
dsn_pwd = "5Kcodi9b00RZRGPZ"      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_driver = "{IBMDB2CL1}"
dsn_database = "bludb"            # e.g. "BLUDB"
dsn_port = "30699"                # e.g. "32733"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"              #i.e. "SSL
dsn_cert="DigiCertGlobalRootCA.crt"
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};"
    "SSLServerCertificate={8};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security,dsn_cert)
conn = 0
try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
except:
    print("Unable to connect: ", ibm_db.conn_errormsg())
print(dsn)