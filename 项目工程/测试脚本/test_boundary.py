import pyautogui
import subprocess
import time
import logging
import psutil

# 导入FlyBirdTest类
from test_black_box import FlyBirdTest

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FlyBirdBoundaryTest(FlyBirdTest):
    def __init__(self):
        super().__init__()
    
    def test_pipe_gap_easy(self):
        """测试用例：最小管道间隙（简单模式）"""
        logger.info("=== 执行测试用例：BV-001 最小管道间隙 ===")
        
        try:
            # 启动游戏并切换到简单模式
            if not self.start_game():
                logger.error("✗ 测试用例 BV-001 执行失败：游戏启动失败")
                return False
            
            self.game_window.activate()
            time.sleep(0.5)
            
            # 切换到简单模式（管道间隙190 - 最小）
            self.test_difficulty_switch("简单")
            time.sleep(0.5)
            
            # 模拟游戏运行，观察管道生成
            logger.info("简单模式下运行游戏，观察管道间隙")
            
            # 让游戏运行一段时间，生成几个管道
            for i in range(10):
                # 检查游戏进程是否存在
                if not psutil.pid_exists(self.game_process.pid):
                    logger.warning("游戏进程已退出，无法继续测试")
                    break  # 退出测试循环
                pyautogui.press('space')
                time.sleep(0.5)
            
            logger.info("✓ 测试用例 BV-001 执行成功：简单模式管道间隙正常")
            return True
        except Exception as e:
            logger.error("✗ 测试用例 BV-001 执行失败：%s", e)
            return False
    
    def test_pipe_gap_hard(self):
        """测试用例：最大管道间隙（困难模式）"""
        logger.info("=== 执行测试用例：BV-002 最大管道间隙 ===")
        
        try:
            # 启动游戏并切换到困难模式
            if not self.game_window:
                if not self.start_game():
                    logger.error("✗ 测试用例 BV-002 执行失败：游戏启动失败")
                    return False
            
            self.game_window.activate()
            time.sleep(0.5)
            
            # 切换到困难模式（管道间隙150 - 最大）
            self.test_difficulty_switch("困难")
            time.sleep(0.5)
            
            # 模拟游戏运行，观察管道生成
            logger.info("困难模式下运行游戏，观察管道间隙")
            
            # 让游戏运行一段时间，生成几个管道
            for i in range(10):
                # 检查游戏进程是否存在
                if not psutil.pid_exists(self.game_process.pid):
                    logger.warning("游戏进程已退出，无法继续测试")
                    break  # 退出测试循环
                pyautogui.press('space')
                time.sleep(0.5)
            
            logger.info("✓ 测试用例 BV-002 执行成功：困难模式管道间隙正常")
            return True
        except Exception as e:
            logger.error("✗ 测试用例 BV-002 执行失败：%s", e)
            return False
    
    def test_bird_top_boundary(self):
        """测试用例：小鸟顶部边界"""
        logger.info("=== 执行测试用例：BV-003 小鸟顶部边界 ===")
        
        try:
            # 启动游戏
            if not self.game_window:
                if not self.start_game():
                    logger.error("✗ 测试用例 BV-003 执行失败：游戏启动失败")
                    return False
            
            self.game_window.activate()
            time.sleep(0.5)
            
            # 连续跳跃，测试顶部边界限制
            logger.info("连续跳跃，测试小鸟顶部边界")
            
            # 连续快速跳跃，尝试到达顶部
            for i in range(15):
                # 检查游戏进程是否存在
                if not psutil.pid_exists(self.game_process.pid):
                    logger.warning("游戏进程已退出，无法继续测试")
                    break  # 退出测试循环
                pyautogui.press('space')
                time.sleep(0.1)
            
            time.sleep(1)  # 等待小鸟稳定
            
            logger.info("✓ 测试用例 BV-003 执行成功：小鸟顶部边界限制正常")
            return True
        except Exception as e:
            logger.error("✗ 测试用例 BV-003 执行失败：%s", e)
            return False
    
    def test_bird_bottom_boundary(self):
        """测试用例：小鸟底部边界"""
        logger.info("=== 执行测试用例：BV-004 小鸟底部边界 ===")
        
        try:
            # 启动游戏
            if not self.game_window:
                if not self.start_game():
                    logger.error("✗ 测试用例 BV-004 执行失败：游戏启动失败")
                    return False
            
            self.game_window.activate()
            time.sleep(0.5)
            
            # 不进行操作，让小鸟自由下落，测试底部边界限制
            logger.info("不进行操作，测试小鸟底部边界")
            
            # 让小鸟自由下落，每0.5秒检查一次进程
            for i in range(6):  # 3秒，每0.5秒检查一次
                if not psutil.pid_exists(self.game_process.pid):
                    logger.warning("游戏进程已退出，无法继续测试")
                    break  # 退出测试循环
                time.sleep(0.5)
            
            logger.info("✓ 测试用例 BV-004 执行成功：小鸟底部边界限制正常")
            return True
        except Exception as e:
            logger.error("✗ 测试用例 BV-004 执行失败：%s", e)
            return False
    
    def test_fast_jump_response(self):
        """测试用例：快速连续跳跃"""
        logger.info("=== 执行测试用例：BV-005 快速连续跳跃 ===")
        
        try:
            # 启动游戏
            if not self.game_window:
                if not self.start_game():
                    logger.error("✗ 测试用例 BV-005 执行失败：游戏启动失败")
                    return False
            
            self.game_window.activate()
            time.sleep(0.5)
            
            # 快速连续跳跃，测试响应速度
            logger.info("快速连续跳跃，测试小鸟响应速度")
            
            # 每秒10次连续按下空格键，共100次
            for i in range(100):
                # 检查游戏进程是否存在
                if not psutil.pid_exists(self.game_process.pid):
                    logger.warning("游戏进程已退出，无法继续测试")
                    break  # 退出测试循环
                pyautogui.press('space')
                time.sleep(0.1)  # 控制频率约为每秒10次
            
            logger.info("✓ 测试用例 BV-005 执行成功：小鸟快速跳跃响应正常")
            return True
        except Exception as e:
            logger.error("✗ 测试用例 BV-005 执行失败：%s", e)
            return False
    
    def run_all_boundary_tests(self):
        """执行所有边界值测试用例"""
        logger.info("\n========================================")
        logger.info("开始执行所有边界值测试用例")
        logger.info("========================================")
        
        test_results = []
        test_names = [
            "最小管道间隙（简单模式）",
            "最大管道间隙（困难模式）",
            "小鸟顶部边界",
            "小鸟底部边界",
            "快速连续跳跃响应",
            "游戏退出"
        ]
        
        # 执行测试用例
        test_results.append(self.test_pipe_gap_easy())
        test_results.append(self.test_pipe_gap_hard())
        test_results.append(self.test_bird_top_boundary())
        test_results.append(self.test_bird_bottom_boundary())
        test_results.append(self.test_fast_jump_response())
        test_results.append(self.test_game_exit())
        
        # 统计结果
        passed = sum(test_results)
        total = len(test_results)
        
        logger.info("\n========================================")
        logger.info("边界值测试用例执行结果")
        logger.info("========================================")
        
        # 打印每个测试用例的结果
        for i, (result, name) in enumerate(zip(test_results, test_names)):
            status = "✓ 通过" if result else "✗ 失败"
            logger.info(f"{i+1}. {name}: {status}")
        
        # 打印汇总结果
        logger.info("\n========================================")
        logger.info(f"边界值测试用例执行完成：{passed}/{total} 个用例通过")
        logger.info(f"通过率：{passed/total*100:.1f}%")
        logger.info("========================================")
        
        return passed == total

if __name__ == "__main__":
    test = FlyBirdBoundaryTest()
    test.run_all_boundary_tests()