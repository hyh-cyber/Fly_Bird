# [步骤1] 环境初始化与游戏启动
Settings.MinSimilarity = 0.7
# 通过命令行或App类确保窗口置顶

# [步骤2] 场景衔接：模拟用户进入游戏
if exists("1767597772752.png"):
    type(Key.ENTER) # 或空格，触发游戏开始逻辑
    print("场景步进：游戏已由菜单进入运行态")

# [步骤3] 业务流程核心：自动控制与状态循环
while True:
    bird = exists("1767597811182.png")
    pipe = exists("1767597822163.png")
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
    # 模拟实际飞行操作
    if bird:
        currY = bird.getY()
        # 逻辑验证：根据日志731坐标触发跳跃，验证Bird类位移响应
        if currY > 300: 
            keyDown(Key.SPACE); wait(0.2); keyUp(Key.SPACE)
            print("业务监控：执行飞行维持操作")

    # 模拟临界点挑战（场景法中的关键业务点）
    if bird and pipe:
        distX = pipe.getX() - bird.getX()
        if 0 < distX < 100:
            print("业务监控：进入管道通过期")

    # [步骤4] 场景终结与自动复活
    if exists("1767597853226.png"):
        print("场景步进：检测到碰撞，业务流转至结算界面")
        wait(1)
        type(Key.SPACE) # 触发 Game::restartGame() 重新开始场景
        print("场景复位：已自动点击重新开始")
        wait(1)
        continue # 重新进入全流程循环