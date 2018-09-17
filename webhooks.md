---
Title: Webhooks
Decription: Webhooks
Author: Bhaskar Mangal
Date: 
Tags: Webhooks
---

**Table of Contents**
* TOC
{:toc}


## Webhooks
- https://webhooks.pbworks.com/w/page/13385124/FrontPage

**What is a WebHook?** 
The concept of a WebHook is simple. A WebHook is an HTTP callback: an HTTP POST that occurs when something happens; a simple event-notification via HTTP POST.

A web application implementing WebHooks will POST a message to a URL when certain things happen. When a web application enables users to register their own URLs, the users can then extend, customize, and integrate that application with their own custom extensions or even with other applications around the web. For the user, WebHooks are a way to receive valuable information when it happens, rather than continually polling for that data and receiving nothing valuable most of the time. WebHooks have enormous potential and are limited only by your imagination! 


https://restful.io/webhooks-dos-and-dont-s-what-we-learned-after-integrating-100-apis-d567405a3671
http://resthooks.org/

https://stripe.com/docs/api#intro

## REST hooks
- http://resthooks.org/docs/
REST Hooks itself is not a specification, it is a collection of patterns that treat webhooks like subscriptions. These subscriptions are manipulated via a REST API just like any other resource. That's it. Really.

## Minimum Implementation
* Mechanism to store subscriptions
At the most basic level, a persisted subscription only really needs the following fields:
  - An event name or names the subscription includes
  - A parent user or account relationship
  - A target URL to send the payloads
  - (optional) Active vs. inactive state
* Mechanism to modify subscriptions via API
  - API access to manipulate their subscriptions like any other resource on your API. For example, if you already have a REST API, the most common and logical solution is another resource: `/api/v1/subscription/`
  - These would simply manipulate the resources like any other REST endpoint, but with the added benefit that subscriptions have one side effect: their existence will cause webhooks be sent to the target URL when an event happens for that account.
* List and implement event types
  - enumerating and implementing each event type you'd like your REST Hooks subscription system to support
  - Each event type needs two things:
    - A name (use the noun.verb dot syntax, IE: contact.create or lead.delete).
    - A payload template (simply mirror the representation from your standard API).
* Mechanism to send hooks
* Retries, intent and identity verification, batching and other components are optional and vary wildly between implementations.
