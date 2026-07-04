# Cloudflare

> 来源：[irazasyed/awesome-cloudflare](https://github.com/irazasyed/awesome-cloudflare)

[![GitHub stars](https://img.shields.io/github/stars/irazasyed/awesome-cloudflare?style=flat)](https://github.com/irazasyed/awesome-cloudflare/stargazers)

# Awesome Cloudflare [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re) [<img src="media/cf-logo.svg" width="250" align="right" alt="Cloudflare">](https://www.cloudflare.com)

> Curated list of awesome [Cloudflare](https://www.cloudflare.com) worker recipes, open-source projects, guides, blogs and other resources.

Cloudflare provides content delivery network (CDN) services, DDoS mitigation, Internet security and distributed domain name server (DNS) services, sitting between the visitor and the Cloudflare user's hosting provider, acting as a reverse proxy for websites.

## Contents

- [Community](#community)
- [Blog](#blog)
- [DNS](#dns)
- [Developers](#developers)
- [Apps](#apps)
  - [Open Source](#open-source)
- [Workers](#workers)
  - [Reference](#reference)
  - [Tools](#tools)
  - [Recipes](#recipes)
  - [AI](#ai)
- [Other](#other)

## Community

- [Forum](https://community.cloudflare.com)
- [Reddit](https://www.reddit.com/r/CloudFlare)
- [`@Cloudflare` on Twitter](https://twitter.com/cloudflare)
- [Facebook](https://www.facebook.com/Cloudflare)
- [YouTube](https://www.youtube.com/cloudflare-)
- [GitHub](https://github.com/cloudflare) [![GitHub stars](https://img.shields.io/github/stars/cloudflare?style=flat)](https://github.com/cloudflare/stargazers)
- [GitHub Topic](https://github.com/topics/cloudflare) [![GitHub stars](https://img.shields.io/github/stars/topics/cloudflare?style=flat)](https://github.com/topics/cloudflare/stargazers)
- [Stack Exchange](https://stackexchange.com/search?q=cloudflare)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/cloudflare)
- [Server Fault](https://serverfault.com/questions/tagged/cloudflare)

## Blog

- [Official Blog](https://blog.cloudflare.com)

## DNS

- [DNS Zone Files](https://github.com/irazasyed/dns-zone-files) [![GitHub stars](https://img.shields.io/github/stars/irazasyed/dns-zone-files?style=flat)](https://github.com/irazasyed/dns-zone-files/stargazers) - Ready to import common config zone files for easy configuration of various services.
- [Lexicon](https://github.com/AnalogJ/lexicon) [![GitHub stars](https://img.shields.io/github/stars/AnalogJ/lexicon?style=flat)](https://github.com/AnalogJ/lexicon/stargazers) - CLI tool to manipulate DNS records on various DNS providers in a standardized way.
- [Th3inspector](https://github.com/Moham3dRiahi/Th3inspector) [![GitHub stars](https://img.shields.io/github/stars/Moham3dRiahi/Th3inspector?style=flat)](https://github.com/Moham3dRiahi/Th3inspector/stargazers) - All in one CLI tool for information gathering.
- [Partner Panel](https://github.com/ZE3kr/Cloudflare-CNAME-Setup) [![GitHub stars](https://img.shields.io/github/stars/ZE3kr/Cloudflare-CNAME-Setup?style=flat)](https://github.com/ZE3kr/Cloudflare-CNAME-Setup/stargazers) - Tool for hosting partners to provide a DNS management panel for customers.
- [CFPMP](https://github.com/Netrvin/CFPMP) [![GitHub stars](https://img.shields.io/github/stars/Netrvin/CFPMP?style=flat)](https://github.com/Netrvin/CFPMP/stargazers) - Partner management panel.
- [Flares](https://github.com/lfaoro/flares) [![GitHub stars](https://img.shields.io/github/stars/lfaoro/flares?style=flat)](https://github.com/lfaoro/flares/stargazers) - DNS backup tool.
- [Block Bad Bot Ruleset](https://github.com/SukkaW/cloudflare-block-bad-bot-ruleset) [![GitHub stars](https://img.shields.io/github/stars/SukkaW/cloudflare-block-bad-bot-ruleset?style=flat)](https://github.com/SukkaW/cloudflare-block-bad-bot-ruleset/stargazers) - Collection of rulesets to block malicious crawlers with firewall rules.
- [Docker DDNS](https://github.com/oznu/docker-cloudflare-ddns) [![GitHub stars](https://img.shields.io/github/stars/oznu/docker-cloudflare-ddns?style=flat)](https://github.com/oznu/docker-cloudflare-ddns/stargazers) - Docker image to use the free DNS Service as a dynamic DNS provider.
- [DDNS script for Synology](https://github.com/joshuaavalon/SynologyCloudflareDDNS) [![GitHub stars](https://img.shields.io/github/stars/joshuaavalon/SynologyCloudflareDDNS?style=flat)](https://github.com/joshuaavalon/SynologyCloudflareDDNS/stargazers) - DDNS script for Synology NAS.
- [Dynamic DNS Bash](https://github.com/yulewang/cloudflare-api-v4-ddns) [![GitHub stars](https://img.shields.io/github/stars/yulewang/cloudflare-api-v4-ddns?style=flat)](https://github.com/yulewang/cloudflare-api-v4-ddns/stargazers) - Dynamic DNS updater in bash script.
- [Dynamic DNS PHP](https://github.com/lyoshenka/cloudflare-ddns) [![GitHub stars](https://img.shields.io/github/stars/lyoshenka/cloudflare-ddns?style=flat)](https://github.com/lyoshenka/cloudflare-ddns/stargazers) - Dynamic DNS updater in PHP.
- [Dynamic DNS Python](https://github.com/adrienbrignon/cloudflare-ddns) [![GitHub stars](https://img.shields.io/github/stars/adrienbrignon/cloudflare-ddns?style=flat)](https://github.com/adrienbrignon/cloudflare-ddns/stargazers) - Dynamic DNS updater in python.
- [Multi-Provider DDNS Script](https://github.com/phuslu/ddns) [![GitHub stars](https://img.shields.io/github/stars/phuslu/ddns?style=flat)](https://github.com/phuslu/ddns/stargazers) - Multiple providers ddns script without dependencies.
- [Argo Tunnel Client](https://github.com/cloudflare/cloudflared) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/cloudflared?style=flat)](https://github.com/cloudflare/cloudflared/stargazers) - CLI client for Argo tunnel, a tunneling daemon that proxies any local webserver through the Cloudflare network.
- [Upper](https://github.com/ostark/upper) [![GitHub stars](https://img.shields.io/github/stars/ostark/upper?style=flat)](https://github.com/ostark/upper/stargazers) - Speeds up craft dramatically using a cache proxy in front of your webserver.
- [Cloud Buster](https://github.com/SageHack/cloud-buster) [![GitHub stars](https://img.shields.io/github/stars/SageHack/cloud-buster?style=flat)](https://github.com/SageHack/cloud-buster/stargazers) - A comprehensive pentest tool that checks sites for origin IP leaks.
- [CLI Tool](https://github.com/danielpigott/cloudflare-cli) [![GitHub stars](https://img.shields.io/github/stars/danielpigott/cloudflare-cli?style=flat)](https://github.com/danielpigott/cloudflare-cli/stargazers) - CLI tool for interacting with Cloudflare.
- [Detector](https://github.com/k4m4/cloudflare-detect) [![GitHub stars](https://img.shields.io/github/stars/k4m4/cloudflare-detect?style=flat)](https://github.com/k4m4/cloudflare-detect/stargazers) - Detect whether a site is running behind Cloudflare.
- [Scrape](https://github.com/Anorov/cloudflare-scrape) [![GitHub stars](https://img.shields.io/github/stars/Anorov/cloudflare-scrape?style=flat)](https://github.com/Anorov/cloudflare-scrape/stargazers) - Python module to bypass anti-bot page.
- [CloudFlair](https://github.com/christophetd/CloudFlair) [![GitHub stars](https://img.shields.io/github/stars/christophetd/CloudFlair?style=flat)](https://github.com/christophetd/CloudFlair/stargazers) - Tool to find origin servers of websites protected by CloudFlare who are publicly exposed.

## Developers

- [Developers Hub](https://developers.cloudflare.com) - Developer docs including API reference, articles, and sample code for all products.
- [Open Source](https://cloudflare.github.io) - Official open-source projects.
- [API Docs](https://api.cloudflare.com) - API documentation.
- [Integration Resources](https://www.cloudflare.com/integrations) - Plugins for content management systems, control panels, cloud providers, ecommerce platforms and more.
- [Technical Resources](https://www.cloudflare.com/technical-resources) - Technical tools and resources.
- [The Serverlist Newsletter](https://blog.cloudflare.com/serverlist) - The serverlist is a Cloudflare-curated newsletter about all things serverless.

## Apps

> [Cloudflare Apps](https://www.cloudflare.com/apps/developers) lets you ship your tool or service to millions of sites. Any Cloudflare customer can preview & install your code on their site in seconds.

- [Apps Directory](https://www.cloudflare.com/apps)
- [Documentation](https://www.cloudflare.com/apps/developer/docs/getting-started)
- [Developer Fund](https://www.cloudflare.com/fund)
- [App Ideas](https://github.com/cloudflare-apps/ideas) [![GitHub stars](https://img.shields.io/github/stars/cloudflare-apps/ideas?style=flat)](https://github.com/cloudflare-apps/ideas/stargazers)

### Open Source

- [Official OSS Apps](https://github.com/cloudflare-apps) [![GitHub stars](https://img.shields.io/github/stars/cloudflare-apps?style=flat)](https://github.com/cloudflare-apps/stargazers) - Collection of official apps.
- [Logflare](https://github.com/Logflare/cloudflare-app) [![GitHub stars](https://img.shields.io/github/stars/Logflare/cloudflare-app?style=flat)](https://github.com/Logflare/cloudflare-app/stargazers) - Log management & event analytics.
- [OpWork.dev](https://github.com/hisorange/opwork) [![GitHub stars](https://img.shields.io/github/stars/hisorange/opwork?style=flat)](https://github.com/hisorange/opwork/stargazers) - Self hosted CloudFlare workers management platform.

## Workers

> [Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers) provides a serverless execution environment that allows you to create entirely new applications or augment existing ones without configuring or maintaining infrastructure.

### Reference

- [Documentation](https://workers.cloudflare.com/docs)
- [Tutorials](https://workers.cloudflare.com/docs/tutorials)
- [Runtime](https://workers.cloudflare.com/docs/reference/runtime)
- [Workers KV](https://workers.cloudflare.com/docs/reference/storage)

### Tools

- [Wrangler](https://github.com/cloudflare/wrangler) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/wrangler?style=flat)](https://github.com/cloudflare/wrangler/stargazers) - `wrangler` is a CLI tool designed for folks who are interested in using Cloudflare workers.
- [Playground](https://www.cloudflareworkers.com) - Simple, instant way to preview and test code directly in the browser against any site.
- [Serverless Plugin](https://workers.cloudflare.com/docs/reference/tooling/serverless) - Plugin for [serverless framework](https://github.com/serverless/serverless) [![GitHub stars](https://img.shields.io/github/stars/serverless/serverless?style=flat)](https://github.com/serverless/serverless/stargazers) to develop and deploy serverless applications using Workers.
- [Worker App Kit](https://github.com/postlight/cloudflare-worker-app-kit) [![GitHub stars](https://img.shields.io/github/stars/postlight/cloudflare-worker-app-kit?style=flat)](https://github.com/postlight/cloudflare-worker-app-kit/stargazers) - Handy set of tools for creating, developing, testing, and deploying worker app.
- [GitHub Action](https://github.com/cpilsworth/cloudflare-worker-action) [![GitHub stars](https://img.shields.io/github/stars/cpilsworth/cloudflare-worker-action?style=flat)](https://github.com/cpilsworth/cloudflare-worker-action/stargazers) - Deploy a worker on push to the master branch.
- [Workers KV Viewer](https://github.com/jroyal/cloudflare-workers-kv-viewer) [![GitHub stars](https://img.shields.io/github/stars/jroyal/cloudflare-workers-kv-viewer?style=flat)](https://github.com/jroyal/cloudflare-workers-kv-viewer/stargazers) - CLI based interactive viewer for workers KV storage.
- [Redirect Management](https://forwarding.app) - Generate redirect worker.

### Recipes

- [Examples Collection](https://github.com/cloudflare/worker-examples) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/worker-examples?style=flat)](https://github.com/cloudflare/worker-examples/stargazers) - Collection of recipes.
- [Hello World JS Boilerplate](https://github.com/cloudflare/worker-template) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/worker-template?style=flat)](https://github.com/cloudflare/worker-template/stargazers) - Template for kick starting a worker project in JS.
- [Hello World Rust Boilerplate](https://github.com/cloudflare/rustwasm-worker-template) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/rustwasm-worker-template?style=flat)](https://github.com/cloudflare/rustwasm-worker-template/stargazers) - Template for kick starting a worker project using wasm-pack.
- [Router](https://github.com/cloudflare/worker-template-router) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/worker-template-router?style=flat)](https://github.com/cloudflare/worker-template-router/stargazers) - Router that can be used with REST APIs or apps for basic routing logic.
- [Static](https://github.com/cloudflare/worker-template-static) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/worker-template-static?style=flat)](https://github.com/cloudflare/worker-template-static/stargazers) - Generate a static HTML or JSON page from raw strings in your workers script.
- [Fetch](https://github.com/cloudflare/worker-template-fetch) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/worker-template-fetch?style=flat)](https://github.com/cloudflare/worker-template-fetch/stargazers) - Examples of making fetch requests and generating JSON post requests.
- [Incoming Request](https://github.com/ashleygwilliams/worker-template-requests) [![GitHub stars](https://img.shields.io/github/stars/ashleygwilliams/worker-template-requests?style=flat)](https://github.com/ashleygwilliams/worker-template-requests/stargazers) - Examples of reading in a POST request body of type JSON and form-data.
- [Redirect](https://github.com/cloudflare/worker-template-redirect) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/worker-template-redirect?style=flat)](https://github.com/cloudflare/worker-template-redirect/stargazers) - Examples of sending single and bulk redirects from a Worker script.
- [Img-Color](https://github.com/xtuc/img-color-worker) [![GitHub stars](https://img.shields.io/github/stars/xtuc/img-color-worker?style=flat)](https://github.com/xtuc/img-color-worker/stargazers) - Retrieve the dominant color of a png or jpeg image.
- [Binast](https://github.com/xtuc/binast-cf-worker-template) [![GitHub stars](https://img.shields.io/github/stars/xtuc/binast-cf-worker-template?style=flat)](https://github.com/xtuc/binast-cf-worker-template/stargazers) - Serve binast via a worker.
- [Pwnage Protection](https://github.com/detroitenglish/pw-pwnage-cfworker) [![GitHub stars](https://img.shields.io/github/stars/detroitenglish/pw-pwnage-cfworker?style=flat)](https://github.com/detroitenglish/pw-pwnage-cfworker/stargazers) - Secure password scoring and user pwnage protection api - [Usage](https://community.cloudflare.com/t/estimate-strength-of-users-new-password-input-with-zxcvbn-and-query-haveibeenpwned-for-matches-against-known-hacked-accounts/26378).
- [Cache Purger Proxy](https://gist.github.com/vdbelt/20f116236d2ebffa92f131e679c0551a) - Proxies purge cache requests - [Usage](https://community.cloudflare.com/t/worker-recipe-cache-purge-proxy/29978).
- [URL Router](https://github.com/berstend/service-worker-router) [![GitHub stars](https://img.shields.io/github/stars/berstend/service-worker-router?style=flat)](https://github.com/berstend/service-worker-router/stargazers) - Fast url router - [Usage](https://community.cloudflare.com/t/open-source-fast-url-router-for-workers-js-typescript/33406).
- [Edge Proxy](https://github.com/DigitalOptimizationGroup/cloudflare-edge-proxy) [![GitHub stars](https://img.shields.io/github/stars/DigitalOptimizationGroup/cloudflare-edge-proxy?style=flat)](https://github.com/DigitalOptimizationGroup/cloudflare-edge-proxy/stargazers) - Enable A/B testing, canary releasing, gatekeeping, and SEO A/B/N testing.
- [Blue / Green Deployments](https://github.com/DigitalOptimizationGroup/blue-green-cloudflare-workers) [![GitHub stars](https://img.shields.io/github/stars/DigitalOptimizationGroup/blue-green-cloudflare-workers?style=flat)](https://github.com/DigitalOptimizationGroup/blue-green-cloudflare-workers/stargazers) - Working example of blue / green deployments with canary releasing.
- [Preact PWA](https://github.com/DigitalOptimizationGroup/cloudflare-worker-preact-pwa) [![GitHub stars](https://img.shields.io/github/stars/DigitalOptimizationGroup/cloudflare-worker-preact-pwa?style=flat)](https://github.com/DigitalOptimizationGroup/cloudflare-worker-preact-pwa/stargazers) - Preact progressive web app.
- [CURL Interceptor](https://github.com/Gaafar/curl-worker) [![GitHub stars](https://img.shields.io/github/stars/Gaafar/curl-worker?style=flat)](https://github.com/Gaafar/curl-worker/stargazers) - Intercepts requests from `curl` command and returns something different.
- [Worker with built-in Router](https://github.com/anderly/cloudflare-worker-routing) [![GitHub stars](https://img.shields.io/github/stars/anderly/cloudflare-worker-routing?style=flat)](https://github.com/anderly/cloudflare-worker-routing/stargazers) - Allows you to separate your worker logic into different functions and/or controllers.
- [Connecting to Google Storage](https://community.cloudflare.com/t/connecting-to-google-storage/32350) - Pull files from Google's cloud storage.
- [CSRF Protection](https://gist.github.com/simonerni/3501b8de6320ac37398d08d9d2d08561) - Protect any origin from CSRF by verifying origin/referer headers.
- [URL Query Strings Parser](https://community.cloudflare.com/t/parse-url-query-strings-with-cloudflare-workers/90286) - Parse url query strings.
- [Regrex Replacement and Injection](https://community.cloudflare.com/t/perform-regex-replacements-and-inject-css-javascript-with-cloudflare-workers/90279) - Perform regex replacements and inject CSS/JS.
- [Webpack Boilerplate](https://github.com/detroitenglish/cloudflare-workers-webpack-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/detroitenglish/cloudflare-workers-webpack-boilerplate?style=flat)](https://github.com/detroitenglish/cloudflare-workers-webpack-boilerplate/stargazers) - Boilerplate to build, bundle and deploy workers with webpack.
- [Basic Auth](https://github.com/dommmel/cloudflare-workers-basic-auth) [![GitHub stars](https://img.shields.io/github/stars/dommmel/cloudflare-workers-basic-auth?style=flat)](https://github.com/dommmel/cloudflare-workers-basic-auth/stargazers) - Protection using basic auth.
- [Send Logs to Logdna](https://github.com/boynet/cf-logdna-worker) [![GitHub stars](https://img.shields.io/github/stars/boynet/cf-logdna-worker?style=flat)](https://github.com/boynet/cf-logdna-worker/stargazers) - Simple recipe to send logs to logdna.
- [IP lookup service](https://github.com/matthewgall/beta.ipinfo.in) [![GitHub stars](https://img.shields.io/github/stars/matthewgall/beta.ipinfo.in?style=flat)](https://github.com/matthewgall/beta.ipinfo.in/stargazers) - IP lookup service using workers.
- [Airtable Proxy](https://github.com/portable-cto/airtable-proxy-worker) [![GitHub stars](https://img.shields.io/github/stars/portable-cto/airtable-proxy-worker?style=flat)](https://github.com/portable-cto/airtable-proxy-worker/stargazers) - Allows you to make secure requests to the Airtable API from your frontend.
- [TypeScript Workers](https://github.com/udacity/cloudflare-typescript-workers) [![GitHub stars](https://img.shields.io/github/stars/udacity/cloudflare-typescript-workers?style=flat)](https://github.com/udacity/cloudflare-typescript-workers/stargazers) - Types and mocks for building a tested typescript worker.
- [Proxies](https://github.com/GitbookIO/proxies-on-cloudflare) [![GitHub stars](https://img.shields.io/github/stars/GitbookIO/proxies-on-cloudflare?style=flat)](https://github.com/GitbookIO/proxies-on-cloudflare/stargazers) - Makes it easy to build workers, by providing high-level proxying primitives addressing common needs.
- [Static Worker](https://github.com/manatarms/static-worker) [![GitHub stars](https://img.shields.io/github/stars/manatarms/static-worker?style=flat)](https://github.com/manatarms/static-worker/stargazers) - Provides functions that make it easy to host a static website.
- [Bannero](https://github.com/nondanee/bannero) [![GitHub stars](https://img.shields.io/github/stars/nondanee/bannero?style=flat)](https://github.com/nondanee/bannero/stargazers) - Bannero image API for simpledesktops.
- [Hasura](https://github.com/nathanwaters/hasura-cloudflare-worker) [![GitHub stars](https://img.shields.io/github/stars/nathanwaters/hasura-cloudflare-worker?style=flat)](https://github.com/nathanwaters/hasura-cloudflare-worker/stargazers) - Example using Facebook-based authorization and graphql proxy queries with hasura.
- [IP Redirects](https://community.cloudflare.com/t/ip-redirects/18285) - Redirect users based on their ip address.
- [Switch Image to WebP](https://github.com/vidaxl-com/cloudflare_webworkers/blob/master/examples/webp.js) [![GitHub stars](https://img.shields.io/github/stars/vidaxl-com/cloudflare_webworkers/blob/master/examples/webp.js?style=flat)](https://github.com/vidaxl-com/cloudflare_webworkers/blob/master/examples/webp.js/stargazers) - Reroute image to webp when supported.
- [Geographic Routing and Load Balancer](https://community.cloudflare.com/t/geographic-routing-and-load-balancing-with-cloudflare-workers/21900) - Geographic routing and load balancing with workers.
- [UTM Tag Stripper](https://community.cloudflare.com/t/strip-utm-query-string/47941) - Strip UTM tags in query string.
- [Short URL Redirector](https://community.cloudflare.com/t/short-url-using-workers/39877) - Redirect short links.
- [Repo Hunt](https://github.com/signalnerve/repo-hunt) [![GitHub stars](https://img.shields.io/github/stars/signalnerve/repo-hunt?style=flat)](https://github.com/signalnerve/repo-hunt/stargazers) - Find cool open-source projects daily.
- [Performance Optimized Workers](https://github.com/pmeenan/cf-workers) [![GitHub stars](https://img.shields.io/github/stars/pmeenan/cf-workers?style=flat)](https://github.com/pmeenan/cf-workers/stargazers) - Collection of worker scripts, generally focused on performance optimizations.
- [Google reCAPTCHA verification](https://github.com/HR/recaptcha-worker) [![GitHub stars](https://img.shields.io/github/stars/HR/recaptcha-worker?style=flat)](https://github.com/HR/recaptcha-worker/stargazers) - Handle the server-side verification of your reCAPTCHA form.
- [Cloudflare Workers Starter Kit](https://github.com/kriasoft/cloudflare-starter-kit) [![GitHub stars](https://img.shields.io/github/stars/kriasoft/cloudflare-starter-kit?style=flat)](https://github.com/kriasoft/cloudflare-starter-kit/stargazers) -  - TypeScript template \w multiple CF Workers, `*.env` files, and local testing.

### AI

- [Moltworker](https://github.com/cloudflare/moltworker) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/moltworker?style=flat)](https://github.com/cloudflare/moltworker/stargazers) - Run Moltbot (formely Clawdbot) on Cloudflare Workers.

## Other

- [Support](https://support.cloudflare.com)
- [System Status](https://www.cloudflarestatus.com)
- [Network Map](https://www.cloudflare.com/network)

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, [Irfaq Syed](https://github.com/irazasyed) [![GitHub stars](https://img.shields.io/github/stars/irazasyed?style=flat)](https://github.com/irazasyed/stargazers) has waived all copyright and
related or neighboring rights to this work.

> Cloudflare is a registered trademark of Cloudflare, Inc.
