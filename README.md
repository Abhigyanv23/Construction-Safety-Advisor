# Construction Safety Advisor

AI-powered safety advisor for construction sites using LangGraph and the Google Gemini API. Because apparently humans keep building giant metal death traps and then acting surprised when safety matters.

---

## 🌐 Live Demo

🚀 [Try it Online](https://construction-safety-advisor-abhigyan.streamlit.app)

---

## ✨ Key Features

- ✅ **Worker Safety Assessment**  
  Risk evaluation based on worker profile, experience, and task type.

- ✅ **Hazard Identification**  
  Site-specific hazard detection and mitigation recommendations.

- ✅ **Emergency Protocols**  
  Step-by-step emergency response guidance for critical situations.

- ✅ **Multi-turn Conversations**  
  Context-aware AI interaction using conversational memory.

- ✅ **Tool-Calling Agent**  
  Gemini-powered agent integrated with specialized safety tools.

---

## 🛠️ Tech Stack

- **LangGraph** & **LangChain** — Agent workflow framework  
- **Google Gemini 3.5 Flash** — Large Language Model  
- **Streamlit** — Frontend UI  
- **Python 3.8+**

---

## 📂 Project Structure

```bash
├── app.py                     # Streamlit frontend
├── safety_advisor.py          # Main AI safety agent
├── tools.py                   # Specialized safety tools
├── requirements.txt           # Project dependencies
├── .env                       # API key configuration
└── README.md                  # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/construction-safety-advisor.git
cd construction-safety-advisor
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add Your API Key

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_key_from_aistudio.google.com
```

> Important: Add `.env` to your `.gitignore` file so your API key does not end up publicly displayed for the entire internet to harvest like abandoned copper wiring.

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## ☁️ Deploy to Streamlit Cloud

```bash
git push origin main
```

Then:

1. Open **Streamlit Community Cloud**
2. Select your repository
3. Go to **App Settings → Secrets**
4. Add:

```env
GOOGLE_API_KEY="your_api_key_here"
```

5. Save and Deploy

---

## 🧠 How It Works

The application uses a **LangGraph ReAct Agent** powered by **Google Gemini** with three specialized safety tools:

### 🔹 `assess_worker_safety()`
- Calculates worker risk score
- Evaluates experience level
- Provides safety recommendations

### 🔹 `identify_site_hazards()`
- Detects construction site hazards
- Covers:
  - Falls
  - Fire hazards
  - Electrical risks
  - Equipment dangers

### 🔹 `get_emergency_protocol()`
- Generates emergency response procedures
- Handles:
  - Injuries
  - Fires
  - Chemical spills
  - Electrical incidents

---

## 💬 Example Interaction

### User Input

```text
Is it safe for a 23-year-old electrician with 6 months experience working on high voltage systems?
```

### AI Response

```text
Risk Score: 72/100 (HIGH)

Recommendations:
- Intensive safety training
- Assigned mentor supervision
- Mandatory PPE usage
- Daily safety briefings
- Restricted high-risk assignments initially
```

---

## 🚀 Future Improvements

- OSHA database integration
- Incident tracking dashboard
- Real-time hazard detection
- Voice-enabled assistant
- Mobile application support
- Worker analytics and reporting

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Developed by **Abhigyan Varma**

- GitHub: https://github.com/Abhigyanv23
- LinkedIn: https://www.linkedin.com/in/abhigyan-varma-199074293
