__author__ = 'Darryl'


class WorkTicket:
    """Individual work ticket"""
    def __init__(self, sys_type, name):
        self.set_sys_type(sys_type)
        self.set_name(name)
        self.id = ''
        self.requester = ''
        self.assigned = ''
        self.status = ''
        self.description = ''

    def set_sys_type(self, sys_type: str):
        self.sys_type = sys_type

    def set_name(self, name: str):
        self.name = name

    def set_id(self, id: str) -> object:
        self.id = id

    def set_requester(self, requester: str) -> object:
        self.requester = requester

    def set_assigned(self, assigned: str) -> object:
        self.assigned = assigned

    def set_status(self, status: str) -> object:
        self.status = status

    def set_description(self, description: str):
        self.description = description


class TicketSystem:
    """Configuration for an external system such as JIRA"""
    def __init__(self):
        self.sys_type = ''
        self.name = ''
        self.url = ''
        self.tkt_id = ''
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

    def set_tkt_id(self, tkt_id: str) -> object:
        self.tkt_id = tkt_id

    def set_tkt_requester(self, tkt_requester: str) -> object:
        self.tkt_requester = tkt_requester

    def set_tkt_assigned(self, tkt_assigned: str) -> object:
        self.tkt_assigned = tkt_assigned

    def set_tkt_status(self, tkt_status: str) -> object:
        self.tkt_status = tkt_status

    def set_tkt_description(self, tkt_description: str):
        self.tkt_description = tkt_description

