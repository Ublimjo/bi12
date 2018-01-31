#!/data/data/com.termux/files/usr/bin/env python
import argparse
import sys
import bible
import part 

version = 0.2

def main():
	print("===========================================")
	print("  Baiboly fandikan-teny ny tontolo vaovao")
	print("    Version :", version)
	print("===========================================")
	
	while True:
		command = input("  bi12 > ").lower()
		cmd = command.split(" ")
		
		#test book
		test = bible.bibleParse()
		test.parse(command)
		if test.verset1 != 0:
			part.parter(test.book, test.verset1, test.verset2)
		
		elif cmd[0] == "help":
			print("")
			print("    Ampidiro ny andinin-teny ilainao ")
			print("    Ohatra: ")
			print("      bi12 > Salamo 83:18")
			print("      bi12 > 1 Jaona 5:19")
			print("")
			print("    Tsy maninona izay ampidirinao na renitsoratra na zanatsoratra ")
			print("    Tsy maintsy misy 'espace' araky ny tokony ho izy")
			print("    Ohatra: ")
			print("      bi12 > mAtiO 24:14")
			print("    Tsy mety ny hoe:")
			print("      bi12 > matio      24   :14")
			print("")
			print("    Command hafa afaka ampidirina:")
			print("      help:")
			print("        Mampiseho an'ity soratra ity")
			print("      exit | quit:")
			print("        Miala amin'ity programa ity")
			print("      version:")
			print("        Mampiseho ny mombamomba an'ity programa ity")
			print("")
		
		elif cmd[0] == "exit":
			break
			
		elif cmd[0] == "version":
			print("")
			
		
			
		
		
		

if len(sys.argv) == 1:
	main()
else:
	view()
