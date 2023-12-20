# PracticalPython
The new website of Practical Python on Discord

---
## How to run without docker
install the requirements with 
```bash
pip install -r requirements.txt
```

run the flask app with 
```bash
python wsgi.py
```
---
## How to run with docker
in root directory run
```bash
docker-compose up -d
```

to shut down the app
```bash
docker-compose down
```

if experiencing something like `executable file not found in $PATH: unknown` then do
```bash
docker-compose build
```
and then do `docker-compose up -d`