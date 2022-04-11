# Install Ubuntu in Windows 10

Follow up [Install Ubuntu on WSL](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview) to install Ubuntu in Windows 10.

The installation will note you to reboot Windows.

You may get following error after reboot when try to launch Ubuntu app in Windows.

```
WslRegisterDistribution failed with error: 0x80370102 
```

The problem may caused by WLS2. Please run command as below to use WLS1.

```
wsl --set-default-version 1
```

