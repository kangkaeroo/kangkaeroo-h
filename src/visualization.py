# 可视化模块
import shelve
import pandas as pd
import matplotlib.pyplot as plt
from jieba import lcut
from wordcloud import WordCloud


def generateWordCloud(bvid):
    ''' 给定bvid，生成 产生对应视频弹幕的词云图 的函数
    
    params: bvid(str): 用于生成弹幕词云图的视频的bvid

    return: generate(func -> None): 用于 生成对应视频弹幕的词云图 的函数
    '''
    # 读取 bvid 对应视频的所有弹幕信息
    with open('../danmu/' + bvid + '-danmu.csv', encoding='utf-8-sig') as dmk_file:
        all_danmukus = ''.join([ele.strip('\n').split(',')[-1] for ele in dmk_file.readlines()][1:])

    def generate(*args, **kwargs):
        ''' 用于生存指定视频的弹幕词云图
        
        params: 参考 wordcloud.WordCloud 类实例化对象时需要的参数
                详情参见：http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud

        return: None
        '''
        # 生成词云图   
        wordcloud_pic = WordCloud(*args, **kwargs)
        wordcloud_pic.generate(' '.join([ele for ele in lcut(all_danmukus) if len(ele) > 1]))
        wordcloud_pic.to_file('../img/wordcloud/' + bvid + '-Wordcloud' + '.jpg')
    
    return generate


def generateDensityPic(bvid):
    ''' 给定bvid，生成 产生对应视频弹幕的密度图 的函数
    
    params: bvid(str): 用于生成弹幕词云图的视频的bvid

    return: generate(func -> None): 用于 生成对应视频弹幕的密度图 的函数
    '''
    danmaku_info = pd.read_csv('../danmu/' + bvid + '-danmu.csv', encoding = 'utf-8-sig')
    
    def generate(title, xlabel, ylabel):
        ''' 用于生存指定视频的弹幕密度图，即
            横坐标: 从第一条弹幕出现到最后一条弹幕出现，中间所有的时刻，单位: 秒
            纵坐标: 横坐标时刻 对应的弹幕总数
        
        params: title: 密度图的标题
                xlabel: 密度图横坐标轴的名称
                ylabel: 密度图纵坐标轴的名称

        return: None
        '''
        # 对 弹幕发送相对于视频播放时间 的时刻进行取整 (单位：秒)
        danmaku_info['video_time'] = danmaku_info['video_time'].apply(lambda x: int(round(x, 0)))
        total_dmk_per_sec = dict(danmaku_info.groupby('video_time').size())
        # 从第一次出现弹幕的时刻，到最后一次出现弹幕的时刻，中间没有弹幕的时刻用0值填充
        for sec in range(min(danmaku_info['video_time']) + 1, max(danmaku_info['video_time'])):
            if sec not in total_dmk_per_sec.keys():
                total_dmk_per_sec[sec] = 0
        #可视化
        x_axis = sorted(total_dmk_per_sec.keys())
        y_axis = [total_dmk_per_sec[v] for v in x_axis]
        plt.plot(x_axis, y_axis)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.savefig('../img/density/' + bvid + '-density figure.jpg')
        plt.close()

    return generate


def generateNumberFig(bvids, partition_method):
    ''' 给定所有bvid的集合，以及划分集合的方法，生成 产生不同视频弹幕总数对比柱状图 的函数

    params: bvids(list(str)): 所有目标视频的bvid
            partition_method( func-> list(list(str)) ): 一个用来 把所有目标视频的bvid list分割成若干块子bvid list 的函数

    return: generate(func -> None): 用于 生成不同视频弹幕总数对比柱状图 的函数
    '''
    bvid_partitioned = partition_method(bvids)
    count = 0
    
    def generate(title, xlabel, ylabel):
        ''' 用于生存不同视频弹幕总数的对比柱状图，即
            横坐标: 不同视频各自的bvid
            纵坐标: 横坐标bvid 对应视频的弹幕总数
        
        params: title: 柱状图的标题
                xlabel: 柱状图横坐标轴的名称
                ylabel: 柱状图纵坐标轴的名称

        return: None
        '''
        for each_partition in bvid_partitioned:
            danmakus_total = {}
            # 统计当前bvid子集对应视频的弹幕总数
            for bvid in each_partition:
                with open('../danmu/' + bvid + '-danmu.csv', 'r', encoding='utf-8-sig') as f:
                    danmakus_total[bvid] = len(f.readlines())
            # 对当前子集生成柱状图
            nonlocal count
            count += 1
            plt.bar(danmakus_total.keys(), danmakus_total.values())
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.savefig('../img/bar/' + 'Number of Total Danmakus in Different Videos Figure-' + str(count) + '.jpg')
            plt.close()
    
    return generate
            

def my_partition(target_set):
    ''' 朴实无华且枯燥的集合划分函数，如果不满意可以自定义。可以上dp算法，但我太菜还不会
    
    params: target_set(线性表): 需要划分的集合 

    return: partitioned_set:(线性表套线性表): 划分完成的集合
    '''
    n = len(target_set)
    k = 4
    partitioned_set = [[] for i in range(n // 4 + 1)]

    cnt = 0
    for i in range(n):
        partitioned_set[cnt].append(target_set[i])
        if i % 4 == 3:
            cnt += 1
    
    return partitioned_set


if __name__ == "__main__":
    # 读取中文分词表
    with open('../stopwords/ch_stopwords.txt', 'r', encoding='utf-8-sig') as stopwd_file:
        ch_stopwords = [ele.strip('\n') for ele in stopwd_file.readlines()]

    # 读取视频库
    videos = shelve.open('../video object/videos')
    total_dmk_per_bvid = {}

    # 词云图和密度图可视化
    for bvid in videos.keys():
       

        bvid_WordCloud = generateWordCloud(bvid)
        bvid_WordCloud(width=1200, font_path="msyh.ttc", height=800, stopwords=ch_stopwords)

        bvid_density_fig = generateDensityPic(bvid)
        bvid_density_fig('Danmaku Density Figure of ' + bvid, 'timeline of video  unit: second', 'Danmaku in Total')

    # 不同视频弹幕总数对比图可视化
    total_dmk_per_video_fig = generateNumberFig(list(videos.keys()), my_partition)
    total_dmk_per_video_fig('Number of Total Danmus in Different Videos', 'bvid', 'number of danmus')