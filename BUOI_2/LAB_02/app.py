from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.transposition import TranspositionCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar", methods=['GET', 'POST'])
def caesar_route():
    encrypted_text = None
    decrypted_text = None
    key = None
    if request.method == 'POST':
        text = request.form.get('inputPlainText') if request.form.get('action') == 'encrypt' else request.form.get('inputCipherText')
        key = request.form.get('inputKeyPlain', type=int) if request.form.get('action') == 'encrypt' else request.form.get('inputKeyCipher', type=int)
        action = request.form.get('action')
        caesar = CaesarCipher()
        if action == 'encrypt':
            encrypted_text = caesar.encrypt_text(text, key)
        elif action == 'decrypt':
            decrypted_text = caesar.decrypt_text(text, key)
    return render_template('caesar.html', encrypted_text=encrypted_text, decrypted_text=decrypted_text, key=key)

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere_route():
    encrypted_text = None
    decrypted_text = None
    key = None
    if request.method == 'POST':
        text = request.form.get('inputPlainText') if request.form.get('action') == 'encrypt' else request.form.get('inputCipherText')
        key = request.form.get('inputKeyPlain') if request.form.get('action') == 'encrypt' else request.form.get('inputKeyCipher')
        action = request.form.get('action')
        vigenere = VigenereCipher(key)
        if action == 'encrypt':
            encrypted_text = vigenere.encrypt(text)
        elif action == 'decrypt':
            decrypted_text = vigenere.decrypt(text)
    return render_template('vigenere.html', encrypted_text=encrypted_text, decrypted_text=decrypted_text, key=key)

@app.route('/railfence', methods=['GET', 'POST'])
def railfence_route():
    ciphertext = None
    plaintext = None
    key = None
    if request.method == 'POST':
        text = request.form.get('inputPlainText') if request.form.get('action') == 'encrypt' else request.form.get('inputCipherText')
        key = request.form.get('inputKeyPlain', type=int) if request.form.get('action') == 'encrypt' else request.form.get('inputKeyCipher', type=int)
        action = request.form.get('action')
        railfence = RailFenceCipher(key)
        if action == 'encrypt':
            ciphertext = railfence.encrypt(text)
        elif action == 'decrypt':
            plaintext = railfence.decrypt(text)
    return render_template('rail_fence.html', ciphertext=ciphertext, plaintext=plaintext, key=key)

@app.route('/playfair', methods=['GET', 'POST'])
def playfair_route():
    ciphertext = None
    plaintext = None
    key = None
    if request.method == 'POST':
        text = request.form.get('inputPlainText') if request.form.get('action') == 'encrypt' else request.form.get('inputCipherText')
        key = request.form.get('inputKeyPlain') if request.form.get('action') == 'encrypt' else request.form.get('inputKeyCipher')
        action = request.form.get('action')
        playfair = PlayFairCipher(key)
        if action == 'encrypt':
            ciphertext = playfair.encrypt(text)
        elif action == 'decrypt':
            plaintext = playfair.decrypt(text)
    return render_template('playfair.html', ciphertext=ciphertext, plaintext=plaintext, key=key)

@app.route('/transposition', methods=['GET', 'POST'])
def transposition_route():
    ciphertext = None
    plaintext = None
    key = None
    if request.method == 'POST':
        text = request.form.get('inputPlainText') if request.form.get('action') == 'encrypt' else request.form.get('inputCipherText')
        key = request.form.get('inputKeyPlain') if request.form.get('action') == 'encrypt' else request.form.get('inputKeyCipher')
        action = request.form.get('action')
        transposition = TranspositionCipher(key)
        if action == 'encrypt':
            ciphertext = transposition.encrypt(text)
        elif action == 'decrypt':
            plaintext = transposition.decrypt(text)
    return render_template('transposition.html', ciphertext=ciphertext, plaintext=plaintext, key=key)

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)