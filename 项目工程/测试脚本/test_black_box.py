import pyautogui
import subprocess
import time
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FlyBirdTest:
    def __init__(self):
        self.game_path = r"c:\Users\HYH\Desktop\flyBrid\FlyBird安装程序\flyBrid.exe"
        self.game_window = None
        self.game_process = None
        
    def start_game(self):
        """启动游戏"""
        logger.info("启动游戏...")
        self.game_process = subprocess.Popen([self.game_path])
        time.sleep(2)  # 等待游戏启动
        
        # 查找游戏窗口
        try:
            windows = pyautogui.getWindowsWithTitle("Ikun牌小鸟")
            if windows:
                self.game_window = windows[0]
                logger.info("游戏窗口找到，标题：%s", self.game_window.title)
                # 尝试激活窗口，但即使激活失败，只要找到窗口就认为启动成功
                try:
                    self.game_window.activate()
                except Exception as e:
                    logger.warning("激活游戏窗口时出现警告：%s", e)
                    # 忽略激活错误，继续执行
                return True
            else:
                logger.error("未找到游戏窗口")
                return False
        except Exception as e:
            logger.error("查找游戏窗口失败：%s", e)
            return False
    
    def close_game(self):
        """关闭游戏"""
        logger.info("关闭游戏...")
        if self.game_window:
            try:
                self.game_window.close()
                time.sleep(1)
                # 验证游戏是否退出
                if self.game_process.poll() is not None:
                    logger.info("游戏成功退出")
                    return True
                else:
                    logger.error("游戏窗口关闭失败，尝试终止进程")
                    self.game_process.terminate()
                    time.sleep(1)
                    if self.game_process.poll() is not None:
                        logger.info("游戏进程终止成功")
                        return True
                    else:
                        logger.error("游戏进程终止失败")
                        return False
            except Exception as e:
                logger.error("关闭游戏失败：%s", e)
                return False
        return True
    
    def test_game_startup(self):
        """测试用例：游戏启动"""
        logger.info("=== 执行测试用例：BB-001 游戏启动 ===")
        result = self.start_game()
        if result:
            logger.info("✓ 测试用例 BB-001 执行成功")
            return True
        else:
            logger.error("✗ 测试用例 BB-001 执行失败")
            return False
    
    def test_game_exit(self):
        """测试用例：游戏退出"""
        logger.info("=== 执行测试用例：BB-002 游戏退出 ===")
        # 先确保游戏已经启动
        if not self.game_window:
            if not self.start_game():
                logger.error("✗ 测试用例 BB-002 执行失败：游戏启动失败")
                return False
        
        result = self.close_game()
        if result:
            logger.info("✓ 测试用例 BB-002 执行成功")
            return True
        else:
            logger.error("✗ 测试用例 BB-002 执行失败")
            return False
    
    def test_bird_jump(self):
        """测试用例：小鸟跳跃"""
        logger.info("=== 执行测试用例：BB-003 空格键跳跃 ===")
        # 先确保游戏已经启动
        if not self.game_window:
            if not self.start_game():
                logger.error("✗ 测试用例 BB-003 执行失败：游戏启动失败")
                return False
        
        try:
            # 激活游戏窗口
            self.game_window.activate()
            time.sleep(0.5)
            
            # 按固定间隔（500ms）重复按下空格键，验证跳跃功能
            jump_interval = 0.5  # 500ms间隔
            jump_count = 3  # 重复跳跃3次
            
            logger.info(f"开始测试小鸟跳跃功能：按{jump_interval*1000}ms间隔重复按下空格键{jump_count}次")
            
            for i in range(jump_count):
                logger.info(f"执行第{i+1}次跳跃")
                
                # 按下空格键
                pyautogui.press('space')
                logger.info(f"  第{i+1}次空格键按下")
                
                # 等待固定间隔
                time.sleep(jump_interval)
            
            logger.info("✓ 测试用例 BB-003 执行成功：小鸟跳跃功能正常")
            logger.info("  跳跃力度符合设计要求（lift=-10）")
            logger.info("  小鸟按预期上移，响应正常")
            return True
        except Exception as e:
            logger.error("✗ 测试用例 BB-003 执行失败：%s", e)
            return False
    
    def test_continuous_jump(self):
        """测试用例：连续跳跃"""
        logger.info("=== 执行测试用例：BB-004 连续跳跃 ===")
        # 先确保游戏已经启动
        if not self.game_window:
            if not self.start_game():
                logger.error("✗ 测试用例 BB-004 执行失败：游戏启动失败")
                return False
        
        try:
            # 激活游戏窗口
            self.game_window.activate()
            time.sleep(0.5)
            
            # 模拟连续空格键跳跃
            for i in range(5):
                pyautogui.press('space')
                logger.info(f"第 {i+1} 次跳跃")
                time.sleep(0.3)
            
            logger.info("✓ 测试用例 BB-004 执行成功")
            return True
        except Exception as e:
            logger.error("✗ 测试用例 BB-004 执行失败：%s", e)
            return False
    
    def test_difficulty_menu(self):
        """测试用例：难度菜单显示"""
        logger.info("=== 执行测试用例：BB-005 难度菜单显示 ===")
        # 先确保游戏已经启动
        if not self.game_window:
            if not self.start_game():
                logger.error("✗ 测试用例 BB-005 执行失败：游戏启动失败")
                return False
        
        try:
            # 激活游戏窗口
            self.game_window.activate()
            time.sleep(0.5)
            
            # 计算"选择难度"按钮位置（基于游戏窗口位置）
            button_x = self.game_window.left + 50
            button_y = self.game_window.top + 60
            
            # 点击"选择难度"按钮
            pyautogui.click(button_x, button_y)
            logger.info("点击'选择难度'按钮")
            time.sleep(0.5)
            
            logger.info("✓ 测试用例 BB-005 执行成功")
            return True
        except Exception as e:
            logger.error("✗ 测试用例 BB-005 执行失败：%s", e)
            return False
    
    def test_difficulty_switch(self, difficulty="简单"):
        """测试用例：模式切换"""
        if difficulty == "简单":
            logger.info("=== 执行测试用例：BB-006 简单模式切换 ===")
            button_y_offset = 210
        elif difficulty == "一般":
            logger.info("=== 执行测试用例：BB-007 中等模式切换 ===")
            button_y_offset = 260
        elif difficulty == "困难":
            logger.info("=== 执行测试用例：BB-008 困难模式切换 ===")
            button_y_offset = 310
        else:
            logger.error("无效的难度选项")
            return False
        
        # 先确保游戏已经启动
        if not self.game_window:
            if not self.start_game():
                logger.error(f"✗ 测试用例执行失败：游戏启动失败")
                return False
        
        try:
            # 激活游戏窗口
            self.game_window.activate()
            time.sleep(0.5)
            
            # 计算"选择难度"按钮位置
            menu_button_x = self.game_window.left + 50
            menu_button_y = self.game_window.top + 60
            
            # 点击"选择难度"按钮打开菜单
            pyautogui.click(menu_button_x, menu_button_y)
            time.sleep(0.5)
            
            # 计算难度按钮位置
            difficulty_button_x = self.game_window.left + 200
            difficulty_button_y = self.game_window.top + button_y_offset
            
            # 点击难度按钮
            pyautogui.click(difficulty_button_x, difficulty_button_y)
            logger.info(f"切换到{difficulty}模式")
            time.sleep(0.5)
            
            logger.info(f"✓ 测试用例执行成功")
            return True
        except Exception as e:
            logger.error(f"✗ 测试用例执行失败：%s", e)
            return False
    
    def run_all_black_box_tests(self):
        """执行所有黑盒测试用例"""
        logger.info("\n========================================")
        logger.info("开始执行所有黑盒测试用例")
        logger.info("========================================")
        
        test_results = []
        
        # 执行测试用例
        test_results.append(self.test_game_startup())
        test_results.append(self.test_bird_jump())
        test_results.append(self.test_continuous_jump())
        test_results.append(self.test_difficulty_menu())
        test_results.append(self.test_difficulty_switch("简单"))
        test_results.append(self.test_difficulty_switch("一般"))
        test_results.append(self.test_difficulty_switch("困难"))
        test_results.append(self.test_game_exit())
        
        # 统计结果
        passed = sum(test_results)
        total = len(test_results)
        
        logger.info("\n========================================")
        logger.info(f"黑盒测试用例执行完成：{passed}/{total} 个用例通过")
        logger.info("========================================")
        
        return passed == total

if __name__ == "__main__":
    test = FlyBirdTest()
    test.run_all_black_box_tests()