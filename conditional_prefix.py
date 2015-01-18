from cloudbot import hook

import re

@hook.sieve
def conditional_prefix(bot, event, plugin):
    if plugin.type == 'command':
        if event.chan in event.conn.config['prefix_blocked_channels']:
            command_prefix = event.conn.config['command_prefix']

            if not event.chan.lower() == event.nick.lower():  # private message, no command prefix
                command_re = r'(?i)^(?:[{}])(\w+)(?:$|\s+)(.*)'.format(command_prefix, event.conn.nick)

                if re.match(command_re, event.content):
                    return None
    return event
