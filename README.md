# How to Production - Guide & Notes
You've got an app, but now what? If you want to share it with the world you've got to consider a number of things. In particular key topics are
- Making is publicly accessible
- Ensuring it runs with monitoring and error logging
- Top 20 under 20 (minutes): fast things you can do for big impact

## Note on work
This is currently scrapy notes from a previous tutorial I've run. These notes are missing specific details and have only been edited up to the section "Sustaining it, monitoring, and error logging". The rest of this repository was accessory code as part of the tutorial.


## Making your app publicly accessible

### Aside:
A quick and dirty way is to use an application called [ngrok](https://ngrok.com/). This let's you forward a port for a locally running app and get a domain you can share. This is very useful for sharing prototypes and for doing development work. When developing a webhook client (like a Slackbot), you often need a HTTPS domain which ngrok can provide while running an app from your machine.

### Domain and DNS
You'll first need a domain and a server. For purposes of the tutorial (and my personal favourites), we'll use [Namecheap](namecheap.com) for a domain, [Google Cloud](cloud.google.com) for servers, and also [Cloudflare](cloudflare.com) for DNS.

To use Cloudflare for DNS, once you have a domain you'll need to set the `nameservers` to point to Cloudflare. When you go to add a site to Cloudflare they have a tutorial outlining this.

### Setting up a server
In Google Cloud, a traditional server that you can SSH in and manage yourself is called the "Compute Engine". These create virtual machines, which you have complete control over and can install anything you want.

I highly recommend getting the [Google Cloud SDK](https://cloud.google.com/sdk/), as it has a command line app called `gcloud` which is very useful for access the machines.

Once you go to the "Compute Engine" panel and create a box[0]. In just a few seconds it'll be allocated, and if you click on the SSH button you can get a `gcloud` command to SSH right into it.

Once you're on the server, you can set up SSH keys for yourself and others if you prefer to not use `gcloud`. To do this, add your public SSH keys to `~/.ssh/authorized_keys` just like you would when you add a new computer to Github. Similarly you might want to create an SSH key on the server and add it to the Github repository for your app so it can `git clone` it[1].

[0]: Probably change the CPU to be cheaper, and make it Ubuntu 16.04. Ubuntu is easiest to manage, with lots of tutorials and docs and is familiar. 16.04 is just the Ubuntu released in April 2016. All 04 releases are "Long Term Support" which is fancy wording for getting security updates for a long time, if that matters to you.

[1]: You can add it as an SSH key for your Github account, although that isn't secure if others have access to the box. I believe you can add "Deploy keys" in the repository settings with restricted access to only that repo.

## Sustaining it, monitoring, and error logging
### Keeping it running
Use supervisorctl – [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps)

### nginx
Using nginx ([Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04)) is important for a few reasons:
Ability to update and change your app without downtime
Able to server static assets with low overhead[0]
Buffer requests in case your application can't handle them fast enough
Host multiple domains and applications from the same server

### Monitoring
Use [New Relic](newrelic.com)

You can set it up to monitor both the machines stats, like memory and CPU, but you can also track application details such as endpoints hit, response time, time spent in certain functions.

New Relic can be used to alert you if your application starts taking a long time to respond, >50% of requests are errors, or using various other metrics.

### Error logging
Use [Bugsnag](bugsnag.com) or [Sentry](sentry.io)

[0]: If you server static assets from a Node.JS, Ruby, or Python application there is a good chance this is extremely slow. Nginx is designed for doing this, and is as easy as telling it `/js` should load from `/my/app/static/js`.

### Deployments and testing
Deployments can be done on push by [CircleCI](circleci.com), which also can run tests automatically.


## Extras

### CDN (Content delivery network)
Just like how serving static assets from Nginx can save a lot on speed, you can take it a step further and have static assets served by a provider who can cache them. Cloudflare has configuration to do this, where they'll serve an asset for a set amount of time, often days, before checking if there's a new one. You can force an update with CDN providers.

### Command cheat sheet
```
apt-get install <name>
   If you need to find an application, go ahead and Google it. Searching for "Ubuntu install X" will often help.


nginx -s reload
   This is will nginx to reload it's configuration. This will either show errors when you run it, or in /var/log/nginx.err  

supervisorctl
     reread
         This gets supervisor to reread the configs
     update
         This gets supervisor to update after the configs (??)
     reload
         This will make all updated applications reload and restart
     start <name>
     stop <name>
     restart <name>
```
