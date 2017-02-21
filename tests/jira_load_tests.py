import jira_load
import work_ticket
import unittest
import JIRA

__author__ = 'Darryl Martin'


class LoadJiraLoadCase(unittest.TestCase):
    self._setup()
    self._teardown()

    def test_get_parameters(self):
        self.assertFalse(True, 'Not implemented')

    def test_connect_jira(self):
        jira = jira_load.connect_jira(self.jira_server, self.jira_user, self.jira_password)
        self.assertIs()
        self.assertFalse(True, 'Not implemented')

    def test_establish_authentication(self):
        self.assertFalse(True, 'Not implemented')

    def test_get_project(self, jira):
        self.assertFalse(True, 'Not implemented')

    def test_update_project(self):
        self.assertFalse(True, 'Not implemented')

    def _setup(self) -> dict:
        print("SETUP!")
        self.jira_server = "http://rentrak.atlassian.net"
        self.jira_user = "dam"
        self.jira_password = "inatercamp1"

    def test_load_tickets(self):
        connections = self._setup()
        tickets = load_tickets.load_tickets(connections)
        self.assertEquals(tickets.id, 'PBM-1')
        self.assertEquals(tickets.status, 'Closed')
        self.assertEquals(tickets.assign, 'Darryl')
        self._teardown()

    def _setup(self) -> dict:
        print("SETUP!")
        connections = {}
        ticket_system = work_ticket.TicketSystem()
        # Create JIRA-cS connection
        ticket_system.set_sys_type('jira')
        ticket_system.set_url('http://rentrak.atlassian.net')
        ticket_system.set_tkt_id('key')
        ticket_system.set_tkt_requester('reporter')
        ticket_system.set_tkt_assigned('assignee')
        ticket_system.set_tkt_description('summary')
        ticket_system.set_tkt_status('status')
        ticket_system.criteria[0] = "key in ('PPTDEV-101', 'PPTDEV-102')"
        # Create JIRA-vob connection
        ticket_system.sys_type = 'jira'
        ticket_system.url = 'http://example.com'
        ticket_system.tkt_id = 'key'
        ticket_system.tkt_requester = 'reporter'
        ticket_system.tkt_assigned = 'assignee'
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
    # unittest.main()




