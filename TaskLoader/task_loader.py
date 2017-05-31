import load_tickets
import loader_types

__author__ = 'Darryl Martin'

###########################################
#
# MAIN
#
###########################################
if __name__ == '__main__':
    config_file = 'C:\Temp\config.txt'
    criteria_file = 'C:\Temp\criteria.txt'

    loader = loader_types.FileConnectionLoader(config_file, criteria_file)
    connections = loader.load_connections()
    for connection in connections:
        tickets = load_tickets.load_tickets(connections[connection])

#    display_tickets()
