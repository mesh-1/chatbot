# Simple Chatbot using DialoGPT

This project is a basic chatbot built using the DialoGPT-medium model from Microsoft.  
The chatbot runs in a simple Python loop and generates responses based on user input.

## Features
- Uses the DialoGPT-medium conversational AI model
- Maintains conversation history
- Runs locally or in Google Colab
- Lightweight and easy to modify

## Installation

1. Clone the repository:
   git clone https://github.com/<mesh-1>/<chatbot>.git
   cd <repo-name>

2. Install dependencies:
   pip install -r requirements.txt

## Running the Chatbot

Run the script:
   python chatbot.py

The chatbot will start and wait for your input:
   Chatbot Ready!
   You:

## Model Used
DialoGPT-medium (Microsoft)  
A pretrained conversational model based on the Transformer architecture.

## Project Structure

chatbot.py        → Main chatbot script  
requirements.txt  → List of required libraries  
README.md         → Project documentation

## Requirements

transformers  
torch  
jupyter  

## Notes
- DialoGPT may sometimes generate unexpected or random replies.
- For more accurate behavior, you can fine-tune the model on your own dataset.

