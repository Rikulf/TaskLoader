import unittest
import work_ticket

__author__ = 'Darryl Martin'

class WorkTicketTestCase(unittest.TestCase):
    def test_work_ticket(self):
        test_ticket = self._setup()
        self.assertEqual(test_ticket.sys_type, 'jira')
        self.assertEqual(test_ticket.name, 'JIRA-vob')
        self._teardown()

    def _setup(self) -> work_ticket:
        print("SETUP!")
        return work_ticket.WorkTicket('jira', 'JIRA-vob')

    def _teardown(self):
        print("TEAR DOWN!")


if __name__ == '__main__':
    unittest.main()
