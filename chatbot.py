import sqlite3

def get_response(user_input):
    conn = sqlite3.connect("atmiya.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT answer FROM enquiries WHERE question LIKE ?",
        ('%' + user_input.lower() + '%',)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return "Sorry, I don't have information on that. Please contact the university office."
