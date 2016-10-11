__author__ = 'Darryl'


class WorkTicket:
    pass


class TicketSystem:
    """Configuration for an external system such as JIRA"""
    def __init__(self, sys_type, param1, param2):
        self.sys_type = sys_type
        self.param1 = param1
        self.param2 = param2

