# anna-discord-bot
Discord bot to action commands

Commands are set using the dict commands.

Key = command (minus action char '!')

value = function to be run (Function should return a message the bot will reply with)

```python
commands = {
    'help': func.show_help,
    'request': func.request,
    'invite': func.invite,
    'issue': func.send_feedback
}
```