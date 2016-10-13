import work_ticket
#import os

__author__ = 'Darryl Martin'


def load_system_config(config_filename: str) -> list:
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


def load_query_criteria(config_filename: str) -> list:
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


def load_tickets(ticket_system: work_ticket.TicketSystem) -> list:

    return tickets


def display_tickets():
    pass



