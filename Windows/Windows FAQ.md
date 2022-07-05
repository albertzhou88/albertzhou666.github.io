# Windows FAQ

### 网络连接不能共享

在regedit中修改一下参数

计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Network Connections

NC_ShowSharedAccessUI 数据值改为 1

### 安装配置Windows的Linux子系统

https://docs.microsoft.com/en-us/windows/wsl/setup/environment

https://docs.microsoft.com/en-us/windows/terminal/install

https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git



### 设置Ubuntu WSL系统启动用户

```shell
 ubuntu.exe config --default-user albert 
```

"albert"是新用户。修改后，系统启动自动进入albert用户。
