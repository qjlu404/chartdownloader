# chartdownloader
currently in early stages.
currently it can only fetch links along with their name.

make sure you have python3 and pip installed.
type `pip install urllib3 lxml wheel wget pdf2image` or replace pip with pip3 if it doesnt work the first time in the command prompt
then go to the same directory as the python script and type `python main.py` or `python3 main.py` or any way that works for you.

     install poppler with these instuctions: https://pdf2image.readthedocs.io/en/latest/installation.html#installing-poppler
     idk why they made it as hard as possible to get poppler to work on windows but idk you're gonna have to find a way.
     
     If the above didnt work for you then create a linux virtual machine, (look up on youtube how to create linux virtual machine)
     install everything with 
     `sudo apt-get install poppler-utils python3 python3-pip`
     
     after thats installed then type 
     
     `pip install urllib3 lxml wheel wget pdf2image`
     
     then navigate to the directory and run it.
