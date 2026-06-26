# Fiber

[![GitHub stars](https://img.shields.io/github/stars/gofiber/awesome-fiber?style=flat)](https://github.com/gofiber/awesome-fiber/stargazers)

# Awesome Fiber [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<a href="https://gofiber.io">
  <picture alt="Fiber Logo" align="right" style="margin-right: 25px">
    <source height="75" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/gofiber/docs/master/static/img/logo-dark.svg">
    <img height="75" alt="Fiber Logo" align="right" style="margin-right: 25px" src="https://raw.githubusercontent.com/gofiber/docs/master/static/img/logo.svg">
  </picture>
</a>

> **Fiber** is an [Express](https://github.com/expressjs/express) [![GitHub stars](https://img.shields.io/github/stars/expressjs/express?style=flat)](https://github.com/expressjs/express/stargazers) inspired **web framework** built on top of [Fasthttp](https://github.com/valyala/fasthttp) [![GitHub stars](https://img.shields.io/github/stars/valyala/fasthttp?style=flat)](https://github.com/valyala/fasthttp/stargazers), the **fastest** HTTP engine for [Go](https://golang.org/doc/). Designed to **ease** things up for **fast** development with **zero memory allocation** and **performance** in mind.

A curated list of awesome Fiber middlewares, boilerplates, recipes, articles and tools.
<br>

## Contents

<!--lint disable awesome-toc-->
<!--lint disable awesome-git-repo-age-->

- [⚙️ Middlewares](#%EF%B8%8F-middlewares)
  - [🧬 Core](#-core)
  - [🔗 External](#-external)
  - [💻 Contrib](#-contrib)
  - [🌱 Third Party](#-third-party)
- [🚧 Boilerplates](#-boilerplates)
- [📁 Recipes](#-recipes)
- [🛠️ Tools](#%EF%B8%8F-tools)
- [📖 Articles](#-articles)
- [📺 Videos](#-videos)
- [🤖 Benchmarks](#-benchmarks)

## ⚙️ Middlewares

Where to discover Fiber middlewares.

### 🧬 Core

List of middlewares that are included within the Fiber framework.

- [Adaptor](https://github.com/gofiber/fiber/tree/main/middleware/adaptor) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/adaptor?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/adaptor/stargazers) - Converter for net/http handlers to/from Fiber request handlers.
- [BasicAuth](https://github.com/gofiber/fiber/tree/main/middleware/basicauth) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/basicauth?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/basicauth/stargazers) - Basic auth middleware provides an HTTP basic authentication. It calls the next handler for valid credentials and 401 Unauthorized for missing or invalid credentials.
- [Cache](https://github.com/gofiber/fiber/tree/main/middleware/cache) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/cache?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/cache/stargazers) - Intercept and cache responses.
- [Compress](https://github.com/gofiber/fiber/tree/main/middleware/compress) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/compress?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/compress/stargazers) - Compression middleware for Fiber, it supports `deflate`, `gzip` and `brotli` by default.
- [CORS](https://github.com/gofiber/fiber/tree/main/middleware/cors) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/cors?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/cors/stargazers) - Enable cross-origin resource sharing (CORS) with various options.
- [CSRF](https://github.com/gofiber/fiber/tree/main/middleware/csrf) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/csrf?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/csrf/stargazers) - Protect from CSRF exploits.
- [Earlydata](https://github.com/gofiber/fiber/tree/main/middleware/earlydata) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/earlydata?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/earlydata/stargazers) - Early data support for Fiber.
- [Encrypt Cookie](https://github.com/gofiber/fiber/tree/main/middleware/encryptcookie) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/encryptcookie?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/encryptcookie/stargazers) - Encrypt middleware which encrypts cookie values.
- [EnvVar](https://github.com/gofiber/fiber/tree/main/middleware/envvar) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/envvar?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/envvar/stargazers) - Expose environment variables with providing an optional config.
- [ETag](https://github.com/gofiber/fiber/tree/main/middleware/etag) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/etag?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/etag/stargazers) - Lets caches be more efficient and save bandwidth, as a web server does not need to resend a full response if the content has not changed.
- [Expvar](https://github.com/gofiber/fiber/tree/main/middleware/expvar) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/expvar?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/expvar/stargazers) - Serves runtime exposed variants in JSON format via its HTTP server.
- [Favicon](https://github.com/gofiber/fiber/tree/main/middleware/favicon) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/favicon?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/favicon/stargazers) - Ignore favicon from logs or serve from memory if a file path is provided.
- [Healthcheck](https://github.com/gofiber/fiber/tree/main/middleware/healthcheck) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/healthcheck?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/healthcheck/stargazers) - Adds health-check endpoints for readiness and liveness probes.
- [Helmet](https://github.com/gofiber/fiber/tree/main/middleware/helmet) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/helmet?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/helmet/stargazers) - Helps secure your apps by setting various HTTP headers.
- [Idempotency](https://github.com/gofiber/fiber/tree/main/middleware/idempotency) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/idempotency?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/idempotency/stargazers) - Enables fault-tolerant APIs when duplicate requests occur.
- [Keyauth](https://github.com/gofiber/fiber/tree/main/middleware/keyauth) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/keyauth?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/keyauth/stargazers) - Key auth middleware provides a key based authentication.
- [Limiter](https://github.com/gofiber/fiber/tree/main/middleware/limiter) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/limiter?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/limiter/stargazers) - Rate-limiting middleware. Use to limit repeated requests to public APIs and/or endpoints such as password reset.
- [Logger](https://github.com/gofiber/fiber/tree/main/middleware/logger) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/logger?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/logger/stargazers) - HTTP request/response logger.
- [Pprof](https://github.com/gofiber/fiber/tree/main/middleware/pprof) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/pprof?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/pprof/stargazers) - Serves runtime profiling data in the format expected by the pprof visualization tool.
- [Proxy](https://github.com/gofiber/fiber/tree/main/middleware/proxy) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/proxy?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/proxy/stargazers) - Allows you to proxy requests to a multiple servers.
- [Recover](https://github.com/gofiber/fiber/tree/main/middleware/recover) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/recover?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/recover/stargazers) - Recovers from panics anywhere in the stack chain and hands control to the centralized ErrorHandler.
- [Redirect](https://github.com/gofiber/fiber/tree/main/middleware/redirect) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/redirect?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/redirect/stargazers) - Handles HTTP redirects in Fiber.
- [RequestID](https://github.com/gofiber/fiber/tree/main/middleware/requestid) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/requestid?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/requestid/stargazers) - Adds a requestid to every request.
- [Responsetime](https://github.com/gofiber/fiber/tree/main/middleware/responsetime) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/responsetime?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/responsetime/stargazers) - Adds an `X-Response-Time` header to responses.
- [Rewrite](https://github.com/gofiber/fiber/tree/main/middleware/rewrite) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/rewrite?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/rewrite/stargazers) - Rewrites the URL path based on provided rules for backward compatibility or cleaner links.
- [Session](https://github.com/gofiber/fiber/tree/main/middleware/session) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/session?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/session/stargazers) - Provides session management. NOTE: This middleware uses our Storage package.
- [Skip](https://github.com/gofiber/fiber/tree/main/middleware/skip) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/skip?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/skip/stargazers) - Skips a wrapped handler when a predicate is true.
- [Static](https://github.com/gofiber/fiber/tree/main/middleware/static) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/static?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/static/stargazers) - Serves static files from a local or custom file system.
- [Timeout](https://github.com/gofiber/fiber/tree/main/middleware/timeout) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber/tree/main/middleware/timeout?style=flat)](https://github.com/gofiber/fiber/tree/main/middleware/timeout/stargazers) - Adds a max time for a request and forwards to ErrorHandler if it is exceeded.

### 🔗 External

List of externally hosted middleware modules and maintained by the [Fiber team](https://github.com/orgs/gofiber/people) [![GitHub stars](https://img.shields.io/github/stars/orgs/gofiber/people?style=flat)](https://github.com/orgs/gofiber/people/stargazers).

- [storage](https://github.com/gofiber/storage) [![GitHub stars](https://img.shields.io/github/stars/gofiber/storage?style=flat)](https://github.com/gofiber/storage/stargazers) - Premade storage drivers that implement the Storage interface, designed to be used with various Fiber middlewares.
- [template](https://github.com/gofiber/template) [![GitHub stars](https://img.shields.io/github/stars/gofiber/template?style=flat)](https://github.com/gofiber/template/stargazers) - This package contains 8 template engines that can be used with Fiber v1.10.x Go version 1.13 or higher is required.

### ‍💻 Contrib

List of third party middlewares and maintained by the Fiber team and community.

- [casbin](https://github.com/gofiber/contrib/tree/main/v3/casbin) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/casbin?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/casbin/stargazers) - Authorization middleware for Fiber powered by Casbin.
- [circuitbreaker](https://github.com/gofiber/contrib/tree/main/v3/circuitbreaker) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/circuitbreaker?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/circuitbreaker/stargazers) - Circuit breaker middleware for Fiber.
- [fgprof](https://github.com/gofiber/contrib/tree/main/v3/fgprof) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/fgprof?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/fgprof/stargazers) - Fiber profiling support via fgprof.
- [hcaptcha](https://github.com/gofiber/contrib/tree/main/v3/hcaptcha) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/hcaptcha?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/hcaptcha/stargazers) - Bot-protection middleware using hCaptcha.
- [i18n](https://github.com/gofiber/contrib/tree/main/v3/i18n) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/i18n?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/i18n/stargazers) - Internationalization middleware built on go-i18n.
- [jwt](https://github.com/gofiber/contrib/tree/main/v3/jwt) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/jwt?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/jwt/stargazers) - JSON Web Token (JWT) auth middleware.
- [loadshed](https://github.com/gofiber/contrib/tree/main/v3/loadshed) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/loadshed?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/loadshed/stargazers) - Load-shedding middleware to protect Fiber services under pressure.
- [monitor](https://github.com/gofiber/contrib/tree/main/v3/monitor) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/monitor?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/monitor/stargazers) - Server metrics monitor middleware for Fiber.
- [newrelic](https://github.com/gofiber/contrib/tree/main/v3/newrelic) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/newrelic?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/newrelic/stargazers) - New Relic instrumentation support for Fiber.
- [opa](https://github.com/gofiber/contrib/tree/main/v3/opa) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/opa?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/opa/stargazers) - Open Policy Agent (OPA) middleware support for Fiber.
- [otel](https://github.com/gofiber/contrib/tree/main/v3/otel) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/otel?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/otel/stargazers) - OpenTelemetry middleware support for Fiber.
- [paseto](https://github.com/gofiber/contrib/tree/main/v3/paseto) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/paseto?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/paseto/stargazers) - Platform-Agnostic Security Tokens (PASETO) auth middleware.
- [sentry](https://github.com/gofiber/contrib/tree/main/v3/sentry) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/sentry?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/sentry/stargazers) - Error monitoring and reporting integration for Fiber with Sentry.
- [socketio](https://github.com/gofiber/contrib/tree/main/v3/socketio) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/socketio?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/socketio/stargazers) - Socket.IO-inspired WebSocket wrapper middleware for Fiber.
- [swaggo](https://github.com/gofiber/contrib/tree/main/v3/swaggo) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/swaggo?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/swaggo/stargazers) - Middleware for serving Swag-generated API docs in Fiber.
- [swaggerui](https://github.com/gofiber/contrib/tree/main/v3/swaggerui) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/swaggerui?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/swaggerui/stargazers) - Swagger UI middleware for serving OpenAPI specs in Fiber.
- [testcontainers](https://github.com/gofiber/contrib/tree/main/v3/testcontainers) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/testcontainers?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/testcontainers/stargazers) - Service implementation for integrating Testcontainers with Fiber.
- [WebSocket](https://github.com/gofiber/contrib/tree/main/v3/websocket) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/websocket?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/websocket/stargazers) - Fasthttp-based WebSocket integration for Fiber with `fiber.Ctx` support.
- [zap](https://github.com/gofiber/contrib/tree/main/v3/zap) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/zap?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/zap/stargazers) - Logging middleware support for Fiber with Zap.
- [zerolog](https://github.com/gofiber/contrib/tree/main/v3/zerolog) [![GitHub stars](https://img.shields.io/github/stars/gofiber/contrib/tree/main/v3/zerolog?style=flat)](https://github.com/gofiber/contrib/tree/main/v3/zerolog/stargazers) - Logging middleware support for Fiber with Zerolog.

### 🌱 Third Party

List of middlewares that are created by the Fiber community.

- [shareed2k/fiber_tracing](https://github.com/shareed2k/fiber_tracing) [![GitHub stars](https://img.shields.io/github/stars/shareed2k/fiber_tracing?style=flat)](https://github.com/shareed2k/fiber_tracing/stargazers) - Middleware trace requests on Fiber framework with OpenTracing API.
- [shareed2k/fiber_limiter](https://github.com/shareed2k/fiber_limiter) [![GitHub stars](https://img.shields.io/github/stars/shareed2k/fiber_limiter?style=flat)](https://github.com/shareed2k/fiber_limiter/stargazers) - Limiter using Redis as store for rate limit with two algorithms for choosing sliding window, gcra leaky bucket.
- [ansrivas/fiberprometheus](https://github.com/ansrivas/fiberprometheus) [![GitHub stars](https://img.shields.io/github/stars/ansrivas/fiberprometheus?style=flat)](https://github.com/ansrivas/fiberprometheus/stargazers) - Prometheus middleware for gofiber.
- [sacsand/gofiber-firebaseauth](https://github.com/sacsand/gofiber-firebaseauth) [![GitHub stars](https://img.shields.io/github/stars/sacsand/gofiber-firebaseauth?style=flat)](https://github.com/sacsand/gofiber-firebaseauth/stargazers) - Fiber Firebase Auth Middleware.
- [aschenmaker/fiber-health-check](https://github.com/aschenmaker/fiber-health-check) [![GitHub stars](https://img.shields.io/github/stars/aschenmaker/fiber-health-check?style=flat)](https://github.com/aschenmaker/fiber-health-check/stargazers) - Health-check middleware support health-check for Fiber️ framework.
- [elastic/apmfiber](https://github.com/elastic/apm-agent-go/tree/master/module/apmfiber) [![GitHub stars](https://img.shields.io/github/stars/elastic/apm-agent-go/tree/master/module/apmfiber?style=flat)](https://github.com/elastic/apm-agent-go/tree/master/module/apmfiber/stargazers) - APM Agent for Go Fiber.
- [eozer/fiber_ldapauth](https://github.com/eozer/fiber_ldapauth) [![GitHub stars](https://img.shields.io/github/stars/eozer/fiber_ldapauth?style=flat)](https://github.com/eozer/fiber_ldapauth/stargazers) - LDAP Authentication Middleware for Fiber.
- [fugue-labs/gollem](https://github.com/fugue-labs/gollem/tree/main/contrib/fiberhandler) [![GitHub stars](https://img.shields.io/github/stars/fugue-labs/gollem/tree/main/contrib/fiberhandler?style=flat)](https://github.com/fugue-labs/gollem/tree/main/contrib/fiberhandler/stargazers) - Handler adapter that wraps a gollem AI agent as a Fiber handler with SSE streaming support.
- [DavidHoenisch/fiber-coraza](https://github.com/DavidHoenisch/fiber-coraza) [![GitHub stars](https://img.shields.io/github/stars/DavidHoenisch/fiber-coraza?style=flat)](https://github.com/DavidHoenisch/fiber-coraza/stargazers) - Coraza WAF middleware for Fiber, providing web application firewall protection with ModSecurity-compatible rules.
- [darkweak/souin](https://github.com/darkweak/souin) [![GitHub stars](https://img.shields.io/github/stars/darkweak/souin?style=flat)](https://github.com/darkweak/souin/stargazers) - HTTP cache, RFC compliant, alternative to Varnish available as a middleware.
- [witer33/fiberpow](https://github.com/witer33/fiberpow) [![GitHub stars](https://img.shields.io/github/stars/witer33/fiberpow?style=flat)](https://github.com/witer33/fiberpow/stargazers) - Anti DDoS/Bot Middleware with a customizable Proof Of Work challenge.
- [beyer-stefan/gofiber-minifier](https://github.com/beyer-stefan/gofiber-minifier) [![GitHub stars](https://img.shields.io/github/stars/beyer-stefan/gofiber-minifier?style=flat)](https://github.com/beyer-stefan/gofiber-minifier/stargazers) - Minifying middleware for HTML5, CSS3, and JavaScript.
- [joffref/opa-middleware](https://github.com/Joffref/opa-middleware) [![GitHub stars](https://img.shields.io/github/stars/Joffref/opa-middleware?style=flat)](https://github.com/Joffref/opa-middleware/stargazers) - Provides an OPA middleware integration for fiber.
- [vladfr/fiber-servertiming](https://github.com/vladfr/fiber-servertiming) [![GitHub stars](https://img.shields.io/github/stars/vladfr/fiber-servertiming?style=flat)](https://github.com/vladfr/fiber-servertiming/stargazers) - A middleware to add Server-Timing headers based on the W3C Server-Timing Spec.
- [airbrake/gobrake](https://github.com/airbrake/gobrake/tree/master/examples/fiber) [![GitHub stars](https://img.shields.io/github/stars/airbrake/gobrake/tree/master/examples/fiber?style=flat)](https://github.com/airbrake/gobrake/tree/master/examples/fiber/stargazers) - An Airbrake middleware that reports performance data (route stats).
- [samber/slog-fiber](https://github.com/samber/slog-fiber) [![GitHub stars](https://img.shields.io/github/stars/samber/slog-fiber?style=flat)](https://github.com/samber/slog-fiber/stargazers) - A logger middleware that uses Go slog library.
- [mikhail-bigun/fiberlogrus](https://github.com/mikhail-bigun/fiberlogrus) [![GitHub stars](https://img.shields.io/github/stars/mikhail-bigun/fiberlogrus?style=flat)](https://github.com/mikhail-bigun/fiberlogrus/stargazers) - A logger middleware that uses logrus and its structured logging features.
- [Idan-Fishman/fiber-bind](https://github.com/Idan-Fishman/fiber-bind) [![GitHub stars](https://img.shields.io/github/stars/Idan-Fishman/fiber-bind?style=flat)](https://github.com/Idan-Fishman/fiber-bind/stargazers) - Request schema validator middleware that validates sources such as the request body, query string parameters, route parameters and even form files.
- [rodrigoodhin/fiper](https://gitlab.com/rodrigoodhin/fiper) - FiPer is a library that provides Fiber with Role Based Access Control (RBAC) using JWT and with database persistence using two ORM libraries are supported: Gorm and Bun.
- [zeiss/fiber-goth](https://github.com/ZEISS/fiber-goth) [![GitHub stars](https://img.shields.io/github/stars/ZEISS/fiber-goth?style=flat)](https://github.com/ZEISS/fiber-goth/stargazers) - Simple middleware to integrate authentication to your Fiber applications.
- [zeiss/fiber-authz](https://github.com/ZEISS/fiber-authz) [![GitHub stars](https://img.shields.io/github/stars/ZEISS/fiber-authz?style=flat)](https://github.com/ZEISS/fiber-authz/stargazers) - A middleware to secure routes in Fiber with a defined RBAC model.
- [zeiss/fiber-htmx](https://github.com/ZEISS/fiber-htmx) [![GitHub stars](https://img.shields.io/github/stars/ZEISS/fiber-htmx?style=flat)](https://github.com/ZEISS/fiber-htmx/stargazers) - A middleware for using HTMX in Fiber.
- [jsorb84/ssefiber](https://github.com/jsorb84/ssefiber) [![GitHub stars](https://img.shields.io/github/stars/jsorb84/ssefiber?style=flat)](https://github.com/jsorb84/ssefiber/stargazers) - A basic SSE Implementation for Fiber.
- [streamerd/fibergun](https://github.com/streamerd/fibergun) [![GitHub stars](https://img.shields.io/github/stars/streamerd/fibergun?style=flat)](https://github.com/streamerd/fibergun/stargazers) - A GunDB middleware for Fiber. Enables easy integration of GunDB, a decentralized database.
- [apitally/apitally-go](https://github.com/apitally/apitally-go) [![GitHub stars](https://img.shields.io/github/stars/apitally/apitally-go?style=flat)](https://github.com/apitally/apitally-go/stargazers) - Simple API monitoring tool for Fiber. Tracks API usage, errors, and performance, and includes request logging and alerting features.
- [newrelic/go-agent](https://github.com/newrelic/go-agent/tree/master/v3/integrations/nrfiber) [![GitHub stars](https://img.shields.io/github/stars/newrelic/go-agent/tree/master/v3/integrations/nrfiber?style=flat)](https://github.com/newrelic/go-agent/tree/master/v3/integrations/nrfiber/stargazers) - Official New Relic middleware for Fiber that manages instrumentation for New Relic monitoring.
- [narmadaweb/limiter](https://github.com/narmadaweb/limiter) [![GitHub stars](https://img.shields.io/github/stars/narmadaweb/limiter?style=flat)](https://github.com/narmadaweb/limiter/stargazers) - A high-performance Redis-backed rate limiter middleware for Fiber, supporting fixed window, sliding window, and token bucket algorithms.
- [narmadaweb/gonify](https://github.com/narmadaweb/gonify) [![GitHub stars](https://img.shields.io/github/stars/narmadaweb/gonify?style=flat)](https://github.com/narmadaweb/gonify/stargazers) - Fiber Minifying middleware for HTML5, CSS3, JavaScript, Json, XML and SVG.
- [oaswrap/fiberopenapi](https://github.com/oaswrap/spec/tree/main/adapter/fiberopenapi) [![GitHub stars](https://img.shields.io/github/stars/oaswrap/spec/tree/main/adapter/fiberopenapi?style=flat)](https://github.com/oaswrap/spec/tree/main/adapter/fiberopenapi/stargazers) - Fiber adapter for OpenAPI 3.x specification generation with automatic route documentation.

## 🚧 Boilerplates

Premade boilerplates for Fiber.

- [gofiber/boilerplate](https://github.com/gofiber/boilerplate) [![GitHub stars](https://img.shields.io/github/stars/gofiber/boilerplate?style=flat)](https://github.com/gofiber/boilerplate/stargazers) - Official fiber boilerplate.
- [fiber-boilerplate](https://github.com/thomasvvugt/fiber-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/thomasvvugt/fiber-boilerplate?style=flat)](https://github.com/thomasvvugt/fiber-boilerplate/stargazers) - A boilerplate for the Fiber web framework.
- [sujit-baniya/fiber-boilerplate](https://github.com/sujit-baniya/fiber-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/sujit-baniya/fiber-boilerplate?style=flat)](https://github.com/sujit-baniya/fiber-boilerplate/stargazers) - Boilerplate on the top of fiber web framework with many middlewares and features.
- [goravel/fiber](https://github.com/goravel/fiber) [![GitHub stars](https://img.shields.io/github/stars/goravel/fiber?style=flat)](https://github.com/goravel/fiber/stargazers) - Laravel similar boilerplate with support for Fiber.
- [create-go-app/fiber-go-template](https://github.com/create-go-app/fiber-go-template) [![GitHub stars](https://img.shields.io/github/stars/create-go-app/fiber-go-template?style=flat)](https://github.com/create-go-app/fiber-go-template/stargazers) - Fiber backend template for Create Go App CLI.
- [efectn/fiber-boilerplate](https://github.com/efectn/fiber-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/efectn/fiber-boilerplate?style=flat)](https://github.com/efectn/fiber-boilerplate/stargazers) - Simple and scalable boilerplate to build powerful and organized REST projects with Fiber.
- [embedmode/fiberseed](https://github.com/embedmode/fiberseed) [![GitHub stars](https://img.shields.io/github/stars/embedmode/fiberseed?style=flat)](https://github.com/embedmode/fiberseed/stargazers) - Fiber boilerplate api with many middlewares.
- [GalvinGao/gofiber-template](https://github.com/GalvinGao/gofiber-template) [![GitHub stars](https://img.shields.io/github/stars/GalvinGao/gofiber-template?style=flat)](https://github.com/GalvinGao/gofiber-template/stargazers) - A production-ready, container-first opinionated gofiber project template. Config by envvars, DI by go.uber.org/fx, Database by uptrace/bun, with out-of-the-box MVC folder structure and CI/CD support.
- [mikhail-bigun/go-app-template](https://github.com/mikhail-bigun/go-app-template) [![GitHub stars](https://img.shields.io/github/stars/mikhail-bigun/go-app-template?style=flat)](https://github.com/mikhail-bigun/go-app-template/stargazers) - Clean architecture Go application boilerplate with enriched Fiber implementation.
- [felipeafonso/go-htmx-starter](https://github.com/FelipeAfonso/go-htmx-starter) [![GitHub stars](https://img.shields.io/github/stars/FelipeAfonso/go-htmx-starter?style=flat)](https://github.com/FelipeAfonso/go-htmx-starter/stargazers) - A front-end opinionated boilerplate for Go + HTMX development, using Tailwind and Vite for Bundling and Hot Reloading.
- [amrebada/go-modules](https://github.com/amrebada/go-modules) [![GitHub stars](https://img.shields.io/github/stars/amrebada/go-modules?style=flat)](https://github.com/amrebada/go-modules/stargazers) - Nest JS like structure for Go Fiber.
- [ingeniousambivert/fiber-bootstrapped](https://github.com/ingeniousambivert/fiber-bootstrapped) [![GitHub stars](https://img.shields.io/github/stars/ingeniousambivert/fiber-bootstrapped?style=flat)](https://github.com/ingeniousambivert/fiber-bootstrapped/stargazers) - A toolkit for Go projects embracing a service-centric architecture, inspired by the principles of FeathersJS.
- [sebajax/go-vertical-slice-architecture](https://github.com/sebajax/go-vertical-slice-architecture) [![GitHub stars](https://img.shields.io/github/stars/sebajax/go-vertical-slice-architecture?style=flat)](https://github.com/sebajax/go-vertical-slice-architecture/stargazers) - Vertical Slice Architecture code archetype using Fiber and Uber dig. A maintainable, and scalable code organization.
- [go-rat/fiber-skeleton](https://github.com/go-rat/fiber-skeleton) [![GitHub stars](https://img.shields.io/github/stars/go-rat/fiber-skeleton?style=flat)](https://github.com/go-rat/fiber-skeleton/stargazers) - Fiber skeleton to powers web projects, support wire-based dependency injection.

## 📁 Recipes

Recipes for Fiber.

- [gofiber/recipes](https://github.com/gofiber/recipes) [![GitHub stars](https://img.shields.io/github/stars/gofiber/recipes?style=flat)](https://github.com/gofiber/recipes/stargazers) - Official Fiber cookbook.
- [kiyonlin/fiblar-demo](https://github.com/kiyonlin/fiblar-demo) [![GitHub stars](https://img.shields.io/github/stars/kiyonlin/fiblar-demo?style=flat)](https://github.com/kiyonlin/fiblar-demo/stargazers) - Fiber v1 + angular demo.
- [koddr/tutorial-go-fiber-rest-api](https://github.com/koddr/tutorial-go-fiber-rest-api) [![GitHub stars](https://img.shields.io/github/stars/koddr/tutorial-go-fiber-rest-api?style=flat)](https://github.com/koddr/tutorial-go-fiber-rest-api/stargazers) - Tutorial for building a restful api with fiber.
- [firebase007/go-rest-api-with-fiber](https://github.com/firebase007/go-rest-api-with-fiber) [![GitHub stars](https://img.shields.io/github/stars/firebase007/go-rest-api-with-fiber?style=flat)](https://github.com/firebase007/go-rest-api-with-fiber/stargazers) - Demo project with fiber, logging, basicAuth and postgresql.
- [chawk/go_fiber_quickstart](https://github.com/chawk/go_fiber_quickstart) [![GitHub stars](https://img.shields.io/github/stars/chawk/go_fiber_quickstart?style=flat)](https://github.com/chawk/go_fiber_quickstart/stargazers) - Fiber quick start example project.
- [EricLau1/go-fiber-auth-api](https://github.com/EricLau1/go-fiber-auth-api) [![GitHub stars](https://img.shields.io/github/stars/EricLau1/go-fiber-auth-api?style=flat)](https://github.com/EricLau1/go-fiber-auth-api/stargazers) - Golang Authentication API with Fiber MongoDB and JWT.
- [alpody/golang-fiber-realworld-example-app](https://github.com/alpody/golang-fiber-realworld-example-app) [![GitHub stars](https://img.shields.io/github/stars/alpody/golang-fiber-realworld-example-app?style=flat)](https://github.com/alpody/golang-fiber-realworld-example-app/stargazers) - Example real world backend API built with Fiber, Gorm, Swagger.
- [kubestellar/console](https://github.com/kubestellar/console) [![GitHub stars](https://img.shields.io/github/stars/kubestellar/console?style=flat)](https://github.com/kubestellar/console/stargazers) - AI-powered multi-cluster Kubernetes dashboard built on Fiber, with real-time observability and CNCF integrations.
- [paundraP/golang-starter-template](https://github.com/paundraP/Go-Starter-Template) [![GitHub stars](https://img.shields.io/github/stars/paundraP/Go-Starter-Template?style=flat)](https://github.com/paundraP/Go-Starter-Template/stargazers) - Golang REST API with authentication, authorization, and integrated payment gateway support.

## 🛠️ Tools

Several tools to make Fiber usage easier.

- [Alibaba/opentelemetry-go-auto-instrumentation](https://github.com/alibaba/opentelemetry-go-auto-instrumentation) [![GitHub stars](https://img.shields.io/github/stars/alibaba/opentelemetry-go-auto-instrumentation?style=flat)](https://github.com/alibaba/opentelemetry-go-auto-instrumentation/stargazers) - A tool to monitor fiber application without changing any code with OpenTelemetry APIs.
- [deepmap/oapi-codegen](https://github.com/deepmap/oapi-codegen) [![GitHub stars](https://img.shields.io/github/stars/deepmap/oapi-codegen?style=flat)](https://github.com/deepmap/oapi-codegen/stargazers) - Generate Go client and server boilerplate from OpenAPI 3 specifications.
- [go-dawn/dawn](https://github.com/go-dawn/dawn) [![GitHub stars](https://img.shields.io/github/stars/go-dawn/dawn?style=flat)](https://github.com/go-dawn/dawn/stargazers) - Dawn is an opinionated web framework that provides rapid development capabilities which on top of Fiber.
- [MUlt1mate/protoc-gen-httpgo](https://github.com/MUlt1mate/protoc-gen-httpgo) [![GitHub stars](https://img.shields.io/github/stars/MUlt1mate/protoc-gen-httpgo?style=flat)](https://github.com/MUlt1mate/protoc-gen-httpgo/stargazers) - A protoc plugin that generates Fiber HTTP server and client code from proto files.
- [ryanbekhen/feserve](https://github.com/ryanbekhen/feserve) [![GitHub stars](https://img.shields.io/github/stars/ryanbekhen/feserve?style=flat)](https://github.com/ryanbekhen/feserve/stargazers) - Feserve is a lightweight application or Docker image to serve frontend and load balancer applications.
- [tompston/gomakeme](https://github.com/tompston/gomakeme) [![GitHub stars](https://img.shields.io/github/stars/tompston/gomakeme?style=flat)](https://github.com/tompston/gomakeme/stargazers) - Generate boilerplate + endpoints for Fiber or Gin REST APIs.

## 📖 Articles

Articles about Fiber written by the community.

- [Working with middlewares and boilerplates](https://dev.to/koddr/go-fiber-by-examples-working-with-middlewares-and-boilerplates-3p0m)
- [Testing the application](https://dev.to/koddr/go-fiber-by-examples-testing-the-application-1ldf)
- [Delving into built-in functions](https://dev.to/koddr/go-fiber-by-examples-delving-into-built-in-functions-1p3k)
- [Go Fiber by Examples: How can the Fiber Web Framework be useful?](https://dev.to/koddr/go-fiber-by-examples-how-can-the-fiber-web-framework-be-useful-487a)
- [Build a RESTful API on Go: Fiber, PostgreSQL, JWT and Swagger docs in isolated Docker containers](https://dev.to/koddr/build-a-restful-api-on-go-fiber-postgresql-jwt-and-swagger-docs-in-isolated-docker-containers-475j)
- [Getting started with Fiber](https://dev.to/fenny/getting-started-with-fiber-36b6)
- [Building an Express-style API in Go with Fiber](https://blog.logrocket.com/express-style-api-go-fiber/)
- [Fiber v1.9.6 How to improve performance by 817% and stay fast, flexible and friendly?](https://dev.to/koddr/fiber-v1-9-5-how-to-improve-performance-by-817-and-stay-fast-flexible-and-friendly-2dp6)
- [Create a travel list app with Go, Fiber, Angular, MongoDB and Google Cloud Secret Manager](https://blog.yongweilun.me/create-a-travel-list-app-with-go-fiber-angular-mongodb-and-google-cloud-secret-manager-ck9fgxy0p061pcss1xt1ubu8t)
- [Building a Basic REST API in Go using Fiber](https://tutorialedge.net/golang/basic-rest-api-go-fiber/)
- [Creating Fast APIs In Go Using Fiber](https://dev.to/jozsefsallai/creating-fast-apis-in-go-using-fiber-59m9)
- [Is switching from Express to Fiber worth it?](https://dev.to/koddr/are-sure-what-your-lovely-web-framework-running-so-fast-2jl1)
- [Fiber v1.8. What's new, updated and re-thinked?](https://dev.to/koddr/fiber-v1-8-what-s-new-updated-and-re-thinked-339h)
- [Fiber released v1.7! What\'s new and is it still fast, flexible and friendly?](https://dev.to/koddr/fiber-v2-is-out-now-what-s-new-and-is-he-still-fast-flexible-and-friendly-3ipf)
- [Welcome to Fiber — an Express.js styled web framework written in Go with ❤️](https://dev.to/koddr/welcome-to-fiber-an-express-js-styled-fastest-web-framework-written-with-on-golang-497)
- [Blazing Fast Unit Tests - Fiber/fasthttp/http Internals](https://medium.com/trendyol-tech/golang-blazing-fast-unit-tests-fiber-fasthttp-http-internals-and-optimizing-http-server-tests-bbd1fe7b944b)
- [Building Microservices in Go : Part 1 - Project Setup, Dockerization](https://saadfarhan124.medium.com/building-microservices-in-go-part-1-e7e58893bc5e)
- [Building Microservices in Go : Part 2 - Live Reload](https://saadfarhan124.medium.com/building-microservices-in-go-part-2-f9c6c535805c)
- [Building Microservices in Go : Part 3 - Database, Models, Migrations](https://saadfarhan124.medium.com/building-microservices-in-go-part-3-database-models-migrations-a4455121bb11)
- [Build a REST API from scratch with Go, Docker & PostgreSQL](https://dev.to/divrhino/build-a-rest-api-from-scratch-with-go-and-docker-3o54)
- [Build a fullstack app with Go Fiber, Docker, and PostgreSQL](https://dev.to/divrhino/build-a-fullstack-app-with-go-fiber-docker-and-postgres-1jg6)
- [Create a CRUD app with Go Fiber, Docker, and PostgreSQL](https://dev.to/divrhino/create-a-crud-app-with-go-fiber-docker-and-postgres-47e3)

## 📺 Videos

Video tutorials created by the community about Fiber.

- [Is Fiber the best Go web framework? Better than Gin?](https://youtu.be/10miByMOGfY)

## 🤖 Benchmarks

Several benchmarks to compare Fiber with other frameworks.

- [TechEmpower](https://www.techempower.com/benchmarks/#section=data-r20&hw=ph&test=json) - Project provides performance measures across a wide field of web application frameworks.
- [web-frameworks-benchmark](https://web-frameworks-benchmark.netlify.app/result) - Project aims to measure the differences between the various programming language frameworks.
- [go-web-framework-benchmark](https://github.com/smallnest/go-web-framework-benchmark) [![GitHub stars](https://img.shields.io/github/stars/smallnest/go-web-framework-benchmark?style=flat)](https://github.com/smallnest/go-web-framework-benchmark/stargazers) - This benchmark suite aims to compare the performance of Go web frameworks.

### 👍 Contributing

Contribution guidelines can be found on [CONTRIBUTING.md](https://github.com/gofiber/awesome-fiber/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/gofiber/awesome-fiber/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/gofiber/awesome-fiber/blob/master/CONTRIBUTING.md/stargazers)

## ☕ Supporters

Fiber is an open-source project that runs on donations to pay the bills, e.g., our domain name, hosting, and serverless infrastructure. If you want to support Fiber, please become a [GitHub Sponsor](https://github.com/sponsors/gofiber) [![GitHub stars](https://img.shields.io/github/stars/sponsors/gofiber?style=flat)](https://github.com/sponsors/gofiber/stargazers).

<!-- sponsors -->

### 📅 Monthly Sponsors

<table>
<tr><td valign="top"><strong>🔥 Fiber Guardian</strong></td><td><a href="https://www.coderabbit.ai/?utm_source=cr_org&amp;utm_medium=github" title="@coderabbitai"><img src="https://github.com/coderabbitai.png" width="50" alt="@coderabbitai" /></a></td></tr>
<tr><td valign="top"><strong>☕ Fiber Supporter</strong></td><td><a href="https://ndole.studio" title="@NdoleStudio"><img src="https://github.com/NdoleStudio.png" width="34" alt="@NdoleStudio" /></a>&nbsp;<a href="https://cyberapper.ai" title="@petercool"><img src="https://github.com/petercool.png" width="34" alt="@petercool" /></a></td></tr>
<tr><td valign="top"><strong>🪴 Fiber Friend</strong></td><td><a href="https://github.com/simonheisstpeter" title="@simonheisstpeter"><img src="https://github.com/simonheisstpeter.png" width="32" alt="@simonheisstpeter" /></a></td></tr>
</table>

### 🎁 One-time Sponsors

<table>
<tr><td valign="top"><strong>🚀 Fiber Hero</strong></td><td><a href="https://www.thanks.dev" title="@thnxdev"><img src="https://github.com/thnxdev.png" width="40" alt="@thnxdev" /></a></td></tr>
</table>
<!-- sponsors -->
