import jira_load
import unittest

__author__ = 'Darryl Martin'


class LoadJiraLoadCase(unittest.TestCase):
    def test_get_parameters_all_long_arguments(self):
        test_args = jira_load.get_parameters(predefined_args=
                                             ("--url https://myco.atlassian.net --user test_user --get" +
                                             " --query issue=PROJECT-145 --password test_password --file test_file" +
                                             " --project=MYPROJECT --test --update")
                                             .split(" "))
        self.assertEqual(test_args.jira_server, "https://myco.atlassian.net", "Failed to process 'url' argument.")
        self.assertEqual(test_args.jira_user, "test_user", "Failed to process 'user' argument.")
        self.assertTrue(test_args.get_tasks, "Failed to process 'get' argument")
        self.assertEqual(test_args.jira_query, "issue=PROJECT-145", "Failed to process 'query' argument.")
        self.assertEqual(test_args.jira_password, "test_password", "Failed to process 'password' argument.")
        self.assertEqual(test_args.arg_file, "test_file", "Failed to process 'file' argument.")
        self.assertEqual(test_args.project_ID, "MYPROJECT", "Failed to process 'project' argument.")
        self.assertTrue(test_args.update_project, "Failed to process 'update' argument")
        self.assertTrue(test_args.test_only, "Failed to process 'test' argument")

    def test_get_parameters_all_short_arguments(self):
        test_args = jira_load.get_parameters(predefined_args=
                                             ("-s https://myco.atlassian.net -u test_user -G" +
                                             " -q issue=PROJECT-145 -p test_password -f test_file" +
                                             " -P=MYPROJECT -t -U")
                                             .split(" "))
        self.assertEqual(test_args.jira_server, "https://myco.atlassian.net", "Failed to process 'url' argument.")
        self.assertEqual(test_args.jira_user, "test_user", "Failed to process 'user' argument.")
        self.assertTrue(test_args.get_tasks, "Failed to process 'get' argument")
        self.assertEqual(test_args.jira_query, "issue=PROJECT-145", "Failed to process 'query' argument.")
        self.assertEqual(test_args.jira_password, "test_password", "Failed to process 'password' argument.")
        self.assertEqual(test_args.arg_file, "test_file", "Failed to process 'file' argument.")
        self.assertEqual(test_args.project_ID, "MYPROJECT", "Failed to process 'project' argument.")
        self.assertTrue(test_args.update_project, "Failed to process 'update' argument")
        self.assertTrue(test_args.test_only, "Failed to process 'test' argument")

    def test_get_parameters_defaults(self):
        test_args = jira_load.get_parameters()
        self.assertFalse(test_args.jira_server, "Failed to default 'url' argument.")
        self.assertFalse(test_args.jira_user, "Failed to default 'user' argument.")
        self.assertFalse(test_args.get_tasks, "Failed to default 'get' argument")
        self.assertFalse(test_args.jira_query, "Failed to default 'query' argument.")
        self.assertFalse(test_args.jira_password, "Failed to default 'password' argument.")
        self.assertFalse(test_args.arg_file, "Failed to default 'file' argument.")
        self.assertFalse(test_args.project_ID, "Failed to default 'project' argument.")
        self.assertFalse(test_args.update_project, "Failed to default 'update' argument")
        self.assertFalse(test_args.test_only, "Failed to default 'test' argument")

    def test_connect_jira(self):
        jira = self._jira.connect_jira("server", "user", "password")
        self.assertIsNone(jira, "Unexpected JIRA connection.")
        # No further tests. We don't have a JIRA test connection available.

    def test_establish_authentication(self):
        pass
        # No way to test this at this time.

    def test_get_tasks(self):
        pass
        # TO DO

    def test_get_project(self):
        pass
        # TO DO

    def test_update_project(self):
        pass
        # TO DO

    def setUp(self):
        self._jira = jira_load.JiraLoader()

    def tearDown(self):
        self._jira = None


if __name__ == '__main__':
    unittest.main()
