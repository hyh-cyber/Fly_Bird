Settings.MinSimilarity = 0.7
# 确保游戏窗口是当前活动窗口

# 如果看到了“选择难度”或者菜单界面，按下空格开始
if exists("1767592846347.png"):
   type(Key.SPACE)
   print("游戏已启动")

# --- 第二部分：自动化碰撞测试循环 ---
while True:
    bird = exists("1767592869703.png")
    pipe = exists("1767592884742.png") 
    if bird:
        currY = bird.getY()
        print "当前小鸟Y轴:", currY
    if currY > 300:
            keyDown(Key.SPACE)
            wait(0.01)
            keyUp(Key.SPACE)
    if bird and pipe:
        # 计算距离和临界点
        distX = pipe.getX() - bird.getX()
        # 引导小鸟接近管道临界点进行碰撞测试
        if 0 < distX < 120:
            # 故意保持在与管道边缘极近的高度
            if bird.getY() > (pipe.getY() - 5): 
                keyDown(Key.SPACE)
                wait(0.05)
                keyUp(Key.SPACE)

    # 验证判定触发：如果检测到GameOver，说明碰撞逻辑执行成功
    if exists("1767592901926.png"):
        print("判定成功：视觉接触与代码逻辑同步触发。")
    
    wait(0.01)