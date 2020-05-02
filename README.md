# BoredProject

A simple web application to find activities to do when bored.
What a great tool for this quarantine time!
The project is based on http://www.boredapi.com/

## Stack

This project makes use of Django, DRF and VueJS.

## How to use
Launch those commands to run project

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Let's load some data from fixture to make it more fun
```
python manage.py loaddata activities_data
```

## API

Some useful endpoint examples if you want play with the API

Let's assume you are running it locally with default options, therefore hostname is 127.0.0.1 :)

To fetch list of activities

```
curl http://127.0.0.1:8000/api/activities/
```

To create a new activity

```
curl http://127.0.0.1:8000/api/activities/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '
        {
            "activity": "Apprendre le python",
            "accessibility": 0.2,
            "type": "0.3",
            "participants" : 1,
            "price": 0,
            "link": "https://www.learnpython.org/"
        }'
```

To fetch an activity randomly

```
curl http://127.0.0.1:8000/api/random-activity
```

To fetch an activity randomly but with a precise price

```
curl http://127.0.0.1:8000/api/random-activity?price=0.2
```

To fetch and activity randomly but with a precise activity type
```
curl http://127.0.0.1:8000/api/random-activity?type=diy
```

To fetch all activity types available (a new activity type is created when one creates one activity and the activity type is not available in the current list)
```
curl http://127.0.0.1:8000/api/activity-types/
``` 

And of course when fetching one activity randomly, you can combine filters as such (filters implemented are type, price and participants)
```
curl http://127.0.0.1:8000/api/random-activity?price=0.2&type=diy
```

## Improvements

- Authenticate user
- Dashboard of user accomplished activities, so that one can track the new skills one learn
- Rating of activities by User
- Smart activities suggestions by web app based on past user activities rating