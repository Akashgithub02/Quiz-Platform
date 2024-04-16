from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime, timedelta
import mysql.connector
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure MySQL connection
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='abyudaya'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rounds')
def rounds():
    return render_template('rounds_time.html')

@app.route('/round1login')
def round1login():
    return render_template('round1/round1login.html')

@app.route('/login1', methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        team_name = request.form['team_name']
        password = request.form['password']

        cursor = mysql_connection.cursor()
        cursor.execute("SELECT id, name FROM teams WHERE name = %s AND password = %s", (team_name, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['team_name'] = user[1]
            # Calculate the end time of the quiz (5 minutes from now)
            session['end_time'] = datetime.now() + timedelta(minutes=5)
            return redirect('/dashboard1')
        else:
            return render_template('round1/round1login.html', message='Invalid credentials. Please try again.')

    return render_template('round1/round1login.html')

start_time = datetime(2024, 4, 16, 11,59 )
end_time = datetime(2024, 4, 16, 12, 0)

@app.route('/dashboard1')
def dashboard1():
    if 'team_name' in session:
          # Set the start time to April 9, 2024, at 11:00 AM
        session['start_time'] = start_time  # Store the start time in the session
        return render_template('round1/dashboard1.html', team_name=session['team_name'], end_time=session.get('end_time'), start_time=start_time)
    else:
        return redirect('/login1')

@app.route('/logout1', methods=['POST'])
def logout1():
    session.pop('team_name', None)
    session.pop('end_time', None)
    return redirect('/round1login')

# Open the JSON file for reading
with open('questions1.json', 'r') as file:
    # Load JSON data from the file
    quizQuestions = json.load(file)

@app.route('/quiz')
def quiz():
    if 'team_name' in session:
        # Pass end time to the template
        return render_template('round1/quiz.html', team_name=session['team_name'], questions=quizQuestions['questions'], end_time=end_time)
    else:
        return redirect('/login1')

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if request.method == 'POST':
        submitted_answers = {}
        for key, value in request.form.items():
            if key.startswith('question'):
                question_number = int(key.replace('question', ''))
                submitted_answers[question_number] = value
        
        # Compare submitted answers with correct answers from JSON file
        correct_answers = {idx: question['solution'] for idx, question in enumerate(quizQuestions['questions'])}
        score = sum(1 for idx, answer in correct_answers.items() if submitted_answers.get(idx) == answer)
        
        # Save the responses and score to the database
        save_responses_and_score(session['team_name'], json.dumps(submitted_answers), score)
        
        # Redirect to the result page with the score
        return redirect(url_for('result1', score=score, total=len(quizQuestions['questions'])))

def save_responses_and_score(team_name, responses, score):
    # Open a cursor to execute SQL queries
    cursor = mysql_connection.cursor()
    
    # Define the SQL query to insert responses and score into the database
    sql_query = "INSERT INTO scores (team_name, responses, score) VALUES (%s, %s, %s)"
    
    # Execute the SQL query with the team name, responses, and score as parameters
    cursor.execute(sql_query, (team_name, responses, score))
    
    # Commit the transaction to save changes to the database
    mysql_connection.commit()
    
    # Close the cursor
    cursor.close()

@app.route('/result1')
def result1():
    # Retrieve the score and total number of questions from the URL parameters
    score = int(request.args.get('score'))
    total = int(request.args.get('total'))
    
    # Optionally, you can fetch additional information from the database
    # For example, you can fetch the team's previous scores
    
    return render_template('round1/result1.html', score=score, total=total)

if __name__ == "__main__":
    # Run the Flask application on the local network
    app.run(host='0.0.0.0', port=5000, debug=True)
