# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

# pnpm
export PNPM_HOME="/home/admin/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# OpenClaw Completion
source "/home/admin/.openclaw/completions/openclaw.bash"
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv bash)"

# Claude Code 环境变量 (绕过登录)
export ANTHROPIC_AUTH_TOKEN="Your API Secret"
export ANTHROPIC_BASE_URL="https://api.minimaxi.com/anthropic"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="MiniMax-M2.1"
export ANTHROPIC_DEFAULT_OPUS_MODEL="MiniMax-M2.1"
export ANTHROPIC_DEFAULT_SONNET_MODEL="MiniMax-M2.1"
export ANTHROPIC_MODEL="MiniMax-M2.1"
export PATH=~/.npm-global/bin:$PATH
