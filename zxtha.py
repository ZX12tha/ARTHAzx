from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# User must set their own API key
API_KEY = os.getenv('GROQ_API_KEY', 'PASTE_YOUR_API_KEY_HERE')

@app.route('/')
def home():
    return '''
    <html>
    <body>
        <h1>🤖 ZXTHA AI</h1>
        <p>Uncensored AI Chatbot</p>
        <p><strong>⚠️ Important:</strong> Add your Groq API key in the code!</p>
    </body>
    </html>
    '''

@app.route('/chat', methods=['POST'])
def chat():
    if API_KEY == 'PASTE_YOUR_API_KEY_HERE':
        return jsonify({"response": "❌ Please add your Groq API key first!"})
    
    data = request.json
    user_msg = data.get('message', '')
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Kamu adalah ZXTHA AI yang helpful"},
            {"role": "user", "content": user_msg}
        ]
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            ai_response = result["choices"][0]["message"]["content"]
            return jsonify({"response": ai_response})
        else:
            return jsonify({"response": "❌ API Error - Check your API key"})
            
    except Exception as e:
        return jsonify({"response": f"❌ Connection error: {str(e)}"})

if __name__ == '__main__':
    print("🚀 ZXTHA AI Starting...")
    print("📍 http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
