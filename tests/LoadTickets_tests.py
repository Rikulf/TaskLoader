from LoadTickets import *
import unittest

__author__ = 'Darryl Martin'

class TicketInfoTestCase(unittest.TestCase):

    def test_load_tickets(self):
        assert (0 == 1)
        pass


    def test_display_tickets(self):
        assert (0 == 1)
        pass


def setup():
    print ("SETUP!")

def teardown():
    print ("TEAR DOWN!")

if __name__ == '__main__':
    unittest.main()