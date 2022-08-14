from flask import Flask, render_template,request
import re
from unittest import result

# Create the Object 
app = Flask(__name__)

# Define the Routes and bind it with a Function
@app.route('/',methods=['GET','POST'])
def regex101():
    if request.method=='POST':
        expression = request.form['reg_exp']
        testString = request.form['test']
        count=0
        if (len(expression) ==0 or len(testString) == 0):
            count=-1
            return render_template("index.html",result="Please provide input",count=count)
        else:
            list=[]
            for match in re.finditer(r'{}'.format(expression),testString):
                string=''
                count+=1
                string=string+"Match {} \"{}\" at start and end indices [{} , {}]".format(count,match.group(),match.start(),match.end())
                list.append(string)
            return render_template("index.html",result ="Matches found", reg_exp=expression, test=testString, lists=list, count=count)

    return render_template("index.html",count=-1)

    
# Run the App
if __name__=='__main__':
    app.run(debug=True)