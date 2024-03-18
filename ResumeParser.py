from pypdf import PdfReader
from openai import OpenAI

client = OpenAI()

reader = PdfReader("sample.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": 'Process the given file to read data and structure it in a JSON format including details and structure like this: "collegeName": ,"yearOfGraduation":,"major":,}],"employmentHistory": [{"companyName": ,"startDate":,"endDate":,"title":,"workDescription":}],}Make sure the date formats are dd-mm-yyyy'},
    {"role": "user", "content": text},
  ]
)
print(response.choices[0].message.content)



