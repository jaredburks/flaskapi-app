from flask import Flask, jsonify
import random 

app = Flask(__name__)

@app.route("/positivity", methods=["GET"])
def positivity():
    # Positive affirmations list
    daily_affirmations = [
     "I am worthy of love and happiness.",
     "I am capable of achieving my goals.",
     "I am grateful for the blessings in my life.",
     "I am strong and resilient.",
     "I am surrounded by love and support.",
     "I am confident in my abilities.",
     "I am worthy of success.",
     "I am open to new possibilities and opportunities.",
     "I am becoming the best version of myself.",
     "I radiate positive energy.",
     "I make a positive difference in the world.",
     "I am in control of my thoughts and emotions.",
     "I trust the process of life.",
     "I embrace challenges as opportunities for growth.",
     "I choose peace and inner harmony." 
    ]
    affirmation = random.choice(daily_affirmations)
    # Print a random affirmation for the day
    return jsonify(affirmation)

if __name__ == "__main__":
    app.run(port=8001)
