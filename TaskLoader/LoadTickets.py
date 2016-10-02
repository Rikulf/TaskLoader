import work_ticket
import os

__author__ = 'Darryl Martin'


def load_system_config(config_filename):
    """

    :type config_filename: str
    """

    system_list = []

    # open config file
    f = open(config_filename, 'r')
    lines = f.readlines()
    for system_line in lines:
        system_line = system_line.rstrip('\r\n')
        system = system_line.split('|')
        system_list.append(work_ticket.TicketSystem(system[0], system[1], system[2]))
    f.close()

    return system_list

def load_query_criteria(config_filename):
    """

    :type config_filename: str
    """

    system_list = []

    # open config file
    f = open(config_filename, 'r')
    lines = f.readlines()
    for system_line in lines:
        system_line = system_line.rstrip('\r\n')
        system = system_line.split('|')
        system_list.append(work_ticket.TicketSystem(system[0], system[1], system[2]))
    f.close()

    return system_list

def _test_system_config():
    filename = 'test_config.txt'
    f = open(filename, 'w')
    f.write('JIRA|param1|param2\n')
    f.write('QTASK|param3|param4\n')
    f.close()
    system_list = load_system_config(filename)
    os.remove(filename)
    assert (system_list[0].sys_type == 'JIRA')
    assert (system_list[0].param1 == 'param1')
    assert (system_list[0].param2 == 'param2')
    assert (system_list[1].sys_type == 'QTASK')
    assert (system_list[1].param1 == 'param3')
    assert (system_list[1].param2 == 'param4')


def _test_get_query_criteria():
    filename = 'test_criteria.txt'
    f = open(filename, 'w')
    f.write('JIRA|param1|param2\n')
    f.write('QTASK|param3|param4\n')
    f.close()
    system_list = load_query_criteria(filename)
    os.remove(filename)
    assert (system_list[0].sys_type == 'JIRA')
    assert (system_list[0].param1 == 'param1')
    assert (system_list[0].param2 == 'param2')
    assert (system_list[1].sys_type == 'QTASK')
    assert (system_list[1].param1 == 'param3')
    assert (system_list[1].param2 == 'param4')


def _test_load_tickets():
    assert (0 == 1)
    pass


def _test_display_tickets():
    assert (0 == 1)
    pass


###############################################
#
#  MAIN -- Tests only
#
###############################################

# Read configs
# -- Get connection info
_test_system_config()
# -- Get query criteria
_test_get_query_criteria()
# Loop through systems
# -- Load tickets meeting criteria
_test_load_tickets()
# Display tickets
_test_display_tickets()
