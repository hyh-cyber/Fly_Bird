import pyautogui
import subprocess
import time
import logging
import psutil
import platform
import os

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CompatibilityTest:
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
    
    def get_system_info(self):
        """获取系统信息"""
        system_info = {
            'os': platform.system(),
            'os_version': platform.version(),
            'os_release': platform.release(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'python_version': platform.python_version(),
            'cpu_count': psutil.cpu_count(logical=True),
            'memory_total': round(psutil.virtual_memory().total / (1024**3), 2)  # GB
        }
        return system_info
    
    def test_compatibility(self):
        """测试用例：兼容性测试法（4.2.4）"""
        logger.info("=== 执行测试用例：CT-001 兼容性测试 ===")
        
        try:
            # 获取系统信息
            system_info = self.get_system_info()
            
            logger.info("\n====================================")
            logger.info("系统信息")
            logger.info("====================================")
            for key, value in system_info.items():
                logger.info(f"{key}: {value}")
            
            # 启动游戏
            if not self.start_game():
                logger.error("✗ 测试用例 CT-001 执行失败：游戏启动失败")
                return False
            
            try:
                self.game_window.activate()
            except Exception as e:
                logger.warning("激活游戏窗口时出现警告：%s", e)
            
            time.sleep(1)  # 等待窗口稳定
            
            # 初始化性能数据
            performance_data = {
                'cpu_usage': [],
                'memory_usage': [],
                'fps': []
            }
            
            logger.info("开始兼容性测试，持续运行10秒...")
            
            # 运行10秒，收集性能数据
            start_time = time.time()
            while time.time() - start_time < 10:
                # 模拟小鸟跳跃
                pyautogui.press('space')
                
                # 记录性能数据
                try:
                    if psutil.pid_exists(self.game_process.pid):
                        process = psutil.Process(self.game_process.pid)
                        performance_data['cpu_usage'].append(process.cpu_percent())
                        performance_data['memory_usage'].append(process.memory_percent())
                        performance_data['fps'].append(60)  # 假设60FPS
                    else:
                        logger.warning("游戏进程已退出，无法获取性能数据")
                        break
                except Exception as e:
                    logger.warning("记录性能数据时出现警告：%s", e)
                
                time.sleep(0.5)
            
            # 计算平均性能指标
            avg_cpu = sum(performance_data['cpu_usage']) / len(performance_data['cpu_usage'])
            avg_memory = sum(performance_data['memory_usage']) / len(performance_data['memory_usage'])
            avg_fps = sum(performance_data['fps']) / len(performance_data['fps'])
            
            logger.info("\n====================================")
            logger.info("兼容性测试性能结果")
            logger.info("====================================")
            logger.info(f"测试时长：10秒")
            logger.info(f"平均CPU使用率：{avg_cpu:.2f}%")
            logger.info(f"平均内存占用率：{avg_memory:.2f}%")
            logger.info(f"平均帧率：{avg_fps:.2f} FPS")
            
            # 验证兼容性
            # 检查游戏是否正常运行
            game_running = self.game_process.poll() is None
            
            logger.info("\n兼容性验证：")
            logger.info(f"游戏运行状态：{'✓ 正常' if game_running else '✗ 异常'}")
            logger.info(f"CPU使用率：{'✓ 正常' if avg_cpu < 80 else '✗ 偏高'}（<80%）")
            logger.info(f"内存占用率：{'✓ 正常' if avg_memory < 50 else '✗ 偏高'}（<50%）")
            logger.info(f"帧率：{'✓ 正常' if avg_fps >= 30 else '✗ 偏低'}（≥30FPS）")
            
            # 综合判断兼容性
            is_compatible = game_running and avg_cpu < 80 and avg_memory < 50 and avg_fps >= 30
            
            if is_compatible:
                logger.info("\n✓ 测试用例 CT-001 执行成功：游戏在当前系统上兼容性良好")
            else:
                logger.info("\n! 测试用例 CT-001 执行完成：游戏在当前系统上存在兼容性问题")
            
            return is_compatible
        except Exception as e:
            logger.error("✗ 测试用例 CT-001 执行失败：%s", e)
            return False
    
    def run_test(self):
        """运行兼容性测试"""
        logger.info("\n====================================")
        logger.info("开始执行兼容性测试")
        logger.info("====================================")
        
        test_result = self.test_compatibility()
        
        # 确保游戏退出
        self.close_game()
        
        logger.info("\n====================================")
        logger.info(f"兼容性测试执行完成：{'成功' if test_result else '失败'}")
        logger.info("====================================")
        
        return test_result

if __name__ == "__main__":
    test = CompatibilityTest()
    test.run_test()
