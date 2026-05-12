from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file provided'}), 400
    
    file = request.files['photo']
    
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'status': 'error', 'message': 'Invalid file type. Allowed: PNG, JPG, JPEG, GIF'}), 400
    
    filename = secure_filename(file.filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}_{filename}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    file.save(filepath)
    
    # Store the filename (not path) in session
    session['photo_path'] = filename
    
    return jsonify({
        'status': 'success',
        'filename': filename,
        'message': 'Photo uploaded successfully',
        'url': url_for('uploaded_file', filename=filename)
    })

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Example summary route showing photo
@app.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        session['personal_info'] = {
            'name': request.form.get('name', ''),
            'email': request.form.get('email', ''),
            'phone': request.form.get('phone', ''),
            'photo': session.get('photo_path', '')
        }
        return redirect(url_for('summary'))
    return render_template('summary.html', personal_info=session.get('personal_info', {}))

# Download CV as HTML
@app.route('/download_cv')
def download_cv():
    from flask import Response
    personal_info = session.get('personal_info', {})
    html_content = render_template('preview.html', personal_info=personal_info)
    name = personal_info.get('name', 'CV').replace(' ', '_')
    filename = f"{name}_CV_{datetime.now().strftime('%Y%m%d')}.html"
    response = Response(html_content, mimetype='text/html')
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    return response

if __name__ == '__main__':
    # Disable reloader if using OneDrive to prevent infinite reload
    app.run(debug=True, use_reloader=False, port=5000)
