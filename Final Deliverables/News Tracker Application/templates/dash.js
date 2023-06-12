const settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://alpha-vantage.p.rapidapi.com/query?interval=5min&function=TIME_SERIES_INTRADAY&symbol=MSFT&datatype=json&output_size=compact",
	"method": "GET",
	"headers": {
		"X-RapidAPI-Key": "14e58ca9ccmshfd7b68165c8bd40p1a1c44jsncc2652d4ca2c",
		"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
	}
};

$.ajax(settings).done(function (response) {
	console.log(response);
});