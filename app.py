import os

from flask import Flask, render_template, request, send_file
from gtts import gTTS

app = Flask(__name__)


def text_to_speech(text, filename='output.mp3'):
    tts = gTTS(text=text, lang='es')
    tts.save(os.path.join(app.static_folder, filename))
    return filename


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate_audio():
    input_text = request.form['input_text']
    filename = text_to_speech(input_text)
    return filename


@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_file(os.path.join(app.static_folder, filename), as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
