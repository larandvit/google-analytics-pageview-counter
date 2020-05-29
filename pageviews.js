gapi.analytics.ready(function() {

  /**
   * Authorize the user with an access token obtained server side.
   */
  gapi.analytics.auth.authorize({
    'serverAuth': {
      'access_token': ANALYTICS_TOKEN
    }
  });
  
  var pagePathFilter = 'ga:pagePath==' + window.location.pathname;
  
  var report = new gapi.analytics.report.Data({
	  query: {
	    ids: 'ga:209816969',
	    'start-date': 'today',
	    'end-date': 'today',
	    metrics: 'ga:pageviews',
	    filters: pagePathFilter
	  }
	});

	report.on('success', function(response) {
		document.getElementById('query-output').value = response.totalsForAllResults['ga:pageviews'];
	});

	report.execute();

  
});