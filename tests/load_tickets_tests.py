import load_tickets
import work_ticket
import unittest

__author__ = 'Darryl Martin'


class TicketInfoTestCase(unittest.TestCase):
    def test_load_tickets(self):
        tickets = load_tickets.load_tickets(work_ticket.TicketSystem('JIRA', 'param1', 'param2'))
        self.assertEquals(tickets.id, 'PBM-1')
        self.assertEquals(tickets.status, 'Closed')
        self.assertEquals(tickets.assign, 'Darryl')

    def test_display_tickets(self):
        assert (0 == 1)
        pass


def _setup():
    print("SETUP!")
    # Add JIRA ticket...
    # Add QTASK ticket...


def teardown():
    print("TEAR DOWN!")
    # Remove JIRA ticket...
    # Remove QTASK ticket...


if __name__ == '__main__':
    unittest.main()
