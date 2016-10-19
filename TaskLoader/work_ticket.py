__author__ = 'Darryl'


class WorkTicket:
    pass


class TicketSystem:
    """Configuration for an external system such as JIRA"""
    def __init__(self):
        self.sys_type = ''
        self.name = ''
        self.url = ''
        self.tkt_requester = ''
        self.tkt_assigned = ''
        self.tkt_status = ''
        self.tkt_description = ''
        self.criteria= []

    def set_sys_type(self, sys_type: str):
        self.sys_type = sys_type

    def set_name(self, name: str):
        self.name = name

    def set_url(self, url: str) -> object:
        self.url = url

    def set_tkt_requester(self, tkt_requester: str) -> object:
        self.tkt_requester = tkt_requester

    def set_tkt_assigned(self, tkt_assigned: str) -> object:
        self.tkt_assigned = tkt_assigned

    def set_tkt_status(self, tkt_status: str) -> object:
        self.tkt_status = tkt_status

    def set_tkt_description(self, tkt_description: str):
        self.tkt_description = tkt_description

