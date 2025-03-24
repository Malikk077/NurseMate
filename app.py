from flask import Flask, request, jsonify, render_template, session
import google.generativeai as genai
from difflib import SequenceMatcher
from database import *

app = Flask(__name__)
app.secret_key = "ai chatbot"

# Initialize Gemini
GEMINI_API_KEY = 'AIzaSyAOSYkDqOVo6o13u5-3KNd2uX6C_yFtuZU'  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Initial prompt template
SYSTEM_PROMPT = """
You are an empathetic and supportive mental health chatbot. Your role is to:
1. Listen actively and respond with understanding
2. Ask relevant follow-up questions to encourage discussion
3. Recognize signs of distress and provide appropriate resources
4. Maintain a supportive and non-judgmental tone
5. Focus on emotional validation and coping strategies

Important guidelines:
- Always provide the suicide prevention hotline (988) if any signs of crisis are detected
- Use open-ended questions to encourage sharing
- Validate emotions without minimizing them
- Be patient and give space for responses
- Maintain appropriate boundaries while being supportive
"""

# Negative Queries List [Your existing negative_queries list remains the same]
negative_queries = [    
    "python", "java", "laptop", "game", "coding", "programming", "computer science", 
    "software development", "debugging", "algorithm", "database", "networking", 
    "internet", "web development", "mobile apps", "coding error", "hacking", "debug", 
    "api", "machine learning", "artificial intelligence", "cloud computing", 
    "data analysis", "cloud storage", "hardware", "firmware", "robotics", "iot", 
    "blockchain", "cryptocurrency", "vr", "ar", "ui/ux design", "seo", "devops", "github", 
    "git", "gitlab", "ide", "compiler", "python script", "application", "debugger", 
    "version control", "source code", "stack overflow", "stack trace", "frontend development", 
    "backend development", "full-stack development", "mobile development", "cloud services", 
    "big data", "data science", "data visualization", "quantum computing", "data mining", 
    "api integration", "web scraping", "php", "javascript", "html", "css", "sql", "nosql", 
    "algorithm complexity", "git clone", "framework", "data structure", "programming languages", 
    "responsive design", "angular", "react", "vue.js", "node.js", "css grid", "electron", 
    "laravel", "django", "ruby on rails", "restful api", "microservices", "cloud platform", 
    "kubernetes", "docker", "containerization", "ci/cd", "virtual machine", "linux", 
    "windows os", "mac os", "java runtime environment", "eclipse ide", "sublime text", 
    "visual studio code", "terminal", "command line interface", "automation", "scripting", 
    "fruits", "vegetables", "electronics", "gadgets", "vehicles", "car", "bike", "apple", 
    "banana", "cabbage", "orange", "mango", "pineapple", "grapes", "strawberry", "blueberry", 
    "watermelon", "peach", "plum", "pear", "avocado", "papaya", "kiwi", "lemon", "lime", 
    "cherry", "apricot", "pomegranate", "cantaloupe", "tomato", "cucumber", "lettuce", "spinach", 
    "carrot", "broccoli", "cauliflower", "asparagus", "green beans", "bell pepper", "eggplant", 
    "zucchini", "onion", "garlic", "potato", "sweet potato", "radish", "peas", "corn", "cabbage", 
    "beetroot", "pumpkin", "chili", "squash", "artichoke", "olive", "figs", "pineapple", "coconut", 
    "papaya", "raspberry", "tangerine", "dragonfruit", "litchi", "ginger", "durian", "mushroom", 
    "tofu", "rice", "washing machine", "refrigerator", "television", "smartphone", "laptop", 
    "tablet", "headphones", "smartwatch", "bluetooth speaker", "microwave", "coffee maker", 
    "electric kettle", "air conditioner", "camera", "drone", "printer", "electric toothbrush", 
    "vacuum cleaner", "rice cooker", "dishwasher", "smart tv", "projector", "fitness tracker", 
    "gaming console", "smart home hub", "car", "bike", "bus", "truck", "train", "scooter", "motorcycle", 
    "electric bike", "electric car", "boat", "bicycle", "suv", "sedan", "pickup truck", "minivan", 
    "convertible", "coupe", "limousine", "sportscar", "hybrid car", "luxury car", "electric scooter", 
    "cargo truck", "jeep", "lorry", "tractor", "rickshaw", "taxi", "god", "diamond", "painting", 
    "travel", "adventure", "nature", "exploration", "art", "photography", "landscape", "vacation", 
    "holiday", "journey", "wilderness", "tourism", "culture", "relaxation", "camping", "road trip", 
    "backpacking", "hiking", "safari", "cruise", "mountains", "ocean", "forest", "desert", "cityscape", 
    "beach", "sunset", "sunrise", "glamping", "wanderlust", "exotic destinations", "luxury travel", 
    "island", "trekking", "sightseeing", "resort", "hotel", "flight", "airport", "road trip", "adventure sports", 
    "scuba diving", "snorkeling", "wildlife", "cultural heritage", "world wonders", "tour guide", "backpacker", 
    "travel blogger", "travel journal", "bucket list", "destination", "excursion", "cruise ship", "skydiving", 
    "mountain climbing", "bungee jumping", "cave exploration", "travel photography", "cultural exchange", 
    "global travel", "spirituality", "religion", "faith", "divinity", "worship", "meditation", "peace", 
    "blessings", "holiness", "grace", "salvation", "prayer", "rituals", "love", "compassion", "forgiveness", 
    "transcendence", "spiritual growth", "mysticism", "divine", "grace", "eternity", "heaven", "destiny", 
    "purpose", "peace of mind", "life purpose", "karma", "enlightenment", "rebirth", "reincarnation", 
    "prophecy", "angels", "miracles", "faith-based", "hope", "blessed", "sacred", "diamond ring", "gemstone", 
    "jewelry", "luxury", "opulence", "riches", "precious stone", "gold", "silver", "platinum", "opal", 
    "emerald", "ruby", "sapphire", "amethyst", "jewels", "ornaments", "gem", "treasures", "wealth", "opulence", 
    "timeless beauty", "brilliance", "sparkle", "radiance", "glamour", "elegance", "dazzling", "lustre", 
    "shimmer", "polished", "shine"
]

