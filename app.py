from flask import Flask, request, render_template, jsonify
from generator import generate_design
import base64
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    try:
        room_type = request.form.get("room_type")
        style = request.form.get("style")
        color = request.form.get("color")
        dimensions = request.form.get("dimensions")

        # Validate inputs
        if not all([room_type, style, color, dimensions]):
            return jsonify({"error": "All fields are required"}), 400

        # Generate image using local model
        image_bytes = generate_design(room_type, style, color, dimensions)

        # Convert the image bytes to base64
        encoded_image = base64.b64encode(image_bytes.getvalue()).decode('utf-8')

        return jsonify({"image_data": f"data:image/png;base64,{encoded_image}"})

    except Exception as e:
        print("Error in /generate route:", e)
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
