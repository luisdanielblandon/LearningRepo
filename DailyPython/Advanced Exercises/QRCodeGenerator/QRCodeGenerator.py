# This Flask app will let users enter a URL, and then it
# generates a QR code they can download as an image. Anyone
# who scans the generated QR code will be pointed to the URL
# associated with the generated QR code.

# Required libraries: flask, qrcode, PIL


from flask import Flask, request, send_file
import qrcode
from PIL import Image
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'
# The index route is the main route of the app. It returns a simple message.

# Must set working directory to the folder where the script is located:
script_dir = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(script_dir, 'QR_output')
os.makedirs(file_dir, exist_ok=True)
os.chdir(script_dir)

@app.route('/qrcode')
def qrcode_generator():
    url = request.args.get('url')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode.png')
    return send_file('qrcode.png', mimetype='image/png')
# The qrcode_generator route is the route that generates the QR code.


if __name__ == '__main__':
      app.run()
# The app.run() method starts the Flask app.


# This will start the Flask app, and you can access it in your browser at http://
# localhost:5000. You can enter a URL in the URL field and click the "Generate QR
# Code" button to generate a QR code. You can then download the generated QR code
# as an image. Anyone who scans the generated QR code will be pointed to the URL
# associated with the generated QR code.