import cgi
import os
from templates import secret_page

creds = ('wstix', 'hunter2')

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

print('Content-Type: text/html\r\n', end='')
if ('HTTP_COOKIE' in os.environ and
        'logged_in=yes' in os.environ['HTTP_COOKIE']):
    print('\r\n', secret_page(creds[0], creds[1]), sep='')
elif username == creds[0] and password == creds[1]:
    print('Set-Cookie: logged_in=yes\r\n\r\n', end='')
    print(secret_page(creds[0], creds[1]))
