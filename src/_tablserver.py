from flask import Flask, request, jsonify, send_from_directory
from flask.wrappers import Response
from flask_cors import CORS
from Tables import TablesDict, TraitsDict, QueryOEIS
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)


# OEIS query endpoint (optional, can be stubbed if QueryOEIS is not available)
@app.route('/query', methods=['POST'])
def query():
    try:
        data = request.get_json()
        input_seq = data.get('seq')
        if not isinstance(input_seq, list) or not input_seq:
            return jsonify({ 'error': 'seq must be a non-empty array of integers' }), 400
        seq = [int(x) for x in input_seq] # type: ignore
        try:
            anum = QueryOEIS(seq, 1, False)
        except Exception:
            anum = 0
        return jsonify({ 'anum': anum })
    except Exception as e:
        return jsonify({ 'error': str(e) }), 500


# Main lookup endpoint: given table and trait, return the sequence and TeX
@app.route('/lookup', methods=['POST'])
def lookup():
    try:
        data = request.get_json()
        table_name = data['table'].strip()
        trait_name = data['trait'].strip()
        T = TablesDict.get(table_name)
        if not T:
            return jsonify({ 'error': f'Unknown table: {table_name}' }), 400
        trait = TraitsDict.get(trait_name)
        if not trait:
            return jsonify({ 'error': f'Unknown trait: {trait_name}' }), 400
        traitfun, size, tex = trait
        seq = traitfun(T, size)
        return jsonify({ 'seq': [str(x) for x in seq], 'tex': tex })
    except Exception as e:
        return jsonify({ 'error': str(e) }), 500


# Return the first 8 rows as a triangle and as an array (diagonals)
@app.route('/triangle', methods=['POST'])
def triangle():
    try:
        data = request.get_json()
        table_name = data['table'].strip()
        T = TablesDict.get(table_name)
        if not T:
            return jsonify({ 'error': f'Unknown table: {table_name}' }), 400
        size = 8
        tab = [list(map(str, row)) for row in T.tab(size)]
        array = [list(map(str, T.diag(n, size))) for n in range(size)]
        tex = f"\\({T.tex}\\)" if getattr(T, 'tex', None) else ''
        return jsonify({ 'tab': tab, 'array': array, 'tex': tex })
    except Exception as e:
        return jsonify({ 'error': str(e) }), 500


# Serve TableExplorer.html and other static files from src/
@app.route('/<path:filename>')
def serve_static(filename) -> Response: # type: ignore
    return send_from_directory(os.path.dirname(__file__), filename) # type: ignore

# Optionally, serve TableExplorer.html as the default page
@app.route('/')
def root() -> Response:
    return send_from_directory(os.path.dirname(__file__), 'TableExplorer.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
