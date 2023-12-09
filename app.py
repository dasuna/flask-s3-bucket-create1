from flask import Flask, request, render_template, redirect 
import boto3

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/create-bucket", methods=["POST"]) 
def create_bucket():
    bucket_name = request.form["bucket_name"]
    #Create an S3 service resource
    s3 = boto3.resource('s3')

    try:
        #Creates an S3 bucket object
        bucket = s3.Bucket(bucket_name)
        response = bucket.create(CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
        if response:
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print("Error creating bucket.")
        
    except Exception as e:
        print(f"Error creating bucket: {e}")

    return redirect("/")

 
if __name__ == "__main__": 
    app.run(debug=True,port=8080,host='0.0.0.0')
