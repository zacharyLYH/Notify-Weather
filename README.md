🌤 Notify Weather
===
A desktop app that eliminates your need to check the weather ever again. We supply a timed notification of what to take out the house for the day, and what kind of weather to expect tomorrow.

# 🍿 Features
* Send system prompts notifying user about weather status
* Ask for when the user 1. leaves the house and 2. expects to go to sleep

# 🌩 Weather API
This app uses the one-call api to fetch weather information based on *location*, *time preferences*
`https://openweathermap.org/api/one-call-api`

# 💭 Notification Generator
There are two type of notifications. One delivers **today's weather** and the other **tomorrow's weather**

> **Process**
> Get info from weather API. If the the user wants today's or tomorrow's weather it returns
> * Temperature
> * Weather
> * Feels like temperature
> * Chance of precipitation
> 
> It will also produce a **what to bring** message. Example below
> > ☔️ Bring an umbrella!

**What to Bring**
This is decided on what the conditions are like. Examples below
| Condition            | Message                                                           |
| ---                  | ---                                                               |
|If raining            | ☔️ Bring an umbrella!                                              | 
|If snowing            | ☃️ Bring a jacket it's snowing                                     | 
|If cold and sunny     | 😎 Bring sweater and shades it's not warm yet                     | 
|If warm and sunny     | ☀️ Dress lightly and bring shades                                    | 