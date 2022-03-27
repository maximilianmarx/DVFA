from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():    
    if(request.cookies.get('admin') == "True"):
        return render_template('admin.html')
    else:
        return render_template('403.html')

@app.route('/analyzer')
def follow_url():
    url = request.args.get('url', '')
    if url:
        r = requests.get(url)
        return render_template('analyzer.html', req=r)
    else:
        return render_template('analyzer-empty-state.html')
    """
    Prevention:
        import ipaddress
        import socket
        from urllib.parse import urlparse
        domain = urlparse(url).netloc
        ip = socket.gethostbyname(domain)
        if(not ipaddress.ip_address(ip).is_private):
            return render_template('analyzer.html', req=r)
        else:
            return render_template('analyzer-empty-state.html')
    """

if __name__ == '__main__':
    app.run(debug=True)