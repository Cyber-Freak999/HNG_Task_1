from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def get_user():
    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate and get the current day in the local timezone
    current_time = datetime.datetime.now(pytz.timezone('Etc/GMT+1'))
    current_day = current_time.strftime('%A')

    # Get the current UTC time with validation of +/-2 hours
    utc_time = datetime.datetime.now(pytz.utc)

    # Validation for slack_name and track
    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track are required.'}), 400

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'track': track,
        'github_file_url': 'https://github.com/username/repo/blob/main/file_name.ext',
        'github_repo_url': 'https://github.com/username/repo', 
        'status_code': 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
