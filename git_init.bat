
rem  git clone https://github.com/cristianalecu/Bets.git


call git init
call git config --global user.name "Cristian Alecu"
call git config --global user.email cristian.alecu@gmail.com

call git add --all .
call git commit -m "My Bets app, first commit"

call git remote add origin https://github.com/cristianalecu/Bets.git

call git push -u origin master
