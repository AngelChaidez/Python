from flask import Flask, jsonify
import json
import threading
import scraper

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
        return jsonify(data)

if __name__ == '__main__':
    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=scraper.run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    app.run(debug=True)
