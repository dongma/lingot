# Lingot 
> `Lingot`受"哪吒系列"动画电影中"魔丸"和"灵珠"的影响，项目名取自中文"灵"(`Ling`)，与英文中表示"铸块"的词根 `-ingot`（如`Gold Ingot`金锭）结合，寓意"灵性的铸块"或"智能的原生体"。

### `miniconda`安装
进入`conda`的[下载页面](https://www.anaconda.com/docs/getting-started/miniconda/install#macos-2)，根据不同操作系统，执行对应的`shell`脚本：
```shell
# mac intel install
$ mkdir -p ~/miniconda3
$ curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
$ bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
$ rm ~/miniconda3/miniconda.sh
```
安装完成后，新创建一个`python`虚拟环境，命名为`deepseek`。
```shell
conda create -n deepseek python=3.13
# 激活环境
conda activate deepseek
```

### 安装`python`依赖包
```shell
pip install -r requirements.txt
```
### 配置DeepSeek API key
根据你使用的命令行工具，在`~/.bashrc`或`~/.zshrc`中配置`DEEPSEEK_API_KEY`环境变量：
```shell
export DEEPSEEK_API_KEY="xxxx"
```
### 安装和配置Jupter Lab
```shell
conda install -c conda-forge jupyterlab
```
使用`Jupyter Lab`开发的最佳实践是后台常驻，下面是相关配置（以`root`用户为例）：
```shell
# 生成 Jupyter Lab 配置文件，
jupyter lab --generate-config
```
打开上面执行输出的`jupyter_lab_config.py`配置文件后，修改以下配置项：
```shell
c.ServerApp.allow_root = True # 非 root 用户启动，无需修改
c.ServerApp.ip = '*'
```
使用`nohup`后台启动`Jupyter Lab`
```shell
nohup jupyter lab --port=8000 --NotebookApp.token='091235_newyork' --notebook-dir=./ &
```
`Jupyter Lab`输出的日志将会保存在`nohup.out`文件（已在`.gitignore`中过滤）。