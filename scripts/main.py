import os
import json
from flask import Flask, render_template, request

app = Flask(__name__)

def createcontact(fname,lname, number, email):
	contactblock={}
	contactblock["fname"]=fname
	contactblock["lname"]=lname
	contactblock["number"]=number
	contactblock["email"]=email
	return contactblock

def delcontact(number, abook):

	return {i:abook[i] for i in abook if i!=number}




@app.route('/')
def abookhome():
	return render_template('abookhome.html')

@app.route('/addressbook', methods=['POST'])
def addressbook():
	with open('../abookHistory/abook.json') as f:
		addressbooks = json.load(f)

	print(addressbooks)
	CONTACTS=addressbooks["contacts"]
	print(CONTACTS)
	for contact in CONTACTS:
		print("First Name:"+contact["fname"])
	return render_template('addressbook.html',CONTACTS=addressbooks)


@app.route('/addressbookadd', methods=['POST'])
def addressbookadd():
	with open('../abookHistory/abook.json') as f:
		addressbooks = json.load(f)
	CONTACTS=addressbooks["contacts"]
	

	fnameentered = request.form['fname']
	lnameentered = request.form['lname']
	numberentered = request.form['number']
	emailentered = request.form['email']

	newcontact = createcontact(fnameentered,lnameentered,numberentered,emailentered)

	CONTACTS.append(newcontact)
	print(CONTACTS)
	newbook = {}
	newbook["contacts"]=CONTACTS
	
	with open('../abookHistory/abook.json', 'w') as fs:
		json.dump(newbook,fs)

	for contact in CONTACTS:
		print("First Name:"+contact["fname"])

	return render_template('addressbook.html',CONTACTS=CONTACTS)

@app.route('/addressbookdel', methods=['POST'])
def addressbookdel():
	with open('../abookHistory/abook.json') as f:
		addressbooks = json.load(f)
	CONTACTS=addressbooks["contacts"]

	numberentered = request.form['number']

	newcontactlist=delcontact(numberentered, addressbooks)
	
	print(newcontactlist)
	newbook = {}
	newbook["contacts"]=CONTACTS
	
	with open('../abookHistory/abook.json', 'w') as fs:
		json.dump(newbook,fs)

	for contact in CONTACTS:
		print("First Name:"+contact["fname"])

	return render_template('addressbook.html',CONTACTS=CONTACTS)
