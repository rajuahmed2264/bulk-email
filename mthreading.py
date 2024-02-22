from flask import Flask, jsonify
import schedule
import time
import threading

app = Flask(__name__)

# Initial count_number
count_number = 0

# Function to be scheduled
def job():
    global count_number
    count_number += 2
    print(f"Task is running... count_number: {count_number}")

# Schedule the job to run every 3 seconds
schedule.every(3).seconds.do(job)

# Flask route to display the current count_number
@app.route('/get_count')
def get_count():
    return jsonify({"count_number": count_number})

if __name__ == '__main__':
    # Run the Flask app in a separate thread
    threading.Thread(target=app.run, kwargs={'debug': False}).start()

    # Run the scheduled job in the main thread
    while True:
        schedule.run_pending()
        time.sleep(1)
