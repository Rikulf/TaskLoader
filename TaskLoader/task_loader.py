import load_tickets
import loader_types

__author__ = 'Darryl Martin'


###############################################
#
#  MAIN
#
###############################################
def main():
    config_file = 'config.txt'
    criteria_file = 'criteria.txt'

    loader = loader_types.ConnectionsInFiles(config_file, criteria_file)
    connections = loader.load_connections()
    tickets = load_tickets(connections)

#    display_tickets()
