class Config():
    '''
    This is the setting file. You can change some parameters here.
    '''

    '''
    --------------------
    主机的地址和端口号
    Host and port of your server
    '''
    HOST = '192.168.1.105'
    PORT = '80'
    '''
    --------------------
    '''

    '''
    --------------------
    Web后台管理页面的用户名和密码
    Username and password of web background management page
    '''
    USERNAME = 'admin'
    PASSWORD = 'admin'
    '''
    --------------------
    '''

    '''
    --------------------
    Web后台管理页面的session秘钥，如果不知道是什么，请不要修改
    Session key of web background management page
    If you don't know what it is, please don't modify it.
    '''
    SECRET_KEY = '1145141919810'
    '''
    --------------------
    '''

    '''
    --------------------
    玩家歌曲下载的24小时次数限制，每个文件算一次
    Player's song download limit times in 24 hours, once per file
    '''
    DOWNLOAD_TIMES_LIMIT = 3000
    '''
    歌曲下载链接的有效时长，单位：秒
    Effective duration of song download link, unit: seconds
    '''
    DOWNLOAD_TIME_GAP_LIMIT = 1000
    '''
    --------------------
    '''

    '''
    --------------------
    Arcaea登录的最大允许设备数量，最小值为1
    The maximum number of devices allowed to log in Arcaea, minimum: 1
    '''
    LOGIN_DEVICE_NUMBER_LIMIT = 1
    '''
    是否允许同设备多应用共存登录
    If logging in from multiple applications on the same device is allowed
    '''
    ALLOW_LOGIN_SAME_DEVICE = False
    '''
    --------------------
    '''

    '''
    --------------------
    是否记录详细的服务器日志
    If recording detailed server logs is enabled
    '''
    ALLOW_LOG_INFO = False
    '''
    --------------------
    '''
