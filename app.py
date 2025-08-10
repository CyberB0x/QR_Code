from flask import Flask, render_template, request
import qrcode
import io
import base64
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_img = None
    input_text = ''

    if request.method == 'POST':
        input_text = request.form.get('text', '').strip()
        if input_text:
            img = qrcode.make(input_text)
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            buf.seek(0)
            qr_img = base64.b64encode(buf.read()).decode('ascii')

    return render_template('index.html', qr_img=qr_img, input_text=input_text)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

