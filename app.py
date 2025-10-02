from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    print("🚀 Serving Crypto Dashboard at http://localhost:3000")
    app.run(host="0.0.0.0", port=3000)
