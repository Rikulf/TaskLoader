__author__ = 'Darryl'

class DisplayTickets:
    """Display each individual work ticket"""
    def __init__(self):
        pass

    def dump_all(self, tickets):
        if tickets is None:
            return None
        print ("SYSTEM_TYPE|SYSTEM|TICKET_ID|DESCRIPTION|STATUS|REQUESTER|ASSIGNED")
        for ticket in tickets:
            print ("%s|%s|%s|%s|%s|%s|%s" % (
                    ticket.sys_type,
                    ticket.name,
                    ticket.id,
                    ticket.description,
                    ticket.status,
                    ticket.requester,
                    ticket.assigned
            ))
