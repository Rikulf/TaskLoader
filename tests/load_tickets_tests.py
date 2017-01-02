import load_tickets
import loader_types
import work_ticket
import unittest

__author__ = 'Darryl Martin'


class LoadTicketsTestCase(unittest.TestCase):
    def test_load_tickets(self):
        connections = self._setup()
        tickets = load_tickets.load_tickets(connections)
        self.assertEquals(tickets.id, 'PBM-1')
        self.assertEquals(tickets.status, 'Closed')
        self.assertEquals(tickets.assign, 'Darryl')
        self._teardown()

    def _setup(self) -> dict:
        print("SETUP!")
        # Create JIRA-cS connection
        pass
        # Create JIRA-vob connection
        connections = {}
        ticket_system = work_ticket.TicketSystem()
        ticket_system.sys_type = 'jira'
        ticket_system.url = 'http://example.com'
        ticket_system.tkt_id = 'key'
        ticket_system.tkt_requester = 'reporter'
        ticket_system.tkt_assigned = 'assigned'
        ticket_system.tkt_description = 'summary'
        ticket_system.tkt_status = 'status'
        ticket_system.criteria[0] = "key in ('PSM-1', 'PSM-2')"
        connections['JIRA-vob'] = ticket_system
        # Create QTASK connection
        ticket_system.sys_type = 'qtask'
        ticket_system.url = 'http://example.com'
        ticket_system.tkt_id = 'ticket_no'
        ticket_system.tkt_requester = 'requester'
        ticket_system.tkt_assigned = 'assigned'
        ticket_system.tkt_description = 'description'
        ticket_system.tkt_status = 'status'
        ticket_system.criteria[0] = "status != 'closed' and project = 'PPT'"
        connections['QTASK'] = ticket_system
        return connections

    def _teardown(self):
        print("TEAR DOWN!")


if __name__ == '__main__':
    unittest.main()

