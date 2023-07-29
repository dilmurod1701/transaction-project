import psycopg2


connection = psycopg2.connect(database=input("Enter your database: "), user=input("enter your user: "),
                              password=input("Enter your password: "), host=input("Enter your host: "),
                              port=input("Enter your port: "))
cur = connection.cursor()


def create_account(account_number, account_owner, balance):
    values = (account_number, account_owner, balance)
    cur.execute('''INSERT INTO accounts (account_number, account_owner, balance) VALUES (%s, %s, %s)''', values)
    connection.commit()
    print("Account muvaffaqiyatli yaratildi")


def send_money(your_account_id, account_number, amount):
    cur.execute('''SELECT balance FROM accounts WHERE account_number=%s''', (account_number,))
    balance = cur.fetchone()[0]
    new_balance = balance + amount
    cur.execute('''UPDATE accounts SET balance = %s WHERE account_number = %s''', (new_balance, account_number))
    low_balance = balance - amount
    cur.execute('''SELECT balance FROM accounts WHERE account_number=%s''', (account_number,))
    cur.execute('''UPDATE accounts SET balance = balance - %s WHERE account_number = %s''', (low_balance, your_account_id))
    connection.commit()


def view_accounts():
    cur.execute('''SELECT * FROM accounts''')
    rows = cur.fetchall()
    for i in rows:
        print(i)


cur.close()
