from flask import Flask
from flask import render_template
from flask import request
from wakeonlan import send_magic_packet


app = Flask(__name__)

# rutas
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    

@app.route('/wol', methods=['GET', 'POST'])
def wol():

    if request.method == 'POST':
        dir_ip = request.form.get('dir_ip')
        dir_mac = request.form.get('dir_mac')
        
        send_magic_packet('1C.1B.0D.A2.7C.53',ip_address='minecraft.rjgu.es',port=9)



    return render_template('index.html')


if __name__ == "__main__":
    app.run('0.0.0.0',5000,debug=False)
