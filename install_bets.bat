rem don't create it if Bets folder exists
IF EXIST ..\Rest\NUL GOTO GO_OUTSIDE

IF EXIST Rest\NUL GOTO NO_OVERWRITE

md Rest
cd Rest

call git init
call git config --global user.name "Cristian Alecu"
call git config --global user.email cristian.alecu@gmail.com

rem call git remote rm origin
call git remote add origin https://github.com/cristianalecu/Rest.git

cd ..

:NO_OVERWRITE 

cd Rest

call pull.bat

cd best_rest

st.bat r s


GOTO EOF

:GO_OUTSIDE

ECHO Move and execute this batch file outside folder Rest\

:EOF