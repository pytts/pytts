# PyTTS

> Generate speech from text

## Usage (Windows)

### Setup (first time only)
```sh
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
```
### Run the program
```sh
.\venv\Scripts\activate.bat
REM The following command will create an output.mp3 file
python main.py "massive wanker"
```
### Run the webserver
```sh
.\venv\Scripts\activate.bat
python server.py
```

## Usage (Linux)

### Setup (first time only)
```sh
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Run the program
```sh
source venv/bin/activate
# The following command will create an output.mp3 file
python main.py "massive wanker"
```
### Run the webserver
```sh
source venv/bin/activate
python server.py
```
