from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Load text from file
def load_text():
    try:
        with open("text_data.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""


# Save text to file
def save_text(text):
    with open("text_data.txt", "w") as file:
        file.write(text)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        save_text(text)
        return redirect(url_for('index'))
    else:
        text = load_text()
        return render_template('index.html', text=text)  # Removed leading slash

if __name__ == '__main__':
    app.run(debug=True)