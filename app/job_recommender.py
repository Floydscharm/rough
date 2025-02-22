import pandas as pd
import re

# Load dataset
df = pd.read_csv('structured_linkdin_data.csv')

# Clean job descriptions
def clean_text(text):
    text = re.sub(r'<.*?>', '', str(text))  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    return text.lower()

df['cleaned_description'] = df['structured_linkdin_data.csv'].apply(clean_text)

import spacy

nlp = spacy.load('en_core_web_sm')

def extract_skills_nlp(text):
    doc = nlp(text)
    return [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]

df['nlp_skills'] = df['cleaned_description'].apply(extract_skills_nlp)
from collections import Counter

# Flatten all skills into one list
all_skills = [skill for sublist in df['extracted_skills'] for skill in sublist]

# Count skill frequencies
skill_counts = Counter(all_skills)

# Convert to dataframe for better visualization
skill_df = pd.DataFrame(skill_counts.items(), columns=['Skill', 'Count']).sort_values(by='Count', ascending=False)
print(skill_df.head(20))

from collections import Counter

# Flatten all skills into one list
all_skills = [skill for sublist in df['extracted_skills'] for skill in sublist]

# Count skill frequencies
skill_counts = Counter(all_skills)

# Convert to dataframe for better visualization
skill_df = pd.DataFrame(skill_counts.items(), columns=['Skill', 'Count']).sort_values(by='Count', ascending=False)
print(skill_df.head(20))

