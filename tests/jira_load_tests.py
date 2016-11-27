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
        self.jira_server = "jira.atlassian.com"
        self.jira_user = "dam"
        self.jira_password = "inatercamp1"

    def _teardown(self):
        print("TEAR DOWN!")


if __name__ == '__main__':
    unittest.main()

