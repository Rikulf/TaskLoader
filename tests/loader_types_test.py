import loader_types
import unittest
import os

__author__ = 'Darryl Martin'


class ConnectionLoaderTestCase(unittest.TestCase):

    def test_connections_in_files(self):
        config_filename, criteria_filename = self._setup()
        loader = loader_types.ConnectionsInFiles(config_filename, criteria_filename)
        connections = loader.load_connections()

        self.assertEqual(connections['JIRA-vob'].sys_type, 'jira')
        self.assertEqual(connections['JIRA-vob'].url, 'http://example.com')
        self.assertEqual(connections['JIRA-vob'].tkt_requester, 'reporter')
        self.assertEqual(connections['JIRA-vob'].tkt_assigned, 'assigned')
        self.assertEqual(connections['JIRA-vob'].tkt_description, 'summary')
        self.assertEqual(connections['JIRA-vob'].tkt_status, 'status')
        self.assertEqual(connections['JIRA-vob'].criteria[0], "key in ('PSM-1', 'PSM-2')")

        self.assertEqual(connections['QTASK'].sys_type, 'qtask')
        self.assertEqual(connections['QTASK'].url, 'http://example.com')
        self.assertEqual(connections['QTASK'].tkt_requester, 'requester')
        self.assertEqual(connections['QTASK'].tkt_assigned, 'assigned')
        self.assertEqual(connections['QTASK'].tkt_description, 'description')
        self.assertEqual(connections['QTASK'].tkt_status, 'status')
        self.assertEqual(connections['QTASK'].criteria[0], "status != 'closed' and project = 'PPT'")
        self._teardown(config_filename, criteria_filename)

    def _setup(self) -> tuple:
        print("SETUP!")
        config_filename = 'test_config.txt'
        f = open(config_filename, 'w')
        f.write("name=JIRA-vob|sys_type=jira|url='http://example.com'|" +
                "tkt_requester=reporter|tkt_assigned=assigned|tkt_description=summary|tkt_status=status\n")
        f.write("name=QTASK|sys_type=qtask|url='http://example.com'|" +
                "tkt_requester=requester|tkt_assigned=assigned|tkt_description=description|tkt_status=status\n")
        f.close()
        criteria_filename = 'test_criteria.txt'
        f = open(criteria_filename, 'w')
        f.write("JIRA-vob|key in ('PSM-1', 'PSM-2')\n")
        f.write("QTASK|status != 'closed' and project = 'PPT'\n")
        f.close()
        # Add JIRA ticket...
        # Add QTASK ticket...
        return config_filename, criteria_filename

    def _teardown(self, config_filename: str, criteria_filename: str):
        print("TEAR DOWN!")
        os.remove(config_filename)
        os.remove(criteria_filename)
        # Remove JIRA ticket...
        # Remove QTASK ticket...


if __name__ == '__main__':
    unittest.main()
