# Nougat OCR

## Introduction
This repository contains the source code for Nougat OCR, a tool for Optical Character Recognition (OCR) using the Nougat model. Follow the instructions below to set up the environment and run the OCR.

## Installation
1. Clone this repository:
   ```bash
   
   git clone https://github.com/cudanexus/nougat.git
   ```

2. Download the model files from Hugging Face using Git LFS: 
- Make sure you have Git LFS installed ([Git LFS Installation]() ) 
- Run the following commands:

```bash
git lfs install
git clone https://huggingface.co/spaces/tomriddle/nougat
``` 
## 2. After the above commands, your folder structure should look like this:

```lua
input
Upload nougat.pdf
nougat
output
Upload nougat.pdf
README.md
app.py
requirements.txt
``` 
## 3. Copy the `nougat` folder (which contains all model files) to the root of this repository. Your updated structure should look like:

```lua
input
nougat
--- config.json
--- pytorch_model.bin
--- special_tokens_map.json
--- tokenizer.json
--- tokenizer_config.json
output
app.py
cog.yaml
output.txt
predict.py
requirements.txt
``` 
## 4. Install the required Python packages:

```bash
pip install -r requirements.txt
```
## Testing

Ensure that everything is installed correctly by running:

```bash
python app.py --pdf_file input/nougat.pdf
```



If the installation is successful, you should see the OCR output.
## Additional Information

For any issues or questions, please refer to the [repository](https://github.com/cudanexus/nougat)  or contact the repository owner.
