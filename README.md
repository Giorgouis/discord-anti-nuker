# discord-mass-channel-delete

A simple bot command I made with discord.py so you can prevent or "fix" your server from a raid.

` you are gonna need a discord bot token`

# How to use

Copy the code
Make sure you have python 3 installed
 
 `pip install discord`
 
 Copy your discord bot token, you can create a bot and get the bot token at https://discord.com/developers/applications
 
 go to the last line of the code and replace `client.run(TOKEN)` with `client.run("your token here ctrl+v")` or `client.run('your token here ctrl+v')`(so it's on a string)
 
run the code

# Commands

### Prefix: ac!

 #### delete_messages <message>
  ###### deletes new messages that are equal to message
 #### delete_channels <channel_name> [exceptions]
  ###### channel_name: name of the channels you want to delete
  ###### exceptions: channel IDs from channels with the same name you might not want to delete
  if more than 1, seperate with `, `
 
 #### delete_roles <role_name> [exceptions]
  ###### role_name: name of the roles you want to delete
  ###### exceptions: role Ids from roles with the same name you might not want to delete
  if more than 1, seperate with `, `
