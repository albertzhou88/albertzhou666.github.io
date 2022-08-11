[TOC]

# HTTP

## HTTP/HTTPS简介

HTTP协议指HyperText Transfer Protocal (超文本传输协议)。是一种用于分布式、协作式和超媒体信息系统的应用层协议。是互联网上应用最广泛的一种网络传输协议。

HTTPS协议是HyperText Transfer Protocal Secure (超文本传输安全协议)。HTTPS由HTTP进行通信，但利用SSL/TLS来加密数据包。HTTPS开发的主要目的，是提供对网站服务器的身份认证，保护交换资料的隐私与完整性。

HTTP默认端口80，HTTPS默认端口443。

```
HTTP + SSL = HTTPS
```



## HTTP工作原理

* HTTP是无连接的：无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并受到客户的应答后，即断开连接。采用这种方式可以节省传输时间。
* HTTP是媒体独立的：只要客户端和服务器知道如何处理数据内容，任何类型的数据都可以通过HTTP发送。客户端和服务器指定使用合适的MIME-type内容类型。
* HTTP是无状态：HTTP协议是无状态协议。无状态是指协议对于事物处理没有记忆能力，缺少状态意味着如果后续处理需要前的信息，则它必须重传，这样可能导致每次连接传送的数据量增大。另一方面，在服务器不需要先前信息时，它的应答就比较快。

```

+-------------+   HTTP protocol  +-------------+
| Web browser | <--------------->| HTTP server |
+-------------+                  +-------------+
                                        |
                                        |
                                 +-------------+
                                 | CGI program | (Common Gateway Interface)
                                 +-------------+
                                        |
                                        |
                                 +-------------+
                                 |   Database  |
                                 +-------------+
```



## HTTP与HTTPS的区别

* HTTP明文传输，数据都是未加密的，安全性较差。HTTPS数据传输过程时加密的，安全性较好。
* 使用HTTPS协议需要到CA (Certificate Authority)申请证书。
* HTTP页面响应速度比HTTPS快。HTTP使用TCP三次握手建立连接，客户端和服务器需要交换3个包。HTTPS除了TCP的三个包，还要加上SSL握手需要的9个包，一共12个包。
* HTTP和HTTPS的端口不一样。前者是80，后者是443。
* HTTPS是建立在SSL/TLS的HTTP协议。所以要比HTTP更耗费服务器资源。



## HTTPS的工作原理

![HTTPS的工作原理](HTTPS的工作原理\HTTPS的工作原理.png)

1. **客户端发起 HTTPS 请求: **用户在浏览器里输入一个 https 网址，然后连接到 server 的 443 端口。
2. **服务端的配置: **采用 HTTPS 协议的服务器必须要有一套数字证书，可以自己制作，也可以向组织申请。区别就是自己颁发的证书需要客户端验证通过，才可以继续访问。而使用受信任的公司申请的证书则不会弹出提示页面。这套证书其实就是一对公钥和私钥。如果对公钥和私钥不太理解，可以想象成一把钥匙和一个锁头。只是全世界只有你一个人有这把钥匙，你可以把锁头给别人。别人可以用这个锁把重要的东西锁起来，然后发给你。因为只有你一个人有这把钥匙，所以只有你才能看到被这把锁锁起来的东西。
3. **传送证书: **这个证书其实就是公钥，只是包含了很多信息，如证书的颁发机构，过期时间等等。
4. **客户端解析证书: **这部分工作是有客户端的TLS来完成的。首先会验证公钥是否有效，比如颁发机构，过期时间等等。如果发现异常，则会弹出一个警告框，提示证书存在问题。如果证书没有问题，那么就生成一个随机值，然后用证书对该随机值进行加密，就好像上面说的，把随机值用锁头锁起来，这样除非有钥匙，不然看不到被锁住的内容。
5. **传送加密信息: **这部分传送的是用证书加密后的随机值，目的就是让服务端得到这个随机值，以后客户端和服务端的通信就可以通过这个随机值来进行加密解密了。
6. **服务端解密信息: **服务端用私钥解密后，得到了客户端传过来的随机值(私钥)，然后把内容通过该值进行对称加密，所谓对称加密就是，将信息和私钥通过某种算法混合在一起，这样除非知道私钥，不然无法获取内容，而正好客户端和服务端都知道这个私钥，所以只要加密算法够彪悍，私钥够复杂，数据就够安全。
7. **传输加密后的信息: **这部分信息是服务段用私钥加密后的信息，可以在客户端被还原。
8. **客户端解密信息: **客户端用之前生成的私钥解密服务段传过来的信息，于是获取了解密后的内容，整个过程第三方即使监听到了数据，也束手无策。

