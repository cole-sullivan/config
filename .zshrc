# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

#
# ~/.zshrc
# Used for executing user's shell configuration and executing commands
# Read when running as an interactive shell
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Add all directories in ~/.local/bin to $PATH
export PATH="$PATH:$(find ~/.local/bin -type d | paste -sd ':' -)"

alias ls='ls --color=auto'
alias grep='grep --color=auto'

source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
