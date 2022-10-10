# Website Status Update Bot

A telegram bot that keeps you updated about the status of your website.

## Quick start guide

1. Get a telegram bot token from bot father
2. Create a channel and get the id of the channel
3. Clone the repository
4. Create a `.env` file. Refer to the section [here](#creating-a-env-file)
5. Create a cronjob based on the duration that you want (On your server)

## Creating a `.env` file

A sample `.env` is provided below

```
TELEGRAM_API_TOKEN = "Your telegram bot token"
GROUP_ID = "Your telegram group id"
URL = "URL you want to check"
```

## Disclaimer

This bot does not come with warranty of any kind.
Feel free to send a pull request if you want to make any form of improvements to the bot
