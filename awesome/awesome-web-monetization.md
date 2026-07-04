# Web Monetization

> 来源：[thomasbnt/awesome-web-monetization](https://github.com/thomasbnt/awesome-web-monetization)

[![GitHub stars](https://img.shields.io/github/stars/thomasbnt/awesome-web-monetization?style=flat)](https://github.com/thomasbnt/awesome-web-monetization/stargazers)

<img src="assets/wm_icon_animated.svg" alt="Logo Web Monetization" align="right" width="120px" />

# Awesome Web Monetization [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> Awesome stuffs about Web Monetization. Learn more, check modules and others tools.

**Web Monetization** is a web service that allows you to send money directly in your browser.
This is a JavaScript browser API that allows the creation of a payment stream from the user agent to the website

## Contents

- [About Web Monetization](#about-web-monetization)
- [How to start monetize my website](#how-to-start-monetize-my-website)
- [Resources](#resources)
  - [Packages](#packages)
  - [Tutorials](#tutorials)
  - [Articles](#articles)
  - [Newsletters](#newsletters)
  - [Tools](#tools)
  - [Community](#community)
- [Contribute](#contribute)
- [Donate](#donate)

## About Web Monetization

- [Webmonetization.org](https://webmonetization.org/)
- [Documentation](https://webmonetization.org/docs/)
- [How Web Monetization work for paying payments](https://webmonetization.org/docs/intro/sending-payments/)
- [How Web Monetization work for receiving payments](https://webmonetization.org/docs/intro/receiving-payments/)
- [Specifications](https://webmonetization.org/specification/)
- [ILP Forum (read only)](https://forum.interledger.org/)
- [Grant For The Web](https://www.grantfortheweb.org/)

---

- [Interledger : Open protocol suite for sending payments across different ledgers](https://interledger.org/)

## How to start monetize my website

If you would like to monetize your content, you must have a Wallet and Provider account. See below the platforms that allow you to use them.

<details><summary>More details about Wallet and Provider account</summary>
<p>

---

| **Wallets** |                                                                                             |                                                                                                                                                                                                         |     |
|:-----------:|:-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---:|
|    Name     | [![GateHub](https://webmonetization.org/img/logo-wallet-gatehub.svg)](https://gatehub.net/) | [New Wallet ?<br>Create a issue !](https://github.com/thomasbnt/awesome-web-monetization/issues/new?assignees=thomasbnt&labels=Wallet%2C+%E2%86%94+WM+repository&template=new-wallet.md&title=%5BWa%5D) [![GitHub stars](https://img.shields.io/github/stars/thomasbnt/awesome-web-monetization/issues/new?assignees=thomasbnt&labels=Wallet%2C+%E2%86%94+WM+repository&template=new-wallet.md&title=%5BWa%5D?style=flat)](https://github.com/thomasbnt/awesome-web-monetization/issues/new?assignees=thomasbnt&labels=Wallet%2C+%E2%86%94+WM+repository&template=new-wallet.md&title=%5BWa%5D/stargazers) |
|    Fees     |                   SEPA: 1.00 EUR < 50,000 EUR<br>Wire: $15 min ($150 max)                   |                                                                                                                                                                                                         |

| **Payments** |        |
|--------------|--------|
| Name         | Empty. |

---

</p>
</details>

On your webpage, integrate your `monetization` tag on meta

```html
<link rel="monetization" href="https://ilp.example.com/alice">
```

and detect if `monetization` is possible, then work

```js
if (document.monetization) {
  document.monetization.addEventListener("monetizationstart", () => {
    console.log(
      "🎉 Awesome ! You use Web Monetization.\nMore information https://webmonetization.org",
    );
  });
}
```

## Resources

### Packages

_Any packages/modules and plugins_

- [monetize.js](https://github.com/sunchayn/monetize.js) [![GitHub stars](https://img.shields.io/github/stars/sunchayn/monetize.js?style=flat)](https://github.com/sunchayn/monetize.js/stargazers) - An event-driven library to manage and simulate Web Monetization. ![](assets/small_icons/javascript.png)
- [types-wm](https://github.com/dacioromero/types-wm) [![GitHub stars](https://img.shields.io/github/stars/dacioromero/types-wm?style=flat)](https://github.com/dacioromero/types-wm/stargazers) - TypeScript definitions for Web Monetization ![](assets/small_icons/typescript.png)
- [ngx-monetization (archived)](https://github.com/CDDelta/ngx-monetization) [![GitHub stars](https://img.shields.io/github/stars/CDDelta/ngx-monetization?style=flat)](https://github.com/CDDelta/ngx-monetization/stargazers) - Web Monetization API for Angular. ![](assets/small_icons/angular.png)
- [react-hook-wm](https://github.com/dacioromero/react-hook-wm) [![GitHub stars](https://img.shields.io/github/stars/dacioromero/react-hook-wm?style=flat)](https://github.com/dacioromero/react-hook-wm/stargazers) - React hooks for integrating with Web Monetization. ![](assets/small_icons/react.png)
- [react-monetize](https://github.com/guidovizoso/react-monetize) [![GitHub stars](https://img.shields.io/github/stars/guidovizoso/react-monetize?style=flat)](https://github.com/guidovizoso/react-monetize/stargazers) - Helpers and hooks to speed up your integration with Web Monetization API. ![](assets/small_icons/react.png)
- [ep_monetization](https://github.com/ISNIT0/ep_monetization) [![GitHub stars](https://img.shields.io/github/stars/ISNIT0/ep_monetization?style=flat)](https://github.com/ISNIT0/ep_monetization/stargazers) - Plugin for applying payment pointer meta tag to Etherpad site. ![](assets/small_icons/javascript.png)
- [wp-connect-coil](https://wordpress.org/plugins/wp-connect-coil/) - Plugin for applying Coil payment pointer meta tag to WordPress site. ![](assets/small_icons/wordpress.png)
- [xrptipbot-wordpress-widget](https://wordpress.org/plugins/widget-xrptipbot/) - WordPress Widget based on XRPTIPBOT embed code to donate content creators. ![](assets/small_icons/wordpress.png)
- [eleventy-plugin-monetization](https://github.com/DanCanetti/eleventy-plugin-monetization) [![GitHub stars](https://img.shields.io/github/stars/DanCanetti/eleventy-plugin-monetization?style=flat)](https://github.com/DanCanetti/eleventy-plugin-monetization/stargazers) - An Eleventy plugin to monetize posts and site content. ![](assets/small_icons/11ty.png)
- [web-monetization-components](https://github.com/philnash/web-monetization-components) [![GitHub stars](https://img.shields.io/github/stars/philnash/web-monetization-components?style=flat)](https://github.com/philnash/web-monetization-components/stargazers) - A collection of web components you can use on your web monetized websites. ![](assets/small_icons/javascript.png)
- [revshare](https://github.com/kewbish/revshare) [![GitHub stars](https://img.shields.io/github/stars/kewbish/revshare?style=flat)](https://github.com/kewbish/revshare/stargazers) - A JS library for revenue sharing. ![](assets/small_icons/javascript.png)
- [web-monetization-proxy](https://github.com/tcdowney/web-monetization-proxy) [![GitHub stars](https://img.shields.io/github/stars/tcdowney/web-monetization-proxy?style=flat)](https://github.com/tcdowney/web-monetization-proxy/stargazers) - Simple Go proxy for injecting Web Monetization meta tags. ![](assets/small_icons/go.png)
- [gridsome-plugin-monetization](https://github.com/Sergix/gridsome-plugin-monetization) [![GitHub stars](https://img.shields.io/github/stars/Sergix/gridsome-plugin-monetization?style=flat)](https://github.com/Sergix/gridsome-plugin-monetization/stargazers) - Web monetization for Gridsome. ![](assets/small_icons/gridsome.png)
- [vuepress-plugin-web-monetization](https://github.com/spekulatius/vuepress-plugin-web-monetization) [![GitHub stars](https://img.shields.io/github/stars/spekulatius/vuepress-plugin-web-monetization?style=flat)](https://github.com/spekulatius/vuepress-plugin-web-monetization/stargazers) - Adds the web-monetization metatag to your VuePress website. ![](assets/small_icons/vuejs.png)
- [jekyll-web_monetization](https://github.com/philnash/jekyll-web_monetization) [![GitHub stars](https://img.shields.io/github/stars/philnash/jekyll-web_monetization?style=flat)](https://github.com/philnash/jekyll-web_monetization/stargazers) - A Jekyll plugin to add Web MonetizationAPI payment pointers to your site. ![](assets/small_icons/jekyll.png)
- [Monetization](https://github.com/KNawm/monetization) [![GitHub stars](https://img.shields.io/github/stars/KNawm/monetization?style=flat)](https://github.com/KNawm/monetization/stargazers) - A wrapper around the Web Monetization API to monetize apps. ![](assets/small_icons/dart.png)
- [react-webmonetization-meta](https://github.com/uchibeke/react-webmonetization-meta) [![GitHub stars](https://img.shields.io/github/stars/uchibeke/react-webmonetization-meta?style=flat)](https://github.com/uchibeke/react-webmonetization-meta/stargazers) - A Web Monetization meta tag manager for React. ![](assets/small_icons/react.png)
- [web-monetization-electron-app](https://github.com/Jasmin2895/web-monetization-electron-app) [![GitHub stars](https://img.shields.io/github/stars/Jasmin2895/web-monetization-electron-app?style=flat)](https://github.com/Jasmin2895/web-monetization-electron-app/stargazers) - Project demonstrate basic setup to enable web monetization in Electron App. ![](assets/small_icons/electron.png)
- [web-monetized-video](https://github.com/Jasmin2895/web-monetized-video) [![GitHub stars](https://img.shields.io/github/stars/Jasmin2895/web-monetized-video?style=flat)](https://github.com/Jasmin2895/web-monetized-video/stargazers) - A web component with has play and pay policy and charges you for the amount of video watched. ![](assets/small_icons/javascript.png)
- [web-monetization-polyfill](https://github.com/immers-space/web-monetization-polyfill/) [![GitHub stars](https://img.shields.io/github/stars/immers-space/web-monetization-polyfill/?style=flat)](https://github.com/immers-space/web-monetization-polyfill//stargazers) - Ensure the JavaScript Web Monetization API is available, even in environments with Content Security Policies enabled. ![](assets/small_icons/javascript.png)
- [web-monetization-video-ads](https://www.npmjs.com/package/web-monetization-video-ads) - Linking Web Monetization with video advertising to allow a freemium business model to be implemented for Web Monetization. ![](assets/small_icons/javascript.png)
- [web-monetization-revenue-share](https://www.npmjs.com/package/web-monetization-revenue-share) - Automated redistribution of funds to a community via smart contracts. ![](assets/small_icons/javascript.png)
- [awesome-jsgames](https://github.com/proyecto26/awesome-jsgames) [![GitHub stars](https://img.shields.io/github/stars/proyecto26/awesome-jsgames?style=flat)](https://github.com/proyecto26/awesome-jsgames/stargazers) - A curated list of awesome JavaScript Games ![](assets/small_icons/javascript.png)
- [mediadisclosures](https://github.com/oofdere/mediadisclosures) [![GitHub stars](https://img.shields.io/github/stars/oofdere/mediadisclosures?style=flat)](https://github.com/oofdere/mediadisclosures/stargazers) - An open-source, always evolving, universal content rating system. ![](assets/small_icons/javascript.png)
- [web-monetization-demo](https://github.com/peter279k/web-monetization-demo) [![GitHub stars](https://img.shields.io/github/stars/peter279k/web-monetization-demo?style=flat)](https://github.com/peter279k/web-monetization-demo/stargazers) - This is a Web Monetization Demo ![](assets/small_icons/javascript.png)
- [money-chat](https://github.com/dfoderick/money-chat) [![GitHub stars](https://img.shields.io/github/stars/dfoderick/money-chat?style=flat)](https://github.com/dfoderick/money-chat/stargazers) - Web Monetization chat app ![](assets/small_icons/javascript.png)

### Tutorials

- [Getting started](https://webmonetization.org/docs/guides/monetize-page/) - Official documents from webmonetization.org.
- [Exclusive content](https://webmonetization.org/docs/guides/provide-exclusive-content/) - Put exclusive content on your website.
- ['A Web Monetization Story'](https://esse-dev.github.io/a-web-monetization-story/) - An interactive, story-based Web Monetization tutorial for online creators.
- [Web Monetization like I'm 5](https://dev.to/hacksultan/web-monetization-like-i-m-5-1418) - Monetizing the web!

### Articles

- [Monetizing Content in View](https://dev.to/godwinagedah/monetizing-content-in-view-paying-for-what-you-see-462a) - Paying for what you see.
- [Web Components](https://dev.to/philnash/web-components-for-the-web-monetization-api-4ed9) - For the Web Monetization API (serie).

### Newsletters

- [Newsletter of grantfortheweb.org](https://www.grantfortheweb.org/signup) - Sign up for email updates.

### Tools

- [Probabilistic Revshare Generator - Web Monetization](https://webmonetization.org/prob-revshare/) - Probabilistic revenue sharing (revshare) is one way to share a portion of a web monetized pages earnings between multiple payment pointers.

  > Use this tool to define a list of payment pointers and their weights.
  > Then, add the generated monetization link element to your site.
  > The link will contain a unique URL hosted on https://webmonetization.org/api/revshare/pay/.
  > If you'd prefer to not use a hosted URL, you can set up revshare by adding a script to your site.

- [Is web monetized](https://github.com/jkga/is-web-monetized) [![GitHub stars](https://img.shields.io/github/stars/jkga/is-web-monetized?style=flat)](https://github.com/jkga/is-web-monetized/stargazers) - A very simple tool for checking if Web Monetization is enabled.

  > ```bash
  > npm install is-web-monetized -g
  > monetized example.com
  > ```
  >
  > You can also test your website with the dependency.

- [Paytrackr](https://github.com/thomasbnt/paytrackr) [![GitHub stars](https://img.shields.io/github/stars/thomasbnt/paytrackr?style=flat)](https://github.com/thomasbnt/paytrackr/stargazers) - (Forked from [wobsoriano/paytrackr](https://github.com/wobsoriano) [![GitHub stars](https://img.shields.io/github/stars/wobsoriano?style=flat)](https://github.com/wobsoriano/stargazers)) - Track and manage your micropayments into one place.

  > PayTrackr is the easiest and safest way to track and manage your micropayments to web monetized websites, having a web monetization provider membership.

- [Akita](https://github.com/esse-dev/akita) [![GitHub stars](https://img.shields.io/github/stars/esse-dev/akita?style=flat)](https://github.com/esse-dev/akita/stargazers) - A browser extension that gives you insight into your involvement with Web Monetization.

  > Akita presents your top visited monetized sites, how much time you're spending on them, and how much you're contributing (or could contribute) to them.

- [Open Monetization Wallet](https://github.com/kristianfreeman/openmonetizationwallet) [![GitHub stars](https://img.shields.io/github/stars/kristianfreeman/openmonetizationwallet?style=flat)](https://github.com/kristianfreeman/openmonetizationwallet/stargazers) - Tools for managing your vanity Web Monetization wallet.

  > Open Monetization Wallet (OMW) makes it easier to accept payments with the Web Monetization API at scale. Some features:
  >
  > - Custom wallet URLs: own your own "Payment Pointer", e.g. $wallet.signalnerve.com, instead of $pay.stronghold.co/abcdef123
  > - Change between wallets/providers with no downtime
  > - Logs of incoming payment requests
  > - Revenue sharing between multiple wallets, e.g. for multiple team members
  > - Infinitely scalable with serverless technology
  > - Free and open-source

### Community

- [Web Monetization Community](https://community.interledger.org/)
- [@GrantForTheWeb on Twitter](https://twitter.com/GrantForTheWeb)
- [Web Monetization tag on DEV](https://dev.to/t/webmonetization)

---

## Contribute

Contributions welcome ! Read the [contribution guidelines](contributing.md) first.
You can also contribute to share this repository and Web Monetization with your friends. 😄

If you want to add a new small icon, the height must be **16px**. Put in `assets/small_icons/NAME.png`. Format PNG only accepted.

> **Powered by Netlify** ✨

Netlify powering [the website](https://awesomewebmonetization.netlify.app/). Thanks to them! 💚

[![Deploys by Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)](https://netlify.com)

## Donate

Feel free to help [me](https://github.com/thomasbnt) [![GitHub stars](https://img.shields.io/github/stars/thomasbnt?style=flat)](https://github.com/thomasbnt/stargazers) for the maintenance of this project !
Thanks to all **Sponsors on GitHub** !

![GitHub Sponsors](https://cdn.jsdelivr.net/gh/thomasbnt/sponsors/sponsors.svg)

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor%20me-%23EA54AE.svg?&style=for-the-badge&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/thomasbnt) [![Support me on Buy Me a Coffee](https://img.shields.io/badge/Support%20me-on%20Buy%20Me%20a%20Coffee-white?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black&labelColor=%23FFDD00)](https://www.buymeacoffee.com/thomasbnt?via=thomasbnt)
