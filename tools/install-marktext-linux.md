# Install MarkText in Linux

[GitHub - marktext/marktext: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.](https://github.com/marktext/marktext)



1. Download [MarkText Linux package](https://github.com/marktext/marktext/releases/latest)

2. Make it executable
   
   ```shell
   chmod +x marktext-x86_64.AppImage
   ```

3. Create desktop application
   
   Download [desktop file](https://raw.githubusercontent.com/marktext/marktext/develop/resources/linux/marktext.desktop)
   
   Copy it to application folder.
   
   ```shell
   cp $HOME/Downloads/marktext.desktop $HOME/.local/share/applications/
   ```
   
   Edit it if necessary.
   
   Update desktop database.
   
   ```shell
   update-desktop-database $HOME/.local/share/applications/
   ```
   
   


