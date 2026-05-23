import streamlit as st
from safety_advisor import SafetyAdvisor
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Construction Safety Advisor",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3050/3050159.png", width=80)
with col2:
    st.title("🏗️ Construction Safety Advisor")
    st.markdown("AI-powered safety guidance using Gemini & LangChain")

st.divider()

# Initialize session state (Updated to look for GOOGLE_API_KEY)
if "advisor" not in st.session_state:
    if not os.getenv("GOOGLE_API_KEY"):
        st.error("❌ GOOGLE_API_KEY not found in environment variables. Please check your .env file.")
        st.stop()
    st.session_state.advisor = SafetyAdvisor()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
with st.sidebar:
    st.header("About This Tool")
    st.markdown("""
    AI advisor for construction safety:
    - Assess worker safety risks
    - Identify site hazards
    - Emergency protocols
    """)
    
    st.divider()
    st.header("Example Prompts")
    examples = [
        "What are hazards of working on a roof?",
        "What should I do if there's a fire?",
        "Is a 23-year-old electrician with 6 months experience safe for high voltage?"
    ]
    
    for i, example in enumerate(examples, 1):
        if st.button(f"📌 {i}", key=f"ex_{i}"):
            st.session_state.user_input = example
    
    if st.button("🔄 Reset Chat"):
        st.session_state.chat_history = []
        st.session_state.advisor.reset_chat()
        st.rerun()

# Main chat
st.subheader("💬 Safety Advisor Chat")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.divider()

# Use session state to capture if an example button was clicked
button_prompt = st.session_state.pop("user_input", None)

# Use Streamlit's dedicated chat input which auto-clears!
chat_prompt = st.chat_input("Ask a safety question...")

# The actual prompt is either the button click OR the typed chat
active_prompt = button_prompt or chat_prompt

if active_prompt:
    with st.chat_message("user"):
        st.markdown(active_prompt)
    
    with st.spinner("🤔 Analyzing..."):
        response = st.session_state.advisor.chat(active_prompt)
    
    st.session_state.chat_history.append({"role": "user", "content": active_prompt})
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    st.rerun()

st.divider()
st.markdown("<p style='text-align:center; color:gray; font-size:12px;'>Built with LangChain, Gemini API, and Streamlit</p>", unsafe_allow_html=True)