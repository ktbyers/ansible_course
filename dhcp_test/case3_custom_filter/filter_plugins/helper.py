from __future__ import unicode_literals
from __future__ import print_function

import io
from ciscoconfparse import CiscoConfParse


def ip_helper(config):
    """Process config find interfaces using ip helper."""
    cfg = CiscoConfParse(config.splitlines())
    helper_obj = cfg.find_objects_w_child(parentspec=r"^interface ", childspec=r"ip helper-address")
    return_intf = []
    for helper in helper_obj:
        _, intf_name = helper.text.split('interface ')
        return_intf.append(intf_name)

    print(return_intf)
    return return_intf


class FilterModule(object):
    """Jinja2 filter to process interfaces finding ip-helper.

    Takes router config file.

    Returns list of VLANs configured with ip-helper.
    """
    def filters(self):
        return {
            'ip_helper': ip_helper,
        }


if __name__ == "__main__":

    # Test code
    test_file = 'pynet_rtr1.txt'
    with io.open(test_file, "rt", encoding='utf-8') as f:
        router_config = f.read()
    ip_helper(router_config)
