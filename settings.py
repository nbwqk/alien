class Settings():
    # 存储游戏的所有设置

    def __init__(self):
        # 屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        # 飞船的设置
        self.ship_speed_factor=1.5