import loader_types
import unittest

__author__ = 'Darryl Martin'


class ConnectionLoaderTestCase(unittest.TestCase):
    def test_connections_in_files(self):
        config_filename = 'test_config.txt'
        f = open(config_filename, 'w')
        f.write('JIRA|param1|param2\n')
        f.write('QTASK|param3|param4\n')
        f.close()
        criteria_filename = 'test_criteria.txt'
        f = open(criteria_filename, 'w')
        f.write('JIRA|param1|param2\n')
        f.write('QTASK|param3|param4\n')
        f.close()
        connections = loader_types.ConnectionsInFiles.load_connections(config_filename, criteria_filename)

        self.assertEqual(system_list[0].sys_type, 'JIRA')
        self.assertEqual(system_list[0].param1, 'param1')
        self.assertEqual(system_list[0].param2, 'param2')
        self.assertEqual(system_list[1].sys_type, 'QTASK')
        self.assertEqual(system_list[1].param1, 'param3')
        self.assertEqual(system_list[1].param2, 'param4')

        self.assertEqual(system_list[0].sys_type, 'JIRA')
        self.assertEqual(system_list[0].param1, 'param1')
        self.assertEqual(system_list[0].param2, 'param2')
        self.assertEqual(system_list[1].sys_type, 'QTASK')
        self.assertEqual(system_list[1].param1, 'param3')
        self.assertEqual(system_list[1].param2, 'param4')

        os.remove(config_filename)
        os.remove(criteria_filename)


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
