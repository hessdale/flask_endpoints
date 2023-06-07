import json
import dbhelper
from flask import Flask ,request
app = Flask(__name__)


@app.get('/api/clients')
def get_all_clients():
    results = dbhelper.run_procedure('call get_all_users',[])
    if(type(results) == list):
        result_Json = json.dumps(results,default=str)
        return result_Json
    else:
        return 'something went wrong'
    
@app.get('/api/loyal_clients')
def get_loyal():
    max_points = request.args.get('max_points')
    results = dbhelper.run_procedure('call get_loyals(?)',[max_points])
    if(type(results) == list):
        result_Json = json.dumps(results,default=str)
        return result_Json
    else:
        return 'something went wrong'
    
app.post('/api/clients')
def post_client():
    username = request.json.get('username')
    password = request.json.get('password')
    results = dbhelper.run_procedure('call new_client(?,?)'[username,password])
    if(type(results) == list):
        result_Json = json.dumps(results,default=str)
        return result_Json
    else:
        return 'something went wrong'


app.run(debug=True)