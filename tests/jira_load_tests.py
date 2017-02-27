import jira_load
import work_ticket
import unittest
#import JIRA

__author__ = 'Darryl Martin'


class LoadJiraLoadCase(unittest.TestCase):

    def test_get_parameters(self):
        '''self._setup()
        self.assertFalse(True, 'Not implemented')
        self._teardown()
'''

    def test_connect_jira(self):
        '''self._setup()
        jira = jira_load.connect_jira(self.jira_server, self.jira_user, self.jira_password)
        self.assertIs()
        self.assertFalse(True, 'Not implemented')
        self._teardown()
'''

    def test_establish_authentication(self):
        '''self._setup()
        self.assertFalse(True, 'Not implemented')
        self._teardown()
'''

    def test_get_project(self, jira):
        '''self._setup()
        self.assertFalse(True, 'Not implemented')
        self._teardown()
'''

    def test_update_project(self):
        '''self._setup()
        self.assertFalse(True, 'Not implemented')
        self._teardown()
'''

###
###  NEXT...
###
    def test_load_tickets(self):
        connections = self._setup()
        tickets = load_tickets.load_tickets(connections)
        self.assertEquals(tickets.id, 'PBM-1')
        self.assertEquals(tickets.status, 'Closed')
        self.assertEquals(tickets.assign, 'Darryl')
        self._teardown()

    def _setup_load_account(self, account_file) -> list:
        account_fp = open(account_file, 'r')
        with open(account_file, "r") as account_fp:
            password = account_fp.readline()
            return password.rstrip('\r\n').split('|')

    def _setup(self) -> dict:
        print("SETUP!")
        connections = {}
        ticket_system = work_ticket.TicketSystem()
        # Create JIRA-cS connection
        ticket_system.set_sys_type('jira')
        ticket_system.set_url('http://rentrak.atlassian.net')
        login, password = self._setup_load_account('rentrak_acct.txt')
        ticket_system.set_login(login)
        ticket_system.set_password(password)
        ticket_system.set_tkt_id('key')
        ticket_system.set_tkt_requester('reporter')
        ticket_system.set_tkt_assigned('assignee')
        ticket_system.set_tkt_description('summary')
        ticket_system.set_tkt_status('status')
        ticket_system.add_criteria("key in ('PPTDEV-101', 'PPTDEV-102')")
        # Create JIRA-vob connection
        ticket_system.sys_type = 'jira'
        ticket_system.url = 'http://example.com'
        login, password = self._setup_load_account('vobile_acct.txt')
        ticket_system.set_login(login)
        ticket_system.set_password(password)
        ticket_system.set_tkt_id('key')
        ticket_system.set_tkt_requester('reporter')
        ticket_system.set_tkt_assigned('assignee')
        ticket_system.set_tkt_description('summary')
        ticket_system.set_tkt_status('status')
        ticket_system.add_criteria("key in ('PSM-1', 'PSM-2')")
        connections['JIRA-vob'] = ticket_system
        # Create QTASK connection
        ticket_system.sys_type = 'qtask'
        ticket_system.url = 'http://example.com'
        login, password = self._setup_load_account('qtask_acct.txt')
        ticket_system.set_login(login)
        ticket_system.set_password(password)
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




