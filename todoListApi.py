from flask import Flask, jsonify, request,abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False
    },
    {
        'id': 3,
        'title': 'Go for a run',
        'description': 'Take a break and enjoy some fresh air', 
        'done': False
    },
    {
        'id': 4,
        'title': 'Read a book',
        'description': 'Choose a novel or a self-development book', 
        'done': False
    },
    {
        'id': 5,
        'title': 'Prepare dinner',
        'description': 'Try a new recipe for tonight\'s dinner', 
        'done': False
    },
    {
        'id': 6,
        'title': 'Workout',
        'description': 'Go for a run and do some push-ups', 
        'done': False
    },
    {
        'id': 7,
        'title': 'Clean the house',
        'description': 'Vacuum, dust, mop the floors, clean the bathrooms', 
        'done': False
    },
    {
        'id': 8,
        'title': 'Buy gifts for friends',
        'description': 'Brainstorm ideas for birthday and anniversary presentsBrainstorm ideas for birthday and anniversary presentsBrainstorm ideas for birthday and anniversary presentsBrainstorm ideas for birthday and anniversary presents', 
        'done': False
    },
    {
        'id': 9,
        'title': 'Visit the dentist',
        'description': 'Get a routine check-up and cleaning', 
        'done': False
    },
    {
        'id': 10,
        'title': 'Plan a weekend getaway',
        'description': 'Research and book a relaxing trip for the upcoming weekend', 
        'done': True
    },
    {
        'id': 11,
        'title': 'Learn a new language',
        'description': 'Start studying Spanish, French, or German with online resources', 
        'done': False
    },
    {
        'id': 12,
        'title': 'Organize closet',
        'description': 'Go through clothes and donate items that no longer fit or are not needed', 
        'done': False
    },
    {
        'id': 13,
        'title': 'Cook dinner',
        'description': 'Prepare a healthy and delicious meal for the family', 
        'done': True
    },
    {
        'id': 14,
        'title': 'Study for an exam',
        'description': 'Review notes and practice problems for an upcoming test', 
        'done': False
    },
    {
        'id': 15,
        'title': 'Go for a run',
        'description': 'Get some exercise and fresh air with a morning jog', 
        'done': False
    }
    

]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
        
    if len(tasks) < 1: 
        task = {
            'id':1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': request.json.get('done', bool),
        }
    else: 
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': request.json.get('done', bool),
        }
    
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'id': task_id})

if __name__ == '__main__':
    app.run(debug=True)
