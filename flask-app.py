from flask import Flask,request,render_template
import os

application=Flask(__name__)
app=application
dict1={}

@app.route('/')
def hello():
        return render_template("index.html")

@app.route('/upload',methods=['POST'])
def upload():
        file1=request.files['files']
        f=open(file1.filename,'w')
        contents=file1.read()
        f.write(contents)

        os.system("hadoop fs -mkdir /assignment")
        os.system("hadoop fs -put " +file1.filename + "/assignment/"+file1.filename)
        os.system("cd /usr/local/hadoop/share/hadoop/tools/lib")
        os.system("hadoop jar hadoop-streaming-2.7.1.jar -file /home/ubuntu/hadoop_flask/mapper.py -mapper /home/ubuntu/hadoop_flask/mapper.py -file /home/ubuntu/hadoop_flask/reducer.py -reducer /home/ubuntu/hadoop_flask/reducer.py -input /assignment/* -output /assignment/output")
        os.system("hadoop fs -cat /assignment/output/part-00000 > /home/ubuntu/hadoop_flask/output.txt")
        file2=open("output.txt",'r')
        contents=file2.read()
        return render_template("output.html",res=contents)
