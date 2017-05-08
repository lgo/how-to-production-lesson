#!/bin/bash

ssh joey@130.211.172.72 "cd /srv/how-to-production-lesson && sudo git pull && sudo supervisorctl \"restart all\""
