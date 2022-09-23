import base64
from flask import Flask, request
from dotenv import load_dotenv
import boto3
import os

load_dotenv()
app = Flask(__name__)

@app.route('/tarea3-201906570', methods=['POST'])
def tarea3_201906570():
    data = request.get_json()
    img = data['img']
    client = boto3.client(
        'rekognition',
        aws_access_key_id=os.getenv("KEY_ID"),
        aws_secret_access_key=os.getenv("ACCESS_KEY"),
        region_name=os.getenv("REGION")
    )
    try:
        res = client.detect_labels(
            Image={
                'Bytes': base64.b64decode(img.encode('ascii'))
            },
            MaxLabels=123
        )
        return { "data": res['Labels'] }, 200
    except:
        return { "data": "Ha ocurrido un error con el servicio Rekognition de AWS" }, 400

if __name__ == '__main__':
    app.run(port=3000, debug=True)