import argparse
from jira.client import JIRA
from jira.config import get_jira

def GetParameters():
	parser = argparse.ArgumentParser(description='Interface with Jira projects.')
	parser.add_argument('--project', '-p', default=False, dest='project_ID')
	parser.add_argument('--get', '-g', action='store_true', default=False, dest='get_project')
	parser.add_argument('--update', '-u', action='store_true', default=False, dest='update_project')
	parser.add_argument('--test', '-t', action='store_false')
	_args = parser.parse_args()
	vars(_args)
	return (_args)

def connect_jira(jira_server, jira_user, jira_password):
	'''
	Connect to JIRA. Return None on error
	'''
	try:
		print("Connecting to JIRA: %s" % jira_server)
		jira_options = {'server': jira_server}
		jira = get_jira(profile='jira')
		jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
		return jira   
    except Exception as e:
        print("Failed to connect to JIRA: %s" % e)
        return None
	

def EstablishAuthentication():
	print ('In EstablishAuthentication')

	#jira=connect_jira("http://rentrak.atlassian.net", "dam", "inatercamp1")
	jira=connect_jira("x","x","x")

	return jira

def GetProject(jira):
	print ('In GetProject')
	if args.project_ID:
		print ('getting project ' + args.project_ID)
		prj = jira.project(args.project_ID)
		print ('Project Name ' + prj.name)
		vars ('Project properties: ' + prj)
	else:
		print ('You must provide a project to get!')
		exit(-1)
	return 1
def UpdateProject():
	print ('In UpdateProject')
	print ('In GetProject')
	if args.project_ID:
		print ('updating project ' + args.project_ID)
	else:
		print ('You must provide a project to update!')
		exit(-1)
	return 1


###########################################
#
# MAIN
#
###########################################

args = GetParameters()
jira=EstablishAuthentication()
if args.get_project:
	GetProject(jira)
if args.update_project:
	UpdateProject()

exit()

