# GetCounselingAtScc
Students at SCC tend to have to wait till midnight for the school's website to restart, we are going to create a website for users to input their preferred times and book them an appointment without the risk of losing sleep.

# Local Fullstack Simulation using Flask server to write inputs onto JSON and running the automation in the backend
![GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamU3cG9qYmxxN2FyZ3M4ZnQxNmlrcmVqM2kzZ2xycjRiMmJndjBsZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/llfsXPN6EV1pPCipMF/giphy.gif)
This is with 1 second delay on each action for visibility.
Sorry for the bad resolution.

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

The inputs into the form will write to "client\public\student_info.json"

- To run the webbot (On another terminal)

Spin up a venv, if you don't have it already on this terminal do:
```bash
.venv/Scripts/activate
```
else, just continue

```bash
cd backend
python script.py
```

This will run if all the inputs from the user match with the LosRios Database for students

## TODO:
Have the Counseling from SCC to release their available appointements for further development

To host and deploy the website with the WebBot running

Create a database to store tables from users as .csv files
