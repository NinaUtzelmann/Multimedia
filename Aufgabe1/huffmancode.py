#!/usr/bin/python

import collections
import math
import operator

from Aufgabe1.Node import Node

fobj = open("midsummer.txt", "r")
counter = 0
dic = {}

for row in fobj:
	for letter in row:
		if letter in dic.keys():
			dic[letter] += 1
		else:
			dic[letter] = 1
		counter += 1

fobj.close()

def sortDic(mydict):
	dicSorted = collections.OrderedDict()

	for key, value in sorted(mydict.items(), key = operator.itemgetter(1), reverse = True):
		dicSorted[key] = value

	return dicSorted

def buildTree(dic):
	nodes = []

	########### change items to nodes
	for key, value in dic.items():
		n = Node(key, value)
		nodes.append(n)

	nodes = sorted(nodes, key=operator.attrgetter('value'))
	counter = 0

	########### take first two elements of the list and add it till there is just one tree left
	while 1 < len(nodes):
		n0 = nodes.pop(0)
		n1 = nodes.pop(0)

		newNode = Node("new" + str(counter), n0.value + n1.value)
		newNode.left = n0
		newNode.right = n1
		nodes.append(newNode)
		nodes = sorted(nodes, key=operator.attrgetter('value'))
		counter += 1

	return nodes[0]

def createBinary(node):
	binary = {}
	createBinaryRec(node.left, "0", binary)
	createBinaryRec(node.right, "1", binary)
	return binary

def createBinaryRec(root, code, binary):
	if root.left is not None and root.right is not None:
		createBinaryRec(root.left, code + "0", binary)
		createBinaryRec(root.right, code + "1", binary)
	else:
		binary[root.key] = code


if __name__ == "__main__":
	tree = buildTree(dic)
	tree = createBinary(tree)
	dic = sortDic(dic)

	print("Anzahl\t Char\t BinaryCode")
	print()

	huffmanLength = 0.0
	entropie = 0.0

	for key, value in dic.items():
		code = tree.get(key)
		huffmanLength += value * len(code)
		p = value / counter
		Ip = (math.log(p, 2)) * (-1)
		entropie += p * Ip
		print("%s\t %s\t %s\t" % (value, repr(key), code))

	print("Average Codelength in einem balanzierten Baum:")
	print(math.log(len(dic),2))
	print("Average Code length mit Huffmancode")
	print(huffmanLength/counter)
	print("Entropie")
	print(entropie)


	





