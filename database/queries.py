CREATE_HACKERS_TABLE = """
    CREATE TABLE IF NOT EXISTS hackers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        company TEXT,
        email TEXT,
        phone TEXT
    )
    """

CREATE_SKILLS_TABLE = """
    CREATE TABLE IF NOT EXISTS skills (
        skill TEXT NOT NULL,
        rating INTEGER NOT NULL,
        hacker_id INTEGER NOT NULL,
        FOREIGN KEY(hacker_id) REFERENCES hackers(id)
    )
    """

INSERT_HACKER_INFO = """
    INSERT INTO hackers(name, company, email, phone) 
    VALUES (?, ?, ?, ?);
"""

INSERT_SKILLS_INFO = """
    INSERT INTO skills(skill, rating, hacker_id) 
    VALUES (?, ?, ?);
"""

GET_ALL_HACKERS = """
    SELECT * FROM hackers
"""

GET_SINGLE_HACKER = """
    SELECT * FROM hackers WHERE id=(?)
"""

GET_SINGLE_HACKER_SKILLS = """
    SELECT * FROM skills WHERE hacker_id=(?)
"""

GET_ALL_SKILLS_RATINGS = """
    SELECT * FROM skills
"""

GET_ALL_SKILL_COUNTS = """
    SELECT skill, count(skill) FROM skills GROUP BY skill
"""

GET_ALL_SKILL_COUNTS_BOUNDED = """
    SELECT skill, count(skill) FROM skills GROUP BY skill HAVING count(skill) BETWEEN (?) AND (?)
"""