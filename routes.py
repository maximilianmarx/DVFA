from flask import Flask, render_template, url_for, redirect, request
import requests
import forms

from app import app
import db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Broken-Access-Control
@app.route('/admin')
def admin():    
    if(request.cookies.get('admin') == "True"):
        return render_template('admin.html')
    else:
        return render_template('403.html')

# SSRF
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

# XSS, CSRF (no CSRF-Token)
@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    search_query = request.args.get('q')
    comments = db.get(search_query)

    form = forms.AddCommentForm()
    if form.validate_on_submit():
        db.add(form.comment.data)

        return redirect(url_for('guestbook'))
    return render_template('guestbook.html', form=form, comments=comments, search_query=search_query)