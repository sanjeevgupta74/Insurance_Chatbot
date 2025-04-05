import streamlit as st
from openai import OpenAI

# Initialize OpenAI client using Streamlit's secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Title of the app
st.title("Health Tips Advisor")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    role, content = message["role"], message["content"]
    with st.chat_message(role):
        st.markdown(content)

# Function to validate user input
def is_health_related(query):
    """
    Check if the query is related to health tips.
    Returns True if related, False otherwise.
    """
    # Define keywords related to health tips
    health_keywords = [
        "symptom", "remedy", "health", "diet", "nutrition", "exercise", "fitness",
        "wellness", "illness", "disease", "pain", "medicine", "treatment", "recovery"
    ]
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in health_keywords)

# Collect user input for symptoms
user_input = st.chat_input("Describe your symptoms here...")

# Function to get a response from OpenAI with health advice
def get_response(prompt):
    # Ensure the assistant only provides fact-based, general health advice
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (
                "You are a Health Tips Advisor. Your responses must be strictly related to health tips, "
                "general remedies, or wellness advice. Avoid personal opinions, speculation, or entertainment. "
                "If the query is unrelated to health, respond with: "
                "'This chat is strictly about health tips. Please ask health-related questions.'"
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
    # Validate if the input is health-related
 #   if is_health_related(user_input):
        # Append user's message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate assistant's response
        assistant_prompt = f"User has reported the following symptoms: {user_input}. Provide a general remedy or advice."
        assistant_response = get_response(assistant_prompt)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
  #    else:
else:
# Reject off-topic queries
  rejection_message = "This chat is strictly about health tips. Please ask health-related questions."
  st.session_state.messages.append({"role": "assistant", "content": rejection_message})
  with st.chat_message("assistant"):
      st.markdown(rejection_message)
