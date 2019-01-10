# tmux — Terminal Multiplexer

## Description

Copied from Linux man page:

> tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen.
> tmux may be detached from a screen and continue running in the background, then later reattached.
>
> When tmux is started it creates a new session with a single window and displays it on screen.
> A status line at the bottom of the screen shows information on the current session and is used to enter interactive commands.
>
> A session is a single collection of pseudo terminals under the management of tmux.  
> Each session has one or more windows linked to it.  
>
> A window occupies the entire screen and may be split into rectangular panes, each of which is a separate pseudo terminal.
> Any number of tmux instances may connect to the same session, and any number of windows may be present in the same session.
>
> Once all sessions are killed, tmux exits.
