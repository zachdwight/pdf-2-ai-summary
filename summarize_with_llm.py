import torch
# https://huggingface.co/prithivMLmods/Llama-Express.1-Tiny
from transformers import AutoModelForCausalLM, AutoTokenizer

# Path to your local model directory, this is just informational
# model_path = "prithivMLmods/Llama-Express.1-Tiny"

import PyPDF2
from transformers import pipeline

def extract_text_from_pdf(pdf_path):
  text = ""
  with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
      text += page.extract_text()
  return text

#identify the PDF to interrogate and then ingest/extract
pdf_path = "/home/company/contract.pdf"
contract_text = extract_text_from_pdf(pdf_path)

# there a lots of LLMs on Hugging face so I just picked one that kinda worked but mainly smaller this example
model_id = "prithivMLmods/Llama-Express.1-Tiny"

# setup the pipeline
pipe = pipeline(
  "text-generation",
  model=model_id,
  torch_dtype=torch.bfloat16,
  device_map="cuda",
)
messages = [
  {"role": "system", "content": "You are a lawyer."}, #define the characteristic of the responder or system role and define the prompt with the user role
  {"role": "user", "content": f""" 
    Could you summarize the following document, emphasizing legal points being made among the parties involved:

    Text: {contract_text}
    """

    },
]
outputs = pipe(
  messages,
  max_new_tokens=256,
)

#print out the response
print(outputs[0]["generated_text"][-1])

# not pretty but simply write out to text file - todo make this more stylish or to PDF template
x = str(outputs[0]["generated_text"][-1])
with open("my_file.txt", "w") as file:
  file.write(x)
