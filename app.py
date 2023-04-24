# Importing required libs
from flask import Flask, render_template, request, send_from_directory
from model import predict_result
from flask import send_file, current_app as app
# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            # img = preprocess_img(request.files['file'].stream)
            pred = predict_result(request.files['file'].stream)
            digit_to_string = {0: "Antracnose", 1: "Healthy", 2: "Leaf Curl", 3: "Leaf Spot", 4: "Powdery Mildew"}
            prediction_string = digit_to_string[pred]
            return render_template("result.html", predictions=prediction_string)

    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)
    

# @app.route('/templates', methods = ['GET'] )
# def show_static_pdf():
#     return send_from_directory("leaf_curl.pdf   ", 'tos.pdf')
#     # with open('C:\\Users\\muttu\\Desktop\\imgrcg\\templates\\leaf_curl.pdf', 'rb') as static_file:
        
#         # return send_file(static_file, download_name ='file.pdf')


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
