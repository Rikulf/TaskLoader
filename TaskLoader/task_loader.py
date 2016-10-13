import work_ticket

__author__ = 'Darryl Martin'


###############################################
#
#  MAIN
#
###############################################
def main():
    config_file = 'config.txt'
    criteria_file = 'criteria.txt'

    # add error checking
    load_system_config(config_file)
    load_query_criteria(criteria_file)
    load_tickets()
    display_tickets()
