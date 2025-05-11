"""
AI Agent 主程序入口
"""
import json
from pathlib import Path
from core.nlp_processor import NLPProcessor
from core.task_executor import TaskExecutor

def load_config():
    """加载配置文件"""
    config_path = Path(__file__).parent / "config"
    settings = json.load(open(config_path / "settings.json"))
    nlp_config = json.load(open(config_path / "nlp_config.json"))
    exec_config = json.load(open(config_path / "execution_config.json"))
    return {
        "settings": settings,
        "nlp": nlp_config,
        "execution": exec_config
    }

def initialize_nlp_processor(config):
    """初始化NLP处理器"""
    return NLPProcessor(config["nlp"])

def initialize_task_executor(config):
    """初始化任务执行引擎"""
    return TaskExecutor(config["execution"])

def run_main_loop(nlp_processor, task_executor):
    """主循环处理用户输入"""
    try:
        while True:
            user_input = input(">> ")
            if user_input.lower() == "exit":
                break
            
            # 处理用户输入
            task = nlp_processor.parse_input(user_input)
            task_executor.execute(task)
    except KeyboardInterrupt:
        print("\n程序已终止")

def main():
    """初始化并启动AI Agent"""
    print("AI Agent 启动中...")
    
    # 加载配置文件
    config = load_config()
    
    # 初始化核心模块
    nlp_processor = initialize_nlp_processor(config)
    task_executor = initialize_task_executor(config)
    
    # 启动主循环
    run_main_loop(nlp_processor, task_executor)

if __name__ == "__main__":
    main()