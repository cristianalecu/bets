if %computername%==L560-CNA set https_proxy=http://192.168.1.29:8080

call env.bat

if [%1] == [r] call pip install -r requirements.txt

call python manage.py makemigrations
call python manage.py migrate

python manage.py runserver 127.0.0.1:5500
