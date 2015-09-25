#!/usr/bin/env python

# SETUP: Import global modules
import TweetStreetCam

g = TweetStreetCam.GraffCam()
mentions = g.GetMentions()

if mentions:
	for tweet in reversed(mentions) :
		g.ActionTweet(tweet)
