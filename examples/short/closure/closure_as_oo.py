#!/usr/bin/python

def Person(name,age):
	o={
		"name":name,
		"age":age
	}
	def getName():
		return o["name"]
	def setName(iname):
		o["name"]=iname
	def getAge():
		return o["age"]
	def setAge(iage):
		o["age"]=iage
	return {
		"getName":getName,
		"setName":setName,
		"getAge":getAge,
		"setAge":setAge
	}

p=Person("Bilbo",111)
p["setAge"](112)
print("age is",p["getAge"]())
p2=Person("Frodo",77)
p2["setAge"](78)
print("age is",p2["getAge"]())
