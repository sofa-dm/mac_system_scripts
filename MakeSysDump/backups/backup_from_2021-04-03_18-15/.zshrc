# all this stuff was autogenerated and i have no idea what it all means
# just like life
zstyle ':completion:*' completer _expand _complete _ignored
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' '' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}'
zstyle ':completion:*' menu select=5
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s


autoload -Uz compinit
compinit

autoload -U colors
colors

# the best prompt
# example: [@robb downloads]$
# export PROMPT="%{$fg_bold[magenta]%}[@%n %c]$ %{$reset_color%}"
export PROMPT="%{$fg_bold[red]%}[@%n %c]$ %{$reset_color%}"
# I LOVE HISTORY
# some people might say i love history too much
# i have never met these people
HISTFILE=~/.zsh_history
HISTSIZE=100000000
SAVEHIST=100000000


# because i love history, appendixes, and appending things
setopt appendhistory

# don't assume i want to cd, that's fucking rude
unsetopt autocd

# seriously why does this shit even exist
unsetopt beep

# DON'T YOU YELL AT ME WHEN YOU CAN'T FIND A MATCH
# THAT'S YOUR PROBLEM, _NOT_ MINE
unsetopt nomatch

# when i put a process in the background,
# it's code for "fuck off and leave me alone"
unsetopt notify


# there'll be time to type sudo when I'm dead
alias pacman="sudo pacman"

# "compile slow, run fast." - family motto
export CFLAGS="-Ofast -march=native -pipe -flto -fuse-linker-plugin"
export CXXFLAGS=${CFLAGS}
export LDFLAGS=${CFLAGS}

export EDITOR=vim
export VISUAL="$EDITOR"
source ~/.zaliases


# COLORIZED LS START
# ~/.dircolors/themefile
# eval $(gdircolors ~/.dircolors/dircolors.ansi-light)

eval $(gdircolors ~/.dircolors/dircolors.256akulich)

# Aliases
alias ls='gls --color=auto'
alias ll='ls -al'
# COLORIZED LS END

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/dm/opt/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/dm/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/dm/opt/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/dm/opt/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<



