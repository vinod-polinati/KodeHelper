# KodeHelper

This repository contains a simple Python script that interacts with the Gradio Zade API for text generation. The script uses the `requests` library for making API requests and the `gradio` library for creating a user interface.

## Setup

1. Make sure you have Python installed on your machine.
2. Install the required libraries using the following command:
3. Activate the environment.
4. Install requirements.txt

5. Clone this repository:

```bash
git clone https://github.com/vinod-polinati/KodeHelper.git
```

6. Navigate to the project directory:

```bash
cd KodeHelper
```

7. Open the `app.py` file and update the `url` variable with the correct Zade API endpoint.

## Usage

Run the script using the following command:

```bash
python app.py
```

This will launch a Gradio interface where you can enter your prompt in the provided textbox. The generated response will be displayed on the interface.

## Code Explanation

The main functionality is in the `generate_response` function, which sends a prompt to the KodeHelper and returns the generated text. The Gradio interface is created using the `gr.Interface` class, taking input from a textbox and displaying the output as text.
