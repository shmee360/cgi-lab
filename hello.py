#!/usr/bin/env python3
import os
import json
import templates

# print('Content-Type: text/text\r\n\r\n')
print('Content-Type: text/html\r\n\r\n')
print('<title>Test CGI</title>')

js_object = json.dumps(dict(os.environ), indent=4)
# print(js_object)

# for k in os.environ.keys():
#     if k == 'QUERY_STRING':
#         print(f'<b>Query String</b>: {os.environ[k]}<br>')
#     if k == 'HTTP_USER_AGENT':
#         print(f'<b>Browser</b>: {os.environ[k]}<br>')

print(templates.login_page())
