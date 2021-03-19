# PyTTS

> Generate speech from text

## Table of contents

- [Usage (Windows)](#usage-windows)
  - [Setup (first time only)](#setup-first-time-only)
  - [Run the program](#run-the-program)
  - [Run the webserver](#run-the-webserver)
- [Usage (Linux)](#usage-linux)
  - [Setup (first time only)](#setup-first-time-only-1)
  - [Run the program](#run-the-program-1)
  - [Run the webserver](#run-the-webserver-1)

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
