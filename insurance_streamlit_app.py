import streamlit as st
from openai import OpenAI

# Initialize OpenAI client using Streamlit's secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Title of the app
st.title("Insurance Advisor")

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

# Collect user input for query
user_input = st.chat_input("Describe your insurance query here...")

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
  rejection_message = "This chat is strictly about insurance related. Please ask insurance-related questions."
  st.session_state.messages.append({"role": "assistant", "content": rejection_message})
  with st.chat_message("assistant"):
      st.markdown(rejection_message)
