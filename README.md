# htnchallenge

This is my Hack the North 2023 Backend Application, created with Flask and SQLite!

## Setup
In the `database` folder, run `./initialize_database.py` to set up the database and insert the dummy data. The data in the table will return to its original state every time this is run.
```
htnchallenge % cd database
htnchallenge/database % ./initialize_database.py
```


**Spin up the local server**

In the **root** directory, use the command `flask run` to run the local server
```
htnchallenge % flask run
```

## Endpoints

**All Users Endpoint**
```
GET http://localhost:5000/users
```
Retrieve all hackers. 
Response is a list of hacker objects, in the following format:
``` json
[
  {
    "name": <string>,
    "company": <string>,
    "email": <string>,
    "phone": <string>,
    "skills": [
      {
        "skill": <string>,
        "rating": <int>
      }
    ]
  },
  ...
]
```

**User Information Endpoint**
```
GET http://localhost:5000/users/<hacker_id>
```
Given a ```hacker_id```, retrieve all their information. First hacker's ```hacker_id``` is ```1```, then ```2```, up to the number of hackers in the database. 
Response is a hacker object, in the following format:
``` json
  {
    "name": <string>,
    "company": <string>,
    "email": <string>,
    "phone": <string>,
    "skills": [
      {
        "skill": <string>,
        "rating": <int>
      }
    ]
  }
```

**Updating User Data Endpoint**
```
PUT http://localhost:5000/users/<hacker_id>
```
Given a ```userid``` and a json request body, update hacker profile with the values in the request body. Any new skills will be added to the hackers profile.
Sample Request:
``` json
  {
        "company": "Hack the South",
        "email": "lorettabrown@htn.net",
        "phone": "+1-999-999-9999",
        "skills": [
            {
                "skill": "Swift",
                "rating": 9
            },
            {
                "skill": "Swagger",
                "rating": 2
            }
        ]
   }
```
Original hacker profile:
```
  {
        "name": "Breanna Dillon",
        "company": "Jackson Ltd",
        "email": "lorettabrown@example.net",
        "phone": "+1-924-116-7963",
        "skills": [
            {
                "skill": "Swift",
                "rating": 4
            },
            {
                "skill": "OpenCV",
                "rating": 1
            }
        ]
    }
```
Response, updated hacker profile:
```
  {
        "name": "Breanna Dillon",
        "company": "Hack the South",
        "email": "lorettabrown@htn.net",
        "phone": "+1-999-999-9999",
        "skills": [
            {
                "skill": "Swift",
                "rating": 9
            },
            {
                "skill": "OpenCV",
                "rating": 1
            },
            {
                "skill": "Swagger",
                "rating": 2
            }
        ]
    }
```

**Skills Endpoint**
```
GET http://localhost:5000/skills/?min_frequency=5&max_frequency=10
```
Given (optional) query parameters min_frequency and max_frequency, return number of hackers with each skill. If query parameters are not passed, print all skill frequencies.

Response without query parameters:
``` json
{
    "ASP.NET": 27,
    "Ada": 15,
    "Angular": 39,
    "Ant Design": 37,
    "Assembly": 29,
    "Aurelia": 22,
    "AutoHotkey": 17,
    "AutoIt": 34,
    "Awk": 27,
    "Backbone.js": 24,
    "Bash": 28,
    "Bokeh": 30,
    "Bootstrap": 31,
    "Buefy": 29,
    "Bulma": 29,
    "C": 27,
    "C#": 26,
    "C++": 25,
    "COBOL": 29,
    "Chakra UI": 30,
    "Clojure": 32,
    "Common Lisp": 34,
    "Dart": 32,
    "Django": 37,
    "Django REST framework": 17,
    "Element UI": 28,
    "Elixir": 27,
    "Elm": 26,
    "Ember.js": 28,
    "Erlang": 32,
    "Express.js": 30,
    "F#": 27,
    "FastAPI": 34,
    "Flask": 27,
    "Flask-RESTful": 32,
    "Fortran": 31,
    "Foundation": 41,
    "Gensim": 25,
    "Go": 26,
    "Godot": 27,
    "Haskell": 31,
    "Java": 24,
    "JavaScript": 32,
    "Julia": 33,
    "Keras": 22,
    "Keras-RL": 30,
    "Kotlin": 35,
    "Laravel": 25,
    "Lisp": 20,
    "Logo": 18,
    "Lua": 23,
    "Materialize": 26,
    "Matplotlib": 21,
    "Meteor": 23,
    "Milligram": 29,
    "NLTK": 31,
    "Nest.js": 28,
    "Next.js": 25,
    "Node.js": 22,
    "Numpy": 20,
    "OCaml": 24,
    "Objective-C": 33,
    "OpenCV": 33,
    "PHP": 32,
    "Pandas": 31,
    "Pascal": 20,
    "Perl": 31,
    "Plotly": 40,
    "Polymer": 17,
    "Prolog": 24,
    "PyTorch": 33,
    "Pygame": 31,
    "Python": 23,
    "R": 36,
    "React": 41,
    "Ruby": 28,
    "Ruby on Rails": 29,
    "Rust": 35,
    "SQL": 32,
    "Sanic": 43,
    "Scala": 33,
    "Scheme": 37,
    "SciPy": 34,
    "Scikit-learn": 26,
    "Seaborn": 28,
    "Sed": 35,
    "Semantic UI": 30,
    "Smalltalk": 28,
    "Spacy": 28,
    "Spectre.css": 29,
    "Spring Boot": 24,
    "Starlette": 21,
    "Svelte": 14,
    "Swift": 28,
    "Tachyons": 19,
    "Tailwind": 33,
    "Tcl": 32,
    "TensorFlow": 32,
    "Theano": 29,
    "Tornado": 27,
    "TypeScript": 24,
    "Unity": 28,
    "Unreal Engine": 37,
    "Visual Basic": 37,
    "Vue.js": 31,
    "mini.css": 32
}

```

Response with ```min_frequency=10``` and ```max_frequency = 20```:
``` json
{
    "Ada": 15,
    "AutoHotkey": 17,
    "Django REST framework": 17,
    "Lisp": 20,
    "Logo": 18,
    "Numpy": 20,
    "Pascal": 20,
    "Polymer": 17,
    "Svelte": 14,
    "Tachyons": 19
}
```
