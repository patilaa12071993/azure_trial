import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/impact', methods=['GET','POST'])
def impact():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return name
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return None


if __name__ == '__main__':
   app.run()
