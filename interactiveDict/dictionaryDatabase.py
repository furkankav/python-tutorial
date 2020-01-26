import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

def translateLike(word):
    cursor.execute("SELECT DISTINCT Expression FROM Dictionary WHERE Expression LIKE '%{}%' AND Length(Expression) < {}".format(word, len(word)+3))
    results = cursor.fetchall()
    if results:
        print("Couldn't find what you are looking for! Here are few suggestions: ")
        return ", ".join([expretion[0] for expretion in results])
    else:
        return "Couldn't find what you are looking for!"

def translate(word):
    # query = cursor.execute("SELECT * FROM Dictionary")
    cursor.execute("SELECT Definition FROM Dictionary WHERE Expression LIKE '{}'".format(word))
    results = cursor.fetchall()
    if results:
        return "\n".join([definition[0] for definition in results])
    else:
        return translateLike(word)

while(True):
    word = input("Enter word: ")
    word = word.lower()
    if word == ":q":
        break
    print(translate(word))

