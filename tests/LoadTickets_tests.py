import unittest
import LoadTickets_tests
#import work_ticket
#import os

__author__ = 'Darryl Martin'

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

class FileHandlingTestCase(unittest.TestCase)

    def _test_system_config(self):
        filename = 'test_config.txt'
        f = open(filename, 'w')
        f.write('JIRA|param1|param2\n')
        f.write('QTASK|param3|param4\n')
        f.close()
        system_list = load_system_config(filename)
        os.remove(filename)
        assert (system_list[0].sys_type == 'JIRA')
        assert (system_list[0].param1 == 'param1')
        assert (system_list[0].param2 == 'param2')
        assert (system_list[1].sys_type == 'QTASK')
        assert (system_list[1].param1 == 'param3')
        assert (system_list[1].param2 == 'param4')


    def _test_get_query_criteria(self):
        filename = 'test_criteria.txt'
        f = open(filename, 'w')
        f.write('JIRA|param1|param2\n')
        f.write('QTASK|param3|param4\n')
        f.close()
        system_list = load_query_criteria(filename)
        os.remove(filename)
        assert (system_list[0].sys_type == 'JIRA')
        assert (system_list[0].param1 == 'param1')
        assert (system_list[0].param2 == 'param2')
        assert (system_list[1].sys_type == 'QTASK')
        assert (system_list[1].param1 == 'param3')
        assert (system_list[1].param2 == 'param4')

class TicketInfoTestCase(unittest.TestCase)
    def _test_load_tickets(self):
        assert (0 == 1)
        pass


    def _test_display_tickets(self):
        assert (0 == 1)
        pass


if __name__ == '__main__':
    unittest.main()