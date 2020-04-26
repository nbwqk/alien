class Settings():
    # 存储游戏的所有设置

    def __init__(self):
        # 屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        # 飞船的设置
        self.ship_speed_factor=1.5
        self.ship_limit=3

        # 外星人设置
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction=1

        # 子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=300
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullet_allowed=3

        # 以什么样的速度加快游戏节奏
        self.speedup_scale=1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        # 记分
        self.alien_points=50

        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction=1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
