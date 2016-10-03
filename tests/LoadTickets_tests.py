from LoadTickets import *
import unittest

__author__ = 'Darryl Martin'

class FileHandlingTestCase(unittest.TestCase):

    def test_system_config(self):
        filename = 'test_config.txt'
        f = open(filename, 'w')
        f.write('JIRA|param1|param2\n')
        f.write('QTASK|param3|param4\n')
        f.close()
        system_list = load_system_config(filename)
        os.remove(filename)
        self.assertEqual(system_list[0].sys_type, 'JIRA')
        self.assertEqual(system_list[0].param1, 'param1')
        self.assertEqual(system_list[0].param2, 'param2')
        self.assertEqual(system_list[1].sys_type, 'QTASK')
        self.assertEqual(system_list[1].param1, 'param3')
        self.assertEqual(system_list[1].param2, 'param4')

    def test_get_query_criteria(self):
        filename = 'test_criteria.txt'
        f = open(filename, 'w')
        f.write('JIRA|param1|param2\n')
        f.write('QTASK|param3|param4\n')
        f.close()
        system_list = load_query_criteria(filename)
        os.remove(filename)
        self.assertEqual(system_list[0].sys_type, 'JIRA')
        self.assertEqual(system_list[0].param1, 'param1')
        self.assertEqual(system_list[0].param2, 'param2')
        self.assertEqual(system_list[1].sys_type, 'QTASK')
        self.assertEqual(system_list[1].param1, 'param3')
        self.assertEqual(system_list[1].param2, 'param4')

'''
class TicketInfoTestCase(unittest.TestCase):

    def test_load_tickets(self):
        assert (0 == 1)
        pass


    def test_display_tickets(self):
        assert (0 == 1)
        pass
'''


def setup():
    print ("SETUP!")

def teardown():
    print ("TEAR DOWN!")

if __name__ == '__main__':
    unittest.main()