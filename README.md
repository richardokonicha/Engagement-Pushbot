# Claire Push bot

###### This is an Instagram engagement push bot 

Engagement groups define a number of social media users who meet through messenger services like Telegram to exchange comments and likes on each others posting on Instagram or Facebook. Sometimes these groups are titled as comment pods or engagement pods
designed to manage  groups. see [Engagement Groups](https://influencerdb.com/blog/engagement-groups/)

Claire Push bot is a telegram bot that is design to manage an engagement group
automatically, taking away most of the hasle of managing an engagement group.

How Claire functions
. Users interested in joining an engagement community can register with Claire and stores their information on Her database 
. An Engagement round can be triggered using a command "/round" only by the admin or a cron/repeating process that would cause a round to be started at a defined interval.
. Once a round is started, users who are registered as members would recieve a notification and can decide to be part of the engagement round started by clicking the join button which add their instagram username to the pool.
. Claire generates a list of all users in the pool who indicated interest and assigns the list to each of them.
. When a user joins a round, they are required to like the last post of every other user on the list generated for them by Claire to fulfill requirement.
. When a user fails to fulfill the above requirement he can be warned by the admin. 
. When a user is warned three times he is automatically blocked from joining any round until he is freed by the admin
. Users can send messages to the admin directly from the bot Claire  /support <followed by their complaint>
. User complaint are forwarded to the admins; admins can respond to users by replying these complaint which are then forwarded to which ever user that sent them.
. Users do not need to interact with each other or the admin in any way, Claire manages every action
. Admin have Ultimate power and can delete a user, block and unblock a user, warn a user, send warning messages to a user and set time for rounds to start

