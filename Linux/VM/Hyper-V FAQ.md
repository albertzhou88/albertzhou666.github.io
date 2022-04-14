# Hyper-V FAQ

[TOC]

### Hyper-V虚拟机Ubuntu不能全屏

解决方案

在Hyper-V虚拟机Ubuntu中打开终端输入

```shell
cd /etc/default
sudo gedit grub
```

修改

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

为

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash video=hyperv_fb:1920x1080"
```

刷新

```
sudo update-grub
```

重启

```
sudo reboot
```

