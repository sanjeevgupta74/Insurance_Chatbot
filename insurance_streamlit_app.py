import streamlit as st
from openai import OpenAI

# Initialize OpenAI client using Streamlit's secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page configuration
# Title of the app
st.set_page_config(
    page_title="Insurance Advisor Chatbot",
    page_icon="🛡️",
    layout="wide",
)

# Custom CSS for beautification
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #fdfbfb, #ebedee);
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
.title {
    text-align: center;
    color: #1f4e79;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Chat bubbles */
.stChatMessage.user {
    background-color: #e8f4ff;
    padding: 12px 18px;
    border-radius: 20px;
    margin: 8px 0;
    border: 1px solid #b3daff;
}

.stChatMessage.assistant {
    background-color: #f4f4f4;
    padding: 12px 18px;
    border-radius: 20px;
    margin: 8px 0;
    border: 1px solid #ddd;
}

/* Input box */
.css-1y4p8pa {
    border-radius: 12px !important;
}

/* Sidebar */
.sidebar .sidebar-content {
    background-color: #f7faff;
    padding: 20px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>🛡️ Insurance Advisor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Your trusted AI-powered guide for insurance queries</p>", unsafe_allow_html=True)

# Sidebar info
with st.sidebar:
    st.header("ℹ️ About")
    st.write("This Insurance Advisor helps answer general insurance-related questions. Please note that it provides **general guidance only** and should not be considered as professional legal or financial advice.")
    st.divider()
    st.caption("Version 1.0 | Powered by OpenAI")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    role, content = message["role"], message["content"]
    with st.chat_message(role):
        st.markdown(content)

# Function to validate user input
def is_insurance_related(query):
    """
    Check if the query is related to insurance.
    Returns True if related, False otherwise.
    """
    # Define keywords related to insurance
    insurance_keywords = [
        "insurance", "policy", "coverage", "premium", "claim", "deductible", "benefit",
        "provider", "network", "enrollment", "underwriting", "exclusion", "limitation", 
        "travel insurance", "health insurance", "life insurance", "auto insurance", 
        "home insurance", "disability insurance", "long-term care insurance", "liability insurance",
        "property insurance", "workers' compensation", "medicare", "medicaid", 
        "reimbursement", "copay", "coinsurance", "out-of-pocket", "pre-existing condition",
        "renewal", "cancellation", "grace period", "waiting period", "claim denial",
        "insurance fraud", "risk assessment", "actuary", "underwriter",
        "insurance agent", "broker", "insurer", "insured", "third-party administrator",
        "beneficiary", "policyholder", "rider", "endorsement", "subrogation",
        "adjuster", "loss", "liability", "premium tax", "self-insurance", "umbrella policy", "general insurance"
    ]
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in insurance_keywords)

# Function to get a response from OpenAI with insurance advice
def get_response(prompt):
    # Ensure the assistant only provides fact-based, general insurance advice
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (
                "You are an Insurance Advisor. Your responses must be strictly related to insurance advice, "
                "Avoid personal opinions, speculation, or entertainment. "
                "If the query is unrelated to insurance, respond with: "
                "'This chat is strictly about insurance. Please ask insurance-related questions.'"
            )},
            *[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            {"role": "user", "content": prompt}
        ]
    )
    # Access the content directly as an attribute
    return response.choices[0].message.content

# Collect user input for query
user_input = st.chat_input("💬 Ask your insurance related question here...")

# Process and display response if there's input
if user_input:
    # Validate if the input is insurance-related
    if is_insurance_related(user_input):
        # Append user's message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate assistant's response
        assistant_prompt = f"User has reported the following insurance query: {user_input}. Provide an insurance related advice."
        assistant_response = get_response(assistant_prompt)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
  #    else:
else:
# Reject off-topic queries
  rejection_message = "⚠️ This chat is strictly about **insurance related**. Please rephrase your query."
  st.session_state.messages.append({"role": "assistant", "content": rejection_message})
  with st.chat_message("assistant"):
      st.markdown(rejection_message)