def generate_gemini_response(prompt):
    """Generate response using Gemini model"""
    try:
        # Combine system prompt with user message
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {prompt}\nAssistant:"
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        print("An error occurred:", e)
        return "I'm sorry, I couldn't process that. Could we try again?"

@app.route('/')
def login():
    return render_template('index_home.html')

@app.route('/login')
def index_home():
    return render_template('login.html')

@app.route('/login_check', methods=['POST'])
def login_check():
    username = request.form['username']
    password = request.form['password']
    q = "SELECT * FROM `user_reg` WHERE `username`='%s' and `password`='%s'" % (username, password)
    res = select(q)
    if res:
        session['user_reg_id'] = res[0]['user_reg_id']
        return "<script>alert('Login Successful');window.location='/user_home';</script>"
    else:
        return "<script>alert('Invalid Username or Password');window.location='/login';</script>"

@app.route('/user_reg')
def user_reg():
    return render_template('user_reg.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    place = request.form['place']
    phone = request.form['phone']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    
    q = "SELECT * FROM `user_reg` WHERE `email`='%s' or `username`='%s'" % (email, username)
    res = select(q)
    if res:
        return "<script>alert('User already exists');window.location='/user_reg';</script>"
    else:
        q = "INSERT INTO `user_reg`(`first_name`, `last_name`, `gender`, `place`, `phone`, `email`, `username`, `password`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (first_name, last_name, gender, place, phone, email, username, password)
        insert(q)
        return "<script>alert('Registration Successful');window.location='/login';</script>"

@app.route('/user_home')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid request. Please send a 'message' key."}), 400

    user_message = data.get('message', '').replace("'", "")
    
    # Check for negative queries
    for query in negative_queries:
        if query.lower() in user_message.lower():
            return jsonify({
                "response": "Let's talk about something else. How are you feeling today?",
                "end_chat": False
            })

    # Check if the user wants to exit
    if similarity(user_message.lower(), "yes") > 0.8 or "exit" in user_message.lower():
        return jsonify({
            "response": "Thank you for talking with me. Remember, you are not alone. Please take care, and seek support whenever needed.",
            "end_chat": True
        })

    # Generate empathetic response using Gemini
    gemini_response = generate_gemini_response(user_message)
    response_message = f"{gemini_response}\n\nWould you like to continue talking about this or share something else?"
    
    # Store chat in database
    q = "INSERT INTO `chat` VALUES (null,'%s','%s','%s',CURRENT_TIMESTAMP())" % (
        session['user_reg_id'], user_message, response_message.replace("'", ""))
    insert(q)

    return jsonify({
        "response": response_message,
        "end_chat": False
    })

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

@app.route('/feelings')
def feelings():
    data = {}
    return render_template('feelings.html', data=data)

@app.route('/insert_feelings', methods=['POST'])
def insert_feelings():
    data = {}
    feelings = request.form['feelingsText']
    from bert import mind_feelings
    mind = mind_feelings(feelings)
    data['results'] = mind
    return render_template('feelings.html', data=data)

@app.route('/view_history')
def view_history():
    data = {}
    q = "SELECT * FROM `chat` WHERE `user_reg_id`='%s' order by chat_id desc" % (session['user_reg_id'])
    res = select(q)
    if res:
        data['res'] = res
    return render_template('history.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5034) 