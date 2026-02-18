import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Simple Q&A App", page_icon="❓", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("❓ Simple Q&A App")
st.markdown("### Ask me anything! Powered by LangChain & Groq 🚀")
st.divider()

@st.cache_resource
def load_model():
    try:
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.7,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        return llm
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

with st.spinner("🔄 Loading..."):
    llm = load_model()

if llm is None:
    st.error("⚠️ Check your API key in .env file")
    st.stop()

st.subheader("💬 Ask Your Question")
user_question = st.text_area("Type your question here:", height=100, placeholder="Example: What is artificial intelligence?")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submit_button = st.button("🚀 Get Answer")

if submit_button:
    if user_question.strip():
        with st.spinner("🤔 Thinking..."):
            try:
                response = llm.invoke(user_question)
                st.success("✅ Answer:")
                st.write(response.content)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a question!")

with st.sidebar:
    st.header("ℹ️ About")
    st.info("""
    **Simple Q&A App**
    
    This app uses:
    - 🦜 LangChain Framework
    - ⚡ Groq AI (Llama3-8b)
    - 🎨 Streamlit Interface
    
    **How to use:**
    1. Type your question
    2. Click "Get Answer"
    3. Get instant AI response!
    """)
    
    st.divider()
    
    st.markdown("**Example Questions:**")
    example_questions = [
        "What is machine learning?",
        "Explain Python in simple terms",
        "What is the capital of Egypt?",
        "How does photosynthesis work?",
        "What is LangChain?"
    ]
    
    for i, question in enumerate(example_questions, 1):
        st.markdown(f"{i}. {question}")
    
    st.divider()
    
    st.markdown("**Built by:** [Youssef Khaled](https://youssefkhaledportfolio.netlify.app)")

st.divider()
st.caption("Made with ❤️ using LangChain & Streamlit | © 2025")