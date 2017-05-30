import load_tickets
import loader_types

__author__ = 'Darryl Martin'


###############################################
#
#  MAIN
#
###############################################
def main():
    config_file = 'C:\Temp\config.txt'
    criteria_file = 'C:\Temp\criteria.txt'

    loader = loader_types.FileConnectionLoader(config_file, criteria_file)
    connections = loader.load_connections()
    tickets = load_tickets(connections)

#    display_tickets()
