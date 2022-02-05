# 介绍
此仓库内的文件若无特殊情况，**均为Python(`.py`)格式**，同时，既然您选择使用Python来进行开发，那么欢迎您提交自己的模块！

## 适用对象
使用Socket和子进程进行调用理论上都可以，但设计的初衷是为了给[小明](https://github.com/Chuanwise/XiaoMingBot)，与小明一样，但本仓库并不会因小明的停止开发而终止。~~删库跑路？不存在的~~

## 语言
~~废话那当然是伟大的[Python][1]了。~~

由于设计初衷，本仓库只收录Python格式的插件，若您想贡献其他语言插件，请联系小明的开发者~~椽椽子~~。

[1]: https://www.python.org
## 配置
由于各个插件实现的功能不尽相同，请参考插件内的`README.md`，进行相应的库安装。~~当然你也可以使用仓库主目录下的懒人脚本然后一条命令直接快活。~~

若无歧义，每个插件对应的`README.md`中的`pip`均可根据需要换成`pip3`

~~快捷方式~~
```bash
pip install -r requirements.txt
```
## 环境
请尽可能使用```Python 3.8/3.9/3.10```，最低请不要低于```3.7.3```（```Debian 10```自带），若您尚未安装Python，且连接官网很慢或根本无法连接，不妨试试阿里巴巴的[Python镜像](https://registry.npmmirror.com/binary.html?path=python/)以及[PyPI镜像](https://developer.aliyun.com/mirror/pypi)。

同时，系统版本尽可能选择Linux，尤其推荐```Ubuntu```、```Debian```或```CentOS```，若认为需要使用```Windows```，也请您务必配置好环境。

~~说了这么多，其实更推荐Conda。~~

另外，由于可能会用的OS命令，您所选择的操作系统请务必支持```path```。

# 贡献

## About us
此仓库目前由HornCopper进行维护，椽子也会抽空看一眼。

## For you
若您想要参与贡献，请提交Pull Request，相关人员会检查您的代码。

## 指南
一个插件只能含有一个文件，所以您只能将所有需要的函数定义在文件内，包括但不限于异步HTTP请求、事件响应器，这些**请您都放置在同一个文件内**。

### 快捷代码
您没有必要全部手搓，部分代码您可以（部分甚至强制您）从此处复制：

#### 异步HTTP GET请求(httpx)
```python
import httpx

async def get_url(url):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url,timeout=300)
            result = resp.text
            return result
        except:
            return "ヾ(≧へ≦)〃 小明的网络请求出现了故障。
```
#### 异步HTTP POST请求(httpx)
```python
import httpx

async def get_url(url):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url,timeout=300)
            result = resp.text
            return result
        except:
            return "ヾ(≧へ≦)〃 小明的网络请求出现了故障。
```
