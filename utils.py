import os
import numpy as np
from openai import OpenAI

# 블랙리스트 및 컨텍스트 키워드
KEYWORDS_BLACKLIST = ['리뷰', 'zㅣ쀼', 'ZI쀼', 'Zl쀼', '리쀼', '찜', '이벤트', '추가', '소스']
KEYWORDS_CONTEXT = ['해장', '숙취', '다이어트']

def is_valid_menu(menu_name):
    """메뉴명이 블랙리스트에 포함되지 않았는지 확인"""
    return not any(keyword in menu_name for keyword in KEYWORDS_BLACKLIST)

def extract_keywords(review_text):
    """리뷰 텍스트에서 컨텍스트와 관련된 키워드 추출"""
    keywords = []
    for word in review_text.split():
        if any(keyword in word for keyword in KEYWORDS_CONTEXT):
            keywords.append(word)
    return keywords

def get_embedding(text, model='text-embedding-3-small'):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    response = client.embeddings.create(
        input=text,
        model=model
    )
    return response.data[0].embedding

def get_embeddings(texts, model='text-embedding-3-small'):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    response = client.embeddings.create(
        input=texts,
        model=model
    )
    return [data.embedding for data in response.data]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def call_openai(prompt, temperature=0.0, model='gpt-4o-2024-08-06'):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    completion = client.chat.completions.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        temperature=temperature
    )
    return completion.choices[0].message.content
