import requests

headers ={}
headers['Authorization'] ='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTIzMjkzMDQxLCJqdGkiOiIxMDM1ZDgzMTI1NmI0MWIyOTUwMGRiZTI1MjU3ODZjMiIsInVzZXJfaWQiOjJ9.ZMrGP5v1JH5MI-3Xhkc0_-huHL1uZNKr1ruPEURXf2E'

r = requests.get('http://127.0.0.1:8000/api/snippet/',headers=headers)

print (r.text)