from charms.reactive import when_not
from charmhelpers.core.hookenv import is_leader, status_set


@when_not('dummy')
def set_status():
    status_set('active', 'Leader: {}'.format(is_leader()))
