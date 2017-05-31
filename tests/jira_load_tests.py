import jira_load
import work_ticket
import unittest

# import JIRA

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

    ##
    #  TODO: NEXT...
    ##

    #args = get_parameters("--url https://rentrak.atlassian.net --user dam --get --query 'issue=PPTDEV-145'")
    args = get_parameters()
    jira = establish_authentication()
    if args.get_tasks:
        get_tasks(jira)
    if args.update_project:
        update_project()

    def test_get_parameters(self):
        pass

    def test_connect_jira(self):
        pass

    def test_establish_authentication(self):
        pass

    def test_get_tasks(self):
        pass

    def test_update_project(self):
        pass

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

        return connections

    def _teardown(self):
        print("TEAR DOWN!")


if __name__ == '__main__':
    unittest.main()
