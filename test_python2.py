import sqlite3

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Utilisation de requêtes paramétrées pour éviter l'injection SQL
    query = "SELECT * FROM users WHERE username=?;"
    cursor.execute(query, (username,))
    
    user = cursor.fetchone()
    conn.close()
    return user

if __name__ == "__main__":
    username = input("Enter username: ")
    user = get_user(username)
    print(user)
