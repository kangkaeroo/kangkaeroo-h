# 获取目标视频对象，并持久化存储在 "video object" 目录下
import shelve
from bilibili_api import video, sync


def storeVideoObject(bvids):
    ''' 给定bvids，获取对应的视频对象，并存储到shelve中

    params: bvids(list): 一系列目标视频的bv号

    return: 所给bv号对应的视频对象，对象详细属性和方法参考
            -> https://www.moyu.moe/bilibili-api/#/modules/video
    '''
    db = shelve.open('../video object/videos')

    for bvid in bvids:
        if bvid not in db.keys():
            # 不存在相关记录时才加入
            db[bvid] = video.Video(bvid = bvid)

    db.close()


def updateVideo():
    ''' 更新当前数据库内的所有视频
    
    params: None

    return: None
    '''
    db = shelve.open('../video object/videos')
    
    for key in db.keys():
        db[key] = video.Video(bvid = key)

    db.close()


if __name__ == '__main__':
    bvids = ['BV1XE411f7vw', 'BV1hb411K7JN', 'BV1t341127nk', 'BV1ff4y1E7ht', 'BV14o4y1y7MF', 'BV1Wk4y1y7AE', 'BV1H7411j7kp']
    storeVideoObject(bvids)