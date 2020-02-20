# Script que automaticamente já baixa e extrai o geckodriver na pasta bin
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz;
tar -xf geckodriver-v0.26.0-linux64.tar.gz;
mv geckodriver ./bin;
