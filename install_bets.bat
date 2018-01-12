rem don't create it if Bets folder exists
IF EXIST Bets\NUL GOTO NO_OVERWRITE

IF EXIST ..\Bets\NUL GOTO GO_OUTSIDE

:NO_OVERWRITE 

cd Bets

call pull.bat

cd bets_rest

start.bat r s


GOTO EOF

:GO_OUTSIDE

ECHO Move and execute this batch file outside folder Bets\

:EOF