
# !!!! Сarefully !!!!

So far, the script does not recognize the addresses distorted by the web archive, so before starting, bring them to their normal form using regular expressions like `/web/(.*)_/`,
`/web/(.{1,17})_/`

# How to set up
To work you need to have python 3.11 and higher

you can download it here `https://www.python.org/downloads/`

after cloning the repository using the terminal, go to the root of the project where the main.py file is located and execute the command: 
```
python -m venv venv
```
the `venv` folder should appear in the root

after that execute the command:
```
source venv/Scripts/activate
```
now you are in a virtual environment isolated from the global  `python` of your PC
#
We need to install the dependencies required for the script to work using the command:
``` 
pip install -r requirements.txt
```

if you turned off the terminal or exited the virtual environment, you just need to start the virtual environment again 
```
source venv/Scripts/activate
``` 
it will be ready to work

# Script execution

unpack the archive in the dedirectory `workdir` and run the following command from the root of the project
```
python main.py
```
the program will prompt you to enter a domain 
`Enter domein in <example.com> format:`
enter it without `www.`

``` 
Enter domein in <example.com> format: example.com
```

after that the program will prompt you to enter the name of the directory `Enter directory name:` enter the name of the directory you exported to the directory `workdir`
``` 
Enter directory name: test
```
