import time

# 初始化统计变量
death_count = 0
start_time = time.time()

print("--- 开始 0.5 小时长时稳定性测试 ---")

while (time.time() - start_time) < 1800: # 运行 1800 秒 (0.5 小时)
    bird = exists("1767600599923.png")
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
    # 存活维持逻辑
    if bird:
        currY = bird.getY()
        # 修正你的 300 阈值为日志显示的 710+，防止卡死
        if currY<720:
            click(bird) 
            # 发送简单的空格指令
            keyDown(Key.SPACE)
            wait(0.02)  # 将按下时间延长至 0.02 秒，这会让物理引擎感知到更持久的向上力
            keyUp(Key.SPACE)
            wait(0.04)  # 关键：跳完之后强制等待 0.04 秒，让小鸟有视觉上的上升过程
            print("白盒监控：小鸟在 Y=%d 执行跳跃" % currY)
            wait(0.02) # 强制等待，防止发包过快导致游戏卡死
    # 自动重启逻辑：这是长时测试的关键
    if exists("1767600628908.png"): # GameOver 图片
        death_count += 1
        print("[%s] 检测到死亡，当前累计重启次数: %d" % (time.ctime(), death_count))
        wait(1)
        type(Key.SPACE) # 重启游戏
        wait(1)
        
    wait(0.01)

print("测试完成。总运行时间: 0.5小时，总死亡次数: %d" % death_count)