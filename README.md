## Python Version
```
3.7.6
```

## Install requirements on local machine
```
pip3 install - r requirements.txt
or 
python -m pip install - r requirements.txt 
```
## Run program

```
python main.py
```
## Algorithm
1. Limit trades by 60.
2. From the first 60 trades, sort the json array by price and time.
3. Get the min element and max element.
4. From there, iterate by 60 from the max element.