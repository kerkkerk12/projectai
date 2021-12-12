from flask import Flask, render_template, Response
from flask_cors import CORS
app=Flask(__name__)
cors = CORS(app)
import face_detection as fd
import face_rec as fr

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/face_d')
def video_feed():
    return Response(fd.main(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/img_fr')
def video_fr():
    return Response(fr.main("test_images/full.jpg"), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=='__main__':
    app.run(debug=True)