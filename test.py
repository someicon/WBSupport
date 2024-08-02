from dotenv import load_dotenv
import os
load_dotenv()

a = os.getenv("ADMIN_ID")
print(a.split(','))

b = [int(admin_id) for admin_id in a.split(',')]
print(b[0])
print(b[1])

string = 's, t, r, i, n, g'
print(string.split(','))
