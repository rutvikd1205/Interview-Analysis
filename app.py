from flask import Flask, render_template, request, jsonify
import os
import requests
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = "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"
DEEPGRAM_API_KEY = "61c5ee4557b33c33767d8cd6efcb981ec811352f"
DEEPGRAM_ENDPOINT = "https://api.deepgram.com/v1/listen"

# Initialize OpenAI API
llm = OpenAI(temperature=0.6)

# Define the prompt template
input_variables = ["conversation"]
input_prompt = PromptTemplate(
    input_variables=input_variables,
    template="I want you to identify key traits or habits of each speaker based on the {conversation}.",
)


app = Flask(__name__)


# Function to transcribe speech using Deepgram
def transcribe_speech(file):
    headers = {"Authorization": f"Token {DEEPGRAM_API_KEY}"}
    files = {"files": file}
    response = requests.post(DEEPGRAM_ENDPOINT, headers=headers, files=files)
    if response.status_code == 200:
        try:
            speech_text = response.json()["results"]["channels"][0]["alternatives"][0][
                "transcript"
            ]
            return speech_text
        except KeyError:
            return None
    else:
        return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    if "file_input" in request.files:
        uploaded_file = request.files["file_input"]
        file_extension = os.path.splitext(uploaded_file.filename)[1].lower()
        if file_extension in (".txt", ".text"):
            conversation_text = uploaded_file.read().decode("latin-1")
            chain = LLMChain(
                llm=llm, prompt=input_prompt, verbose=True, output_key="insights"
            )
            speaker_insights = chain({"conversation": conversation_text})
            result = "Processed text: " + speaker_insights["insights"]
        elif file_extension in (".mp3", ".wav", ".ogg"):
            conversation_text = transcribe_speech(uploaded_file)
            chain = LLMChain(
                llm=llm, prompt=input_prompt, verbose=True, output_key="insights"
            )
            speaker_insights = chain({"conversation": conversation_text})
            result = "Processed audio file: " + speaker_insights["insights"]
        else:
            return jsonify({"error": "Unsupported file type"})
        return jsonify({"result": result, "conversation": conversation_text})
    else:
        return jsonify({"error": "No file uploaded"})


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5001, debug=True)
    app.run(debug=True)
