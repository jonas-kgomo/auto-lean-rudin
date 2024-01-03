import subprocess
import uuid
import os
import requests
import argparse

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


def nougat_ocr(file_name):
    cli_command = (
        'nougat '
        f'--out output '
        f'pdf {file_name} '
        f'--checkpoint nougat '
        '--markdown'
    )
    print("running---------os.system")
    os.system(cli_command)

def predict(pdf_file, pdf_link):
    if pdf_file is None and pdf_link == '':
        print("No file is uploaded, and no link is provided.")
        return "No data provided. Upload a pdf file or provide a pdf link and try again!"

    if pdf_file is not None:
        file_name = pdf_file
    else:
        file_name = get_pdf(pdf_link)

    print(f'file_name is - {file_name}')
    nougat_ocr(file_name)

    file_name = file_name.split('/')[-1][:-4]
    with open(f'output/{file_name}.mmd', 'r') as file:
        content = file.read()

    content = content.replace(r'\(', '$').replace(r'\)', '$').replace(r'\[', '$$').replace(r'\]', '$$')
    return content

def main(args):
    pdf_file = args.pdf_file
    pdf_link = args.pdf_link

    result = predict(pdf_file, pdf_link)
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nougat OCR Demo")
    parser.add_argument("--pdf_file", help="Path to the PDF file")
    parser.add_argument("--pdf_link", help="Link to the PDF file")

    args = parser.parse_args()
    main(args)
