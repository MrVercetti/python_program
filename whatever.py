# -*- coding:utf-8 -*-

import json
import requests
import xlwt
import time
from lxml import etree

# 解决编码的问题
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 获取存储职位信息的json对象，遍历获得公司名、福利待遇、工作地点、学历要求、工作类型、发布时间、职位名称、薪资、工作年限
def get_json(url, datas):
    my_headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/60.0.3112.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=',
    }
    cookies = {
        'Cookie': 'user_trace_token=20170824135842-485287de-8891-11e7-a544-525400f775ce; LGUID=20170824135842-48528e05-8891-11e7-a544-525400f775ce; JSESSIONID=ABAAABAAADEAAFI772FD1B9AABBF0C5553E874B0F860350; _putrc=B95D7C5E94F53DA8; login=true; unick=%E9%83%AD%E5%B2%A9; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=3; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1; TG-TRACK-CODE=index_search; SEARCH_ID=f0acbb8b2145433cb8fe7086f23be622; index_location_city=%E5%8C%97%E4%BA%AC; _gid=GA1.2.397092414.1504747009; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1504756944,1504761486,1504783443,1504839029; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1504839719; _ga=GA1.2.1499897355.1503554319; LGSID=20170908105032-7b45520c-9440-11e7-8aae-525400f775ce; LGRID=20170908110159-14c6e1a8-9442-11e7-8ab1-525400f775ce'
    }
    time.sleep(8)
    content = requests.post(url=url, cookies=cookies, headers=my_headers, data=datas)
    # content.encoding = 'utf-8'
    result = content.json()
    print result
    info = result['content']['positionResult']['result']
    # print info
    info_list = []
    for job in info:
        information = []
        information.append(job['positionId'])  # 岗位对应ID
        information.append(job['companyFullName'])  # 公司全名
        information.append(job['companyLabelList'])  # 福利待遇
        information.append(job['district'])  # 工作地点
        information.append(job['education'])  # 学历要求
        information.append(job['firstType'])  # 工作类型
        information.append(job['formatCreateTime'])  # 发布时间
        information.append(job['positionName'])  # 职位名称
        information.append(job['salary'])  # 薪资
        information.append(job['workYear'])  # 工作年限
        info_list.append(information)
        # 将列表对象进行json格式的编码转换,其中indent参数设置缩进值为2
        print json.dumps(info_list, ensure_ascii=False, indent=2)
        print info_list
    return info_list


def main():
    page = int(raw_input('请输入你要抓取的页码总数：'))
    # kd = raw_input('请输入你要抓取的职位关键字：')
    # city = raw_input('请输入你要抓取的城市：')


    info_result = []
    title = ['岗位id', '公司全名', '福利待遇', '工作地点', '学历要求', '工作类型', '发布时间', '职位名称', '薪资', '工作年限']
    info_result.append(title)
    for x in range(1, page + 1):
        url = 'https://www.lagou.com/jobs/positionAjax.json?&needAddtionalResult=false'
        datas = {
            'first': True,
            'pn': x,
            'kd': 'python',
            'city': '上海'
        }
        info = get_json(url, datas)
        info_result = info_result + info
        # 创建workbook,即excel
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建表,第二参数用于确认同一个cell单元是否可以重设值
        worksheet = workbook.add_sheet('lagouzp', cell_overwrite_ok=True)
        for i, row in enumerate(info_result):
            # print row
            for j, col in enumerate(row):
                # print col
                worksheet.write(i, j, col)
        workbook.save('lagouzp.xls')


if __name__ == '__main__':
    main()
