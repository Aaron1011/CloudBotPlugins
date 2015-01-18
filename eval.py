from cloudbot import hook

@hook.command("eval", permissions=["botcontrol"])
def eval_command(text, chan, nick, db, conn, bot, message, reply,
        action, ctcp, notice, has_permission):
    exec(text)
