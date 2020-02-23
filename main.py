from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from wakeonlan import send_magic_packet
from flask import session


app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'

# rutas
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'dir_ip' in session:
        dir_ip = session['dir_ip']
        dir_mac = session['dir_mac']
        return render_template('index.html',dir_ip=dir_ip, dir_mac=dir_mac)
    else:
        return render_template('index.html')
    

@app.route('/wol', methods=['GET', 'POST'])
def wol():
    if request.method == 'POST':
        dir_ip = request.form.get('dir_ip')
        dir_mac = request.form.get('dir_mac')

        session['dir_ip']=dir_ip
        session['dir_mac']=dir_mac

        send_magic_packet(dir_mac,ip_address=dir_ip, port=9)

#test mac 1C.1B.0D.A2.7C.53

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run('0.0.0.0',5000,debug=True)