## HTTP消息结构

一个HTTP"客户端"是一个应用程序（Web浏览器或其他任何客户端），通过连接到服务器达到向服务器发送一个或多个HTTP的请求的目的。

一个HTTP"服务器"同样也是一个应用程序（通常是一个Web服务，如Apache Web服务器或IIS服务器等），通过接收客户端的请求并向客户端发送HTTP响应数据。

HTTP使用统一资源标识符（Uniform Resource Identifiers, URI）来传输数据和建立连接。

一旦建立连接后，数据消息就通过类似Internet邮件所使用的格式[RFC5322](https://www.rfc-editor.org/rfc/rfc5322.html)和多用途Internet邮件扩展（MIME）[RFC2045](https://www.rfc-editor.org/rfc/rfc2045.html)来传送。



客户端请求

```http
GET /hello.txt HTTP/1.1		#请求行
User-Agent: curl/7.64.1 	#请求头部
Host: www.example.com 		#请求头部
Accept-Language: en, mi		#请求头部
```

服务的响应

```http
HTTP/1.1 200 OK									#状态行
Date: Mon, 27 Jul 2009 12:28:53 GMT				#消息报头
Server: Apache									#消息报头
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT	#消息报头
ETag: "34aa387-d-1568eb00"						#消息报头
Accept-Ranges: bytes							#消息报头
Content-Length: 51								#消息报头
Vary: Accept-Encoding							#消息报头
Content-Type: text/plain						#消息报头
												#空行
Hello World! My content includes a trailing CRLF.	#正文
```

## HTTP 请求方法

根据 HTTP 标准，HTTP 请求可以使用多种请求方法。

HTTP1.0 定义了三种请求方法： GET, POST 和 HEAD 方法。

HTTP1.1 新增了六种请求方法：OPTIONS、PUT、PATCH、DELETE、TRACE 和 CONNECT 方法。

|      | Method                                                       | Description                                                  |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [GET](https://www.rfc-editor.org/rfc/rfc9110.html#GET)       | 请求指定的页面信息，并返回实体主体。Transfer a current representation of the target resource. |
| 2    | [HEAD](https://www.rfc-editor.org/rfc/rfc9110.html#HEAD)     | 类似于 GET 请求，只不过返回的响应中没有具体的内容，用于获取报头。Same as GET, but do not transfer the response content. |
| 3    | [POST](https://www.rfc-editor.org/rfc/rfc9110.html#POST)     | 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST 请求可能会导致新的资源的建立和/或已有资源的修改。Perform resource-specific processing on the request content. |
| 4    | [PUT](https://www.rfc-editor.org/rfc/rfc9110.html#PUT)       | 从客户端向服务器传送的数据取代指定的文档的内容。Replace all current representations of the target resource with the request content. |
| 5    | [DELETE](https://www.rfc-editor.org/rfc/rfc9110.html#DELETE) | 请求服务器删除指定的页面。Remove all current representations of the target resource. |
| 6    | [CONNECT](https://www.rfc-editor.org/rfc/rfc9110.html#CONNECT) | HTTP/1.1 协议中预留给能够将连接改为管道方式的代理服务器。Establish a tunnel to the server identified by the target resource. |
| 7    | [OPTIONS](https://www.rfc-editor.org/rfc/rfc9110.html#OPTIONS) | 允许客户端查看服务器的性能。Describe the communication options for the target resource. |
| 8    | [TRACE](https://www.rfc-editor.org/rfc/rfc9110.html#TRACE)   | 回显服务器收到的请求，主要用于测试或诊断。Perform a message loop-back test along the path to the target resource. |

## HTTP 状态码

当浏览者访问一个网页时，浏览者的浏览器会向网页所在服务器发出请求。当浏览器接收并显示网页前，此网页所在的服务器会返回一个包含 HTTP 状态码的信息头（server header）用以响应浏览器的请求。

HTTP 状态码的英文为 **HTTP Status Code**。。

## HTTP 状态码分类

HTTP 状态码由三个十进制数字组成，第一个十进制数字定义了状态码的类型。响应分为五类。官方定义 [RFC9110-18.3-Status Code Registration](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-code-registration)

| 分类 | 分类描述                                         |
| ---- | ------------------------------------------------ |
| 1**  | 信息响应：服务器收到请求，需要请求者继续执行操作 |
| 2**  | 成功响应：操作被成功接收并处理                   |
| 3**  | 重定向：需要进一步的操作以完成请求               |
| 4**  | 客户端错误：请求包含语法错误或无法完成请求       |
| 5**  | 服务器错误：服务器在处理请求的过程中发生了错误   |

HTTP状态码列表:

| 状态码 | 状态码英文名称                                               | 中文描述                                                     |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 100    | Continue                                                     | 继续。客户端应继续其请求                                     |
| 101    | Switching Protocols                                          | 切换协议。服务器根据客户端的请求切换协议。只能切换到更高级的协议，例如，切换到HTTP的新版本协议 |
|        |                                                              |                                                              |
| 200    | OK                                                           | 请求成功。一般用于GET与POST请求                              |
| 201    | Created                                                      | 已创建。成功请求并创建了新的资源                             |
| 202    | Accepted                                                     | 已接受。已经接受请求，但未处理完成                           |
| 203    | Non-Authoritative Information                                | 非授权信息。请求成功。但返回的meta信息不在原始的服务器，而是一个副本 |
| 204    | No Content                                                   | 无内容。服务器成功处理，但未返回内容。在未更新网页的情况下，可确保浏览器继续显示当前文档 |
| 205    | Reset Content                                                | 重置内容。服务器处理成功，用户终端（例如：浏览器）应重置文档视图。可通过此返回码清除浏览器的表单域 |
| 206    | Partial Content                                              | 部分内容。服务器成功处理了部分GET请求                        |
|        |                                                              |                                                              |
| 300    | Multiple Choices                                             | 多种选择。请求的资源可包括多个位置，相应可返回一个资源特征与地址的列表用于用户终端（例如：浏览器）选择 |
| 301    | Moved Permanently                                            | 永久移动。请求的资源已被永久的移动到新URI，返回信息会包括新的URI，浏览器会自动定向到新URI。今后任何新的请求都应使用新的URI代替 |
| 302    | Found                                                        | 临时移动。与301类似。但资源只是临时被移动。客户端应继续使用原有URI |
| 303    | See Other                                                    | 查看其它地址。与301类似。使用GET和POST请求查看               |
| 304    | Not Modified                                                 | 未修改。所请求的资源未修改，服务器返回此状态码时，不会返回任何资源。客户端通常会缓存访问过的资源，通过提供一个头信息指出客户端希望只返回在指定日期之后修改的资源 |
| 305    | Use Proxy                                                    | 使用代理。所请求的资源必须通过代理访问                       |
| 306    | Unused                                                       | 已经被废弃的HTTP状态码                                       |
| 307    | Temporary Redirect                                           | 临时重定向。与302类似。使用GET请求重定向                     |
| 308    | [Permanent Redirect](https://www.rfc-editor.org/rfc/rfc9110.html#name-308-permanent-redirect) | The 308 (Permanent Redirect) status code indicates that the [target resource](https://www.rfc-editor.org/rfc/rfc9110.html#target.resource) has been assigned a new permanent URI and any future references to this resource ought to use one of the enclosed URIs. |
|        |                                                              |                                                              |
| 400    | Bad Request                                                  | 客户端请求的语法错误，服务器无法理解                         |
| 401    | Unauthorized                                                 | 请求要求用户的身份认证                                       |
| 402    | Payment Required                                             | 保留，将来使用                                               |
| 403    | Forbidden                                                    | 服务器理解请求客户端的请求，但是拒绝执行此请求               |
| 404    | Not Found                                                    | 服务器无法根据客户端的请求找到资源（网页）。通过此代码，网站设计人员可设置"您所请求的资源无法找到"的个性页面 |
| 405    | Method Not Allowed                                           | 客户端请求中的方法被禁止                                     |
| 406    | Not Acceptable                                               | 服务器无法根据客户端请求的内容特性完成请求                   |
| 407    | Proxy Authentication Required                                | 请求要求代理的身份认证，与401类似，但请求者应当使用代理进行授权 |
| 408    | Request Timeout                                              | 服务器等待客户端发送的请求时间过长，超时                     |
| 409    | Conflict                                                     | 服务器完成客户端的 PUT 请求时可能返回此代码，服务器处理请求时发生了冲突 |
| 410    | Gone                                                         | 客户端请求的资源已经不存在。410不同于404，如果资源以前有现在被永久删除了可使用410代码，网站设计人员可通过301代码指定资源的新位置 |
| 411    | Length Required                                              | 服务器无法处理客户端发送的不带Content-Length的请求信息       |
| 412    | Precondition Failed                                          | 客户端请求信息的先决条件错误                                 |
| 413    | Request Entity Too Large                                     | 由于请求的实体过大，服务器无法处理，因此拒绝请求。为防止客户端的连续请求，服务器可能会关闭连接。如果只是服务器暂时无法处理，则会包含一个Retry-After的响应信息 |
| 414    | Request-URI Too Large                                        | 请求的URI过长（URI通常为网址），服务器无法处理               |
| 415    | Unsupported Media Type                                       | 服务器无法处理请求附带的媒体格式                             |
| 416    | Requested range not satisfiable                              | 客户端请求的范围无效                                         |
| 417    | Expectation Failed                                           | 服务器无法满足Expect的请求头信息                             |
| 418    | (unused)                                                     |                                                              |
| 421    | [Misdirected Request](https://www.rfc-editor.org/rfc/rfc9110.html#status.421) | The 421 (Misdirected Request) status code indicates that the request was directed at a server that is unable or unwilling to produce an authoritative response for the target URI. |
| 422    | [Unprocessable Content](https://www.rfc-editor.org/rfc/rfc9110.html#status.422) | The 422 (Unprocessable Content) status code indicates that the server understands the content type of the request content (hence a [415 (Unsupported Media Type)](https://www.rfc-editor.org/rfc/rfc9110.html#status.415) status code is inappropriate), and the syntax of the request content is correct, but it was unable to process the contained instructions. |
| 426    | [Upgrade Required](https://www.rfc-editor.org/rfc/rfc9110.html#status.426) | The 426 (Upgrade Required) status code indicates that the server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. |
|        |                                                              |                                                              |
| 500    | Internal Server Error                                        | 服务器内部错误，无法完成请求                                 |
| 501    | Not Implemented                                              | 服务器不支持请求的功能，无法完成请求                         |
| 502    | Bad Gateway                                                  | 作为网关或者代理工作的服务器尝试执行请求时，从远程服务器接收到了一个无效的响应 |
| 503    | Service Unavailable                                          | 由于超载或系统维护，服务器暂时的无法处理客户端的请求。延时的长度可包含在服务器的Retry-After头信息中 |
| 504    | Gateway Timeout                                              | 充当网关或代理的服务器，未及时从远端服务器获取请求           |
| 505    | HTTP Version not supported                                   | 服务器不支持请求的HTTP协议的版本，无法完成处理               |

