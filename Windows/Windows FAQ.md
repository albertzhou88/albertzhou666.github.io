# Windows FAQ

### 网络连接不能共享

在regedit中修改一下参数

计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Network Connections

NC_ShowSharedAccessUI 数据值改为 1

