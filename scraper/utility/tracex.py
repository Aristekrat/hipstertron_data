import sys
# This module lives halfway between test and utility. Included here simply because I don't want to import another folder.

def determine_file_mode():
	if (len(sys.argv) == 2):
		return sys.argv[1]
	else: 
		return "normal"

# Clears the trace file and imports the datetime module
def initialize_trace_file(mode, filename):
	if (mode == "debug"):
		write_file = "../../test/stack_trace/" + filename + "_trace.py"
		initialize = open(write_file, 'w')
		initialize.write("import datetime")
		initialize.close()

# Writes a variable to file
def create_trace(mode, filename, varname, trace):
	if (mode == "debug"):
		write_file = "../../test/stack_trace/" + filename + "_trace.py"
		source = open(write_file, 'a')
		source.write("\n\n" + str(varname) + " = " + str(trace))
		source.close()