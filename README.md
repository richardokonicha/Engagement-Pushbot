# Chukwudi Push bot [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fkonichar%2FEngagement-Pushbot&via=konichar&text=Checkout%20this%20cool%20Instagram%20Engagement%20bot%20for%20Telegram.%20&hashtags=telegram%2Cinstagrambot%2Cengagement)
> This is a Telegram Engagement Push bot designed to organize and manage an Engagement groups automatically to help members increase engagement on each other’s social media content; taking away most of the hasle of managing an engagement group from admins. See Bot [@chukwudi_pushbot](https://telegram.me/chukwudi_pushbot)


<p align="center">
<a href="https://github.com/konichar" target="_blank" rel="noopener noreferrer">
    <img src="https://media.giphy.com/media/UX4jlqJHg2qXAzqARz/giphy.gif" width="150" alt="re-frame logo">
  </a>
  <a href="https://github.com/konichar" target="_blank" rel="noopener noreferrer">
    <img src="./assets/chukwudi.svg" width="300" alt="re-frame logo">
  </a>
  <a href="https://github.com/konichar" target="_blank" rel="noopener noreferrer">
    <img src="https://media.giphy.com/media/gdfoIF3QFMGWsj18ri/giphy.gif" width="150" alt="re-frame logo">
  </a>
</p>


</p align="center">
   <a href="https://www.instagram.com/r.e.e.c.h.e.e" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/r.e.e.c.h.e.e-ffcbcb?style=social&logo=instagram" alt="re-frame logo"></a>
    <a href="https://twitter.com/konichar" target="_blank"><img src="https://img.shields.io/twitter/follow/konichar?style=social" alt="re-frame logo"></a>
    <a href="https://github.com/konichar/Engagement-Pushbot" target="_blank"><img src="https://img.shields.io/github/stars/konichar/engagmentpushbot?style=social" alt="re-frame logo"></a>
<p>


<!-- ![Chukwudi](./assets/chukwudi.svg#L1) -->
<!-- <img src="./assets/chukwudi.svg"> -->
<!-- 
![Alt text](https://raw.github.com/konichar/engagmentpushbot/blob/master/assets/chukwudiupper.svg#L1)
<img src="https://raw.github.com/konichar/engagmentpushbot/blob/master/assets/chukwudiupper.svg#L1"> -->


![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/konichar/Engagement-Pushbot?logo=python)
![GitHub last commit](https://img.shields.io/github/last-commit/konichar/Engagement-Pushbot?color=%23679b9b&logoColor=%23679b9b)
![GitHub repo size](https://img.shields.io/github/repo-size/konichar/engagmentpushbot?color=%23679b9b&logo=%23663399&logoColor=%23117A65%20&style=plastic)
<!-- ![GitHub deployments](https://img.shields.io/github/deployments/konichar/Engagement-Pushbot/epush-bot?color=%23aacfcf&logoColor=%23aacfcf&style=plastic&logo=appveyor) -->

---
<!-- 
[![GitHub stars](https://img.shields.io/github/stars/konichar/engagmentpushbot?style=social)](https://github.com/konichar/Engagement-Pushbot)
[![GitHub watchers](https://img.shields.io/github/watchers/konichar/engagmentpushbot?color=%23ffcbcb&style=social)](https://github.com/konichar/Engagement-Pushbot)
[![Twitter Follow](https://img.shields.io/twitter/follow/konichar?style=social)](https://twitter.com/konichar)
[![Instagram](https://img.shields.io/badge/r.e.e.c.h.e.e-ffcbcb?style=social&logo=instagram)](https://www.instagram.com/r.e.e.c.h.e.e/) -->



Engagement groups define a number of social media users who meet through messenger services like Telegram to exchange comments and likes on each others posting on Instagram or Facebook. Sometimes these groups are titled as comment pods or engagement pods
designed to manage  groups. see [Engagement Groups](https://influencerdb.com/blog/engagement-groups/)

---
>- [How Users interact with Chukwudi](#How-Users-interact-with-Chukwudi)
>- [How Admins interact with Chukwudi](#How-admins-interact-with-Chukwudi)
>- [How to setup Chukwudi](#How-to-Setup-Chukwudi)

## How Users interact with Chukwudi

- Users interested in joining the engagement group can register with Chukwudi as members using the command `/start` and tapping on `register` button.

- Users can set social media handle to be liked. ex. `https://Instagram.com/r.e.e.c.h.e.e`

- Engagement Rounds are triggered at specific times; this is set by the Admin

- Members are notified about the start of a Round during a Drop Session; which is a few minutes/seconds before a round starts; they have a button option to `Join` the coming round or pass.

- Round starts immediately after Drop Session ends. Only Members who joined the round can participate in that Round.

- Chukwudi generates a list of all RoundParticipant's social media links i.e  `https://Instagram.com/allparticipantsprofiles`; shuffles the list and sends list to all RoundParticipants with instructions. 

- RoundParticipants are required to goto the links provided, like and comment on the last social media post of every other RoundParticipant on the list distributed. 

- All Members can be sent a warning by Admin if they fail to like and comment on other RoundParticipants posts or abide by any of the engagement rules set by Admin. Users are blocked from joining any round after three warnings and would need to send complaint to the Admin/support.

- Users can send complains to Admins using the command `/support followed by their complaint` e.g. `/support please reactivate my account`

- Users/Members do not need to interact with each other or the admin directly in any way, Chukwudi manages every action.

- Users/Members have access to a mini dashboard that displays number of warns they have and number of engagements they have been part of as well as the time of the next engagement using the command `/dashboard`, `/menu`. 


## How Admins interact with Chukwudi

- Admins can set specific times for engagement rounds to be triggered automatically during installation or setup this is a cron/repeating process Admins can also manually trigger a Round using the command "/round"-only an Admin can use this command.

- When a user fails to fulfill the above requirement he can be warned by the Admin with the command `/warn @username`, a user is blocked from joining rounds after three warn until freed.

- Admins can free users from blocks by taking their number of warns to zero with the command `/free @username`

- Admins would recieve all User complaints, questions and can send responses to the users by replying on the exact message that was sent by user.

- Admins can view all users and their number of warns with the command `/warn`

- Admin have Ultimate power and can `/delete` a user, block and unblock a user, warn a user, send warning messages to a user and set time for rounds to start.

> For more comprehensive command listing see document > link


## How to setup Chukwudi for develpment

- Goto to the project's  [Github page](https://github.com/konichar/Engagement-Pushbot) and star this project by tapping on the star button at the top right of the page.

- Clone this repository using `git clone <link>`
- Create a .env file; this is where your configuration would live.
```bash
Created .env file

//make list of Userids Admins, seperated by spaces
ADMIN=123456789 3445454656

// cron job for automatic round trigger at set time
CRON=50 15,17,19 * * *

// Created Telegram bot token from bot father
TOKEN=821000128:EXAMple_toKENBOTtokenI0WDiayAnxxqGFmyU

// url of your bot when hosted at heroku - for deployment use only
URL='your-bot.herokuapp.com'

// Session duration <dropsession duration = 10minutes> <checklist notification=10minutes before endofround > <round duration = 30minutes>
SESSION_DURATION=10 10 30

// Always set to True for development (locally), set to False when deployed on heroku
DEBUG=True
```

- Create a python virtual environment and install the requirements

  Install pipenv
  ```
  pip install pipenv
  ```
  Create virtual environment within project directory and activate
  ```
  pipenv shell
  ```
  Installing dependency from Pipfile.lock
  ```
  pipenv install
  ```

- Run application from the entry point `epush_bot.py`

  Run application from entry point
  ```
  python epush_bot.py
  ```


## Built With

* [Flask](https://flask.palletsprojects.com/) - The web framework used
* [pytelebotapi](https://github.com/eternnoir/pyTelegramBotAPI) - Telegram bot API wrapper
* [Heroku](https://heroku.com/) - Deployment

## Authors

* **Richard Okonicha** 

## License

This project is licensed under the MIT License and is free to use and reproduce - see the [LICENSE.md](LICENSE.md) file for details

Built with love and the spirit of [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu_philosophy) >>>
~~Star this repo *~~





