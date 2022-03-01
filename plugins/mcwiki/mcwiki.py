# -*- coding: utf-8 -*-
import httpx
import json
import asyncio

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
            return "ヾ(≧へ≦)〃 小明的网络请求出现了故障。" # Meaningless because of this line has no fact effect
def api(msg):
    return f"https://minecraft.fandom.com/zh/api.php?action=query&titles={msg}&prop=extracts&format=json&redirects=True&explaintext=True"
async def wiki(title):
    redirect_flag = False
    redirect_from = None
    redirect_to = None
    info = await get_url(api(title))
    info = json.loads(info)
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
                return f"ヾ(≧▽≦*)o  你的输入不准确哦，已经帮你将{redirect_from}重定向到{redirect_to}啦：\n{link}\n{desc}"
            else:
                return f"ヾ(≧▽≦*)o  小明找到啦：\n{link}\n{desc}"
        except:
            return f"ヾ(≧へ≦)〃 小明发生了一些错误，是因为这个页面没有分段落造成的，但已经确认页面存在，链接如下：{link}"

def main():
    title = input()
    msg = asyncio.run(wiki(title))
    print(msg.encode('gbk', 'ignore').decode('gbk'))
if __name__ == "__main__":
    main()
