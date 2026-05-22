# Construction Safety Advisor

AI-powered safety advisor for construction sites using LangChain and Claude API.

## 🌐 Live Demo

[Try it online](https://construction-safety-advisor-abhigyan.streamlit.app)

## Key Features

✅ Worker Safety Assessment — Risk evaluation based on profile  
✅ Hazard Identification — Site-specific hazard mitigation  
✅ Emergency Protocols — Step-by-step incident response  
✅ Multi-turn Conversation — Context-aware dialogue  
✅ Tool-Calling Agent — Claude with specialized functions  

## Tech Stack

- LangChain (agent framework)
- Claude 3.5 Sonnet (LLM)
- Streamlit (UI)
- Python 3.8+

## Setup

### 1. Install
```bash
pip install -r requirements.txt
```

### 2. Add API Key
Create `.env`:
```bash
ANTHROPIC_API_KEY=your_key_from_console.anthropic.com
```
### 3. Run Locally
```bash
streamlit run app.py
```

### 4. Deploy to Streamlit Cloud
```bash
git push
# Go to streamlit.io/cloud
# Add ANTHROPIC_API_KEY to secrets
# Deploy
```

## How It Works

Claude AI agent with 3 tools:
1. `assess_worker_safety()` — Risk scoring
2. `identify_site_hazards()` — Hazard mitigation
3. `get_emergency_protocol()` — Emergency steps

## Example
User: "Is it safe for a 23-year-old electrician with 6 months experience on high voltage?"
Advisor: Risk Score: 72/100 (HIGH)
Recommendations:

Intensive safety training
Assigned mentor for all tasks
Mandatory PPE
Regular safety briefings
Limited initial assignments

## Future Improvements

- OSHA database integration
- Incident tracking
- Real-time hazard detection
- Mobile app

## License

MIT