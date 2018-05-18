http http://127.0.0.1:5500/snippets/
http -a saturn:Go4Cristi http://127.0.0.1:5500/snippets/

http -a saturn:Go4Cristi http://127.0.0.1:5500/rsusr/
http POST http://127.0.0.1:5500/rsusr/ myemail="sss@dsd.ro" mypassword="asasasas"

http -a sss@dsd.ro:asasasas PUT http://127.0.0.1:5500/rsusr/18/ myemail="sss18@dsd.ro" mypassword="asasasas18"