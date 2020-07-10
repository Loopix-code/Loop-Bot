Les event: https://discordpy.readthedocs.io/en/latest/api.html#event-reference




Les permission discord :

create_instant_invite
Returns True if the user can create instant invites.



kick_members
Returns True if the user can kick users from the guild.



ban_members
Returns True if a user can ban users from the guild.



administrator
Returns True if a user is an administrator. This role overrides all other permissions.
This also bypasses all channel-specific overrides.



manage_channels
Returns True if a user can edit, delete, or create channels in the guild.
This also corresponds to the “Manage Channel” channel-specific override.



manage_guild
Returns True if a user can edit guild properties.



add_reactions
Returns True if a user can add reactions to messages.



view_audit_log
Returns True if a user can view the guild’s audit log.



priority_speaker
Returns True if a user can be more easily heard while talking.



stream
Returns True if a user can stream in a voice channel.



read_messages
Returns True if a user can read messages from all or specific text channels.



view_channel
An alias for read_messages.
New in version 1.3.



send_messages
Returns True if a user can send messages from all or specific text channels.



send_tts_messages
Returns True if a user can send TTS messages from all or specific text channels.



manage_messages
Returns True if a user can delete or pin messages in a text channel.
Note Note that there are currently no ways to edit other people’s messages.



embed_links
Returns True if a user’s messages will automatically be embedded by Discord.



attach_files
Returns True if a user can send files in their messages.



read_message_history
Returns True if a user can read a text channel’s previous messages.



mention_everyone
Returns True if a user’s @everyone or @here will mention everyone in the text channel.



external_emojis
Returns True if a user can use emojis from other guilds.



use_external_emojis
An alias for external_emojis.
New in version 1.3.



view_guild_insights
Returns True if a user can view the guild’s insights.
New in version 1.3.



connect
Returns True if a user can connect to a voice channel.



speak
Returns True if a user can speak in a voice channel.



mute_members
Returns True if a user can mute other users.



deafen_members
Returns True if a user can deafen other users.



move_members
Returns True if a user can move users between other voice channels.



use_voice_activation
Returns True if a user can use voice activation in voice channels.



change_nickname
Returns True if a user can change their nickname in the guild.



manage_nicknames
Returns True if a user can change other user’s nickname in the guild.



manage_roles
Returns True if a user can create or edit roles less than their role’s position.

This also corresponds to the “Manage Permissions” channel-specific override.


manage_permissions
An alias for manage_roles.



manage_webhooks
Returns True if a user can create, edit, or delete webhooks.


manage_emojis
Returns True if a user can create, edit, or delete emojis.
