#Post data to open search from cli.
curl -XPOST -u 'username:password' 'open-search-domain/_bulk' --data-binary @bulk_movies.json -H 'Content-Type: application/json'


#Search from cli
curl -XGET -u 'username:password' 'open-search-domain/movies/_search?q=hero&pretty=true'