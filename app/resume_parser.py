# from google-genai import GeminiClient
from google import genai
import yaml
from google import genai

client = genai.Client(api_key="AIzaSyBkyRStcMREJ9wDNHt0-7yi8Ck0nTqflvw")





def ats_extractor(resume_data):
    prompt = ''' 
    You are an AI bot designed to act as a professional for parsing resumes. You are given with resume and your job is to extract the following information from the resume:
    1. full name
    2. email id
    3. github portfolio
    4. linkedin id
    5. employment details
    6. technical skills
    7. soft skills
    Give the extracted information in json format only
    '''
    # GeminiClient =GeminiClient(
        # api_key = api_key
    # )    

    messages=[
        {"role": "system", 
        "content": prompt}
        ]
    
    user_content = 'Who is Shahrukh Khan'
    
   

    response = client.models.generate_content(
    
                model="gemini-2.0-flash",
                contents = user_content)
        
    
                            
    candidates = response.candidates
    text = candidates[0].content.parts[0].text
    print(text)


    # return data

# ats_extractor('D:/FastAPI/app/13014900.pdf')