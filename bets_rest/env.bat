
IF EXIST ..\..\venv\venv_bets\NUL GOTO NO_CREATE

cd ..\..\
md venv
cd venv

call python -m venv  venv_bets

cd ..\Bets\bets_rest



:NO_CREATE


call ..\..\venv\venv_bets\Scripts\activate.bat  

