# Filesystem Hierarchy Standard (FHS)

* [/](#/)

* [/bin](#/bin)

* [/etc](#/etc)

* [/sbin](#/sbin)

* [/usr](#/usr)

* [/var](#/var)



## /

```bash
bin    #Essential command binaries
boot    # Static files of the boot loader
dev    # Device files
etc    # Host-specific system configuration
home    # User home directories
lib    # Essential shared libraries and kernel modules
lib<qual>    # Alternate format essential shared libraries
media    # Mount point for removable media
mnt    # Mount point for mounting a filesystem temporarily
opt    # Add-on application software packages
root    # Home directory for the root user
run    # Data relevant to running processes
sbin    # Essential system binaries
srv    # Data for services provided by this sytem
tmp     # Temporary files
usr    # Secondary hierarchy
var    # Variable data
```

## /bin

```bash
cat    # Concatenate files to standard output
chgrp    # Change file group ownership
chmod    # Change file access permissions
chown    # Change file owner and group
cp        # Copy files and directories
csh    # C shell
date    # Print or set the system date and time
dd        # Convert and copy a file
df        # Report filesystem disk space usage
dmesg    # Print or control the kernel message buffer
echo    # Display a line of text
false     # Do nothing, unsuccessfully
gunzip    # GNU uncompression utility
gzip    # GNU compression utility
hostname     # Show or set the system's host name
kill    # Send signals to processes
ln        # Make links between files
login    # Begin a session on the system
ls        # List directory contents
mkdir    # Make directories
mknod    # Make block or character special files
more    # Page through text
mount    # Mount a filesystem
mv        # Move/rename files
netstat    # Network statistics utility
ping    # ICMP network test utility
ps        # Report process status
pwd        # Print name of current working directory
rm        # Remove empty directories
rmdir    # Remove empty directories
sed        # Stream editor
sh        # POSIX compatible command shell
stty    # Change and print terminal line settings
su        # Change user ID
sync    # Flush filesystem buffers
tar    # Archiving utility
true    # Do nothing, successfully
umount    # Unmount file systems
uname    # Print system information
```

## /etc

```bash
csh.login    # System wide initialization file for C shell logins
exports    # NFS file system access control list
fstab    # Static information about file systems
ftpusers    # FTP daemon user access control list
gateways    # File which lists gateways for routed
gettydefs    # Speed and terminal settings used by getty
group    # User group file
host.conf    # Resolver configuration
hosts    # Static information about host names
hosts.allow    # Host access file for TCP wrappers
hosts.deny    # Host access file for TCP wrappers
hosts.equiv    # List of trusted hosts for rlogin, rsh, rcp
hosts.lpd    # List of trusted hosts for lpd
ineted.conf    # Configuration file for inetd
inittab    # Configuration file for init
issue    # Pre-login message and identification file
ld.so.conf    # List of extra directories to search for shared libraries
motd    # Post-login message of the day file
mtab    # Dynamic information about file systems
mtools.conf    # Configuration file for mtools
networks     # Static information about network names
passwd    # The password file
printcap    # The lpd printer capability database
profile    # System wide initialization file for sh shell logins
protocols    # IP protocol listing
resolve.conf    # Resolver configuration file
rpc    # RPC protocol
securetty    # TTY access control for root login
services     # Port names for network services
shells    # Path names of valid login shells
syslog.conf    # Configuration file for syslogd
```

## /sbin

```bash
fastboot    # Reboot the system withbout checking the disks
fasthalt    # Stop the system without checking the disks
fdisk    # Partition table manipulator
fsck    # File system check and repair utility
fsck.*    # File system check and repair utility for a specific file system
getty    # The getty program
halt    # Command to stop the system
ifconfig    # Configure a network interface
init    # Initial process
mkfs    # Command to build a file system
mkfs.*     # Command to build a specific file system
mkswap    # Command to set up a swap area
reboot    # Command to reboot the system
route    # IP routing table utility
swapon    # Enable paging and swapping
swapoff    # Disable paging and swapping
update    # Daemon to periodically flush file system buffers
```

## /usr

```bash
bin    # Most user commands
include    # Header files included by C programs
lib    # Libraries
libexec    # Binaries run by other programs
local    # Local hierarchy
sbin    # Non-vital system binaries
share    # Architecture-independent data
src    # Source code
```

## /var

```bash
cache    # Application cache data
lib    # Variable state information
local    # Variable data for /usr/local
lock    # Lock files
log    # Log files and directories
opt    # Variable data fro /opt
run    # Data relevant to running processes
spool    # Application spool data
tmp    # Temporary files preserved between system reboots
```
