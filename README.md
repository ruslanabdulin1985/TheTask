# About



Battleships is a 2-player game at the same computer, in the old-fashioned style. It is played on ruled grids on which each player's fleet of ships are marked. Players make moves one by one trying to guess where the opponent hided their ships. The one who find opponents ships faster wins the game.



# Requirements

* python3.6 +

* python-flask

* web-browser

  

The game is a web application written in Flask framework https://flask.palletsprojects.com/en/1.1.x/



## How to install

Install python and flask according to instructions:

https://flask.palletsprojects.com/en/1.1.x/installation/#



**Keep in mind that you do not have to install virtual environments if you do not want to.*

Copy Battleship folder somewhere on your computer

You can now run the application





## How to run

### Linux & Mac

in 'Battleships' folder run 

```
$ export FLASK_APP=main
$ flask run
```



### Alternative way

in 'Battleships' folder run 

```bash
$python3 main.py
```

then open a web browser on address

```
http://localhost:5000/
```





## Windows

Windows CMD: Navigate to  'Battleships' folder and run

```
> set FLASK_APP=hello
> flask run
```



### Alternative way

in 'Battleships' folder run 

```cmd
<path-to-python-folder>bin/python main.py
```

then open a web browser on address

```
http://localhost:5000/
```



### More information how to run flask applications

https://flask.palletsprojects.com/en/1.1.x/cli/#application-discovery