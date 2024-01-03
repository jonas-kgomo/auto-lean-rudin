import subprocess
import uuid
import os
import requests
import argparse
from cog import BasePredictor, Path, Input,BaseModel,File
def get_pdf(pdf_link):
    # Generate a unique filename
    unique_filename = f"input/downloaded_paper_{uuid.uuid4().hex}.pdf"

    # Send a GET request to the PDF link
    response = requests.get(pdf_link)

    if response.status_code == 200:
        # Save the PDF content to a local file
        with open(unique_filename, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print("PDF downloaded successfully.")
    else:
        print("Failed to download the PDF.")
    return unique_filename

import os
import time

def nougat_ocr(file_name):
    cli_command = [
        'nougat',
        '--out', 'output',
        'pdf', f'{file_name}',
        '--checkpoint', 'nougat',
        '--markdown','--no-skipping'
    ]
    print("running---------subprocess")
    output = subprocess.run(cli_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(output)

class Predictor(BasePredictor):
  def predict(self,pdf_file:Path =Input(description="input the pdf"))->Path:
        pdf_link=None
        if pdf_file is None and pdf_link == '':
            print("No file is uploaded, and no link is provided.")
            return "No data provided. Upload a pdf file or provide a pdf link and try again!"
        if pdf_file is not None:
            file_name = pdf_file
        else:
            file_name = get_pdf(pdf_link)

        print(f'file_name is - {file_name}')
        # Print the contents of the current working directory
        nougat_ocr(file_name)
        # time.sleep(12)


        file_name=str(file_name)
        file_name = file_name.split('/')[-1][:-4]
        with open(f'output/{file_name}.mmd', 'r') as file:
            content = file.read()
        import os
        cwd = os.getcwd()
        print("-----------------",cwd)

        content = content.replace(r'\(', '$').replace(r'\)', '$').replace(r'\[', '$$').replace(r'\]', '$$')
        markdown_output_file = f'/src/output/{file_name}_formatted.txt'
        with open(markdown_output_file, 'w') as markdown_file:
            markdown_file.write(content)
        print(markdown_output_file)
        return Path(markdown_output_file)
