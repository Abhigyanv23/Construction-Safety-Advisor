from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv

load_dotenv()

# We swapped the LLM here!
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

@tool
def assess_worker_safety(worker_type: str, age: int, experience_years: int) -> dict:
    """Assess safety risk for construction worker based on profile."""
    risk_score = 50
    
    if age < 25:
        risk_score += 10
    elif age > 60:
        risk_score += 15
    
    if experience_years < 1:
        risk_score += 20
    elif experience_years > 10:
        risk_score -= 15
    
    dangerous_roles = {
        'crane operator': 25,
        'high altitude worker': 30,
        'electrician': 20,
        'heavy equipment operator': 22
    }
    risk_score += dangerous_roles.get(worker_type.lower(), 5)
    risk_score = max(0, min(100, risk_score))
    
    if risk_score < 30:
        risk_level = "LOW"
        recommendation = "Worker has good safety profile. Continue standard protocols."
    elif risk_score < 60:
        risk_level = "MODERATE"
        recommendation = "Worker requires regular safety training. Monitor closely."
    elif risk_score < 80:
        risk_level = "HIGH"
        recommendation = "Worker needs intensive safety supervision. Consider reassignment."
    else:
        risk_level = "CRITICAL"
        recommendation = "Worker unsuitable for this role without extensive training."
    
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "worker_type": worker_type,
        "age": age,
        "experience": experience_years,
        "recommendation": recommendation
    }

@tool
def identify_site_hazards(hazard_type: str, location: str) -> dict:
    """Identify potential hazards at construction site."""
    hazards_db = {
        ('fall', 'roof'): {
            'severity': 'CRITICAL',
            'description': 'High risk of falling from height',
            'mitigation': [
                'Mandatory harness and safety line',
                'Install guardrails at edges',
                'Use safety nets below work area',
                'Regular equipment inspections'
            ]
        },
        ('electrical', 'basement'): {
            'severity': 'HIGH',
            'description': 'Risk of electrical shock from wet environment',
            'mitigation': [
                'Use GFCI outlets',
                'Keep moisture levels low',
                'Insulated tools only',
                'Regular electrical audits'
            ]
        },
        ('fire', 'site'): {
            'severity': 'CRITICAL',
            'description': 'Fire hazard from flammable materials',
            'mitigation': [
                'No smoking signs posted',
                'Fire extinguishers available',
                'Clear emergency exits',
                'Regular fire drills'
            ]
        }
    }
    
    hazard_key = (hazard_type.lower(), location.lower())
    hazard_info = hazards_db.get(hazard_key, {
        'severity': 'MODERATE',
        'description': f'{hazard_type} hazard at {location}',
        'mitigation': [
            'Conduct risk assessment',
            'Implement site-specific controls',
            'Train workers on hazards',
            'Regular safety inspections'
        ]
    })
    
    return {
        'hazard_type': hazard_type,
        'location': location,
        'severity': hazard_info['severity'],
        'description': hazard_info['description'],
        'mitigation_strategies': hazard_info['mitigation']
    }

@tool
def get_emergency_protocol(incident_type: str) -> dict:
    """Get emergency response protocol for construction incidents."""
    protocols = {
        'injury': {
            'priority': 'CRITICAL',
            'steps': [
                '1. STOP all work immediately',
                '2. Call emergency services (911)',
                '3. Do not move injured person',
                '4. Provide first aid if trained',
                '5. Document scene',
                '6. Notify supervisor',
                '7. Secure area'
            ]
        },
        'fire': {
            'priority': 'CRITICAL',
            'steps': [
                '1. Sound alarm immediately',
                '2. Evacuate all personnel',
                '3. Call 911',
                '4. Use fire extinguisher if safe',
                '5. Close doors to contain fire',
                '6. Account for all workers',
                '7. Wait for emergency services'
            ]
        },
        'chemical spill': {
            'priority': 'HIGH',
            'steps': [
                '1. Evacuate personnel',
                '2. Identify chemical',
                '3. Use spill kit',
                '4. Prevent drain entry',
                '5. Dispose properly',
                '6. Notify authorities if needed',
                '7. Decontaminate area'
            ]
        }
    }
    
    protocol = protocols.get(incident_type.lower(), {
        'priority': 'HIGH',
        'steps': [
            '1. Evacuate if necessary',
            '2. Call emergency if critical',
            '3. Notify supervisor',
            '4. Document incident',
            '5. Secure area',
            '6. Follow company procedures'
        ]
    })
    
    return {
        'incident_type': incident_type,
        'priority': protocol['priority'],
        'steps': protocol['steps']
    }

class SafetyAdvisor:
    def __init__(self):
        tools = [assess_worker_safety, identify_site_hazards, get_emergency_protocol]
        self.system_message = "You are an expert Construction Safety Advisor. Use your tools to provide specific, actionable safety advice. Always prioritize worker safety."
        
        self.agent = create_react_agent(llm, tools)
        self.chat_history = []
    
    def chat(self, user_message: str) -> str:
        messages = [SystemMessage(content=self.system_message)] + self.chat_history + [HumanMessage(content=user_message)]
        
        response = self.agent.invoke({"messages": messages})
        
        assistant_message = response["messages"][-1].content
        
        self.chat_history.append(HumanMessage(content=user_message))
        self.chat_history.append(AIMessage(content=assistant_message))
        
        return assistant_message
    
    def reset_chat(self):
        self.chat_history = []

if __name__ == "__main__":
    advisor = SafetyAdvisor()
    print("Safety Advisor ready! Type 'quit' to exit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = advisor.chat(user_input)
        print(f"\nAdvisor: {response}\n")