from pypdf import PdfReader
from openai import OpenAI

client = OpenAI()

reader = PdfReader("sample/sample.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

jd_path = './sample/sample_jd.txt'
with open(jd_path, 'r') as file:
    jd_text = file.read()

# printing the pdf file's text
# print(text)
    
# print(jd_text)

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": 'Process the given resume data and job description to check if the resume matches the jd and give me a percentage for the match. Job description: ' + jd_text},
    {"role": "user", "content": text},
  ]
)
print(response.choices[0].message.content)