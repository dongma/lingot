# Lingot 
> `Lingot`受"哪吒系列"动画电影中"魔丸"和"灵珠"的影响，项目名取自中文"灵"(`Ling`)，与英文中表示"铸块"的词根 `-ingot`（如`Gold Ingot`金锭）结合，寓意"灵性的铸块"或"智能的原生体"。

### `miniconda`安装
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