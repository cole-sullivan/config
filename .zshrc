#
# ~/.zshrc
# Used for executing user's shell configuration and executing commands
# Read when running as an interactive shell
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1="%{%F{9}%}%n%{%F{7}%}@%{%F{15}%}%m %{%F{9}%}%1~ %{%f%}%$ "
