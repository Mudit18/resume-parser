from pypdf import PdfReader
from openai import OpenAI

client = OpenAI()

reader = PdfReader("sample.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"content": text}
  ]
)
print(response.choices[0].message.content)
