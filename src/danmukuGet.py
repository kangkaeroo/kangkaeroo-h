import pandas as pd
import time
import shelve
from bilibili_api import video, sync, exceptions


def getDanmaku(video):
    ''' 给定video对象，获取该视频对应的所有弹幕

    params: video(bilibili_api.video): 目标视频的对象，需要手动指定

    return: danmakus(dict): 包含目标视频所有弹幕信息的字典
    '''
    # TODO 考虑一个视频bv号对应多个分p的情况，是不是要把所有的弹幕都爬下来？ 用DFS吧
    
    # video_time 存放弹幕在视频中出现的时间位置
    # send_time 存放弹幕发送时对应的现实时间
    # content 存放弹幕的内容
    danmakus = {'video_time': [], 'send_time': [], 'content': []}
    
    # 试探-回溯
    cnt = 0

    while(True):
        try:
            for dm in sync(video.get_danmakus(page_index = cnt)):
                danmakus['video_time'].append(dm.dm_time)
                danmakus['send_time'].append(time.strftime('%Y-%m-%d %H:%M', time.gmtime(dm.send_time)))
                danmakus['content'].append(dm.text)
        except exceptions.ArgsException:
            break
        cnt += 1
    
    return danmakus


if __name__ == '__main__':
    videos = shelve.open('../video object/videos')

    for bvid in videos.keys():
        dm = pd.DataFrame(getDanmaku(videos[bvid]))
        dm.to_csv('../danmu/' + bvid + '-danmu.csv', encoding='utf-8-sig', index = False)

    videos.close()