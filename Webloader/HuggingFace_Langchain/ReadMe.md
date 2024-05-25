Langchain Hugging Face LLM Integration
This project demonstrates how to call Hugging Face Large Language Models (LLMs) directly from Langchain code.

Partner Package

This project utilizes a new partner package co-developed by Hugging Face and Langchain. This package simplifies the process of integrating Hugging Face LLMs into your Langchain workflows.

Calling Hugging Face LLMs

The following steps outline how to call Hugging Face LLMs from Langchain:

Installation:

Install the required libraries:

Langchain
Transformers
Hugging Face
Use a package manager like pip:

Bash
pip install langchain transformers huggingface-hub
Use code with caution.
content_copy
Import Libraries:

Import the necessary libraries in your Langchain code:

Python
import langchain
from transformers import pipeline
Use code with caution.
content_copy
Specify Model and Task:

Define the Hugging Face model ID and the desired task (e.g., text generation).

Pipeline Setup:

Create a pipeline using the pipeline function from the transformers library:

Python
model_name = " hugging-face-model-id"
task = "text-generation"  # Replace with desired task

pipe = pipeline(task, model=model_name)
Use code with caution.
content_copy
Call the Model:

Provide the prompt or query to the pipeline:

Python
prompt = "Write a poem about nature."
output = pipe(prompt)
Use code with caution.
content_copy
Process Output:

The pipeline will return the model's output. Process or display the output as needed.

Hugging Face Hub API Token

The video mentions that you can leverage a Hugging Face Hub API token to call the entire model. Refer to the Hugging Face documentation for details on creating and using API tokens https://huggingface.co/docs/hub/en/security-tokens.

Further Exploration

This project provides a foundational example. Explore the Langchain and Hugging Face documentation for more advanced use cases and customizations.

Langchain Docs: https://readthedocs.org/projects/langchain/
Hugging Face Transformers: https://huggingface.co/docs/transformers/en/index