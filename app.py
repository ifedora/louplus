#!/usr/bin/env python3
import json
import os
from flask import Flask,render_template,abort

app=Flask(__name__)
class Files(object):
	filespath = os.path.join(os.path.dirname(__name__),"..","files")
	def __init__(self):
		self._files = self._read_all_files()
	def _read_all_files(self):
		result={}
		for filename in os.listdir(self.filespath):
			path=os.path.join(self.filespath,filename)
			with open(path) as f:
				result[filename[:-5]]=json.load(f)
			return result
	def get_title_list(self):
		return [item["title"] for item in self._files.values()]
	def get_by_filenames(self,filename):
		return self._files.get(filename)
files = Files
@app.route("/")
def index():
	return render_template("index",title_list=files.get_title_list)

@app.route("files/<filename>")
def file(filename):
	file.item=files.get_by_filenames(filename)
	if not file_item:
		abort(404)
		return render_template('file.html',file_item=file_item)
@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

if __name__=="__main__":
	app.run(port=3000)

