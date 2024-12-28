from flask import Flask, request, jsonify
from flask_cors import CORS
from fuzzywuzzy import process



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

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