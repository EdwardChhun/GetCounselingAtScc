# GetCounselingAtScc
### Inspiration: 
Students at SCC tend to have to wait till midnight for the school's website to restart, we are going to create a website for users to input their preferred times and book them an appointment without the risk of losing sleep.

# Project DEMO
![GIF](https://github.com/EdwardChhun/GetCounselingAtScc/blob/main/2024-05-2719-24-02-Trim-ezgif.com-video-to-gif-converter.gif)

Working bot, currently it is the end of spring semester so counseling options are on *I think*. Hopefully we get this running for next fall semester for students to utilize.

## To Run Locally:

Make sure you have 3 terminals open

Create and activate python venv [Link to setting up a virtual environment](https://python.land/virtual-environments/virtualenv)

For Windows its:

```bash
.venv/Scripts/activate
```
Then install the requirements:
```bash
pip install -r requirements.txt
```

- Spin up the Flask server:
```bash
cd backend
python server.py
```

- Host the front end on local (On another terminal) (Ctrl+C to close)
```bash
cd client
npm run dev
```

## TODO:
1. Host Website & FLASK server on Google Cloud
2. Finalize the web bot functions after appointments are updated for next semester
3. Input validations
