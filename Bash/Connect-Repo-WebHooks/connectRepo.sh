url=https://api.github.com/repos
payload_url=$1
username=$2
reponame=$3
token=$4
value=$(curl --request POST ''$url/$username/$reponame/hooks'' \
 --header 'Authorization: token '$token'' \
  --header 'Content-Type: application/json' \
   --data-raw '{ "name":"web", "active": true, "events":["push","pull_request","fork","star","public","create","delete","member","status"], "config":{ "url": "'$payload_url/github'", "content_type": "json", "insecure_ssl": "0" } }' )
echo $value
