import AOList
import os
# from flask import Flask, request
# from flask_cors import CORS, cross_origin
import urllib.parse

urls = open("list.txt").read().split("\n")
downloadurls = []


if not os.path.exists("roms.txt"):
  for url in urls:
    if url != "":
      downloadurls = downloadurls + AOList.listFileTypeUrls(url, filetype="iso")
  open("roms.txt", "w").write("")
  for url in downloadurls:
    open("roms.txt", "a").write(url+"\n")
else:
  downloadurls = open("roms.txt", "r").read().split("\n")

# app = Flask(__name__)
# CORS(app, support_credentials=True)
#
# @app.route('/')
# def index():
#   finalhtml = ""
#   search = request.args.get('search')
#   for url in downloadurls:
#     if search is not None:
#       if search.lower() in urllib.parse.unquote(url).lower():
#         finalhtml = finalhtml+url+"\n"
#     else:
#       finalhtml = finalhtml+url+"\n"
#   return finalhtml
#
# @app.route('/count/')
# def count():
#   return str(len(downloadurls))
#
#
# app.run(host='0.0.0.0', port=81)
