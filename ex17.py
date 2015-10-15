from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

#print "The input file is %d bytes long" % len(indata)

exists = exists(to_file)
#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input

out_file = open(to_file, 'w')
out_file.write(indata)

#print "Alright, all done."
print "Copied %d bytes from %s to %s. Output file overwritten: %r" % (
    len(indata), from_file, to_file, exists)

in_file.close()
out_file.close()
