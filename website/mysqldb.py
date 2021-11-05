import sqlite3

def connect():
    conn=sqlite3.connect("glucoselevelmonitor.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patients (first_name text,last_name text, gender text, age integer, contact integer,address text,room_no integer,  bed_no integer, glucose integer, need_glucose text)")
    conn.commit()
    conn.close()

def insert(first_name,last_name,gender,age,contact,address,room_no,bed_no):
    conn=sqlite3.connect("glucoselevelmonitor.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO patients VALUES (?,?,?,?,?,?,?,?,NULL,NULL)",(first_name,last_name,gender,age,contact,address,room_no,bed_no))
    conn.commit()
    conn.close()
    view()

def view():
    searchs = []
    dicts = {}
    conn=sqlite3.connect("glucoselevelmonitor.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM patients")
    rows=cur.fetchall()
    conn.close()

    for i in range(len(rows)):
        dicts = {"first_name": rows[i][0] if rows[i][0] else None,
                 "last_name": rows[i][1] if rows[i][1] else None,
                 "gender": rows[i][2] if rows[i][2] else None,
                 "age": rows[i][3] if rows[i][3] else None,
                 "contact": rows[i][4] if rows[i][4] else None,
                 "address": rows[i][5] if rows[i][5] else None,
                 "room_no": rows[i][6] if rows[i][6] else None,
                 "bed_no": rows[i][7] if rows[i][7] else None,
                 "glucose": rows[i][8] if rows[i][8] else None,
                 "need_glucose": rows[i][9] if rows[i][9] else None,
                 }
        searchs.append(dicts)
    return searchs

def search(first_name='',last_name='',gender='',age='',contact='',address='',room_no='',bed_no=''):
    first_name=first_name.lstrip()
    last_name =last_name.lstrip()
    res =[]
    searchs = []
    dicts = {}
    conn=sqlite3.connect("glucoselevelmonitor.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM patients WHERE first_name=? OR last_name=? OR gender=? OR age=? OR contact=? OR address=?  OR room_no=? OR bed_no=?", (first_name,last_name,gender,age,contact,address,room_no,bed_no))
    rows=cur.fetchall()
    conn.close()
    [res.append(x) for x in rows if x not in res]
    try:
        res.remove(('', '', '', '', '', '', '', '', None, None))
    except:
        pass
    for i in range(len(res)):
        dicts = {"first_name": res[i][0],
                 "last_name": res[i][1],
                 "gender": res[i][2],
                 "age": res[i][3],
                 "contact": res[i][4],
                 "address": res[i][5],
                 "room_no": res[i][6],
                 "bed_no": res[i][7],
                 "glucose": res[i][8],
                 "need_glucose": res[i][9],
                 }
        searchs.append(dicts)
    return searchs

def delete(first_name,last_name=""):
    first_name = first_name.lstrip()
    last_name = last_name.lstrip()
    conn=sqlite3.connect("glucoselevelmonitor.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM patients WHERE first_name=? OR last_name=?",((first_name,last_name,)))
    conn.commit()
    conn.close()

def filter(age=0,gender='',last_name=''):
    last_name = last_name.lstrip()
    res = []
    searchs = []
    dicts = {}
    conn = sqlite3.connect("glucoselevelmonitor.db")
    cur = conn.cursor()
    if gender == '' and last_name == '':
        cur.execute("SELECT * FROM patients WHERE age <=?", ((age,)))
    elif gender != '' and last_name == '':
        cur.execute("SELECT * FROM patients WHERE age <=? AND gender=?", (age,gender))
    else:
        cur.execute("SELECT * FROM patients WHERE age <=? AND last_name =?", (age,last_name))
    rows = cur.fetchall()
    conn.close()
    [res.append(x) for x in rows if x not in res]
    try:
        res.remove(('', '', '', '', '', '', '', '', None, None))
    except:
        pass
    for i in range(len(res)):
        dicts = {"first_name": res[i][0],
                 "last_name": res[i][1],
                 "gender": res[i][2],
                 "age": res[i][3],
                 "contact": res[i][4],
                 "address": res[i][5],
                 "room_no": res[i][6],
                 "bed_no": res[i][7],
                 "glucose": res[i][8],
                 "need_glucose": res[i][9],
                 }
        searchs.append(dicts)
    return searchs

def update(first_name,last_name,gender,age,contact,address,room_no,bed_no,glucose="",need_glucose=""):
    first_name = first_name.lstrip()
    last_name = last_name.lstrip()
    conn=sqlite3.connect("glucoselevelmonitor.db")
    cur=conn.cursor()
    cur.execute("UPDATE patients SET last_name=?, gender=?, age=?, address=?, contact=?, bed_no=?, room_no=?, glucose=?, need_glucose=? WHERE first_name=?",(last_name,gender,age,contact,address,bed_no,room_no,glucose,need_glucose,first_name))
    conn.commit()
    conn.close()


def search_multiple(*arguments):
    searchs = []
    conn = sqlite3.connect("glucoselevelmonitor.db")
    cur = conn.cursor()
    for names in arguments[0]:
        names = names.lstrip()
        cur.execute("SELECT * FROM patients WHERE first_name=?",(names,))
        rows = cur.fetchall()
        dicts = {"first_name": rows[0][0] if rows[0][0] else None,
                 "last_name": rows[0][1] if rows[0][1] else None,
                 "gender": rows[0][2] if rows[0][2] else None,
                 "age": rows[0][3] if rows[0][3] else None,
                 "contact": rows[0][4] if rows[0][4] else None,
                 "address": rows[0][5] if rows[0][5] else None,
                 "room_no": rows[0][6] if rows[0][6] else None,
                 "bed_no": rows[0][7] if rows[0][7] else None,
                 "glucose": rows[0][8] if rows[0][8] else None,
                 "need_glucose": rows[0][9] if rows[0][9] else None,
                 }
        searchs.append(dicts)
    conn.close()
    return searchs



connect()
#insert("The Sun","John Smith",1918,913123132)
# delete("gugan")
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))

