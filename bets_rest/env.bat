
IF EXIST ..\..\venv\venv_rest\NUL GOTO NO_CREATE

cd ..\..\
md venv
cd venv

call python -m venv  venv_rest

cd ..\Rest\best_rest



:NO_CREATE


call ..\..\venv\venv_rest\Scripts\activate.bat  

