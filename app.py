from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from fuzzywuzzy import process

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return send_file("index.html")

# Serve CSS
@app.route("/styles.css")
def css():
    return send_file("styles.css", mimetype='text/css')

# Serve JavaScript
@app.route("/script.js")
def js():
    return send_file("script.js", mimetype='application/javascript')

# Serve Images
@app.route("/logo.png")
def logo():
    return send_file("logo.png", mimetype='image/png')

@app.route("/chatbot.png")
def chatbot_icon():
    return send_file("chatbot.png", mimetype='image/png')

@app.route("/bg.jpg")
def bg():
    return send_file("bg.jpg", mimetype='image/jpeg')

@app.route("/bg1.jpg")
def bg1():
    return send_file("bg1.jpg", mimetype='image/jpeg')

@app.route("/btech.jpg")
def btech():
    return send_file("btech.jpg", mimetype='image/jpeg')

@app.route("/mtech.jpg")
def mtech():
    return send_file("mtech.jpg", mimetype='image/jpeg')

@app.route("/mca.jpg")
def mca():
    return send_file("mca.jpg", mimetype='image/jpeg')

@app.route("/student1.png")
def student1():
    return send_file("student1.png", mimetype='image/png')

@app.route("/student2.png")
def student2():
    return send_file("student2.png", mimetype='image/png')

@app.route("/student3.png")
def student3():
    return send_file("student3.png", mimetype='image/png')

@app.route("/student4.png")
def student4():
    return send_file("student4.png", mimetype='image/png')

@app.route("/student5.png")
def student5():
    return send_file("student5.png", mimetype='image/png')

# Predefined educational responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help?",
    "hy": "Hey there! What do you need help with?",
    "courses": "We offer a variety of courses in Master of Computer Applications, B.Tech, and M.Tech.",
    "admission": "The admission process involves filling out the online application and submitting required documents.",
    "fees": "Our course fees range from $500 to $1500 per semester.",
    "contact": "You can contact us at askifyuniversity.edu.in or call +123 456 7890.",
    "thankyou": "You're welcome! Let me know if there's anything else you need.",
    "thanks": "No problem! Happy to help.",
    "bye": "Goodbye! Have a great day ahead!",
    "goodbye": "Take care! Feel free to reach out anytime.",
    "faculty": "Our faculty members are experienced professionals and industry experts.",
    "location": "We are located at 123 Education Lane, Knowledge City, Techland.",
    "hostel": "We offer separate hostels for boys and girls with 24/7 security and all essential amenities.",
    "placements": "Our placement cell has a strong record, with top companies visiting every year.",
    "library": "Our library is well-stocked with over 50,000 books, journals, and e-resources.",
    "labs": "We have state-of-the-art labs for various departments, fully equipped with modern tools.",
    "timing": "Our campus is open from 8:00 AM to 6:00 PM from Monday to Saturday.",
    "events": "We host annual tech fests, cultural programs, and workshops for holistic development.",
    "transport": "We provide transport facilities across major routes in the city.",
    "scholarships": "We offer merit-based scholarships and financial aid for deserving students.",
    "programming": "We provide excellent resources for programming enthusiasts, including coding bootcamps and hackathons.",
    "internships": "Our industry tie-ups ensure quality internship opportunities for students.",
    "about": "We are a premier institution focusing on academic excellence and innovation since 2000.",
    "okay": "Alright! Let me know if you need anything else.",
    "ok": "Got it! Feel free to ask me more questions.",
    "your name": "My name is Askify, your friendly chatbot assistant!"
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip().lower()

    # Check for valid user input
    if not user_message:
        return jsonify({"response": "Please enter a message to continue the chat."})

    # Fuzzy matching to find the best response
    best_match = process.extractOne(user_message, responses.keys())
    if best_match and best_match[1] > 70:  # Match confidence > 70%
        response = responses[best_match[0]]
    else:
        response = "I'm sorry, I didn't understand that. Can you please rephrase?"

    # Return the response
    return jsonify({"response": response})

if __name__ == "__main__":
    # Run the app on a specific port if needed
    app.run(debug=True)
