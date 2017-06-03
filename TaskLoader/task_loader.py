import logging
import sys
import os
import load_tickets
import loader_types

__author__ = 'Darryl Martin'

###########################################
#
# MAIN
#
###########################################
if __name__ == '__main__':
    if os.environ.get("DEBUGMODE"):
        logLevel = logging.DEBUG
    else:
        logLevel = logging.WARNING
    logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', stream=sys.stderr, level=logLevel
        )
    logit = logging.getLogger(__name__)

    config_file = 'C:\Temp\config.txt'
    criteria_file = 'C:\Temp\criteria.txt'

    loader = loader_types.FileConnectionLoader(config_file, criteria_file)
    connections = loader.load_connections()
    for connection in connections:
        tickets = load_tickets.load_tickets(connections[connection])

#    display_tickets()
