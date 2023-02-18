from flask import Flask, request
import sqlite3
from database.queries import *
from sqlite3 import Error
conn = sqlite3.connect('database/hackers.db')
conn.row_factory = sqlite3.Row 

app = Flask(__name__)

def complete_hacker_profile(user_data, skills_data):
    cols = ["name", "company", "email", "phone"]
    hacker_rsp = {}
    for i in range (len(cols)):
       hacker_rsp[cols[i]] = user_data[i+1]
    
    skills = {}
    for s in skills_data:
       skill = s[0]
       rating = s[1]
       skills[skill] = rating

    hacker_rsp["skills"] = skills
    return hacker_rsp

@app.route("/")
def hello_world():
    return "Hello, HTN!"

@app.route('/users', methods=["GET"])
def get_all_hackers():
   with sqlite3.connect("database/hackers.db") as conn:
        all_hackers = []
        cur = conn.cursor()
        cur.execute(GET_ALL_HACKERS)

        rows = cur.fetchall()
        for hacker in rows:
            id = hacker[0]
            # retrieve hackers skills given id
            cur.execute(GET_SINGLE_HACKER_SKILLS, (id,))
            hacker_skills = cur.fetchall()
            all_hackers.append(complete_hacker_profile(hacker, hacker_skills))

        cur.close()
        return all_hackers


@app.route('/users/<hacker_id>', methods=["GET"])
def get_single_user(hacker_id):
    with sqlite3.connect("database/hackers.db") as conn:
        cur = conn.cursor()
        cur.execute(GET_SINGLE_HACKER, (hacker_id,))
        
        hacker = cur.fetchall()[0]

        cur.execute(GET_SINGLE_HACKER_SKILLS, (hacker_id,))
        skills = cur.fetchall()
        cur.close()

        return complete_hacker_profile(hacker, skills)
    

def update_user_skills(hacker_id, skills):
    with sqlite3.connect("database/hackers.db") as conn:
        for skill in skills:
            # check if skill already exists
            cur = conn.cursor()
            cur.execute("SELECT rating FROM skills WHERE skill=(?) AND hacker_id=(?)", (skill, hacker_id,))
            rsp = cur.fetchall()
            if len(rsp) == 0:
                # skill does not exist
                skillsData = (skill, skills[skill], hacker_id)
                cur.execute(INSERT_SKILLS_INFO, skillsData)
            
            else:
                # skill exists, update entry
                UPDATE_USER_SKILL = """UPDATE skills SET rating = (?) WHERE hacker_id=(?) AND skill=(?)"""
                cur.execute(UPDATE_USER_SKILL, (skills[skill], hacker_id, skill,))

        conn.commit()

@app.route('/users/<hacker_id>', methods=["POST", "PUT"])
def update_user(hacker_id):
    with sqlite3.connect("database/hackers.db") as conn:
        UPDATE_HACKER_PROFILE = """UPDATE hackers SET """
        toModify = request.get_json()
        colsToModify = list(toModify.keys())
        if ("skills" in colsToModify):
            colsToModify.remove("skills")
            update_user_skills(hacker_id, toModify["skills"])

        # update query depending on which fields were passed in request body
        for i in range (len(colsToModify)):
            UPDATE_HACKER_PROFILE = UPDATE_HACKER_PROFILE + colsToModify[i] + "=?"
            if (i != len(colsToModify) - 1):
                UPDATE_HACKER_PROFILE += ", "
            else:
                UPDATE_HACKER_PROFILE += " WHERE id=(?)"
        
        updatedValues = []

        for k in colsToModify:
            updatedValues.append(toModify[k])
        updatedValues.append(hacker_id)

        cur = conn.cursor()
        cur.execute(UPDATE_HACKER_PROFILE, updatedValues)
        conn.commit()
        
        return get_single_user(hacker_id)


@app.route('/skills/', methods=["GET"])
def skills_info():
    with sqlite3.connect("database/hackers.db") as conn:
        cur = conn.cursor()
        args = request.args.to_dict()
        agg = {}
        if ('min_frequency' in args and 'max_frequency' in args):
            min_freq = args['min_frequency']
            max_freq = args['max_frequency']
            print(min_freq)
            print(max_freq)
            cur.execute(GET_ALL_SKILL_COUNTS_BOUNDED, (int(min_freq), int(max_freq)))
            skill_counts = cur.fetchall()
            for pair in skill_counts:
                agg[pair[0]] = pair[1]
            
            cur.close()

        else:
            cur.execute(GET_ALL_SKILL_COUNTS)
            skill_counts = cur.fetchall()
            for pair in skill_counts:
                agg[pair[0]] = pair[1]
            
            cur.close()

    return agg