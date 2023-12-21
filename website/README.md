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
if you make changes to the website, and need to see the new changes, use
```bash
docker compose up -d --build website
```

to shut down the app
```bash
docker-compose down
```