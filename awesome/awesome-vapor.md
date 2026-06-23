# Vapor

[![GitHub stars](https://img.shields.io/github/stars/vapor-community/awesome-vapor?style=flat)](https://github.com/vapor-community/awesome-vapor/stargazers)

# Awesome Vapor [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="img/vapor-logo.png" align="right" width="150">](https://vapor.codes)

[Vapor](https://vapor.codes) is currently one of the most popular server-side Swift frameworks. It allows you to take the language you already know if you ever developed an iOS application and use it in a whole new way, to develop fast, scalable and reliable back-end systems that integrate easily with a wide range of third party services. This is a curated list of:

- modern libraries that easily integrate with Vapor and follow Vapor’s philosophy of providing simple, clean yet powerful APIs;
- well-written tutorials, books, videos and education materials;
- tools to make your development process simpler and more enjoyable;
- and more!

## Contents

- [How to use](#how-to-use)
- [Libraries](#libraries)
- [Tools](#tools)
- [Services](#services)
- [Education](#education)
  - [Articles](#articles)
  - [Books](#books)
  - [Newsletters](#newsletters)
  - [Videos](#videos)
- [Open-source Projects](#open-source-projects)
- [License](#license)

## How to use

Simply press <kbd>Command</kbd> + <kbd>F</kbd> to search for a keyword. If you’re only interested in entries related to [Vapor 3](https://github.com/Cellane/awesome-vapor/blob/filtered/vapor-3.md) [![GitHub stars](https://img.shields.io/github/stars/Cellane/awesome-vapor/blob/filtered/vapor-3.md?style=flat)](https://github.com/Cellane/awesome-vapor/blob/filtered/vapor-3.md/stargazers) or only to [Vapor 4](https://github.com/Cellane/awesome-vapor/blob/filtered/vapor-4.md) [![GitHub stars](https://img.shields.io/github/stars/Cellane/awesome-vapor/blob/filtered/vapor-4.md?style=flat)](https://github.com/Cellane/awesome-vapor/blob/filtered/vapor-4.md/stargazers), you may use the automatically generated filtered lists available on the `filtered` branch by visiting the links in this sentence. You may also find the legacy archived content in the `legacy` folder.

## Libraries

- ![v3](img/vapor-3.png) [API Error Middleware](https://github.com/skelpo/APIErrorMiddleware) [![GitHub stars](https://img.shields.io/github/stars/skelpo/APIErrorMiddleware?style=flat)](https://github.com/skelpo/APIErrorMiddleware/stargazers) – Vapor middleware for converting thrown errors to JSON responses.
- ![v3](img/vapor-3.png) [APNS](https://github.com/vapor-community/apns) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/apns?style=flat)](https://github.com/vapor-community/apns/stargazers) – Vapor APNS for iOS.
- ![v3](img/vapor-3.png) [Bugsnag](https://github.com/nodes-vapor/bugsnag) [![GitHub stars](https://img.shields.io/github/stars/nodes-vapor/bugsnag?style=flat)](https://github.com/nodes-vapor/bugsnag/stargazers) – Report errors with Bugsnag.
- ![v3](img/vapor-3.png) [CouchDB Client](https://github.com/makoni/couchdb-vapor) [![GitHub stars](https://img.shields.io/github/stars/makoni/couchdb-vapor?style=flat)](https://github.com/makoni/couchdb-vapor/stargazers) – Simple CouchDB client for Vapor.
- ![v3](img/vapor-3.png) [CrudRouter](https://github.com/twof/VaporCRUDRouter) [![GitHub stars](https://img.shields.io/github/stars/twof/VaporCRUDRouter?style=flat)](https://github.com/twof/VaporCRUDRouter/stargazers) – Automatic RESTful CRUD router generation for any Fluent Model.
- ![v3](img/vapor-3.png) [CSRF](https://github.com/vapor-community/CSRF) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/CSRF?style=flat)](https://github.com/vapor-community/CSRF/stargazers) – A package to add protection to Vapor against CSRF attacks.
- ![v3](img/vapor-3.png) [CSV Framework](https://github.com/skelpo/CSV) [![GitHub stars](https://img.shields.io/github/stars/skelpo/CSV?style=flat)](https://github.com/skelpo/CSV/stargazers) – A simple framework to read and write CSV files.
- ![v3](img/vapor-3.png) [Ferno](https://github.com/vapor-community/ferno) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/ferno?style=flat)](https://github.com/vapor-community/ferno/stargazers) – Vapor Firebase Realtime database provider.
- ![v3](img/vapor-3.png) [Flash](https://github.com/nodes-vapor/flash) [![GitHub stars](https://img.shields.io/github/stars/nodes-vapor/flash?style=flat)](https://github.com/nodes-vapor/flash/stargazers) – Flash messages between views.
- ![v3](img/vapor-3.png) [FluentQuery](https://github.com/MihaelIsaev/FluentQuery) [![GitHub stars](https://img.shields.io/github/stars/MihaelIsaev/FluentQuery?style=flat)](https://github.com/MihaelIsaev/FluentQuery/stargazers) – Build complex raw SQL queries while still using Swift keypaths.
- ![v3](img/vapor-3.png) [Gatekeeper](https://github.com/nodes-vapor/gatekeeper) [![GitHub stars](https://img.shields.io/github/stars/nodes-vapor/gatekeeper?style=flat)](https://github.com/nodes-vapor/gatekeeper/stargazers) – Rate limiting middleware for Vapor.
- ![v3](img/vapor-3.png) [Google Cloud Provider](https://github.com/vapor-community/google-cloud-provider) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/google-cloud-provider?style=flat)](https://github.com/vapor-community/google-cloud-provider/stargazers) – Interact with Google Cloud Platform APIs from your Vapor project.
- ![v3](img/vapor-3.png) [Guardian](https://github.com/Jinxiansen/Guardian) [![GitHub stars](https://img.shields.io/github/stars/Jinxiansen/Guardian?style=flat)](https://github.com/Jinxiansen/Guardian/stargazers) – Modern rate-limiting middleware.
- ![v3](img/vapor-3.png) [Imperial](https://github.com/vapor-community/Imperial) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/Imperial?style=flat)](https://github.com/vapor-community/Imperial/stargazers) – Federated Authentication with OAuth providers.
- ![v3](img/vapor-3.png) [JWT Keychain](https://github.com/nodes-vapor/jwt-keychain) [![GitHub stars](https://img.shields.io/github/stars/nodes-vapor/jwt-keychain?style=flat)](https://github.com/nodes-vapor/jwt-keychain/stargazers) – Easily scaffold a keychain using JWT for Vapor.
- ![v3](img/vapor-3.png) [JWT Middleware](https://github.com/skelpo/JWTMiddleware) [![GitHub stars](https://img.shields.io/github/stars/skelpo/JWTMiddleware?style=flat)](https://github.com/skelpo/JWTMiddleware/stargazers) – Middleware to Authenticate and Authorize Requests in Vapor.
- ![v3](img/vapor-3.png) [Leaf Error Middleware](https://github.com/brokenhandsio/leaf-error-middleware) [![GitHub stars](https://img.shields.io/github/stars/brokenhandsio/leaf-error-middleware?style=flat)](https://github.com/brokenhandsio/leaf-error-middleware/stargazers) – Serve up custom 404 and server error pages for your Vapor App.
- ![v3](img/vapor-3.png) [Leaf Markdown](https://github.com/vapor-community/leaf-markdown) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/leaf-markdown?style=flat)](https://github.com/vapor-community/leaf-markdown/stargazers) – Markdown renderer for Vapor.
- ![v3](img/vapor-3.png) [Lingo Vapor](https://github.com/vapor-community/Lingo-Vapor) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/Lingo-Vapor?style=flat)](https://github.com/vapor-community/Lingo-Vapor/stargazers) – Vapor provider for Lingo – the Swift localization library.
- ![v3](img/vapor-3.png) [Local Storage](https://github.com/gperdomor/local-storage) [![GitHub stars](https://img.shields.io/github/stars/gperdomor/local-storage?style=flat)](https://github.com/gperdomor/local-storage/stargazers) – Storage driver using local filesystem.
- ![v3](img/vapor-3.png) [MailCore](https://github.com/LiveUI/MailCore) [![GitHub stars](https://img.shields.io/github/stars/LiveUI/MailCore?style=flat)](https://github.com/LiveUI/MailCore/stargazers) – Sending e-mails via SMTP, MailGun and SendGrid.
- ![v3](img/vapor-3.png) [Meow](https://github.com/OpenKitten/Meow) [![GitHub stars](https://img.shields.io/github/stars/OpenKitten/Meow?style=flat)](https://github.com/OpenKitten/Meow/stargazers) – An alternative codable ORM for MongoDB.
- ![v3](img/vapor-3.png) [MongoKitten](https://github.com/OpenKitten/MongoKitten) [![GitHub stars](https://img.shields.io/github/stars/OpenKitten/MongoKitten?style=flat)](https://github.com/OpenKitten/MongoKitten/stargazers) – MongoDB driver in Swift.
- ![v3](img/vapor-3.png) [Pagination](https://github.com/vapor-community/pagination) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/pagination?style=flat)](https://github.com/vapor-community/pagination/stargazers) – Simple Vapor 3 Pagination.
- ![v3](img/vapor-3.png) [Paginator](https://github.com/nodes-vapor/paginator) [![GitHub stars](https://img.shields.io/github/stars/nodes-vapor/paginator?style=flat)](https://github.com/nodes-vapor/paginator/stargazers) – Query pagination for Vapor and Fluent.
- ![v3](img/vapor-3.png) [S3](https://github.com/LiveUI/S3) [![GitHub stars](https://img.shields.io/github/stars/LiveUI/S3?style=flat)](https://github.com/LiveUI/S3/stargazers) – Library for accessing the Amazon S3 service (and compatible) with support for most commonly used operations.
- ![v3](img/vapor-3.png) [S3 Storage](https://github.com/anthonycastelli/s3-storage) [![GitHub stars](https://img.shields.io/github/stars/anthonycastelli/s3-storage?style=flat)](https://github.com/anthonycastelli/s3-storage/stargazers) – Library for simple access to the Amazon S3 service.
- ![v3](img/vapor-3.png) [Sanitize](https://github.com/gperdomor/sanitize) [![GitHub stars](https://img.shields.io/github/stars/gperdomor/sanitize?style=flat)](https://github.com/gperdomor/sanitize/stargazers) – Powerful model extraction from Vapor JSON requests.
- ![v3](img/vapor-3.png) [SendGrid Provider](https://github.com/vapor-community/sendgrid-provider) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/sendgrid-provider?style=flat)](https://github.com/vapor-community/sendgrid-provider/stargazers) – SendGrid-powered mail backend for Vapor.
- ![v3](img/vapor-3.png) [SimpleFileLogger](https://github.com/hallee/vapor-simple-file-logger) [![GitHub stars](https://img.shields.io/github/stars/hallee/vapor-simple-file-logger?style=flat)](https://github.com/hallee/vapor-simple-file-logger/stargazers) – A simple file logging provider for Vapor.
- ![v3](img/vapor-3.png) [Slugify](https://github.com/nodes-vapor/slugify) [![GitHub stars](https://img.shields.io/github/stars/nodes-vapor/slugify?style=flat)](https://github.com/nodes-vapor/slugify/stargazers) – Convenience for sluggifying your strings.
- ![v3](img/vapor-3.png) [Storage](https://github.com/nodes-vapor/storage) [![GitHub stars](https://img.shields.io/github/stars/nodes-vapor/storage?style=flat)](https://github.com/nodes-vapor/storage/stargazers) – Eases the use of multiple storage and CDN services.
- ![v3](img/vapor-3.png) [Stripe Provider](https://github.com/vapor-community/stripe-provider) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/stripe-provider?style=flat)](https://github.com/vapor-community/stripe-provider/stargazers) – Stripe Provider for Vapor.
- ![v3](img/vapor-3.png) [Submissions](https://github.com/nodes-vapor/submissions) [![GitHub stars](https://img.shields.io/github/stars/nodes-vapor/submissions?style=flat)](https://github.com/nodes-vapor/submissions/stargazers) – Conveniences for creating forms and validating (form) submissions.
- ![v3](img/vapor-3.png) [Sugar](https://github.com/nodes-vapor/sugar) [![GitHub stars](https://img.shields.io/github/stars/nodes-vapor/sugar?style=flat)](https://github.com/nodes-vapor/sugar/stargazers) – A package of sugar for Vapor.
- ![v3](img/vapor-3.png) [SwifQL](https://github.com/MihaelIsaev/SwifQL) [![GitHub stars](https://img.shields.io/github/stars/MihaelIsaev/SwifQL?style=flat)](https://github.com/MihaelIsaev/SwifQL/stargazers) – Easily build flexible and type-safe SQL with pure Swift.
- ![v3](img/vapor-3.png) [SwiftyBeaver Provider](https://github.com/vapor-community/swiftybeaver-provider) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/swiftybeaver-provider?style=flat)](https://github.com/vapor-community/swiftybeaver-provider/stargazers) – SwiftyBeaver Logging Provider for Vapor, the server-side Swift web framework.
- ![v3](img/vapor-3.png) [Telesign Provider](https://github.com/vapor-community/telesign-provider) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/telesign-provider?style=flat)](https://github.com/vapor-community/telesign-provider/stargazers) – A Telesign provider for Vapor.
- ![v3](img/vapor-3.png) [Vapor Mailgun Service](https://github.com/vapor-community/VaporMailgunService) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/VaporMailgunService?style=flat)](https://github.com/vapor-community/VaporMailgunService/stargazers) – A service to be used with Vapor to send emails.
- ![v3](img/vapor-3.png) [Vapor reCAPTCHA](https://github.com/gotranseo/vapor-recaptcha) [![GitHub stars](https://img.shields.io/github/stars/gotranseo/vapor-recaptcha?style=flat)](https://github.com/gotranseo/vapor-recaptcha/stargazers) – Validate Google reCAPTCHAs using Vapor.
- ![v3](img/vapor-3.png) [Vapor Request Storage](https://github.com/skelpo/vapor-request-storage) [![GitHub stars](https://img.shields.io/github/stars/skelpo/vapor-request-storage?style=flat)](https://github.com/skelpo/vapor-request-storage/stargazers) – A replacement for `request.storage` which was available in Vapor 1 & 2.
- ![v3](img/vapor-3.png) [Vapor Security Headers](https://github.com/brokenhandsio/VaporSecurityHeaders) [![GitHub stars](https://img.shields.io/github/stars/brokenhandsio/VaporSecurityHeaders?style=flat)](https://github.com/brokenhandsio/VaporSecurityHeaders/stargazers) – Harden Your Security Headers For Vapor.
- ![v3](img/vapor-3.png) [Vapor Test Tools](https://github.com/LiveUI/VaporTestTools) [![GitHub stars](https://img.shields.io/github/stars/LiveUI/VaporTestTools?style=flat)](https://github.com/LiveUI/VaporTestTools/stargazers) – Helper designed to make testing your endpoints in Vapor 3 pain-free.
- ![v3](img/vapor-3.png) [VaporExt](https://github.com/vapor-community/vapor-ext) [![GitHub stars](https://img.shields.io/github/stars/vapor-community/vapor-ext?style=flat)](https://github.com/vapor-community/vapor-ext/stargazers) – A collection of Swift extensions for wide range of Vapor data types and classes.
- ![v3](img/vapor-3.png) [WKHTMLTOPDF](https://github.com/MihaelIsaev/wkhtmltopdf) [![GitHub stars](https://img.shields.io/github/stars/MihaelIsaev/wkhtmltopdf?style=flat)](https://github.com/MihaelIsaev/wkhtmltopdf/stargazers) – Build PDF files from Leaf templates or web pages through the `wkhtmltopdf` CLI tool.
- ![v3](img/vapor-3.png) [XMLCoding](https://github.com/LiveUI/XMLCoding) [![GitHub stars](https://img.shields.io/github/stars/LiveUI/XMLCoding?style=flat)](https://github.com/LiveUI/XMLCoding/stargazers) – XML encoder and decoder.

## Tools

- [Ether](https://github.com/Ether-CLI/Ether) [![GitHub stars](https://img.shields.io/github/stars/Ether-CLI/Ether?style=flat)](https://github.com/Ether-CLI/Ether/stargazers) – A Command-Line Interface for the Swift Package Manager.
- [Heroku buildpack: curl with HTTP/2 support](https://github.com/vzsg/heroku-buildpack-curl-http2) [![GitHub stars](https://img.shields.io/github/stars/vzsg/heroku-buildpack-curl-http2?style=flat)](https://github.com/vzsg/heroku-buildpack-curl-http2/stargazers)
- [Ice](https://github.com/jakeheis/Ice) [![GitHub stars](https://img.shields.io/github/stars/jakeheis/Ice?style=flat)](https://github.com/jakeheis/Ice/stargazers) – A developer friendly package manager for Swift; 100% compatible with Swift Package Manager.
- [Sourcery](https://github.com/krzysztofzablocki/Sourcery) [![GitHub stars](https://img.shields.io/github/stars/krzysztofzablocki/Sourcery?style=flat)](https://github.com/krzysztofzablocki/Sourcery/stargazers) – Meta-programming for Swift, stop writing boilerplate code.
- ![v3](img/vapor-3.png) [Sublimate](https://github.com/gabrielepalma/sublimate) [![GitHub stars](https://img.shields.io/github/stars/gabrielepalma/sublimate?style=flat)](https://github.com/gabrielepalma/sublimate/stargazers) – Fast prototyping with synchronization and authentication based on Sourcery.
- [Swifter](https://github.com/LiveUI/Swifter) [![GitHub stars](https://img.shields.io/github/stars/LiveUI/Swifter?style=flat)](https://github.com/LiveUI/Swifter/stargazers) – A macOS tool to help you manage your Xcode projects and give you a quick access to DerivedData folder cleaning and management.

## Services

- [Vapor Cloud](https://vapor.cloud)
- [Vapor Red](https://vapor.red)

## Education

### Articles

- ![v3](img/vapor-3.png) [Deep Dive into Setup and Deployment for Heroku and Ubuntu](https://learningswift.brightdigit.com/vapor-heroku-ubuntu-setup-deploy/)
- ![v3](img/vapor-3.png) [How to test controllers by mocking dependencies in Vapor 3 and Swift](https://mikemikina.com/blog/how-to-test-controllers-by-mocking-dependencies-in-vapor-3-and-swift/)
- ![v3](img/vapor-3.png) [Vapor 3 Tutorials](https://mihaelamj.github.io/Vapor%20%203%20Tutorial/) – Big collection of small tutorials.
- ![v3](img/vapor-3.png) [Transforming from Vapor 2 to Vapor 3](https://www.skelpo.com/blog/vapor2-to-vapor3/) – Transitioning from Vapor 2 to Vapor 3 with a real world project.
- ![v3](img/vapor-3.png) [Tutorials for Beginner to Advanced](https://medium.com/@martinlasek) – Written tutorials for Beginner to Advanced.
- ![v3](img/vapor-3.png) [Using the dependency injection framework for testing in Vapor 3 and Swift](https://mikemikina.com/blog/using-the-dependency-injection-framework-for-testing-in-vapor-3-and-swift/) – How to use dependency injection framework which will help you manage dependencies and mock them inside your tests.
- ![v3](img/vapor-3.png) [Watermarking photos with ImageMagick, Vapor 3 and Swift on macOS and Linux](https://mikemikina.com/blog/watermarking-photos-with-imagemagick-vapor-3-and-swift-on-macos-and-linux/) – Tutorial on how to use the ImageMagick library in Swift.
- ![v4](img/vapor-4.png) [What’s new in Vapor 4?](https://theswiftdev.com/2019/08/26/whats-new-in-vapor-4/)

### Books

- ![v3](img/vapor-3.png) [Server Side Swift with Vapor](https://store.raywenderlich.com/products/server-side-swift-with-vapor)
- ![v3](img/vapor-3.png) [Server-Side Swift (Vapor Edition)](https://www.hackingwithswift.com/store/server-side-swift)

### Newsletters

- [VaporNation](http://vapornation.news) – Weekly Vapor newsletter with all things Vapor.

### Videos

- ![v3](img/vapor-3.png) [Server Side Swift with Vapor](https://www.raywenderlich.com/4493-server-side-swift-with-vapor/lessons/1)
- ![v3](img/vapor-3.png) [Vapor - Beginner to Advanced](https://www.youtube.com/channel/UCoLEXFUHIKXunm9QJjsAftw/videos)

## Open-source Projects

- ![v3](img/vapor-3.png) [SteamPress](https://github.com/brokenhandsio/SteamPress) [![GitHub stars](https://img.shields.io/github/stars/brokenhandsio/SteamPress?style=flat)](https://github.com/brokenhandsio/SteamPress/stargazers) – A Blogging Engine and Platform written in Swift for use with the Vapor Framework.
- ![v3](img/vapor-3.png) [User Manager Service](https://github.com/skelpo/UserManager) [![GitHub stars](https://img.shields.io/github/stars/skelpo/UserManager?style=flat)](https://github.com/skelpo/UserManager/stargazers) – A small, useful user manager made for production application setups.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, _Milan Vit_ has waived all copyright and related or neighbouring rights to this work.
