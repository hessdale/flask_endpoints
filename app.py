import json
import dbhelper

from flask import Flask
app = Flask(__name__)


@app.get('/api/clients')
def get_all_clients():
    results = dbhelper.run_procedure('call get_all_users',[])
    if(type(results) == list):
        result_Json = json.dumps(results,default=str)
        return result_Json
    else:
        return 'something went wrong'
    


app.run(debug=True)