from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import sys
app = Flask(__name__)

@app.route('/mypage/me.html', methods=['GET'])
def message_my_page():
    print("I am written to the file")
    return render_template("/mypage/me.html")
if __name__ == '__main__':
    app.run()

@app.route('/mypage/contact.html', methods=['GET', 'POST'])
def message_contact_page():
   items = ["mail:mail2maciek@gmail.com", "phone: 111-122-133"]
   if request.method == 'GET':
       print("We received GET")
       return render_template("/mypage/contact.html", items=items)
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

   if __name__ == '__main__':
      app.run()


