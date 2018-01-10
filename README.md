# Micro.Blog CLI

This project is under construction. Things may change. Often. 

## Overview

It is was it says it is. 

## Available Commands 

- [ ] [account](#account)
- [ ] [post](#post)
- [ ] [feed](#feed)
- [ ] [conversation](#conversation)
- [ ] [reply](#reply)

### account

```
$ microblog account add <username>
$ microblog account switch <username>
$ microblog account list
```

Add, switch between, or list accounts.

### post 

``` 
$ microblog post <text>
$ microblog post -t <title> <text>
```

Post text to the current micro.blog account with an optional title.

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


