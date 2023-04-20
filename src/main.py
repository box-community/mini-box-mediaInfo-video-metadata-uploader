from media_metadata_attach import attachMetdata
from metadata_template_create import create_metadata_template
from box_cc_client import get_cc_client

import getopt, sys

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "cm:"

try:
    client = get_cc_client()
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options)
    
    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-c"):
            create_metadata_template(client)
            
        elif currentArgument in ("-m"):
            attachMetdata(client, currentValue)
            
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))