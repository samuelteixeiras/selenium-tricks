from flask import Flask, request, jsonify
from scrappy import callUrl
from flask_executor import Executor
import time
import uuid
import os
import io
import contextlib

futures = {}
app = Flask(__name__)
executor = Executor(app)
current_Path = os.path.abspath(os.getcwd())


def execute_and_capture(fileName):
    with open(os.path.join(current_Path,fileName), 'r') as file:
        code = file.read()

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(code)
    
    return {'status': output.getvalue()}

@app.route('/tasks')
def tasks():
    pending_futures = {}

    for future_id in futures:
        future = futures.get(future_id)
        if future is None:
            return jsonify({'status': 'Invalid task ID'}), 404
        if future.done():
            continue
        else:
            pending_futures[future_id] = future
        
    return jsonify(pending_futures)
    


@app.route('/task-status/<future_id>', methods=['GET'])
def task_status(future_id):
    future = futures.get(future_id)
    if future is None:
        return jsonify({'status': 'Invalid task ID'}), 404
    if future.done():
        response = {
            'status': 'completed',
            'result': future.result()
        }
    else:
        response = {
            'status': 'pending'
        }
    return jsonify(response)

@app.route('/scrap-async')
def selenium():
    future_id = str(uuid.uuid4())
    future = executor.submit(execute_and_capture,'scrappy2.py')
    futures[future_id] = future

    return jsonify({'status': 'Task started!','future_id': future_id }), 202

@app.route('/scrap-sync')
def selenium():
    callUrl()
    time.sleep(5)
    return 'done'

@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)