# Script que automaticamente já baixa e extrai o geckodriver na pasta bin
wget https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip;
unzip chromedriver_linux64.zip;
mkdir bin;
mv chromedriver ./bin/chromedriver;
rm chromedriver_linux64.zip;
