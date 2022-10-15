#!/usr/bin/env python
# coding: utf-8

# In[4]:


from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)

@app.route('/print_sum/<s>')
def print_sum(s):
    return render_template('index.html' , s=s)
    

@app.route('/' , methods=["GET" , "POST"])
def sum():
    if request.method == "POST":
        a = request.form['a']
        b = request.form['b']
        if a != None or b != None:
            s = int(a) + int(b)
            print(s)
            return redirect(url_for('print_sum' , s = s))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)
    


# In[ ]:




