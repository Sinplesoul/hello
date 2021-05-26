# 查看指定仓库中所有镜像与标签

import requests
import json
import traceback
#python 3.6
#repo_ip = '172.18.228.109'
#repo_port = 5000
print("查询指定私有仓库的所有镜像及其tag，按示例输入仓库地址。")
repo_ip = input("请输入仓库地址（示例：81.68.126.166）：")
repo_port = input("请输入仓库端口（示例：5000）：")

def getImagesNames(repo_ip,repo_port):

    docker_images = []
    try:
        url = "http://" + repo_ip + ":" +str(repo_port) + "/v2/_catalog"
        res =requests.get(url).content.strip()
        res_dic = json.loads(res)
        images_type = res_dic['repositories']
        for i in images_type:
            url2 = "http://" + repo_ip + ":" +str(repo_port) +"/v2/" + str(i) + "/tags/list"
            res2 =requests.get(url2).content.strip()
            res_dic2 = json.loads(res2)
            name = res_dic2['name']
            tags = res_dic2['tags']
            for tag in tags:
                docker_name = str(repo_ip) + ":" + str(repo_port) + "/" + name + ":" + tag
                docker_images.append(docker_name)
                print (docker_name)
    except:
        traceback.print_exc()
    return docker_images

a=getImagesNames(repo_ip, repo_port)
#print (a)
