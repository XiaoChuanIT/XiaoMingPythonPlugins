import httpx
import json
import socket
import sys
import threading

global redirect_flag 
global redirect_from
global redirect_to
async def get_url(url):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url,timeout=300)
            result = resp.text
            return result
        except:
            return "ヾ(≧へ≦)〃 小明的网络请求出现了故障。"
def api(title):
    return f"https://minecraft.fandom.com/zh/api.php?action=query&titles={title}&prop=extracts&exchars=500&format=json&redirects=True&explaintext=True"
async def wiki(title):
    redirect_flag = False
    redirect_from = None
    redirect_to = None
    info = json.loads(await get_url(api(title)))
    try:
        info["query"]["interwiki"]
        for i in info["query"]["interwiki"]:
            title = i["title"]
        interwiki_link = "https://minecraft.fandom.com/zh/wiki/" + title
        return f"ヾ(≧へ≦)〃 你的搜索跨站了嗷，小明没办法完成，但是小明可以给你链接：{interwiki_link}"
    except:
        curid_json = info["query"]["pages"]
        for i in curid_json:
            if str(i) == "-1":
                return f"ヾ(≧へ≦)〃 你要找的页面不存在哦。"
            else:
                try:
                    info["query"]["redirects"]
                    redirect_flag = True
                    for a in info["query"]["redirects"]:
                        redirect_from = str(a["from"])
                        redirect_to = str(a["to"])
                except:
                    redirect_flag = False
                curid = str(i)
        link = "https://minecraft.fandom.com/zh/index.php?curid=" + curid
        try:
            all_desc = str(curid_json[curid]["extract"])
            desc = all_desc[:int(all_desc.find("\n\n\n"))]
            if redirect_flag:
                return f"(๑•̀ㅂ•́)و✧  你的输入不准确哦，已经帮你将{redirect_from}重定向到{redirect_to}啦：\n{link}\n{desc}"
            else:
                return f"(๑•̀ㅂ•́)و✧  小明找到啦：\n{link}\n{desc}"
        except:
            return f"ヾ(≧へ≦)〃 小明发生了一些错误，是因为这个页面没有分段落造成的，但已经确认页面存在，链接如下：{link}"

def main():
    chaunwise = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 24826
    chaunwise.bind((host,port))
    chaunwise.listen(5)
    myaddr = chaunwise.getsockname()
    print("Server adress:%s"%str(myaddr))
    while True:
        clientsocket,addr = chaunwise.accept()
        print("socket adress:%s" % str(addr))
        try:
            t = ServerThreading(clientsocket)
            t.start()
            pass
        except Exception as identifier:
            print(identifier)
            pass
        pass
    chaunwise.close()
    pass
class ServerThreading(threading.Thread):
    # words = text2vec.load_lexicon()
    def __init__(self,clientsocket,recvsize=1024*1024,encoding="utf-8"):
        threading.Thread.__init__(self)
        self._socket = clientsocket
        self._recvsize = recvsize
        self._encoding = encoding
        pass
    async def run(self):
        print("thread start.....")
        try:
            msg = ''
            while True:
                rec = self._socket.recv(self._recvsize)
                msg += rec.decode(self._encoding)
                if msg.strip().endswith('CHUANWISE'):
                    msg=msg[:-9]
                    break
            print("accept msg:%s" % str(msg))
            sendmsg = await wiki(msg)
            self._socket.send(("%s"%sendmsg).encode(self._encoding))
            pass
        except Exception as identifier:
            self._socket.send("500".encode(self._encoding))
            print(identifier)
            pass
        finally:
            self._socket.close() 
        print("thread over.....")
        pass
    def __del__(self):
        pass
if __name__ == "__main__":
    main()
