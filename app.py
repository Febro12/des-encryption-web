from flask import Flask, render_template, request
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

app = Flask(__name__)

key = b'12345678'

@app.route("/", methods=["GET","POST"])
def index():
    ciphertext = ""
    decrypted = ""

    if request.method == "POST":
        pesan = request.form["pesan"]

        cipher = DES.new(key, DES.MODE_ECB)

        encrypted = cipher.encrypt(pad(pesan.encode(), DES.block_size))
        ciphertext = encrypted.hex()   # supaya tampil rapi

        decrypted = unpad(cipher.decrypt(encrypted), DES.block_size).decode()

    return render_template("index.html", ciphertext=ciphertext, decrypted=decrypted)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)