# Ansible Lookup plugin - Github team members

this small project is an [ansible](todo link) [lookup plugin](todo link) that
fetches [Github](todo link) users that belong to a given team.
This small project is an [Ansible](https://www.ansible.com/) [lookup
plugin](https://docs.ansible.com/ansible/2.5/plugins/lookup.html) that
fetches [Github](https://github.com/) [users that belong to a given
team](https://developer.github.com/v3/teams/).

Calling the team APi to directly get members of a team is however often not 
enough since it actually only returns public members of this team. If you 
belong to an organization that has teams, you can view these teams members.

