import load_tickets
import loader_types
import work_ticket
import unittest

__author__ = 'Darryl Martin'

#Needs attention
class LoadTicketsTestCase(unittest.TestCase):
    def test_load_tickets(self):
        connections = self._setup()
        for system in list(connections):
            tickets = load_tickets.load_tickets(connections[system])
            if system == 'JIRA-vob':
                self.assertEquals(tickets.id, 'PBM-1')
                self.assertEquals(tickets.status, 'Closed')
                self.assertEquals(tickets.assign, 'Darryl')
        self._teardown()

    def _setup(self) -> dict:
        print("SETUP!")
        connections = {}
        # Create JIRA-cS connection
        ticket_system = work_ticket.TicketSystem()
        ticket_system.set_sys_type('jira')
        ticket_system.set_url('http://sample.atlassian.net')
        ticket_system.set_tkt_id('key')
        ticket_system.set_tkt_requester('reporter')
        ticket_system.set_tkt_assigned('assignee')
        ticket_system.set_tkt_description('summary')
        ticket_system.set_tkt_status('status')
        ticket_system.add_criteria("key in ('PPTDEV-101', 'PPTDEV-102')")
        connections['JIRA-cS'] = ticket_system
        # Create JIRA-vob connection
        ticket_system = work_ticket.TicketSystem()
        ticket_system.set_sys_type('jira')
        ticket_system.set_url('http://example.com')
        ticket_system.set_tkt_id('key')
        ticket_system.set_tkt_requester('reporter')
        ticket_system.set_tkt_assigned('assignee')
        ticket_system.set_tkt_description('summary')
        ticket_system.set_tkt_status('status')
        ticket_system.add_criteria("key in ('PSM-1', 'PSM-2')")
        connections['JIRA-vob'] = ticket_system
        # Create QTASK connection
        ticket_system = work_ticket.TicketSystem()
        ticket_system.set_sys_type('qtask')
        ticket_system.set_url('http://example.com')
        ticket_system.set_tkt_id('ticket_no')
        ticket_system.set_tkt_requester('requester')
        ticket_system.set_tkt_assigned('assigned')
        ticket_system.set_tkt_description('description')
        ticket_system.set_tkt_status('status')
        ticket_system.add_criteria("status != 'closed' and project = 'PPT'")
        connections['QTASK'] = ticket_system
        return connections

    def _teardown(self):
        print("TEAR DOWN!")


if __name__ == '__main__':
    unittest.main()

