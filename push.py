import os
import sys
import subprocess
import datetime

def run_command(command):
    """执行命令并返回输出"""
    print(f"执行命令: {command}")
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        print(result.stdout)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
        print(e.stderr)
        return False, e.stderr

def main():
    # 获取提交信息和分支名称
    commit_message = sys.argv[1] if len(sys.argv) > 1 else f"更新于 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    # 获取当前分支名称
    print("获取当前分支...")
    success, branch_output = run_command("git rev-parse --abbrev-ref HEAD")
    if not success:
        print("获取分支名称失败，默认使用master")
        branch_name = "master"
    else:
        branch_name = branch_output.strip()
        print(f"当前分支: {branch_name}")
    
    # 检查git状态
    print("检查git状态...")
    success, output = run_command("git status")
    if not success:
        print("检查git状态失败")
        return
    
    # 检查是否有更改需要提交
    has_changes = "nothing to commit, working tree clean" not in output
    
    if has_changes:
        # 添加所有更改
        print("添加所有更改...")
        success, _ = run_command("git add .")
        if not success:
            print("添加更改失败")
            return
        
        # 提交更改
        print(f"提交更改: {commit_message}")
        success, _ = run_command(f'git commit -m "{commit_message}"')
        if not success:
            print("提交更改失败")
            return
    else:
        print("没有更改需要提交，但将继续执行推送操作")
    
    # 设置远程仓库
  
    github_url = "https://github.com/YYLMZXC/Portal.git"
    
    # 检查并更新远程仓库配置
    print("配置远程仓库...")
    
 
    
    # 如果没有github远程，添加它
    if "github" not in output:
        success, _ = run_command(f"git remote add github {github_url}")
        if not success:
            print("添加github远程失败，但继续尝试")
    else:
        # 更新github远程URL
        success, _ = run_command(f"git remote set-url github {github_url}")
        if not success:
            print("更新github远程URL失败，但继续尝试")
    
  
    
    # 推送到GitHub
    print(f"推送到GitHub的{branch_name}分支...")
    success, _ = run_command(f"git push github {branch_name}")
    if success:
        print("成功推送到GitHub")
    else:
        print("推送到GitHub失败")
    
    print("推送完成！")

if __name__ == "__main__":
    main()