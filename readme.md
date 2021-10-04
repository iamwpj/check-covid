> :info: Vaccines are acquired and this Twitter account is no longer active. This is uploaded merely for historical record.

# Check for COVID Vaccine

I will use this to monitor a Twitter account and send me a text when there are appointments near me. I could go to "the source", but I prefer to catch an availability a little more casually then those who are desperate.

This is one of those spend 30 minutes and be happy to have a text arrive situations. Very low effort and temporary.

## Running
I run this from a `cron` job and simply hardcoded all the details. At best this was always temporary.

## Dependencies

* Access to Twitter API
* Twilio account, the freebies were more than enough
* A location to execute from (got a VPS laying around?)
* Fill in missing fields from `api.py` (search for `fillme`) with relevant info