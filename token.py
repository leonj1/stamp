import sys, getopt
import os.path
import json
import re

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg

   if os.path.exists(inputfile):
      config = json.loads(open(inputfile).read())
      if len(config) > 0:
         for file in config:
            if (os.path.exists(file['file']) and len(file['keys']) > 0):
               print "Editing " + file['file']
               f = open(file['file'],'r')
               filedata = f.read()
               f.close()

               for key in file['keys']:
                  oldValue = key['target'] + '.*\n'
                  newValue = key['target'] + ' ' + key['value'] + '\n'
                  print 'Replacing: ' + oldValue
                  filedata = re.sub(oldValue, newValue, filedata)

               outfile = file['file']
               print "Writing: " + outfile
               f = open(outfile,'w')
               f.write(filedata)
               f.close()
            else:
                print 'Target file in template does not exist: ' + file['file']
      else:
         print 'No files in template to edit'
   else:
      print 'Provided file does not exist: ' + inputfile

if __name__ == "__main__":
   main(sys.argv[1:])
