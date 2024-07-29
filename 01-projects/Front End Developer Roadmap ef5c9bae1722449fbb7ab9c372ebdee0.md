# Front End Developer Roadmap

Created: November 13, 2023 12:03 PM
Link: https://roadmap.sh/frontend

### How does the internet work

- A network is a group of computers or other devices which are connected to each other. Networks connected together forms internet
- The internet was developed in the late 1960s by the United States Department of Defense as a means of creating a decentralized communication network that could withstand a nuclear attack.
- At a high level, the internet works by connecting devices and computer systems together using a set of standardized protocols. These protocols define how information is exchanged between devices and ensure that data is transmitted reliably and securely.
- Data is divided in packets, router examines packet and sends to next closest router to its destination, process continues till it reaches destination.
- IP ( Internet Protocol ) is responsible for routing packets to their correct destination
- TCP ( Transmission Control Protocol ) ensures that packets are transmitted reliably and in the correct order.
- SSL/TLS Provides secure connect, these uses certificate. Certificates are signed by trusted third party ( Certificate Authority )
- During the SSL/TLS handshake process, the client and server exchange information to negotiate the encryption algorithm and other parameters for the secure connection.

### What is HTTP ( Hyper Text Transfer  Protocol )

- Used to load webpages using hypertext links
- Protocol for standardizing client server communication.
- Client opens connection request → waiting until receives a response from server
- Stateless protocol. Server does not keep any data between requests
- HTTP Request :
    - Consist of header, body, method ( GET/POST/ etc. )
    - Header, key value information about request
    - Body, Information being sent to server
- HTTP Response :
    - Contains status code, headers, body
    - Status codes, codes to give information about status of request ( success, failure, etc. )
        - 1xx informational
        - 2xx success
        - 3xx redirection
        - 4xx client error
        - 5xx server error
- HTTP uses port 80, HTTPS uses port 443
- HTTP 0.9 [ 1991 ], only `GET` method allowed. only HTML responses
- HTTP 1.0 [ 1996 ], added status code, `POST` method, response support for image, videos, plain text file, support for character set and content encoding.
- HTTP 1.1 [ 1997], added new methods `PUT`, `PATCH`, `OPTIONS`, `DELETE`. Added host-name identification, support for persistent connection, support for pipelining to serve multiple responses in single connection ( `content-length` header is used for it ), Support for Chunked transfer , Added support for better authentication, caching,
- HTTP 2 [ 2015 ], Designed for low latency transport of content. Developed from SPDY . Uses Binary instead of textual, Multiplexing , uses HPACK for header compression,

### Domain Name

- User friendly address for website. Mapped to websites IP address by DNS ( Domain Name System ).
- Different from URL ( Uniform Resource Locator ), as in URL includes site name as well as other information such as protocol, path, etc.
- Divided in 2 parts separated by dot ( . )
    - TLD ( Top Level Domain ) : .com, .net, .org, .uk, .in, .jp
    - 2LD ( 2nd level Domain ) : .co.uk, .co.in ( “co” is 2LD )
    - 3LD ( 3rd level Domain ) : google.co.uk, google.co.in ( “google” is 3LD )

### DNS ( Domain Name System )

- Translates domain names to IP address of website.
- DNS Recoursor : The DNS recursor is a server designed to receive queries from client machines through applications such as web browsers.
- Root Server : details on the DNS servers in charge of top-level domains (TLDs), including .com, .org, and .net
- TLD Server : Keeps track of data on domain names that fall under certain top-level domain, such as .com, .org
- There 13 sets of root servers, strategically placed around world.

![Untitled](Front%20End%20Developer%20Roadmap%20ef5c9bae1722449fbb7ab9c372ebdee0/Untitled.png)

![Untitled](Front%20End%20Developer%20Roadmap%20ef5c9bae1722449fbb7ab9c372ebdee0/Untitled.jpeg)

### Hosting

