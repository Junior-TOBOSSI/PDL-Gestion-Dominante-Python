

class ConnectionDao:


    def __init__(self):
        self._username = "C##BDD8_7"
        self._password = "BDD87"
        host = "oracle.esigelec.fr"
        port = 1521
        service_name = "orcl.intranet.int"
        self._dsn = f"{host}:{port}/{service_name}"

    

            

                