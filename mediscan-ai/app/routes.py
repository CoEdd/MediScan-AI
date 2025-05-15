from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
import os
from .predict import predict_image # Changed to relative import

routes = Blueprint('routes', __name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')

@routes.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        result = predict_image(filepath)

    return render_template('index.html', result=result)
