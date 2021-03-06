# Micro.Blog CLI

This project is under construction. Things may change. Often. 

## Overview

It is was it says it is. 

## Todo

- [ ] Tests!
- [ ] Complete all commands below. 

## Available Commands 

- [X] [account](#account)
- [X] [post](#post)
- [ ] [feed](#feed)
- [ ] [conversation](#conversation)
- [ ] [reply](#reply)
- [X] [follow](#follow)
- [X] [unfollow](#unfollow)
- [X] [am_following](#am_following)
- [X] [following](#following)

### account

```
$ microblog account add <username>
$ microblog account update <username>
$ microblog account switch <username>
$ microblog account list
```

Add, switch between, or list accounts.

### post 

``` 
$ microblog post <text>
$ microblog post -t <title> <text>
```

Post text to the current micro.blog account with an optional title. This is only available for hosted Micro.blog accounts for now. 

### feed 

```
$ microblog feed
$ microblog feed <username>
$ microblog feed --single
```

Show the current feed since the last viewed post or the most recent posts by a specific user.

-s/--single - View posts one at a time with options to continue or reply.

### conversation

```
$ microblog conversation <id>
```

Show the conversation around a given post id

### reply

```
$ microblog reply <text>
$ microblog reply <id> <text>
```

Reply to a specific post. If no post id is specified, uses the last post viewed from the feed.

### follow

```
$ microblog follow <username>
```

Follow somebody

### unfollow

```
$ microblog unfollow <username>
```

Unfollow somebody

### am_following

```
$ microblog am_following <username>
```

Determine if you are following a specific user. 

### following

```
$ microblog following <username>
```

Get a list of who a user is following. If no username is provided, defaults to current account. 
