import:
	mongoimport --db carpedm20 --collection food --type json --jsonArray --file spider/data/food2.json
	mongoimport --db carpedm20 --collection food --type json --jsonArray --file spider/data/food.json

mongoexport:
	mongoexport -d carpedm20 -c food -o distinct-food.json

mongoimport:
	mongoimport -d carpedm20 -c food --file distinct-food.json
