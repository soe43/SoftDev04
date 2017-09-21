#William Soe
#Period 9
#lemme_flask_u_sumpn

from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def cool():
    return 'Welcome to this webpage!'
@my_app.route('/hello')
def why():
    return 'Why are you still here?'
@my_app.route('/hello/hidden')
def ok():
    return 'Please go away now this site is still under construction.'

if __name__ == '__main__':
    my_app.debug == True
    my_app.run()
    
