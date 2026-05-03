import streamlit as st
import json
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
import dotenv
import os

prompt='''
From the below article extract the heading of the news and less than 300  words about the news return in json format each entry have title and news
only return the json format no preamble
analyze the article and set the title it should be professional and extract each and every news from the article
Article
============
{article}
'''
from dotenv import load_dotenv
load_dotenv()
pt=PromptTemplate.from_template(prompt)
api_key = "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"
llm=ChatGroq(model_name="llama-3.3-70b-versatile",groq_api_key=api_key)
chain=pt | llm

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="News Summarizer",
    page_icon="📰",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #eef2ff, #fdf2f8);
        }
        .title {
            font-size: 42px;
            font-weight: 700;
            text-align: center;
            color: #4f46e5;
        }
        .subtitle {
            text-align: center;
            color: #6b7280;
            margin-bottom: 30px;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
            margin-top: 20px;
        }
        .heading {
            font-size: 22px;
            font-weight: 600;
            color: #111827;
        }
        .summary {
            font-size: 15px;
            color: #374151;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">📰 News Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Extract multiple news insights from a paragraph</div>', unsafe_allow_html=True)

# ---------- INPUT ----------
news_input = st.text_area("Enter News Paragraph", height=200)

# ---------- YOUR FUNCTION ----------
def extract_news(text):
    response = chain.invoke({'article': text})
    data = json.loads(response.content)
    return data

# ---------- BUTTON ----------
if st.button("✨ Extract"):
    if news_input.strip() == "":
        st.warning("Please enter some news content.")
    else:
        try:
            result = extract_news(news_input)

            # Convert string → JSON if needed
            if isinstance(result, str):
                result = json.loads(result)

            # Normalize to list
            if isinstance(result, dict):
                result = [result]

            # ---------- DISPLAY ----------
            for i, item in enumerate(result):
                title = item.get("title", f"News {i+1}")
                summary = item.get("news", "No summary available")

                st.markdown(f"""
                    <div class="card">
                        <div class="heading">📰 {title}</div>
                        <div class="summary">{summary}</div>
                    </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error processing result: {e}")