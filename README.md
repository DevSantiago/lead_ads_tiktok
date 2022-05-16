# Camper TikTok Lead Ads integration

Server-side app that reads incoming leads coming from TikTok Lead Ads' webhook and sends them to Camper's CRM after giving them proper format. Built with Python.

## Running locally

Requisites:
- python3
- pip

1. Set up a Python virtual environment

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

2. Install dependencies

```bash
$ pip install -r requirements.txt
```

3. Run the app:

```bash
$ python3 main.py
```

Server will be running on http://127.0.0.1:5000