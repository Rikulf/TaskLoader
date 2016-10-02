__author__ = 'Darryl'


class WorkTicket:
    pass


class TicketSystem:
    """Configuration for an external system such as JIRA"""
    #    _sides[object side] = []
    def __init__(self, sys_type, param1, param2):
        self.sys_type = sys_type
        self.param1 = param1
        self.param2 = param2

    def num_sides(self):
        pass
