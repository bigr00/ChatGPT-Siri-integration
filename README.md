# ChatGPT Siri integration

## Apple Shortcuts based approach for ChatGPT

## Main features
- Supports Apple Watch, iPad, iPhone and MacOS
- "Hey Siri" support
- Clipboard pasting and reading
- Change system message to what you need
- More languages supported than English
- Keyboard shortcuts to trigger ChatGPT

## Guide

The basis of this service is the OpenAI chat completions. This requires an OpenAI API key.

### Guide for OpenAI API key
1. [Log into OpenAI (Google login supported)](https://platform.openai.com)
2. [Go to API keys](https://platform.openai.com/account/api-keys)
3. Create new secret key -> Copy key. Once key is created, it is hidden from web, take that into account.
4. [Do not give your key to anybody!](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
5. Download [Execute OpenAI API.shortcut](https://github.com/bigr00/ChatGPT-Siri-integration/blob/main/Execute%20OpenAI%20API.shortcut)
6. Copy key to "Execute OpenAI API" shortcut Text 
7. Run automation, allow permissions. [Short guide.](#about-shortcut-files)
8. Download [Smarty Pants](https://github.com/bigr00/ChatGPT-Siri-integration/blob/main/Smarty%20Pants.shortcut)
9. Download [more .shortcut files that uses "Execute OpenAI API.shortcut".](https://github.com/bigr00/ChatGPT-Siri-integration)

You have free 18 dollars of usage with OpenAI. This will take a while to spend.

## You're set! Run the automation or use "Hey Siri".
You can either run the automation without Siri, add it to your Dock or keyboard shortcut or ask Siri to run the automation. Current name of the Voice Assistant is Smarty Pants. You can change that, by renaming the automation.

Example Siri commands:
- "Hey Siri. Smarty Pants. What are some good programming languages for smartphones?."
- "Hey Siri. Use clipboard with Smarty Pants. Translate it to English and change the tone to friendly."

## Make your own automation
The "Execute OpenAI API" automation is designed in a way that it is possible to use it in your own automation. It receives input from another automation and if there is no automation executing it, it will ask for input with a text box. 

For example you can create automation specific to your own needs, forwarding input or using the output of the "Execute OpenAI API" automation in a custom way.

[Examples.](https://github.com/bigr00/ChatGPT-Siri-integration/tree/main/Examples)

## Changing system message 

System message is the context, or [pre-load that you pass to ChatGPT before you start talking.](https://platform.openai.com/docs/guides/chat/introduction)

## Clipboard features
You can run the automation: "Copy to Smarty Pants" that will take your clipboard contents and forward it to ChatGPT alongside with the user input. 
### This is limited by max tokens - 4096 for ChatGPT

For example:
- Copy a table of basketball scores.
- Trigger "Copy to Smarty Pants"
- "What are some interesting conclusions for this basketball game?"
- Result is copied to clipboard.

## Share the results
You can use the "Share" functionality of the result window in the automation trigger or use the provided share automations.

## Max tokens
Every request is spent according to words used and words answered. [Measuring unit is a token - about 0.75 English words.](https://platform.openai.com/docs/guides/chat/managing-tokens)

When you have longer questions or longer answers, you will burn through your tokens faster. 
One can limit tokens by adding the variable "max_tokens" to the API request *Get contents of URL*.

Every model has their own maximum query size - ChatGPT has 4096.

## Language support
Siri supports only a select amount of languages, but ChatGPT supports more.

## About .shortcut files
iPhone, iPad:
YOUTUBE VIDEO

MacOS:
Just click on file. Before adding, you can look into the automation.
