"""
In order to execute this program you neet to have python3 installed.
"apt update && apt install python3 python3-pip" (under ubuntu/debian based distro)
"virtualenv -p python3 venv", "source venv/bin/activate", "pip3 install -r requirements.txt" to satisfy all libraries. 
Now run python3 app.py
You can click over "127.0.0.1" with ctrl pressed or open your web brower at 127.0.0.1:5000.
Et voila' the program is running (hoepfully).

For this program I used Flask with a basic html file with css and bootstrap grids. I was thinking about using JS to make it similar to google but needed more time.
app.py gets values from web forms and pass those as parameters to "autocomplete" function;
then either returns a list with "," between values or just a string.
"auto_complete" function opens "corpus.txt" file and assign wordList all the words inside the file,
splitting them and making the lowercase.
If "complete" word is entered, function matches all words inside "wordList" with "prefix" all lowercase with startwith() function.
In order to calculate occurence for each prefix inserted, most_common function is used.
Finally if there are some occurences, function return the list to "app.py" "result" variable.

Test was done using unit test library checking Parameters and if file exists.
"""
