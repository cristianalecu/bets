http http://127.0.0.1:5500/snippets/
http -a saturn:Go4Cristi http://127.0.0.1:5500/snippets/

TEST RestUser

#1. list users  not logged on
http  http://127.0.0.1:5500/rsusr/

#2. list users as staff
http -a saturn:Go4Cristi http://127.0.0.1:5500/rsusr/

#3. create not logged on
http POST http://127.0.0.1:5500/rsusr/ myemail="sss@dsd.ro" mypassword="asasasas"

#4. create user as staff
http -a saturn:Go4Cristi POST http://127.0.0.1:5500/rsusr/ myemail="sss2@dsd.ro" mypassword="asasasas2"

#5. list user logged on
http -a sss@dsd.ro:asasasas http://127.0.0.1:5500/rsusr/

#6. change user not logged on
http PUT http://127.0.0.1:5500/rsusr/22/ myemail="sss2@dsd.ro" mypassword="asasasas2"

#7. change user logged on fail
http -a saturn:saturn PUT http://127.0.0.1:5500/rsusr/22/ myemail="sss2@dsd.ro" mypassword="asasasas2"

#8. change own user 
http -a sss@dsd.ro:asasasas PUT http://127.0.0.1:5500/rsusr/22/ myemail="sss3@dsd.ro" mypassword="asasasas3"

#9. change user as staff
http -a saturn:Go4Cristi PUT http://127.0.0.1:5500/rsusr/22/ myemail="sss4@dsd.ro" mypassword="asasasas4"
http -a sss2@dsd.ro:asasasas2 PUT http://127.0.0.1:5500/rsusr/22/ myemail="sss3@dsd.ro" mypassword="asasasas3"

#10. duplicate user email
http POST http://127.0.0.1:5500/rsusr/ myemail="sss2@dsd.ro" mypassword="asasasas2"
http -a saturn:Go4Cristi PUT http://127.0.0.1:5500/rsusr/22/ myemail="sss2@dsd.ro" mypassword="asasasas2"

#11. incorrect user email
http POST http://127.0.0.1:5500/rsusr/ myemail="sss2sd.ro" mypassword="asasasas2"

#12. ioncorrect password
http POST http://127.0.0.1:5500/rsusr/ myemail="sss779@dsd.ro" mypassword=""

#13. delete own user
http -a sss@dsd.ro:asasasas DELETE http://127.0.0.1:5500/rsusr/30/

#14. delete user not logged on
http DELETE http://127.0.0.1:5500/rsusr/31/

#15 create validation code
http POST http://127.0.0.1:5500/rsusr/ myemail="sssvvv@dsd.ro" mypassword="asasasas"
http -a sssvvv@dsd.ro:asasasas PUT http://127.0.0.1:5500/rsusr/32/
http POST http://127.0.0.1:5500/rsusr/ myemail="sss999@dsd.ro" mypassword="asasasas"

#16 - get validation code 

#17 - change password


http -a saturn:Go4Cristi http://127.0.0.1:5500/rsusr/
http POST http://127.0.0.1:5500/rsusr/ myemail="sss@dsd.ro" mypassword="asasasas"

http -a sss@dsd.ro:asasasas PUT http://127.0.0.1:5500/rsusr/18/ myemail="sss18@dsd.ro" mypassword="asasasas18"