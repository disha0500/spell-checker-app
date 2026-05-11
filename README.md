# 📝 Spell Checker Using Minimum Edit Distance

A simple and interactive Spell Checker Web Application developed using Python and Streamlit.  
The project uses the **Minimum Edit Distance (Levenshtein Distance)** algorithm to detect spelling mistakes and suggest the closest correct word from a dictionary dataset.

---

# 🚀 Features

- Spell checking using Minimum Edit Distance
- Suggests nearest correct word
- Interactive web interface using Streamlit
- Lightweight and beginner-friendly
- Real-world examples included
- Public deployment support using Streamlit Cloud

---

# 🛠 Technologies Used

- Python
- Streamlit
- TextDistance Library

---

# 📂 Project Structure

```text
spell-checker-app/
│
├── app.py
├── words.txt
├── requirements.txt
└── README.md
📥 Installation
Step 1: Clone Repository
git clone https://github.com/your-username/spell-checker-app.git
Step 2: Open Project Folder
cd spell-checker-app
Step 3: Install Required Packages
pip install -r requirements.txt
▶ Running the Application

Run the following command:

python -m streamlit run app.py

The application will open in your browser at:

http://localhost:8501
🌐 Live Demo

Add your deployed Streamlit link here:

https://your-app-name.streamlit.app
📖 How It Works
User enters a word
Application compares the word with dictionary words
Minimum Edit Distance is calculated
Closest matching word is suggested
🧠 Minimum Edit Distance

Minimum Edit Distance calculates the minimum number of operations required to convert one word into another.

Operations include:

Insertion
Deletion
Replacement

Example:

speling → spelling

📌 Future Enhancements
Sentence spell checking
Grammar correction
Voice input support
AI-powered suggestions
Dark mode UI

👩‍💻 Author

Disha Prakasha
Rithika K

📄 License

This project is created for educational and learning purposes.