- Online service that allows to publish website files onto internet.
- Web server serves these published files
- Types of Hosting :
    - Free Hosting : no cost hosting with limitations.
    - Shared / Virtual Hosting : Multiple sites reside on same hardware. Resources are shared might slow down server, its less flexible than dedicated hosting.
    - Dedicated Hosting : Hosted on dedicated server. Best for large sites. Expensive and requires superior skill set.
    - Co-located hosting : Services let you place your own web server on premises of service provider e.g.. AWS. Hardware is managed by third party service providers.

### How Browsers Work

- Main function is to present web resource by requesting it from server and displaying it in browser window.
- Resources can be HTML, PDF, Image, etc.
- Browsers interprets & displays HTML, CSS using specification maintained by W3C ( World Wide Web Consortium ).
- Main Components :
    - UI : Address bar, navigation buttons, etc.
    - Browser Engine : controls actions between the UI and the rendering engine.
    - Render Engine : IE uses Trident, Firefox uses Gecko, Safari uses WebKit. Chrome and Opera (from version 15) use Blink, a fork of WebKit.
    - Networking
    - UI Backend : Used for drawing basic widgets like combo boxes and windows, Uses OS UI methods.
    - JS Interpreter : Used to parse and execute JS code.
    - Data Storage
    
    ![Untitled](Front%20End%20Developer%20Roadmap%20ef5c9bae1722449fbb7ab9c372ebdee0/Untitled%201.png)
    
- **Response** :
    - Response for initial request for webpage contains first byte of data. The first chunk of content is usually 14KB of data.
    - **TTFB** ( Time to First Byte ): Time between users request and receives of first packet of HTML.
    - Linked resources are not requested until browser parses HTML response.
- **Parsing :**
    - Browser turns data into DOM and CSSOM ( CSS Object Model ).
    - DOM is internal representation of markup for the browser.
    - While parsing any non blocking resources ( image, CSS ) will be requested, while it continues to parse HTML
    - Script elements without `async` or `defer` attribute blocks rendering, use preload scanner faster loading these elements.
    - Preload Scanner : while HTML is being parsed, it will parse through content available & request high-priority resources eg CSS, JS, Web Fonts.
    - CSS doesn’t block HTML parsing, it block JS since it is used to query CSS properties.
- Building CSSOM ( CSS Object Model ) :
    - CSS tress similar to DOM tree.
    - Browser goes through each rules in CSS, creates tree with parent, child nodes and sibling relationships.
    - “Recalculate Style” in dev tools shows time taken to parse CSS, optimization.
- **JS Compilation :**
    - While CSS being parsed, JS is parsed, compiled and interpreted. Scripts are parsed into abstract syntax tree.
- **Building Accessibility Tree :**
    - Tree used by assistive devices to parse and interpret content.
    - **AOM** ( Accessibility Object Model ) is similar to semantic version of DOM.
    - Browser update AOM when DOM is updated.
    - Tress is not modifiable by assistive technologies.
    - Until the AOM is built, content is not accessible to screen readers.
- **Render :**
    - Includes styles, Layout, Paint and compositing.
    - Combines CSSOM & DOM tree which is painted on screen.
    - Some cases, content is promoted to its own layer to be painted by GPU
- **Layout :**
    - Process by which dimensions & location of all nodes are determined in render tree.
    - Computes geometry of each node.
    - First time sizing and position of each node is determined is called layout. Subsequent recalculations of are called reflows.
- **Paint :**
    - Paints individual nodes to screen.
    - First occurrence is called **First Meaningful Paint**.
    - For ensuring smooth scrolling and animation, everything on main thread must take less than **16.67 ms**
    - Painting can break elements in layout tree into layers. Promoting content into layers on GPU.  ( eg. different z-index values )
- **Interactivity :**
    - JS is executed after `onload` event is fired.
    - **TTI** ( Time to Interactive ) : Time between first request to when page is interactive.

### HTML ( Hyper Text Markup Language ) :

- Language for describing structure of web documents
-