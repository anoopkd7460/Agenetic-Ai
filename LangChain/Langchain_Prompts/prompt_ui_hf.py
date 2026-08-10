from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

# Load environment variables
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.3
)

model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.set_page_config(page_title="Research Paper Summarizer", page_icon="📚")

st.title("AI Research Paper Summarizer")

paper_input = st.selectbox(
    "Select Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-friendly",
        "Technical",
        "Code-oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (Detailed explanation)"
    ]
)

# Prompt Template
template = PromptTemplate(
    template="""
You are an expert AI Research Assistant.

Summarize the research paper titled:

"{paper_input}"

Follow these instructions carefully:

Explanation Style:
{style_input}

Explanation Length:
{length_input}

Include the following sections:

1. Main Objective
2. Problem Statement
3. Key Contributions
4. Model/Architecture
5. Important Mathematical Concepts or Equations (if available)
6. Working Explanation
7. Simple Real-world Analogy
8. Advantages
9. Limitations
10. Real-world Applications

If applicable, include simple Python or pseudocode snippets.

Do NOT make up information.
If any information is unavailable, write:
"Insufficient information available."

Generate the response in proper Markdown format using headings and bullet points.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

# Fill the prompt
prompt = template.invoke(
    {
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    }
)

# Generate response
if st.button("Summarize Paper"):
    with st.spinner("Generating Summary..."):
        result = model.invoke(prompt)
    st.success("Summary Generated Successfully!")
    st.markdown(result.content)