from xmlrpc.client import ServerProxy

supervisor_url="http://admin:admin@8.134.127.43:8001/RPC2"

def get_supervisor_client():
    try:
        server=ServerProxy(supervisor_url)
        return server
    except Exception as e:
        raise ConnectionError(f"无法连接到supervisor,错误{e}")

def get_processes():
    """获取supervisor的全部进程状态"""
    try:
        client=get_supervisor_client()
        process=client.supervisor.getAllProcessInfo()
        return process
    except Exception as e:
        raise ConnectionError(f"获取进程列表失败：{str(e)}")
# print(get_processes())

def get_process_name(name:str):
    """获取指定进程的状态"""
    try:
        client=get_supervisor_client()
        info=client.supervisor.getProcessInfo(name)
        return info
    except Exception as e:
        raise ConnectionError(f"进程：{name}获取失败，{str(e)}")
# print(get_process_name('hello_supervisor'))

def get_process_log(name:str,offset=int(0),length=int(10000)):
    """获取指定进程的日志"""
    try:
        client=get_supervisor_client()
        logs,offset,length=client.supervisor.tailProcessStdoutLog(name,offset,length)
        format_logs=logs.replace('\\n','\n')
        log_lines = [line.strip() for line in format_logs.split('\n') if line.strip()]
        return log_lines
    except Exception as e:
        raise ConnectionError(f"获取{name}进程日志失败：{str(e)}")
# print(get_process_log("hello_supervisor"))
