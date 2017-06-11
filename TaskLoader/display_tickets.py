__author__ = 'Darryl'


class DisplayTickets:
    """Display each individual work ticket"""
    def __init__(self):
        pass

    def dump_all(self, tickets):
        if tickets is None:
            return None
        for ticket in tickets:
            print ("key=%s|display=%s" % (ticket.ticket_id, ticket.name))