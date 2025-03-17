import os
import sys
import json
from pathlib import Path

def check_conda_env():
    """检查conda环境状态"""
    conda_env = os.environ.get('CONDA_DEFAULT_ENV')
    if not conda_env:
        return False, '未检测到激活的conda环境'
    return True, f'当前conda环境: {conda_env}'

def check_dependencies():
    """检查必要的依赖包"""
    try:
        import dotenv
        return True, '核心依赖包已安装'
    except ImportError:
        return False, '缺少必要的依赖包，请运行: pip install python-dotenv'

def check_api_keys():
    """检查API密钥配置"""
    env_template_path = Path(__file__).parent / 'owl' / '.env_template'
    env_path = Path(__file__).parent / 'owl' / '.env'
    
    if not env_path.exists():
        return False, '未找到.env文件，请从.env_template复制并配置'
    
    from dotenv import load_dotenv
    load_dotenv(env_path)
    
    required_keys = [
        'OPENAI_API_KEY',
        'QWEN_API_KEY',
        'DEEPSEEK_API_KEY',
        'GOOGLE_API_KEY',
        'SEARCH_ENGINE_ID',
        'CHUNKR_API_KEY',
        'FIRECRAWL_API_KEY'
    ]
    
    missing_keys = []
    for key in required_keys:
        if not os.getenv(key) or os.getenv(key) == 'Your_Key':
            missing_keys.append(key)
    
    if missing_keys:
        return False, f'以下API密钥未配置: {", ".join(missing_keys)}'
    return True, 'API密钥配置完成'

def check_project_files():
    """检查项目文件完整性"""
    required_files = [
        'owl/webapp.py',
        'owl/utils/common.py',
        'requirements.txt',
        'README.md'
    ]
    
    missing_files = []
    for file in required_files:
        if not (Path(__file__).parent / file).exists():
            missing_files.append(file)
    
    if missing_files:
        return False, f'缺少以下项目文件: {", ".join(missing_files)}'
    return True, '项目文件完整'

def main():
    print('\n=== Owl项目状态检查 ===\n')
    
    checks = [
        ('Conda环境', check_conda_env()),
        ('依赖包', check_dependencies()),
        ('API配置', check_api_keys()),
        ('项目文件', check_project_files())
    ]
    
    all_passed = True
    for name, (status, message) in checks:
        status_symbol = '✓' if status else '✗'
        print(f'{status_symbol} {name}: {message}')
        if not status:
            all_passed = False
    
    print('\n状态: ' + ('所有检查通过 ✓' if all_passed else '存在配置问题 ✗'))

if __name__ == '__main__':
    main()