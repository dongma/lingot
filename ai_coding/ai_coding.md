# `OpenClaw`、`Claude Code`安装

`OpenClaw`安装依赖于`node.js`，故进行前置安装：
```shell
# 安装nvm工具后，安装node.js 24
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install 24
nvm use 24   # 启用node.js 24
# 在node.js 24下安装openclaw，官网推荐的版本
npm install -g openclaw@latest
```

`npm`安装`Claude Code`，`node.js`也需要是`24`版本，由于外网模型受限，可以下载`cc-switch`对接国产大模型。
```shell
npm install -g @anthropic-ai/claude-code
# 官方建议的一键安装程序
curl -fsSL https://claude.ai/install.sh | bash
```


## `OpenClaw`安装`skills`
`clawhub`安装`skills`，执行完成后，会在`.openclaw/workspace`下生成一个`skills`文件夹。
```shell
npm i -g clawhub 
# 安装self-improving-agent skill
clawhub install "self-improving-agent"
```
