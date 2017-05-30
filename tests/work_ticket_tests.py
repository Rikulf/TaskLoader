import unittest
import work_ticket

__author__ = 'Darryl Martin'


class WorkTicketTestCase(unittest.TestCase):
    # Test work_ticket.WorkTicket
    def test_work_ticket(self):
        test_ticket = self._setup_work_ticket()
        self.assertEqual(test_ticket.sys_type, 'jira')
        self.assertEqual(test_ticket.name, 'JIRA-vob')
        self._teardown_work_ticket()

    # Test work_ticket.TicketSystem
    def test_ticket_system(self):
        test_system = self._setup_ticket_system()
        test_system.add_criteria("key in ('PPTDEV-101', 'PPTDEV-102')")
        test_system.add_criteria("status = 'OPEN'")
        self.assertEqual(test_system.criteria[0], "key in ('PPTDEV-101', 'PPTDEV-102')")
        self.assertEqual(test_system.criteria[1], "status = 'OPEN'")
        self._teardown_ticket_system()

    def _setup_work_ticket(self) -> work_ticket.WorkTicket:
        print("SETUP WORK TICKET!")
        return work_ticket.WorkTicket('jira', 'JIRA-vob')

    def _teardown_work_ticket(self):
        print("TEAR DOWN WORK TICKET!")

    def _setup_ticket_system(self) -> work_ticket.TicketSystem:
        print("SETUP TICKET SYSTEM!")
        return work_ticket.TicketSystem()

    def _teardown_ticket_system(self):
        print("TEAR DOWN TICKET SYSTEM!")

if __name__ == '__main__':
    unittest.main()
