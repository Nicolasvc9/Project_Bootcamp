from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se proporcionó ningún archivo'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío'}), 400

    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        df = pd.read_csv(filepath)

        os.remove(filepath)

        columns = df.columns.tolist()
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_columns = df.select_dtypes(exclude=[np.number]).columns.tolist()

        stats = df[numeric_columns].describe().to_dict() if numeric_columns else {}
        table_data = df.head(100).to_dict(orient='records')

        return jsonify({
            'success': True,
            'columns': columns,
            'numeric_columns': numeric_columns,
            'categorical_columns': categorical_columns,
            'chart_data': {
                'stats': stats
            },
            'table_data': table_data,
            'row_count': len(df)
        })

    except Exception as e:
        return jsonify({'error': f'Error al procesar el archivo: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
