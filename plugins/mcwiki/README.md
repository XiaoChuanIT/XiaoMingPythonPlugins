# 说明
搜索[Minecraft Wiki](https://minecraft.fandom.com/zh/wiki/Minecraft_Wiki)，使用了API，配合异步HTTP请求，大约消息处理部分能达100条/分钟。

# 需求的库
使用了异步HTTP请求，请安装```httpx```，或根据自己的需求更换为```pip3```、```conda```之类：
```bash
pip install httpx
```

# 作者
[HornCopper](https://github.com/HornCopper) - Python - 100%

# 版本
当前版本为```v1.0-HotFix```。

# 更新日志
## 已完成

* 异步HTTP请求；
* 异步&同步结合；
* 使用```curid```以缩短```url```长度；
* 使消息更加人性化。
## 正在进行

* 获取信息框图片（需要格式化成Mirai码）；
* ~~开发者少咕一点。~~

## 计划

* 添加对所有Wiki的适配，请参见[MediaWiki](https://mediawiki.org)。

# 标签
标签的限制使用请见Wiki。
```http``` ```async``` ```wiki```

# 不兼容性
* 运行此插件时**务必不要开启任何代理服务器包括但不限于```http```和```socks5```**，或者手动设置Python使用的代理，但是极不推荐，因为这可能需要多次修改启动参数以指定代理服务器。
