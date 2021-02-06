# anna-discord-bot
Discord bot to action commands

Commands are set using the dict commands.

Key = command (minus action char '!')

value = function to be run (Function should return a message the bot will reply with)

```python
commands = {
    'command': function_to_run,
    ...
}
```
