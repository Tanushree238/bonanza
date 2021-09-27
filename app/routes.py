from flask.helpers import url_for
from app import app
from flask import render_template


@app.route("/", methods=["GET","POST"] )
def home():
	return render_template("try.html")

@app.route("/do_you_remember", methods=["GET","POST"] )
def do_you_remember():
	questions = []
	ques_file = list(open("app/questions/do_you_remember.txt","r"))
	for line in ques_file:
		line = line.strip("\n")
		if line:
			if line.split(" - ")[0]=="Theme":
				questions.append([line.split(" - ")[1].strip()])
			elif line.split(" - ")[0] in ["1","2","3"]:
				questions[-1].append([line.strip()])
			elif "-" not in line:
				questions[-1][-1].append(line.strip())
			elif line.split("- ")[0]=="":
				if len(questions[-1][-1])==2:
					questions[-1][-1].append(line.split("- ")[1].strip())
				else:
					questions[-1][-1][-1] += "|"+(line.split("- ")[1].strip())
	print(questions)
	return render_template("do_you_remember.html", themes=questions)

@app.route("/jumble_family", methods=["GET","POST"] )
def jigsaw_puzzle():
	return render_template("jigsaw_puzzle.html")
